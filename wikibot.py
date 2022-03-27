import click
from mylib.bot import scrape

@click.command()
@click.option('--name',
              help='Web page we want to scape')
@click.option('--length',
                help='The length of the output for wikipedia')

def cli(name, length):
    result = scrape(name, length=length)
    click.echo(click.style(f"{result}:", bg="black", fg="white"))

if __name__ == '__main__':
    cli()


