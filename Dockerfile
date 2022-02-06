ARG GOLANG_VERSION
ARG ALPINE_VERSION

# build
FROM golang:${GOLANG_VERSION}-alpine${ALPINE_VERSION} AS builder

RUN apk --no-cache add make git; \
    adduser -D -h /tmp/dummy dummy

USER dummy

WORKDIR /tmp/dummy

COPY --chown=dummy Makefile Makefile
COPY --chown=dummy go.mod go.mod

RUN go mod download

ARG VERSION
ARG APPNAME

COPY --chown=dummy main.go main.go
COPY --chown=dummy index.html index.html

RUN make build

# execute
FROM alpine:${ALPINE_VERSION}

ARG VERSION
ARG APPNAME

ENV SERVER_PORT ""

COPY --from=builder /tmp/dummy/${APPNAME}-${VERSION} /usr/bin/${APPNAME}
COPY --from=builder /tmp/dummy/index.html /index.html

CMD ["geolocator"]
