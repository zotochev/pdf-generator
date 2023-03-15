import weasyprint
import click


@click.command()
@click.argument('html_template')
@click.option('--styles', '-s', multiple=True, help='css styles file or directory')
def main(template: str):
    pass


if __name__ == "__main__":
    main()
