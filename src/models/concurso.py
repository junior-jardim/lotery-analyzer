from dataclasses import dataclass
from datetime import date

@dataclass(slots=True)
class Concurso:
    """Representa um concurso de loteria"""
    numero: int
    data: date
    dezenas: list[int]

    def __post_init__(self) -> None:
        if len(self.dezenas) != 6:
            raise ValueError("Um concurso deve possuir 6 dezenas")
        
        if len(set(self.dezenas)) !=6:
            raise ValueError ("Existem dezenas repetidas")
        
        for dezena in self.dezenas:
            if dezena < 1 or dezena > 60:
                raise ValueError(f"Dezena Invalida: {dezena}")
        
        self.dezenas.sort()