import uuid

from sqlalchemy import text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, declarative_mixin, mapped_column


@declarative_mixin
class UUIDMixin:
    """
    Mixin to provide a uuid primary key, based on
    https://www.postgresql.org/docs/current/functions-uuid.html

    - example usage::

        from accentdatabase.base import Base
        from accentdatabase.mixins import UUIDMixin

        class MyTable(UUIDMixin, Base)
            pass

    """

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        server_default=text("gen_random_uuid()"),
    )
