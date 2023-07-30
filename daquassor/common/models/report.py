from pydantic import BaseModel, constr, Field


class Report(BaseModel):
    id: str = Field(..., strict=True, min_length=1)
    data_source_id: str = Field(..., strict=True, min_length=1)
