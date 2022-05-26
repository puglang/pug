.DEFAULT_GOAL: build
.PHONY: build

build: clean
	@tox -e build
	@pip install .

clean:
	@pip uninstall -y puglang
	@tox -e clean

test:
	@tox
