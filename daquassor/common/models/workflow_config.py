from pydantic import BaseModel, Field


class WorkflowConfig(BaseModel):
    id: str = Field(..., strict=True, min_length=1)
