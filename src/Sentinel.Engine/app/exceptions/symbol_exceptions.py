class DuplicateSymbolException(Exception):
    """Raised when attempting to create a symbol that already exists."""

    def __init__(self, symbol: str):
        self.symbol = symbol
        super().__init__(f"Symbol '{symbol}' already exists.")