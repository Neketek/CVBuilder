.PHONY: all
all:

.PHONY: drun
drun:
	docker run -it -v $(shell pwd):/cv cv:prod bash

.PHONY: dbuild
dbuild:
	docker build --rm -t cv:prod .
