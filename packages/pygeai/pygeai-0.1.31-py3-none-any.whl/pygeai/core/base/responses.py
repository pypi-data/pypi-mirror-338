from pydantic.main import BaseModel

from pygeai.core.base.models import Error


class ErrorListResponse(BaseModel):
    errors: list[Error]

    def to_dict(self):
        return [error.to_dict() for error in self.errors]


class EmptyResponse(BaseModel):
    content: dict
