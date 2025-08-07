from datetime import datetime
from typing import Optional

from pydantic import BaseModel, validator


class CoreModel(BaseModel):
    """
    Any common logic to be shared with all models goes here.
    """
    pass


class IDModelMixin(BaseModel):
    id: int


class DateTimeModelMixin(BaseModel):
    created_at: datetime
    updated_at: datetime

    @validator('created_at', 'updated_at', pre=True)
    def default_datetime(cls, value: datetime) -> datetime:
        return value or datetime.now()