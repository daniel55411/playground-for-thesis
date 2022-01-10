FROM python:3.8

EXPOSE 5000

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

ENTRYPOINT ["flask", "run"]

CMD ["--host=0.0.0.0"]
