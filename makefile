.PHONY: compose
compose: css
	python compose.py

.PHONY: css
css:
	npx node-sass index.scss build/index.css

.PHONY: pfreeze
pfreeze:
	pip freeze -l > requirements.txt
