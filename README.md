# Linear Regression System with CI/CD

## The Code

## Run the unittest
```
python -m pytest
```

## Docker
```
Make sure an app directory has been created
$ cd $PROJECT_DIR
$ docker build --tag lin2023 .
$ docker run -i -p 5000:5000 -d lin2023
```

Pull a Docker image from Docker Hub
```
$ docker pull budi2020/lin2023[:tagName]
$ docker pull budi2020/lin2023:v0.0.1
```
