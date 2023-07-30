from typing import Optional

from pydantic import BaseModel, Field


class DataSource(BaseModel):
    id: str = Field(..., strict=True, min_length=1)
    connection_details: dict = Field(default_factory=dict)
    default_chunk_size: Optional[int]
