from imuthes.alchemy.exceptions import AlchemyException


class DefaultRecordNotFoundError(AlchemyException):
    """Raised when no default record was found, or the table does not support a default record.

    :param table_class: Class this Error is raised for
    :type table_class: ORM Class
    """

    def __init__(self, table_class):
        self.table_class = table_class
        super().__init__(
            f"No default record found for {self.table_class.display_name__} ({self.table_class.__tablename__})."
        )
        self.log()
