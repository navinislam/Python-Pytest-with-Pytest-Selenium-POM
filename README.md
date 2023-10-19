
## Structure
The overall directory structure is as follows
* **pages**: Page Object Model based framework page files, with functions and constants related to the major pages
* **tests**: UI tests

### Environment Setup

1. Global Dependencies
    * [Install Python](https://www.python.org/downloads/)
    * Or Install Python with [Homebrew](http://brew.sh/)
    ```
    $ brew install python
    ```
    * Install [pip](https://pip.pypa.io/en/stable/installing/) for package installation 
   
2. Project
  * The recommended way to run your tests would be in [virtualenv](https://virtualenv.readthedocs.org/en/latest/). It will isolate the build from other setups you may have running and ensure that the tests run with the specified versions of the modules specified in the requirements.txt file.
  ```$ pip install virtualenv```
  * Create a virtual environment in your project folder the environment name is arbitrary.
  ```$ virtualenv venv```
  * Activate the environment:
  ```$ source venv/bin/activate```
  * Install the required packages:
  ```$ make install or pip install -r requirements.txt```
### Environment Variables:
    To run locally WITHOUT docker:
* install direnv https://direnv.net/docs/installation.html
* create an .envrc file with the following:
  *    ```
       #!/bin/bash
       source venv/bin/activate
       export URI=https://www.saucedemo.com
       export HUB=http://localhost:4444/wd/hub 
* Run ```` direnv allow .envrc````
* For docker compose and running tests on docker
  * Edit the docker-compose.yml file for the following env var only
    * ```    
      environment:
      - URI=https://saucedemo.com/```
### Running Tests: 

*  Run tests locally and produce html report in root directory: To run tests in parallel run:
    ```
      make test-local
    ```
*  To run all in a docker container
    ```
      make test-docker
    ```
* Clean up containers
    ```
  make teardown
  ```
