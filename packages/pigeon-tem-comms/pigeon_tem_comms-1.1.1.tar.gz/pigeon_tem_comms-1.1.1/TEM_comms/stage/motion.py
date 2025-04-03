from pigeon import BaseMessage


class Command(BaseMessage):
    x: int | None = None
    y: int | None = None
    z: int | None = None
    calibrate: bool = False


class Status(BaseMessage):
    x: int | None
    y: int | None
    z: int | None
    in_motion: bool
    error: str = ""
