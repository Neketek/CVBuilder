.PHONY: all
all:


.PHONY: run
run:
	docker run -it --rm \
	-v $(shell pwd)/data:/cv/data \
	-v $(shell pwd)/templates:/cv/templates \
	-v $(shell pwd)/out/:/cv/out \
	cv:prod


.PHONY: build
build:
	docker build -f prod.Dockerfile --rm -t cv:prod .


.PHONY: devrun
devrun:
	docker run -it --rm \
	-v $(shell pwd):/cv \
	cv:dev

.PHONY: devbuild
devbuild:
	docker build -f dev.Dockerfile --rm -t cv:dev .
