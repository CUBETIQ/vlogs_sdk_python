
all: build install test

build:
	make clean && poetry build

install:
	pip3 install dist/*.whl --force-reinstall

test:
	poetry run pytest

clean:
	rm -rf dist && pip3 uninstall -y vlogs

publish:
	poetry publish --build