.PHONY: test lint test test-cov

all: ;

lint:
	flake8 main.py test_cloud_functions.py

test: all
	py.test -v
#	python -m unittest -v test_cloud_functions.py

test-cov: all
	py.test --cov
	# coverage run --source test_cloud_functions.py -m py.test
