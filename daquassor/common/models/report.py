from pydantic import BaseModel, constr


class Report(BaseModel):
    id: constr(strict=True, min_length=1)
    data_source_id: constr(strict=True, min_length=1)
