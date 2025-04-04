import inspect
from typing import Optional

from hakisto import Logger, logger_globals

logger = Logger("imuthes/alchemy/columns")
logger_globals.register_excluded_source_file(inspect.currentframe().f_code.co_filename)

from sqlalchemy import select

from sqlalchemy.orm import Mapped, mapped_column

from .default_record_not_found_error import DefaultRecordNotFoundError


class DefaultFlagColumn:
    """Mixin providing column to indicate that a specific record should be used as default.

    Only one record per table can be flagged as default.

    This is enforced by setting the column as UNIQUE, but allow NULL.
    """

    default_flag_: Mapped[Optional[bool]] = mapped_column(unique=True, sort_order=9998)
    """Column that indicates that a specific record should be used as default."""

    @classmethod
    def get_default__(cls, session):
        """Return the default record.
        
        :param session: SQLAlchemy session
        :type session: :py:class:`sqlalchemy.orm.Session`
        :return: Default record
        :rtype: ORM Class
        :raises DefaultRecordNotFoundError: if no default record was found
        """
        # logger.debug(f"{cls.__name__}.get_default__()")
        record = session.scalar(select(cls).where(cls.default_flag_ == True))
        if record is None:
            raise DefaultRecordNotFoundError(cls)
        return record

    @property
    def default_flag_inner_str(self) -> str:
        """String ``IS_DEFAULT`` indicates that this is the default record."""
        return "IS_DEFAULT" if self.default_flag_ else ""
