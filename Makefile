default: run

run:
	docker build -t parsegit .
	docker run --rm parsegit
