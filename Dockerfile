FROM python:3.6-alpine
COPY . /app
WORKDIR /app
RUN pip install pipenv \
    && pipenv install --system --deploy --ignore-pipfile
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:4000", "app:app"]