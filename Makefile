.PHONY: build deploy image image-create image-finalize bundle

SERVICE=$(shell basename $(shell git rev-parse --show-toplevel))
REGISTRY=registry.openculinary.org
PROJECT=reciperadar

IMAGE_NAME=${REGISTRY}/${PROJECT}/${SERVICE}
IMAGE_COMMIT := $(shell git rev-parse --short HEAD)
IMAGE_TAG := $(strip $(if $(shell git status --porcelain --untracked-files=no), latest, ${IMAGE_COMMIT}))

build: image

deploy:
	kubectl apply -f k8s
	kubectl set image deployments -l app=${SERVICE} ${SERVICE}=${IMAGE_NAME}:${IMAGE_TAG}

image: image-create bundle image-finalize

image-create:
	$(eval container=$(shell buildah --storage-opt overlay.mount_program=/usr/bin/fuse-overlayfs from docker.io/library/nginx:alpine))

image-finalize:
	buildah copy ${container} 'public' '/usr/share/nginx/html'
	buildah copy ${container} 'public/posts' '/usr/share/nginx/html'
	buildah config --port 80 --cmd '/usr/sbin/nginx -g "daemon off;"' $(container)
	buildah commit --quiet --rm --squash --storage-opt overlay.mount_program=/usr/bin/fuse-overlayfs $(container) ${IMAGE_NAME}:${IMAGE_TAG}

bundle:
	hugo
