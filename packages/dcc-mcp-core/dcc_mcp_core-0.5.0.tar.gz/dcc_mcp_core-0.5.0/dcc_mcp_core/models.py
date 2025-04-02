"""Pydantic models for DCC-MCP-Core action management.

This module defines the ActionResultModel for structured action execution results.
All other models have been moved to the new Action system.
"""

# Import built-in modules
from typing import Any
from typing import Dict
from typing import Optional

# Import third-party modules
from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field


class ActionResultModel(BaseModel):
    """Model representing the structured result of an action function execution.

    This model provides a standardized format for returning results from action functions,
    including a message about the execution result, a prompt for AI to guide next steps,
    and a context dictionary containing additional information.
    """

    success: bool = Field(True, description="Whether the execution was successful")
    message: str = Field(description="Human-readable message about the execution result")
    prompt: Optional[str] = Field(None, description="Suggestion for AI about next steps or actions")
    error: Optional[str] = Field(None, description="Error message if execution failed")
    context: Dict[str, Any] = Field(default_factory=dict, description="Additional context or data from the execution")

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [
                {
                    "success": True,
                    "message": "Successfully created 10 spheres",
                    "prompt": "If you want to modify these spheres, you can use the modify_spheres function",
                    "error": None,
                    "context": {
                        "created_objects": ["sphere1", "sphere2", "sphere3"],
                        "total_count": 3,
                        "scene_stats": {"total_objects": 15, "memory_usage": "2.5MB"},
                    },
                },
                {
                    "success": False,
                    "message": "Failed to create spheres",
                    "prompt": "Inform the user about the error and suggest a solution. "
                    "Wait for user confirmation before proceeding.",
                    "error": "Out of memory",
                    "context": {
                        "error_details": {
                            "code": "MEM_LIMIT",
                            "scene_stats": {"available_memory": "1.2MB", "required_memory": "5.0MB"},
                        },
                        "possible_solutions": [
                            "Reduce the number of objects",
                            "Close other scenes",
                            "Increase memory allocation",
                        ],
                    },
                },
            ]
        }
    )
