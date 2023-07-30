from typing import Optional

from pydantic import BaseModel, constr


class DataSource(BaseModel):
    id: constr(strict=True, min_length=1)
    connection_details: dict
    default_chunk_size: Optional[int]
