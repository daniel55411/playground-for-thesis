FROM python:3.8

EXPOSE 5000

COPY . .

RUN pip3 install -r requirements.txt

ENTRYPOINT ["flask", "run"]

CMD ["--host=0.0.0.0"]
