.PHONY: all
all:


.PHONY: run
run:
	docker run -it \
	-v $(shell pwd)/data:/cv/data \
	-v $(shell pwd)/templates:/cv/templates \
	cv:prod bash


.PHONY: build
build:
	docker build --rm -t cv:prod .


.PHONY: devrun
devrun:
	docker run -it \
	-v $(shell pwd):/cv \
	cv:dev bash


.PHONY: devbuild
devbuild:
	docker build -f dev.Dockerfile --rm -t cv:dev .
