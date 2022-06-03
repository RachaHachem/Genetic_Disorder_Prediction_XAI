FROM python:3.9

RUN set -ex && mkdir /Genetic_Disorder_Prediction_XAI

WORKDIR /Genetic_Disorder_Prediction_XAI

COPY requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

COPY ./disorder_model.py

COPY . ./

EXPOSE 8000

ENV PYTHONPATH /Genetic_Disorder_Prediction_XAI

CMD python3 /Genetic_Disorder_Prediction_XAI/flask_app.py