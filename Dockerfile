FROM python:3.8

WORKDIR /webhookTest

COPY requirements.txt .

RUN pip install -r requirements.txt

ENTRYPOINT bash -c "python3 main.py"