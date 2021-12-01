FROM python:3.7

WORKDIR /usr/src/app

COPY . .

RUN pip3 install -r requirements.txt
RUN pip3 install python-dotenv
RUN export FLASK_APP=main.py

RUN chmod u+x startup.sh

EXPOSE 5432
EXPOSE 5000
CMD [ "./startup.sh" ]
