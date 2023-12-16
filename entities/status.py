from enum import IntEnum
from http import HTTPStatus


class Status(IntEnum):
    SUCCESS = HTTPStatus.OK
    FAIL = HTTPStatus.INTERNAL_SERVER_ERROR
