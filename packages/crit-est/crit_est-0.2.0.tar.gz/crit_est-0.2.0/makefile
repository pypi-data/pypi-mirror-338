PYTHON?=python


all: build upload clean


build: pypi-req
	$(PYTHON) setup.py sdist bdist_wheel

pypi-req:
	$(PYTHON) -m pip install -r pypi_requirements.txt

upload:
	$(PYTHON) -m twine upload dist/*

clean:
	rm -rf build *.egg-info dist