TAG=root/accountsdb
VERSION=latest
META=root_accountsdb

default: build

build: 
	docker build . --label $(META) -t $(TAG):$(VERSION)  &&  echo "===" && docker images | grep $(TAG)

run: 
	docker run -p 0.0.0.0:3306:3306 --rm -i -t $(TAG):$(VERSION) 
 
console: 
	docker run -p 0.0.0.0:3306:3306 --rm -i -t $(TAG):$(VERSION) /bin/bash

