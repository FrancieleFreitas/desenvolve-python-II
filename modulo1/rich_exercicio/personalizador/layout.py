"""
Módulo de layout com tabelas utilizando Rich.
Fornece funções que utilizam recursos de layout da biblioteca Rich
"""

from rich.console import Console
from rich.table import Table

console = Console()


def simples(texto: str, isArquivo: bool = False):
    """
    Exibe uma tabela simples com uma coluna.
    
    Args:
        texto (str): Texto ou caminho de arquivo.
        isArquivo (bool): Se True, lê o texto de um arquivo.
    """
    if isArquivo:
        with open(texto, "r", encoding="utf-8") as f:
            texto = f.read()

    itens = [p.strip() for p in texto.split(";") if p.strip()]
    tabela = Table(title="Tabela Simples")
    tabela.add_column("Item")

    for item in itens:
        tabela.add_row(item)

    console.print(tabela)


def dupla(texto: str, isArquivo: bool = False):
    """
    Exibe uma tabela com duas colunas.
    
    Args:
        texto (str): Texto ou caminho de arquivo. Espera pares separados por ';' e ':'.
        isArquivo (bool): Se True, lê o texto de um arquivo.
    """
    if isArquivo:
        with open(texto, "r", encoding="utf-8") as f:
            texto = f.read()

    pares = [p.strip() for p in texto.split(";") if p.strip()]
    tabela = Table(title="Tabela Dupla")
    tabela.add_column("Coluna 1")
    tabela.add_column("Coluna 2")

    for p in pares:
        if ":" in p:
            c1, c2 = [x.strip() for x in p.split(":", 1)]
            tabela.add_row(c1, c2)
        else:
            tabela.add_row(p, "")

    console.print(tabela)