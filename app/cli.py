import typer
from typer import Typer
import rich
from wiki_classes import Clear_bibliography
from tokens import Sack_tokens,Resume
from compare import Compare
from supply import default_compare

app = Typer()

__version__ = '0.000.01'


def version(arg):
    if arg:
        rich.print(f'CLI demonstração Versão:[b][green] {__version__}[/]')
        raise typer.Exit(code=0)


def options_default(index: int):
    if 0 <= index < len(default_compare):
        return default_compare[index]
    else:
        raise typer.BadParameter("Índice inválido")


@app.callback(invoke_without_command=True)
def typer_callback(
    ctx: typer.Context,
    version: bool = typer.Option(False,
                                 '--version', '-v',
                                 is_eager=True,
                                 is_flag=True,
                                 callback=version),
    default_index: int = typer.Option(0,
                                      '--default-index', '-d',
                                      help='Índice do item padrão',
                                      callback=options_default)
):
    if ctx.invoked_subcommand:
        return
    rich.print("[bold]Utilize os comandos:[/]\n"+
               "[bold]`default`[/] com a flag --option ou -o para valores de [0-3]"+
               "\nResposta: Uso do [Mask] pela função Compare"+
               "\n[bold]`request-wiki`[/] com os argumentos wiki e palavra-chave para retornar uma lista de sentenças"+
               "\nExemplo: python cli.py request-wiki '/wiki/Albert_Einstein' 'relatividade'")


@app.command()
def default(
    option: str = typer.Option(
        None, '--option', '-o', help='Opção para o comando padrão'
    )
):
    if option is None:
        rich.print('Por favor, forneça uma opção com --option ou -o')
        raise typer.Exit(code=1)

    ops = option.strip().capitalize()
    try:
        ops_index = int(ops)  
        result = default_compare[ops_index]
        rich.print(Compare(result).__str__())
    except (ValueError, IndexError):
        rich.print('Opção inválida')
        raise typer.Exit(code=1)


@app.command()
def request_wiki(
    wiki:str = typer.Argument(),
    palavra_chave: str = typer.Argument()
):
    print("aguardando...")
    text = Clear_bibliography(wiki).content
    sack = Sack_tokens(text).word_sack
    response = Resume(sack,text)
    print(getattr(response,palavra_chave))



if __name__ == "__main__":
    app()

