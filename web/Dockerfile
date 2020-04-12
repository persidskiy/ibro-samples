FROM alpine:3.11.5

COPY entrypoint.sh /entrypoint.sh

RUN \
    chmod +x /entrypoint.sh && \
    apk add --update --no-cache python3 && \
    pip3 install --upgrade pip && \
    pip3 install flask gunicorn

EXPOSE 8080

COPY src /

ENTRYPOINT ["/entrypoint.sh"]
