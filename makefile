.PHONY: all
all:
	echo "There is no default command"

.PHONY: css
css:
	npx node-sass index.scss index.css

.PHONY: pfreeze
pfreeze:
	pip freeze -l > requirements.txt

.PHONY: compose
compose: css
	python compose.py
