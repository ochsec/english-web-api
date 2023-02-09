from pprint import pprint
from lib.gpt_params import gpt_params
from lib.gpt_utils import GptUtil
from database.schema_feed import SchemaFeed

if __name__ == '__main__':
    q1 = 'Write a SQL query to list all the films that actor "Julia Zellweger" was in and sort the films by category.\nUse the following table schemas as a reference:'
    schema_feed = SchemaFeed()
    gpt_util = GptUtil(schema_feed)
    q1_modified = gpt_util.add_relevant_schemas(q1)
    with open('q1_modified.txt', 'w') as f:
        f.write(q1_modified)
    gpt_resp = gpt_util.get_completion(q1_modified, gpt_params)
    with open('gpt_resp.txt', 'w') as f:
        f.write(gpt_resp.choices[0].text)
