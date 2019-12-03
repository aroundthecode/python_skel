all: build

build:
	@./venv/bin/pip install wheel
	@./venv/bin/python setup.py sdist bdist_wheel

test:
	@pytest --flake8 --cov=myproject --cov-report term-missing

test_report:
	@pytest --flake8 --cov=myproject --cov-report html

clean:
	@rm -rf dist build *.egg-info

