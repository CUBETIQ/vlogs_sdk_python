
all: build install test

build:
	poetry build

install:
	pip3 install dist/*.whl --force-reinstall

test:
	poetry run python3 tests/test.py

clean:
	rm -rf dist

publish:
	poetry publish --build