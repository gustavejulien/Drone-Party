FROM node:14.17.1-alpine3.12

COPY ./ /app/
WORKDIR /app/
RUN npm install
RUN npx tsc
EXPOSE 8000

CMD npm start