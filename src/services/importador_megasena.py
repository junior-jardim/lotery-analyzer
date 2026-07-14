from datetime import datetime
from pathlib import Path

import pandas as pd

from src.domain.contest import Contest
from src.lotteries.megasena.lottery import MEGA_SENA


class ImportadorMegaSena:
    """Importa concursos da Mega-Sena a partir de um arquivo CSV."""

    def __init__(self, arquivo: Path) -> None:
        self.arquivo = arquivo

    def importar(self) -> list[Contest]:
        """Lê o CSV e retorna uma lista de objetos Concurso."""

        dataframe = pd.read_csv(
            self.arquivo,
            sep=";",
        )

        contests: list[Contest] = []

        for _, linha in dataframe.iterrows():

            contest = Contest(
                lottery=MEGA_SENA,
                numero=int(linha["concurso"]),
                data=datetime.strptime(
                    linha["data"],
                    "%d/%m/%Y",
                ).date(),
                dezenas=[
                    int(linha["bola1"]),
                    int(linha["bola2"]),
                    int(linha["bola3"]),
                    int(linha["bola4"]),
                    int(linha["bola5"]),
                    int(linha["bola6"]),
                ],
            )

            contests.append(contest)

        return contests