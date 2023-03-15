# pdf generator

## Info
This is some helper scripts for creating, testing and generating pdf out of html templates.

## How To
* Before starting to create template start `./init.sh` script for setting up the environment.
* Edit `templates/invoice-template-0/template.html` using [Jinja2](https://jinja.palletsprojects.com/en/3.1.x/templates) syntax.
* Edit `templates/invoice-template-0/invoice.css` for styling the html.
* Add or edit data to `invoice_data.json` file. Data from this file will be used by script for population of html.
* Run `./generate` script to generate pdf in `templates` directory.

## Initialization of environment
```bash
./init.sh
```

## Generation of pdf file
```bash
./generate.sh
```
