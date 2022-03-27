# functions-from-zero
live training by Noah Gift from "Pagmatic AI Labs" Youtube Channel

[![Python application test with Github Actions](https://github.com/checkbox-org/functions-from-zero/actions/workflows/main.yml/badge.svg)](https://github.com/checkbox-org/functions-from-zero/actions/workflows/main.yml)


### To call Microservice

something like this
```bash
curl -X 'POST' \
  'https://checkbox-org-functions-from-zero-qp96797h4rpp-8080.githubpreview.dev/wiki' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "Microsoft"
}'
```


### Build container
`docker build .``
`docker image ls`

### Run container
Something like this:

`docker run -p 127.0.0.1:8080:8080 6bb47b5c4f0f`

### Invoke POST request

run `invoke.sh`
