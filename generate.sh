#!/usr/bin/env bash

TEMPLATE_PATH="templates/invoice-template-0"

# generate html from template
python main "$TEMPLATE_PATH"

# generate pdf from html
weasyprint -s "$TEMPLATE_PATH/invoice.css" "$TEMPLATE_PATH/invoice.html" results/invoice-$(date +"%d%m%Y%H%M%S").pdf