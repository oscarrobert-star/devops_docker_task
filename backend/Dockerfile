FROM python:3.7

WORKDIR /usr/src/app

COPY . .

RUN pip3 install -r requirements.txt
RUN pip3 install python-dotenv
RUN export FLASK_APP=main.py

RUN chmod u+x startup.sh
# RUN export DATABASE_URL='postgresql://ajua:ajuapass@localhost:5432/ajua'
# RUN flask db init
# RUN flask db migrate
# RUN flask db upgrade

CMD [ "./startup.sh" ]
