lint:
	flake8 --exclude=.venv
start:
	.venv/bin/python3 main.py
clean:
	rm -rf .venv
install:
	python3 -m venv .venv
	source .venv/bin/activate && pip install -r requirements.txt