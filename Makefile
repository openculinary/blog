.PHONY: build deploy image image-create image-finalize bundle

SERVICE=$(shell basename $(shell git rev-parse --show-toplevel))
REGISTRY=registry.openculinary.org
PROJECT=reciperadar

IMAGE_NAME=${REGISTRY}/${PROJECT}/${SERVICE}
IMAGE_COMMIT := $(shell git rev-parse HEAD)
IMAGE_TAG := $(strip $(if $(shell git status --porcelain --untracked-files=no), latest, ${IMAGE_COMMIT}))

build: image

deploy:
	kubectl apply -f k8s
	kubectl set image deployments -l app=${SERVICE} ${SERVICE}=${IMAGE_NAME}:${IMAGE_TAG}

image: image-create bundle image-finalize

image-create:
	$(eval container=$(shell buildah from docker.io/library/nginx:alpine))
	buildah copy $(container) 'etc/nginx' '/etc/nginx'

image-finalize:
	buildah copy $(container) 'public' '/usr/share/nginx/html/reciperadar'
	buildah copy $(container) 'public/posts' '/usr/share/nginx/html/reciperadar'
	buildah config --cmd '/usr/sbin/nginx -g "daemon off;"' --port 80 $(container)
	buildah commit --quiet --rm --squash $(container) ${IMAGE_NAME}:${IMAGE_TAG}

bundle:
	hugo
