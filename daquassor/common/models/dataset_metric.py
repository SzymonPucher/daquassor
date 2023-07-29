from pydantic import BaseModel, constr


class DatasetMetric(BaseModel):
    id: constr(strict=True, min_length=1)
