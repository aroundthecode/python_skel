all: build

BUILDNUM := $(shell cat build.info)

venv:
	@python -m venv venv
	@venv/bin/pip install -r requirements.txt
	@echo
	@echo "  *** remember to activate venv with ***"
	@echo "  source ./venv/bin/activate"

bootstrap:
	@pip install -e ".[test]"

build:
	@./venv/bin/pip install wheel
	@./venv/bin/python setup.py sdist bdist_wheel

test:
	@pytest --flake8 --cov=myproject --cov-report term-missing

test_report:
	@pytest --flake8 --cov=myproject --cov-report html

clean:
	@rm -rf dist build *.egg-info

