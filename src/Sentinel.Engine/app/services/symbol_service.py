from app.models.symbol import Symbol
from app.repositories.symbol_repository import SymbolRepository
from fastapi import HTTPException, status

class SymbolService:
    def __init__(self, repository: SymbolRepository):
        self.repository = repository

    def create_symbol(
        self,
        symbol: str,
        exchange: str,
        is_active: bool = True,
    ) -> Symbol:

        if self.repository.exists(symbol):\
            raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Symbol '{symbol}' already exists."
            )
            

        new_symbol = Symbol(
            symbol=symbol,
            exchange=exchange,
            is_active=is_active,
        )

        return self.repository.create(new_symbol)

    def get_symbols(self) -> list[Symbol]:
        return self.repository.get_all()