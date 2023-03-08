# Linear Regression System with Github Actions Workflow
Code-named lin2023, this project features a linear regression system with a CI/CD workflow based on Github Actions. Upon pushing to the main branch, the following tasks are carried out:

- Run the unit tests using PyTest,
- Create a Docker image and publish it to Docker Hub using image name 'lin2023',
- Deploy the Docker image to Azure.

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
The code has been published as a PyPi package named 'lin2023'. The pyproject.toml and setup.cfg files are used for this purpose. The steps to package the code can be found on
https://packaging.python.org/en/latest/tutorials/packaging-projects/. Packaging is not part of the workflow because PyPi does not allow duplicate files of the same package. However, it is possible to publish a package as part of a Github Actions workflow. See https://packaging.python.org/en/latest/guides/publishing-package-distribution-releases-using-github-actions-ci-cd-workflows/.

To install the package, run the following command:
```
pip install lin2023
```

## Docker
A Docker image named lin2023 is published to Docker Hub every time the workflow is triggered.
To pull the Docker image, do this:
```
$ docker pull budi2020/lin2023[:tagName]
$ docker pull budi2020/lin2023:v0.0.3
```

To run the Docker image on port 5000, do the following:
```
$ docker run -i -p 80:80 -d budi2020/lin2023:v0.0.3

```

## Invoking the API
Use curl in Linux:
- curl -X GET http://ip_address:5000/
- curl -X POST -H "Content-Type: application/json" -d '{"input":500}' http://ip_address:5000/stream
- curl -X POST -H "Content-Type: application/json" -d '{"input":[100,200,500]}' http://ip_address:5000/batch

In production:
- curl -X GET https://lin2023.azurewebsites.net/
- curl -X POST -H "Content-Type: application/json" -d '{"input":500}' https://lin2023.azurewebsites.net/stream
- curl -X POST -H "Content-Type: application/json" -d '{"input":[100,200,500]}' https://lin2023.azurewebsites.net/batch

## Known Problems
The unit tests are currently commented out due to permission problems in Github Actions.

## Ideas for Improvement
- Write the version number as a text file
- Write more unit tests catering for more scenarios
- More error handling in the Flask functions
- Include the publication to PyPi in the workflow
