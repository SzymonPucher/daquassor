import datetime as dt

from pydantic import BaseModel, constr


class DatasetMetric(BaseModel):
    id: constr(strict=True, min_length=1)
    data_source_id: constr(strict=True, min_length=1)
    dataset_id: constr(strict=True, min_length=1)
    calculated_at: dt.datetime
