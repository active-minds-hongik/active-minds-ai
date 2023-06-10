FROM python:3.9.6

WORKDIR /test
COPY . .

RUN pip uninstall -r requirements.txt -y && pip install --upgrade tensorflow && pip install -r requirements.txt && apt-get update && apt-get -y install libgl1-mesa-glx

EXPOSE 5000

CMD python ./app.py