from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.symbol import Symbol
from app.repositories.base_repository import BaseRepository


class SymbolRepository(BaseRepository[Symbol]):
    def __init__(self, db: Session):
        super().__init__(db)

    def create(self, symbol: Symbol) -> Symbol:
        self.db.add(symbol)
        self.db.commit()
        self.db.refresh(symbol)
        return symbol

    def get_all(self) -> list[Symbol]:
        statement = select(Symbol).order_by(Symbol.symbol)
        return list(self.db.scalars(statement).all())

    def get_by_symbol(self, symbol: str) -> Symbol | None:
        statement = select(Symbol).where(Symbol.symbol == symbol)
        return self.db.scalar(statement)

    def exists(self, symbol: str) -> bool:
        return self.get_by_symbol(symbol) is not None