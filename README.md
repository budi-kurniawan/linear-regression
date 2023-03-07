# Linear Regression System with CI/CD
A machine learning workflow featuring a linear regression system based on stochastic gradient descent.
The workflow is based on Github Actions. Upon pushing to the main branch, the following tasks are carried out:

- Run the unit tests using PyTest,
- Create a Docker image and publish it to Docker Hub using image name 'lin2023',
- Deploy the Docker image to ...

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

## Running Unit Tests
```
python -m pytest
```

## Packaging the Code
The code has been published as a PyPi package named 'lin2023'. The steps to package the code can be found on
https://packaging.python.org/en/latest/tutorials/packaging-projects/. Packaging is not part of the workflow because PyPi does not allow duplicate files of the same package.

To install the package, run the following command:
```
pip install lin2023
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
