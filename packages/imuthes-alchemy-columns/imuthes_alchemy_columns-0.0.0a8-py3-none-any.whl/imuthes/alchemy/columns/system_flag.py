from sqlalchemy.orm import Mapped, mapped_column


class SystemFlagColumn:
    """Mixin providing column to indicate that record is used for internal purposes.

    These records are Usually not displayed in lists.
    """

    system_flag_: Mapped[bool] = mapped_column(default=False, sort_order=9999)
    """Column that indicates that record is used for internal purposes."""

    @property
    def system_flag_inner_str(self) -> str:
        """String ``IS_SYSTEM`` indicates that record is used for internal purposes."""
        return "IS_SYSTEM" if self.system_flag_ else ""
