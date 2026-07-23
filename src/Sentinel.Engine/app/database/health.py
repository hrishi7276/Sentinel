from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

from app.database.session import engine


def check_database_connection() -> bool:
    """
    Returns True if PostgreSQL is reachable.
    """

    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        return True

    except SQLAlchemyError:
        return False