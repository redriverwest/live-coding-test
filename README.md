<p align="center">
  <img src="https://espaceconnecte.franceinvest.eu/uploads/company_images/65290e6e3c7c7774780278.svg" width="200" height="200" />
</p>

# Red River West - Live coding test

Hello, please run through the whole setup before the interview.

## Usage

You will be coding in the `src/main.py` file.

To run your code you can use the following command

With pipenv:  
`pipenv run start`

Without pipenv:  
`python -m src.main`

## Setup

We installing [Pipenv](https://pipenv.pypa.io/en/latest/) as a package manager for the project to handle the virtual environment and python versioning.

### Prerequisites

- Python 3.10+ (3.9 might work but not tested)
- Python package manger (pip or pipenv)

### Clone the repository

You can use the following command to run clone the repository into folder `/live-coding-test` and move into it

`git clone https://github.com/redriverwest/live-coding-test.git live-coding-test && cd live-coding-test`

### Package installation

With pipenv:  
`pipenv install`

Without pipenv:  
`pip install -r requirements.txt`

### Environment file

Create a file named `.env` with the content from `.env.example` and fill in the values. (`DATABASE_URL` will be provided during the interview)

### Database

During the interview we will provide you with a `DATABASE_URL` environment variable to set in your environment file. It would be nice if you could try with a local / free PostgreSQL database beforehand to make sure everything works.

You can get a free hosted PostgreSQL database through [Supabase](https://database.new) or [Neon](https://neon.tech)

### Test

Test your setup by running the following command

With pipenv:  
`pipenv run test`

Without pipenv:  
`python -m src.utils.test`
