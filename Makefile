install:
    pip install -r requirements.txt

test:
    python app.py

# Run the app with a specific transformer model
run-model:
	python app.py --model $(MODEL)

