FROM python:alpine3.7
WORKDIR /code

COPY requirements.txt requirements.txt


COPY . .
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["App.py"]