FROM matouskyncl/archlinux

RUN mkdir /code
RUN mkdir /logs

RUN pip install gunicorn

ADD requirements.txt ./

RUN pip install -r requirements.txt

ADD ./ /code/

WORKDIR /code
