from pathlib import Path

from src.services.importador_megasena import ImportadorMegaSena


def test_importa_cinco_concursos() -> None:
    caminho = Path("data/raw/mega_sena.csv")

    importador = ImportadorMegaSena(caminho)

    concursos = importador.importar()

    assert len(concursos) == 5