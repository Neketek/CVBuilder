.PHONY: all
all:
	echo "There is no default command"

.PHONY: css
css:
	npx node-sass index.scss index.css
