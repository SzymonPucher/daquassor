from pydantic import BaseModel, constr


class WorkflowConfig(BaseModel):
    id: constr(strict=True, min_length=1)
