from __future__ import annotations
from typing import List

def processar_movimentacoes(data_processo: str) -> List[str]:   
    raise NotImplementedError("Implemente a leitura/consolidação e o retorno das mensagens.")


def gerar_arquivos_boleta(data_processo: str, caminho_saida: str) -> None:   
    raise NotImplementedError("Implemente a escrita dos arquivos conforme layouts.")