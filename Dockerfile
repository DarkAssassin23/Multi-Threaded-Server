FROM alpine:latest
WORKDIR /server  
COPY . ./
RUN apk add make build-base && \
	make && \
	apk --purge del make build-base && \
	rm -rf *.o
EXPOSE 8989
CMD ["./server"]
