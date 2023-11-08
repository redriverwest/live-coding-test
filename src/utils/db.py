import os
import unittest
import warnings

import sqlalchemy
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base

import dotenv

dotenv.load_dotenv()
warnings.filterwarnings('ignore')

# Get database URL from environment variables
DATABASE_URL = os.environ.get('DATABASE_URL', None)

# Ensure the database URL is set
if not DATABASE_URL:
    raise ValueError(
        'Could not find DATABASE_URL in environment variables')

# Connect to the database
connection = create_engine(DATABASE_URL)

# Reflect the database schema
schema = automap_base()
schema.prepare(connection, reflect=True)

session = Session(connection)
tables = schema.classes
