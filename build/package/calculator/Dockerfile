FROM golang:1.16-alpine
ADD . /app
WORKDIR /app
RUN cd /app/cmd/calculator && go build
FROM alpine
COPY --from=0 /app/cmd/calculator /app
CMD ["/app/calculator"]
