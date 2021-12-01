FROM node:14.18.1

WORKDIR /usr/src/app

COPY . .

RUN npm install 
# RUN npm start 
# RUN export REACT_APP_BACKEND_URL='http://127.0.0.1:5000'

EXPOSE 3000

CMD ["npm", "start" ]