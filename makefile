.PHONY: compose
compose: css
	python compose.py

.PHONY: css
css:
	npx node-sass index.scss build/index.css
	npx postcss build/index.css -u autoprefixer -r

.PHONY: pfreeze
pfreeze:
	pip freeze -l > requirements.txt

.PHONY: pdf
pdf: compose
	wkhtmltopdf -T 0 -B 0 -L 0 -R 0 --page-width 26cm --page-height 115cm build/index.html cv.pdf

.PHONY: printpdf
printpdf:
	wkhtmltopdf -T 0 -B 0 -L 0 -R 0 --page-size A4 build/index.html print-cv.pdf
