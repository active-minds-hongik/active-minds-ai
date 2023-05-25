FROM python:3.9.6

WORKDIR /test
COPY . .

RUN pip install -r requirements.txt
RUN apt-get update
RUN apt-get -y install libgl1-mesa-glx

EXPOSE 5000

CMD python ./app.py