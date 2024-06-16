# django-test

Test project for Django

## Installation

Everything is run with Docker in this project so the only requirement to run this locally is having Docker installed.

If you want to create a new django project run this command:

```shell
docker-compose run --rm app sh -c "django-admin startproject app ."
```

Note: This is not necessary in this case as the project already exists.

## Usage

- To build a docker image using the `prod` version run the following command:

  ```shell
  docker build .
  ```

- To build a docker image using the `dev` version run the following command:

  ```shell
  docker-compose build
  ```

- To run a linting test execute the following command:

  ```shell
  docker-compose run --rm app sh -c "flake8"
  ```

- To run a unit test execute the following command:

  ```shell
  docker-compose run --rm app sh -c "python manage.py test"
  ```

- To start the web service run this command:
  ```shell
  docker-compose up
  ```

## Explanation stuff

### Postgres connector

A postgres connector is needed to allow django to connect with Postgres. The most popular package is `psycopg2`. This package however needs additional packages to be build as this will be compiled from source when the package is installed. Therefore in the [DOCKERFILE](./Dockerfile) the required dependencies will be installed first before running pip install:

```
apk add --update --no-cache postgresql-client && \
apk add --update --no-cache --virtual .tmp-build-deps \
    build-base postgresql-dev musl-dev libpq-dev
```

After the installation of the python packages this can be removed as it was only required to compile the `psycopg2` package:

```
apk del .tmp-build-deps
```
