# Linear Regression System with CI/CD
A machine learning workflow featuring a linear regression system based on stochastic gradient descent.
The workflow is based on Github Actions. Upon pushing to the main branch, the following tasks are carried out:

- Run the unit tests using PyTest,
- Create a PyPi package and publish it to PyPi using package name 'lin2023',
- Create a Docker image and publish it to Docker Hub using image name 'lin2023',
- Deploy the Docker image to ...

## The Code
Cloning the code:
```
git clone https://github.com/budi-kurniawan/linear-regression
```

Installing the code:
```
pip install lin2023
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
