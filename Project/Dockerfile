FROM python:3-alpine3.11
WORKDIR /playme
COPY . /playme/
RUN pip install -r requirements.txt
EXPOSE 5000
CMD python ./run.py