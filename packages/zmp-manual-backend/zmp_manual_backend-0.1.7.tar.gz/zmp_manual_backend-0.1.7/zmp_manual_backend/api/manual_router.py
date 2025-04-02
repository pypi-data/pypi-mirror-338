from fastapi import (
    APIRouter,
    HTTPException,
    Query,
    Path as FastAPIPath,
    BackgroundTasks,
    Depends,
)
from sse_starlette.sse import EventSourceResponse
from zmp_manual_backend.core.manual_service import ManualService
from zmp_manual_backend.models.manual import (
    PublishRequest,
    PublishStatus,
    JobState,
    Notification,
    SolutionType,
    SidebarMenu,
    SidebarMenuItem,
    FailureReason,
)
from zmp_manual_backend.models.auth import TokenData
from zmp_manual_backend.api.oauth2_keycloak import get_current_user
import asyncio
import os
from dotenv import load_dotenv
from typing import List, Optional
import logging
from pathlib import Path
import uuid
import time
from datetime import datetime
import json

# Load environment variables from the project root directory
project_root = Path(__file__).parent.parent.parent
env_path = project_root / ".env"

# Parse VSCODE_ENV_REPLACE for environment variables
vscode_env = os.environ.get("VSCODE_ENV_REPLACE", "")
if vscode_env:
    # Split by : and parse each key=value pair
    env_pairs = vscode_env.split(":")
    for pair in env_pairs:
        if "=" in pair:
            key, value = pair.split("=", 1)
            # Only set if the value is not empty
            if value:
                os.environ[key] = value.replace("\\x3a", ":")  # Fix escaped colons

# Load .env file as fallback
load_dotenv(dotenv_path=env_path)

router = APIRouter()
logger = logging.getLogger("appLogger")


# Create a custom JSON encoder that can handle datetime objects
class DateTimeEncoder(json.JSONEncoder):
    """Custom JSON encoder for handling datetime objects."""

    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)


def initialize_manual_service() -> ManualService:
    """Initialize and return a ManualService instance."""
    try:
        notion_token = os.environ.get("NOTION_TOKEN")
        if not notion_token:
            logger.error("NOTION_TOKEN not found in environment variables")
            logger.error(f"Looking for .env file at: {env_path}")
            logger.error(f".env file exists: {env_path.exists()}")
            raise ValueError("NOTION_TOKEN environment variable is not set")

        logger.info(f"Initializing manual service with token: {notion_token[:5]}...")

        # Log the available root page IDs
        for solution in ["ZCP", "APIM", "AMDP"]:
            env_var = f"{solution}_ROOT_PAGE_ID"
            if os.environ.get(env_var):
                logger.info(f"Found {env_var} in environment variables")

        return ManualService(
            notion_token=notion_token,
            root_page_id=os.environ.get(
                "ZCP_ROOT_PAGE_ID"
            ),  # For backward compatibility
            repo_path=os.environ.get("REPO_BASE_PATH", "./repo"),
            source_dir=os.environ.get("SOURCE_DIR", "docs"),
            target_dir=os.environ.get("TARGET_DIR", "i18n"),
            github_repo_url=os.environ.get("GITHUB_REPO_URL"),
            target_languages=set(
                lang.strip()
                for lang in os.environ.get("TARGET_LANGUAGES", "ko,ja,zh").split(",")
            ),
        )
    except Exception as e:
        logger.error(f"Failed to initialize manual service: {str(e)}")
        raise


# Initialize service instance
manual_service = initialize_manual_service()


def get_manual_service() -> ManualService:
    """Dependency function to get the ManualService instance."""
    return manual_service


