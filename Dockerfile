FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
RUN pip install fastapi uvicorn websockets
COPY ./app /code/app 
COPY ./src /code/src
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "9000"]