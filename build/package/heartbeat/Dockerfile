FROM golang:1.16-alpine
ADD . /app
WORKDIR /app
RUN cd /app/cmd/heartbeat && go build
FROM alpine
COPY --from=0 /app/cmd/heartbeat /app
CMD ["/app/heartbeat"]