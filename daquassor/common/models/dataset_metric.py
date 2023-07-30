import datetime as dt

from pydantic import BaseModel, Field


class DatasetMetric(BaseModel):
    id: str = Field(..., strict=True, min_length=1)
    data_source_id: str = Field(..., strict=True, min_length=1)
    dataset_id: str = Field(..., strict=True, min_length=1)
    calculated_at: dt.datetime
