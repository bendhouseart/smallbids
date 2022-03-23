getspec:
	@echo "Pulling bids-specification from github repository"
	git submodule update --init --recursive

installspecreqs:
	@echo "Installing python requirements from specification requirements.txt"
	cd bids-specification && poetry run pip install -r requirements.txt

installprojectreqs:
	@echo "Installing project level requirements e.g. main module requirements"
	poetry install

installreqs: installprojectreqs getspec installspecreqs