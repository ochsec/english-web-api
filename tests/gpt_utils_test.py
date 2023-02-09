import unittest
from lib.gpt_utils import GptUtil
from database.schema_feed import SchemaFeed

class TestGptUtils(unittest.TestCase):

    def setUp(self):
        self.q1 = 'Write a SQL query to list all the films that actor "Julia Zellweger" was in and sort the films by category.\nUse the following table schemas as a reference:'
        self.schema_feed = SchemaFeed()
        self.gpt_util = GptUtil(self.schema_feed)

    def test_get_relevant_schemas(self):
        relevant_schemas = self.gpt_util.get_relevant_schemas(self.q1)
        self.assertListEqual(sorted(relevant_schemas), ['actor', 'category', 'film'])

    def test_add_relevant_schemas(self):
        q1_modified = self.gpt_util.add_relevant_schemas(self.q1)
        self.assertIn('TABLE actor', q1_modified)
        self.assertIn('TABLE category', q1_modified)
        self.assertIn('TABLE film', q1_modified)

if __name__ == '__main__':
    unittest.main()