@router.get("/manuals")
async def get_manuals(
    selected_solution: SolutionType = Query(
        default=SolutionType.ZCP,
        description="The solution type to retrieve manuals for (zcp, apim, amdp)",
    ),
):
    """Get hierarchical list of manuals and folders for the specified solution"""
    try:
        items = await manual_service.get_manuals(selected_solution=selected_solution)

        # Convert Node objects to dictionaries
        items_dicts = []
        for item in items:
            item_dict = {
                "object_id": item.object_id,
                "title": item.name,
                "is_directory": item.is_directory,
                "parent_id": item.parent.object_id if item.parent else None,
                "notion_url": item.notion_url,
                "index": item.index,
            }
            items_dicts.append(item_dict)

        return {"items": items_dicts}
    except Exception as e:
        logger.error(f"Error getting manuals: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@router.post(
    "/publish", openapi_extra={"security": [{"OAuth2AuthorizationCodeBearer": []}]}
)
async def publish_manual(
    request: PublishRequest,
    background_tasks: BackgroundTasks,
    manual_service: ManualService = Depends(get_manual_service),
    current_user: TokenData = Depends(get_current_user),
) -> dict:
    """Publish a manual by exporting it from Notion and translating it."""
    try:
        if not request.notion_page_id:
            raise HTTPException(status_code=400, detail="notion_page_id is required")

        user_id = current_user.username

        # Generate job ID and create initial status with complete information
        job_id = str(uuid.uuid4())
        solution_value = (
            request.selected_solution.value
            if isinstance(request.selected_solution, SolutionType)
            else request.selected_solution
        )

        manual_service.active_jobs[job_id] = PublishStatus(
            job_id=job_id,
            status=JobState.STARTED,
            message="Starting publication process",
            progress=0.0,
            notion_page_id=request.notion_page_id,  # Set notion_page_id immediately
            solution=solution_value,  # Set solution immediately
            initiated_by=current_user.username,  # Track which user initiated this job
            title=request.title,  # Add title information
            is_directory=request.is_directory,  # Add is_directory information
            parent_id=request.parent_id,  # Add parent_id information
        )

        # Define an error handler for the background task
        async def publish_with_error_handling():
            try:
                await manual_service.publish_manual(
                    request.notion_page_id,
                    request.selected_solution,
                    request.target_languages,
                    user_id,
                    job_id=job_id,  # Pass the job_id explicitly
                    title=request.title,  # Pass title
                    is_directory=request.is_directory,  # Pass is_directory
                    parent_id=request.parent_id,  # Pass parent_id
                )
            except Exception as e:
                logger.error(f"Background task error in publish: {str(e)}")
                # Make sure job is marked as failed if there's an unhandled exception
                if job_id in manual_service.active_jobs:
                    manual_service.active_jobs[job_id].status = JobState.FAILED
                    manual_service.active_jobs[
                        job_id
                    ].message = f"Publication failed: {str(e)}"
                    manual_service.active_jobs[
                        job_id
                    ].failure_reason = FailureReason.UNKNOWN

        # Add the error-handled publication process to background tasks
        background_tasks.add_task(publish_with_error_handling)

        logger.info(
            f"Created job {job_id} for publishing manual (running in background)"
        )

        # Return the job ID to the client immediately
        return {"job_id": job_id}
    except ValueError as e:
        logger.error(f"Validation error in publish request: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.error(f"Error starting publication: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/jobs/{job_id}", response_model=Optional[PublishStatus])
async def get_job_status(
    job_id: str = FastAPIPath(..., description="The ID of the job to check"),
    manual_service: ManualService = Depends(get_manual_service),
):
    """Get current status of a publication job"""
    try:
        logger.info(f"Fetching status for job: {job_id}")
        status = await manual_service.get_job_status(job_id)
        if not status:
            logger.warning(f"Job not found: {job_id}")
            raise HTTPException(status_code=404, detail="Job not found")
        logger.info(f"Job {job_id} status: {status.status}")
        return status
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error getting job status: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/watch/{job_id}")
async def watch_publication(
    job_id: str = FastAPIPath(..., description="The ID of the job to watch"),
    current_user: TokenData = Depends(get_current_user),
    manual_service: ManualService = Depends(get_manual_service),
):
    """Watch publication progress using Server-Sent Events"""
    try:
        # Check if job exists first
        status = await manual_service.get_job_status(job_id)
        if not status:
            raise HTTPException(status_code=404, detail="Job not found")

        # Check if the current user is authorized to watch this job
        # Users should only see their own jobs
        if (
            hasattr(status, "initiated_by")
            and status.initiated_by
            and status.initiated_by != current_user.username
        ):
            # Exception for admin users
            if current_user.username not in ["cloudzcp-admin", "admin"]:
                raise HTTPException(
                    status_code=403, detail="Not authorized to watch this job"
                )

        logger.info(
            f"Starting SSE stream for job {job_id} by user {current_user.username}"
        )

        async def event_generator():
            retry_count = 0
            max_retries = 5  # Increased max retries
            ping_interval = 10  # Send ping every 10 seconds
            last_ping_time = time.time()
            last_status_json = None
            completion_time = None
            error_sent = False  # Track if we've sent an error event

            # Initial status update to client
            initial_status = await manual_service.get_job_status(job_id)
            if initial_status:
                # Convert PublishStatus to dictionary format for consistent response format
                status_dict = initial_status.to_dict()
                status_json = json.dumps(
                    status_dict, separators=(",", ":"), cls=DateTimeEncoder
                )
                yield {"data": status_json}
                last_status_json = status_json
                logger.info(
                    f"Sent initial job status: {initial_status.status} for job {job_id}"
                )

                # If already in completed state, set completion time to start shutdown sequence
                if initial_status.status in [
                    JobState.COMPLETED,
                    JobState.FAILED,
                ]:
                    completion_time = time.time()
                    logger.info(
                        f"Job {job_id} already in completed state: {initial_status.status}"
                    )

            while True:
                try:
                    current_time = time.time()

                    # Check if we need to send a ping
                    if current_time - last_ping_time >= ping_interval:
                        ping_data = f"ping - {datetime.now().isoformat()}"
                        yield {"event": "ping", "data": ping_data}
                        logger.debug(f"Sent ping: {ping_data} for job {job_id}")
                        last_ping_time = current_time

                    # Get latest job status
                    status = await manual_service.get_job_status(job_id)
                    if not status:
                        if retry_count >= max_retries:
                            logger.warning(
                                f"Job {job_id} not found after {max_retries} retries"
                            )
                            if not error_sent:
                                yield {"event": "info", "data": "Job not found"}
                                error_sent = True
                            break
                        retry_count += 1
                        await asyncio.sleep(1)
                        continue

                    # Reset retry count if we successfully got a status
                    retry_count = 0

                    # Convert PublishStatus to dictionary format for consistent response format
                    status_dict = status.to_dict()
                    status_json = json.dumps(
                        status_dict, separators=(",", ":"), cls=DateTimeEncoder
                    )

                    # Only send update if status changed
                    if status_json != last_status_json:
                        yield {"data": status_json}
                        last_status_json = status_json
                        logger.info(
                            f"Sent job status update: {status.status} for job {job_id}"
                        )

                    # Check if job is completed
                    if status.status in [
                        JobState.COMPLETED,
                        JobState.FAILED,
                    ]:
                        if completion_time is None:
                            # Record when the job completed
                            completion_time = time.time()
                            logger.info(
                                f"Job {job_id} completed with status {status.status}, will keep connection alive for a while"
                            )

                            # For FAILED, send an info message rather than error to avoid connection issues
                            if status.status == JobState.FAILED:
                                yield {
                                    "event": "info",
                                    "data": f"Job failed: {status.message or 'Unknown error'}",
                                }

                            # Always send the full status json as a data event
                            yield {"data": status_json}

                        # Keep the connection alive for a short period after completion
                        # to ensure the client receives the final status
                        elif (
                            time.time() - completion_time > 15
                        ):  # Increased grace period to 15 seconds
                            logger.info(
                                f"Closing SSE stream for job {job_id} after completion grace period"
                            )
                            # Send one final ping before closing
                            yield {
                                "event": "ping",
                                "data": f"final - {datetime.now().isoformat()}",
                            }
                            break

                    # Sleep shorter intervals to ensure more responsive updates
                    await asyncio.sleep(0.5)

                except Exception as e:
                    logger.error(f"Error in event stream for job {job_id}: {str(e)}")
                    retry_count += 1

                    if retry_count >= max_retries:
                        if not error_sent:
                            logger.warning(
                                f"Too many errors in stream for job {job_id}, sending error and closing"
                            )
                            yield {"event": "info", "data": f"Stream error: {str(e)}"}
                            error_sent = True
                            # Don't break immediately, give the client a chance to receive the error
                            completion_time = completion_time or time.time()
                        elif time.time() - (completion_time or time.time()) > 5:
                            break

                    await asyncio.sleep(1)

        return EventSourceResponse(
            event_generator(),
            ping=None,  # Disable automatic pings, we'll handle them manually
            media_type="text/event-stream",
            headers={"Cache-Control": "no-cache", "Connection": "keep-alive"},
        )
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error setting up event stream: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/jobs", response_model=List[PublishStatus])
async def list_jobs(
    status: Optional[str] = Query(None, description="Filter by status"),
    limit: int = Query(10, ge=1, le=100, description="Number of jobs to return"),
    manual_service: ManualService = Depends(get_manual_service),
):
    """List recent publication jobs with optional status filter"""
    try:
        # Get all jobs from the manual service
        jobs = list(manual_service.active_jobs.values())
        logger.info(f"Found {len(jobs)} active jobs")

        if status:
            jobs = [job for job in jobs if job.status == status]

        # Sort by most recent first (assuming job_id contains timestamp)
        jobs.sort(key=lambda x: x.job_id, reverse=True)

        return jobs[:limit]
    except Exception as e:
        logger.error(f"Error listing jobs: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/notifications", response_model=List[Notification])
async def get_notifications(
    limit: int = Query(
        50, ge=1, le=100, description="Number of notifications to return"
    ),
    include_read: bool = Query(
        False, description="Whether to include read notifications"
    ),
    job_id: Optional[str] = Query(
        None, description="Filter notifications for a specific job"
    ),
    manual_service: ManualService = Depends(get_manual_service),
    current_user: TokenData = Depends(get_current_user),
):
    """Get recent notifications for the current authenticated user."""
    try:
        notifications = await manual_service.get_notifications(
            limit=limit,
            include_read=include_read,
            user_id=current_user.username,
            job_id=job_id,
        )

        # Enhance notifications with document title
        for notification in notifications:
            # Add a custom attribute for document title
            if (
                notification.job_id
                and notification.job_id in manual_service.active_jobs
            ):
                job_status = manual_service.active_jobs[notification.job_id]
                if job_status.title:
                    setattr(notification, "document_title", job_status.title)

        return notifications
    except Exception as e:
        logger.error(f"Error getting notifications: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/notifications/latest", response_model=Optional[Notification])
async def get_latest_notification(
    include_read: bool = Query(
        False, description="Whether to include read notifications"
    ),
    job_id: Optional[str] = Query(
        None, description="Filter notifications for a specific job"
    ),
    manual_service: ManualService = Depends(get_manual_service),
    current_user: TokenData = Depends(get_current_user),
):
    """Get the latest notification only for the current authenticated user.

    Note: For real-time updates, consider using the /notifications/stream endpoint instead.
    """
    try:
        notification = await manual_service.get_notifications(
            include_read=include_read,
            user_id=current_user.username,
            latest_only=True,
            job_id=job_id,
        )

        # Enhance notification with document title if it exists
        if (
            notification
            and notification.job_id
            and notification.job_id in manual_service.active_jobs
        ):
            job_status = manual_service.active_jobs[notification.job_id]
            if job_status.title:
                setattr(notification, "document_title", job_status.title)

        return notification
    except Exception as e:
        logger.error(f"Error getting latest notification: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/notifications/stream")
async def stream_notifications(
    include_read: bool = Query(
        False, description="Whether to include read notifications"
    ),
    manual_service: ManualService = Depends(get_manual_service),
):
    """Stream all notifications in real-time using Server-Sent Events (SSE).

    This endpoint uses SSE to push notifications to the client in real-time.
    Clients will receive new notifications as they are created without polling.
    This endpoint does not require authentication and will stream notifications for all jobs.
    Each notification includes the user_id field indicating who initiated the job and
    document_title field showing the title of the Notion document being processed.
    """
    try:
        logger.info("Starting notification stream for all jobs")

        async def event_generator():
            notification_queue = asyncio.Queue()
            ping_interval = 10  # Send ping every 10 seconds
            last_ping_time = time.time()

            # Register client without specific user_id for global notifications
            queue_id = await manual_service.register_notification_client(
                queue=notification_queue, user_id=None
            )
            logger.info(
                f"Registered notification client {queue_id} for global notifications"
            )

            try:
                # First send existing notifications
                notifications = await manual_service.get_notifications(
                    include_read=include_read,
                    limit=10,  # Limit to recent notifications only
                )

                # Send the latest notification if any exist
                if notifications:
                    latest = notifications[0]  # Already sorted newest first

                    # Enhance notification with document title if job_id exists
                    notification_data = latest.to_dict()
                    if latest.job_id and latest.job_id in manual_service.active_jobs:
                        job_status = manual_service.active_jobs[latest.job_id]
                        if job_status.title:
                            notification_data["document_title"] = job_status.title

                    notification_json = json.dumps(
                        notification_data, separators=(",", ":"), cls=DateTimeEncoder
                    )
                    yield {"data": notification_json}
                    logger.info(
                        "Sent initial notification to global notification stream"
                    )

                # Then listen for new notifications
                while True:
                    current_time = time.time()

                    # Send periodic ping
                    if current_time - last_ping_time >= ping_interval:
                        ping_data = f"ping - {datetime.now().isoformat()}"
                        yield {"event": "ping", "data": ping_data}
                        logger.debug(f"Sent ping to notification stream: {ping_data}")
                        last_ping_time = current_time

                    # Use a timeout to allow for periodic pings even when there are no notifications
                    try:
                        notification = await asyncio.wait_for(
                            notification_queue.get(), timeout=0.5
                        )
                    except asyncio.TimeoutError:
                        # No notification received within timeout, continue loop
                        continue

                    if notification is None:  # None is our signal to stop
                        logger.info("Notification stream closing")
                        break

                    # Skip read notifications unless explicitly included
                    if not include_read and notification.is_read:
                        notification_queue.task_done()
                        continue

                    # Send the notification with enhanced data
                    try:
                        # Convert to dict first to enhance with additional data
                        notification_data = notification.to_dict()

                        # Add document title to notification if job_id exists
                        if (
                            notification.job_id
                            and notification.job_id in manual_service.active_jobs
                        ):
                            job_status = manual_service.active_jobs[notification.job_id]
                            if job_status.title:
                                notification_data["document_title"] = job_status.title

                        notification_json = json.dumps(
                            notification_data,
                            separators=(",", ":"),
                            cls=DateTimeEncoder,
                        )
                        yield {"data": notification_json}
                        logger.debug(
                            f"Sent notification {notification.id} to notification stream"
                        )
                    except Exception as e:
                        logger.error(f"Error serializing notification: {str(e)}")

                    # Mark the item as processed
                    notification_queue.task_done()

            finally:
                # Always unregister client to avoid memory leaks
                await manual_service.unregister_notification_client(queue_id)
                logger.info(f"Unregistered notification client {queue_id}")

        return EventSourceResponse(
            event_generator(),
            ping=None,  # Disable automatic pings, we're handling them manually
            media_type="text/event-stream",
            headers={
                "Cache-Control": "no-cache",
                "Connection": "keep-alive",
                "X-Accel-Buffering": "no",  # Disable buffering in nginx
            },
        )
    except Exception as e:
        logger.error(f"Error in notification stream: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/notifications/{notification_id}/read")
async def mark_notification_read(
    notification_id: str = FastAPIPath(
        ..., description="The ID of the notification to mark as read"
    ),
    manual_service: ManualService = Depends(get_manual_service),
):
    """Mark a notification as read."""
    try:
        success = await manual_service.mark_notification_read(notification_id)
        if not success:
            raise HTTPException(status_code=404, detail="Notification not found")
        return {"status": "success"}
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error marking notification as read: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/notifications/clear")
async def clear_notifications(
    manual_service: ManualService = Depends(get_manual_service),
):
    """Clear all notifications."""
    try:
        await manual_service.clear_notifications()
        return {"status": "success"}
    except Exception as e:
        logger.error(f"Error clearing notifications: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/sidebar", response_model=SidebarMenu)
async def get_sidebar_menu(
    manual_service: ManualService = Depends(get_manual_service),
):
    """Get information about all available solutions for the sidebar menu."""
    try:
        solutions = []
        for solution_type in SolutionType:
            root_page_id = manual_service.root_page_ids.get(solution_type)
            if root_page_id:
                solutions.append(
                    SidebarMenuItem(
                        name=solution_type.value.upper(),
                        solution_type=solution_type,
                        root_page_id=root_page_id,
                    )
                )

        return SidebarMenu(solutions=solutions)
    except Exception as e:
        logger.error(f"Error getting sidebar menu: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))
