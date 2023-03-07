# Linear Regression System with CI/CD

## The Code
Cloning the code:
```
git clone https://github.com/budi-kurniawan/linear-regression
```

Creating A Model:
```
python simple_linear_regrsssion.py
```
The model (model.sav file) will be saved to the current directory.

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

To pull the Docker image from Docker Hub
```
$ docker pull budi2020/lin2023[:tagName]
$ docker pull budi2020/lin2023:v0.0.1
```
