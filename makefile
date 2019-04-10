.PHONY: all
all:

.PHONY: pfreeze
pfreeze:
	pip freeze -l > requirements.txt
