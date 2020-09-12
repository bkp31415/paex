FROM python:3.8-slim

WORKDIR /paex

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./paxe .

CMD [ "python", "./main.py" ]
