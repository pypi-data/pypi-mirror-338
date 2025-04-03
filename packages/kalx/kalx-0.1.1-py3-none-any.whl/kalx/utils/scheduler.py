"""
Task scheduling utilities.
"""

from typing import Optional, Dict, Any
import json
import os
from pathlib import Path
from datetime import datetime
from croniter import croniter
from kalx.utils.logger import get_logger

logger = get_logger(__name__)

def schedule_task(
    task_type: str,
    schedule: str,
    recipient: str,
    content: str,
    user_id: Optional[str] = None
) -> bool:
    """Schedule a task using cron syntax."""
    try:
        # Validate cron expression
        if not croniter.is_valid(schedule):
            raise ValueError("Invalid cron schedule format")

        # Create tasks directory
        tasks_dir = os.path.join(Path.home(), ".kalx", "tasks")
        os.makedirs(tasks_dir, exist_ok=True)

        # Create task file
        task = {
            "type": task_type,
            "schedule": schedule,
            "recipient": recipient,
            "content": content,
            "user_id": user_id,
            "created_at": datetime.now().isoformat()
        }

        task_id = f"task_{datetime.now().strftime('%Y%m%d%H%M%S')}"
        task_file = os.path.join(tasks_dir, f"{task_id}.json")

        with open(task_file, 'w') as f:
            json.dump(task, f, indent=4)

        logger.info(f"Scheduled task {task_id} for {schedule}")
        return True

    except Exception as e:
        logger.error(f"Failed to schedule task: {str(e)}")
        return False
