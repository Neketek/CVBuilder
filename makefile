.PHONY: compose
compose: css
	python compose.py

.PHONY: css
css:
	npx node-sass index.scss build/index.css

.PHONY: pfreeze
pfreeze:
	pip freeze -l > requirements.txt

.PHONY: pdf
pdf: compose
	wkhtmltopdf -T 0 -B 0 -L 0 -R 0 --page-width 30cm --page-height 68cm build/index.html cv.pdf
