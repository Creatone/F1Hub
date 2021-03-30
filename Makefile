define execute_in_venv
	source venv/bin/activate && $(1) && deactivate
endef

venv:
	@echo Preparing virtual environment.
	python3 -m venv venv
	$(call execute_in_venv, pip install -r requirements.txt)

run:
	$(call execute_in_venv, python main.py)


all: venv run
