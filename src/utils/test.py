import unittest
import sqlalchemy

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from src.utils.db import tables, session


class SetupTests(unittest.TestCase):
    def test_db_connection(self):
        """
        Test that the database connection is working
        """
        self.assertIsInstance(session, sqlalchemy.orm.session.Session)


if __name__ == '__main__':
    unittest.main()
