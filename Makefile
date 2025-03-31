.PHONY: build-front-end
build-front-end:
	docker build -t front-end ./nextjs-front-end

.PHONY: build-back-end
build-back-end:
	docker build -t back-end ./python-fastapi-s3aws-api

.PHONY: run-back-end
run-back-end:
	docker run \
	--name api \
	--env-file ./python-fastapi-s3aws-api/.env.local \
	-p 8000:8000 \
	api

.PHONY: run-front-end
run-front-end:
	docker run \
	--name front-end \
	-e API_URL=http://localhost:8000/generate-qr \
	-p 3000:3000 \
	front-end

.PHONY: run-both
run-both:
	$(MAKE) run-api & \
	$(MAKE) run-front-end