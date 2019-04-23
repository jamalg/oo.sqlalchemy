from datetime import timezone

from sqlalchemy.types import TypeDecorator, DateTime

SQLITE = "sqlite"

class UTCDateTime(TypeDecorator):
    """Custom datetime types that:
    - Only accepts *aware* :class:`~datetime.datetime` objects
    - Always writes *aware* datetimes as UTC to db
    - Raise :exc:`ValueError` if *naive* datetime is given
    - When using SQLITE it assumes that datetime are utc an returns a *aware* datetime
    """

    impl = DateTime(timezone=True)

    def process_bind_param(self, value, dialect):
        if value is not None:
            if value.tzinfo is None:
                raise ValueError("Only aware datetime are allowed")
        return value.astimezone(timezone.utc)

    def process_result_value(self, value, dialect):
        if dialect.name == SQLITE:
            return value.replace(tzinfo=timezone.utc)
        return value