import shutil
from pathlib import Path
import logging
import json

import weasyprint
import click
from jinja2 import Environment, FileSystemLoader


RESULTS_DIR = './results'
assert Path(RESULTS_DIR).is_dir(), f"{__file__}: directory with results `{RESULTS_DIR}` not found."


def copy_template_to_results(template) -> Path:
    template_dir = Path(template)
    assert template_dir.is_dir(), f"generate_pdf: `{template_dir}` is not a directory."
    result_dir = Path(RESULTS_DIR, template_dir.name)

    if result_dir.is_dir():
        logging.warning(f"Removing template `{result_dir}`.")
        shutil.rmtree(result_dir, ignore_errors=True)
    logging.warning(f"Creating copy of template: `{template_dir}` to `{result_dir}`")
    shutil.copytree(src=template_dir, dst=result_dir)
    return result_dir


def generate_html(template: str, data: dict):
    template_dir = copy_template_to_results(template)
    dst_path = Path(template_dir, 'index.html')

    environment = Environment(loader=FileSystemLoader(template_dir))
    template = environment.get_template("template.html")
    content = template.render(**data)

    with dst_path.open('w') as f:
        f.write(content)


def generate_pdf(template: str):
    pass


def read_json(data_file) -> dict:
    data_file = Path(data_file)
    assert data_file.is_file(), f"{data_file.resolve()} is not found or invalid file."

    with data_file.open() as f:
        return json.load(f)


@click.command()
@click.argument('template')
# @click.option('--style', '-s', default=None, help='css file or directory')
@click.option('--data', '-d', help='Data to render into template')
def main(template: str, data: str):
    data_dict = read_json(data)
    generate_html(template, data_dict)


if __name__ == "__main__":
    main()
