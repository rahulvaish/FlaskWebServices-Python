FROM python:3.6.7-alpine3.8

ENV workdir="/usr/src/app"

WORKDIR $workdir

COPY ./my_project $workdir
COPY ./requirements.txt $workdir

RUN apk update
RUN apk add nginx
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN chmod 555 run.sh

EXPOSE 5000

CMD ./run.sh
