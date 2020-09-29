FROM python:3

WORKDIR /app
RUN pip install flask flask_httpauth flask_jwt_extended flask_caching

COPY simple-app.py .

ENTRYPOINT [ "python", "simple-app.py" ]