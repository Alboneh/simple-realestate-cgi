FROM nginx:latest

RUN apt-get update && \
    apt-get install -y python3 fcgiwrap spawn-fcgi && \
    rm -rf /var/lib/apt/lists/*

COPY nginx.conf /etc/nginx/nginx.conf

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

CMD service fcgiwrap start && chmod 777 /var/run/fcgiwrap.socket && nginx -g "daemon off;"

