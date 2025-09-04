import os
from datetime import datetime
from .business_arx import processar_movimentacoes, gerar_arquivos_boleta


def rodar(datahora: str, gerar_arquivos: bool):
    
    dt = datetime.fromisoformat(datahora)
    data = dt.strftime("%Y-%m-%d")
    hora = dt.strftime("%H:%M:%S")

    print(f"\n=== Rodada (DATA={data}, HORA={hora}, gerar={gerar_arquivos}) ===")

    mensagens = processar_movimentacoes(data)
    for msg in mensagens:
        print(msg)

    if gerar_arquivos:
        outdir = "outputs"
        gerar_arquivos_boleta(data, outdir)


def main():
    rodar("2025-08-29 11:30:34", False)
    rodar("2025-08-29 12:05:15", True)
    rodar("2025-08-29 13:47:07", True)
    rodar("2025-08-29 14:05:56", False)
    rodar("2025-08-29 14:55:18", True)


if __name__ == "__main__":
    main()
