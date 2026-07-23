from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.repositories.symbol_repository import SymbolRepository
from app.schemas.symbol import SymbolCreate, SymbolResponse
from app.services.symbol_service import SymbolService

router = APIRouter(
    prefix="/symbols",
    tags=["Symbols"],
)


def get_symbol_service(db: Session = Depends(get_db)) -> SymbolService:
    repository = SymbolRepository(db)
    return SymbolService(repository)


@router.post(
    "",
    response_model=SymbolResponse,
    status_code=201,
)
def create_symbol(
    symbol: SymbolCreate,
    service: SymbolService = Depends(get_symbol_service),
):
    return service.create_symbol(
        symbol=symbol.symbol,
        exchange=symbol.exchange,
        is_active=symbol.is_active,
    )


@router.get(
    "",
    response_model=list[SymbolResponse],
)
def get_symbols(
    service: SymbolService = Depends(get_symbol_service),
):
    return service.get_symbols()