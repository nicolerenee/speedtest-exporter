GIT_BRANCH  := $(shell git rev-parse --abbrev-ref HEAD)
GIT_HASH    := $(shell git rev-parse --short HEAD)

IMAGE_NAME = quay.io/nicolerenee/speedtest-exporter:$(GIT_BRANCH)-$(GIT_HASH)

build-image:
	docker build -t $(IMAGE_NAME) .

push-image:
	docker push $(IMAGE_NAME)

run-image:
	docker run --rm -it --net host $(IMAGE_NAME)

run-shell:
	docker run --rm -it --net host $(IMAGE_NAME) /bin/bash
