.PHONY: test lint test test-cov

all: 
	export GOOGLE_APPLICATION_CREDENTIALS="dont-panic-auff-kee.json"

lint:
	flake8 main.py test_cloud_functions.py

test: all
	py.test -v
#	python -m unittest -v test_cloud_functions.py

test-cov: all
	py.test --cov
	# coverage run --source test_cloud_functions.py -m py.test

test-cov-lines: all
	pytest --cov-report term-missing --cov=functions test_cloud_functions.py
