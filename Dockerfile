FROM python:3.11.9-alpine3.19 as build
LABEL authors="Roman Zhulin, Anton Borovskikh"

ENV HOME=/home/app
RUN mkdir -p $HOME

ADD requirements.txt $HOME

WORKDIR $HOME
RUN pip install --no-cache-dir -r requirements.txt

FROM build

ADD . $HOME
WORKDIR $HOME

ENTRYPOINT [""]