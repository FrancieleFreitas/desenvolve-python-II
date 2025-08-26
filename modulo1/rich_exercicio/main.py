"""
Arquivo principal com interface de linha de comando usando argparse.
Permite escolher o módulo e função do pacote personalizador para exibir texto formatado com Rich.
"""

import argparse
import sys
from rich.console import Console
from personalizador import layout, painel, progresso, estilo

console = Console()


def main():
    parser = argparse.ArgumentParser(description="Exercício Rich - Interface de Linha de Comando")

    parser.add_argument("texto", help="Texto ou caminho de arquivo")
    parser.add_argument("-a", "--arquivo", action="store_true", help="Indica que o argumento é um arquivo")
    parser.add_argument("-m", "--modulo", choices=["layout", "painel", "progresso", "estilo"],
                        required=True, help="Escolha o módulo (layout, painel, progresso, estilo)")
    parser.add_argument("-f", "--funcao", required=True,
                        help="Escolha a função do módulo (ex: simples, dupla, caixa, titulo, barra, passos, info, erro)")

    args = parser.parse_args()
    texto = args.texto

    if args.modulo == "layout":
        funcoes = {"simples": layout.simples, "dupla": layout.dupla}
    elif args.modulo == "painel":
        funcoes = {"caixa": painel.caixa, "titulo": painel.titulo}
    elif args.modulo == "progresso":
        funcoes = {"barra": progresso.barra, "passos": progresso.passos}
    elif args.modulo == "estilo":
        funcoes = {"info": estilo.info, "erro": estilo.erro}
    else:
        console.print("[bold red]Módulo inválido[/bold red]")
        sys.exit(1)

    if args.funcao not in funcoes:
        console.print("[bold red]Função inválida para o módulo[/bold red]")
        sys.exit(2)

    # Executa a função escolhida
    funcoes[args.funcao](texto, args.arquivo)


if __name__ == "__main__":
    main()
