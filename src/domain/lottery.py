from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Lottery:
    """Representa uma modalidade de loteria."""

    nome: str
    total_dezenas: int
    dezenas_sorteadas: int