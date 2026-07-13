from datetime import date

from src.models.concurso import Concurso


def test_cria_concurso_valido() -> None:
    concurso = Concurso(
        numero=2865,
        data=date(2026, 7, 12),
        dezenas=[5, 18, 21, 37, 49, 58],
    )

    assert concurso.numero == 2865
    assert concurso.dezenas == [5, 18, 21, 37, 49, 58]

import pytest

def test_concurso_com_menos_de_seis_dezenas() -> None:
    with pytest.raises(ValueError):
        Concurso(
            numero=1,
            data=date.today(),
            dezenas=[1, 2, 3],
        )

def test_concurso_com_dezenas_repetidas() -> None:
    with pytest.raises(ValueError):
        Concurso(
            numero=1,
            data=date.today(),
            dezenas=[1, 2, 2, 4, 5, 6],
        )

def test_dezena_maior_que_sessenta() -> None:
    with pytest.raises(ValueError):
        Concurso(
            numero=1,
            data=date.today(),
            dezenas=[1, 2, 3, 4, 5, 80],
        )