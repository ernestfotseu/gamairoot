FROM python:3.6

RUN mkdir /gamaicode
WORKDIR /gamaicode

RUN pip3 install django>=4.0
# RUN pip3 install -r requirements.txt
RUN pip3 install -U  django-sitetree
RUN pip3 install requests
RUN pip3 install psycopg2
RUN pip3 install psycopg2-binary
RUN pip3 install plotly==4.5.0
RUN pip3 install pandas
RUN pip3 install Pillow
RUN pip3 install django-filter

COPY . /gamaicode

