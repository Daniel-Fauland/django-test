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

- To start the web service run this command:
  ```shell
  docker-compose up
  ```
