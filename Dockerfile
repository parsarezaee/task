FROM python:3.10

ENV PYTHONUNBUFFERED 1

RUN mkdir /src
COPY ./src /src
WORKDIR /src/

# install requirements
ADD /src/requirements.txt /src/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
