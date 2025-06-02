FROM python:slim-bullseye
WORKDIR /client
ENV SERVER_IP="127.0.0.1"
ENV SERVER_PORT="65432"
COPY . . 
CMD ["python", "echoClient.py"]
