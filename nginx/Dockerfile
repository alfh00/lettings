FROM nginx:1.19.0-alpine
WORKDIR /etc/nginx/
RUN rm /etc/nginx/conf.d/default.conf
COPY default.conf /etc/nginx/conf.d/
EXPOSE 80