start:
	poetry run gunicorn -w 4 app:app

test:
	poetry run pytest
