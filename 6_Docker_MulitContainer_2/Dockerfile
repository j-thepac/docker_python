FROM python:3.8.0-slim
COPY ./app /home/app/
WORKDIR /home/app/
RUN pip install -r requirements.txt
EXPOSE 5000
ENTRYPOINT ["python3", "Person.py"]
