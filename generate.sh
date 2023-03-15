#!/usr/bin/env bash

TEMPLATE="invoice-template-0"
TEMPLATE_PATH="templates/$TEMPLATE"
RESULT_PATH="results/$TEMPLATE"
DATA_PATH="./invoice_data.json"

source venv/bin/activate

# generate html from template
python main.py "$TEMPLATE_PATH" -d "$DATA_PATH"

# generate pdf from html
weasyprint -s "$RESULT_PATH/invoice.css" "$RESULT_PATH/index.html" results/invoice-$(date +"%d%m%Y%H%M%S").pdf
