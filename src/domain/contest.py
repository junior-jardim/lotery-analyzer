from dataclasses import dataclass
from datetime import date

from src.domain.lottery import Lottery


@dataclass(slots=True)
class Contest:
    """Representa um concurso de qualquer modalidade."""

    lottery: Lottery
    numero: int
    data: date
    dezenas: list[int]

    def __post_init__(self) -> None:

        if len(self.dezenas) != self.lottery.dezenas_sorteadas:
            raise ValueError(
                f"O concurso deve possuir "
                f"{self.lottery.dezenas_sorteadas} dezenas."
            )

        if len(set(self.dezenas)) != len(self.dezenas):
            raise ValueError(
                "Existem dezenas repetidas."
            )

        for dezena in self.dezenas:
            if not 1 <= dezena <= self.lottery.total_dezenas:
                raise ValueError(
                    f"Dezena inválida: {dezena}"
                )

        self.dezenas.sort()