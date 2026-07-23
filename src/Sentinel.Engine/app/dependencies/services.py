from fastapi import Depends
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.repositories.symbol_repository import SymbolRepository
from app.services.symbol_service import SymbolService


def get_symbol_service(
    db: Session = Depends(get_db),
) -> SymbolService:
    repository = SymbolRepository(db)
    return SymbolService(repository)