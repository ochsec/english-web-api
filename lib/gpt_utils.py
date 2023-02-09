import string
import openai
from dotenv import dotenv_values

class GptUtil:

    def __init__(self, schema_feed):
        self.schema_feed = schema_feed

    def remove_punctuation(self, txt):
        new_txt = txt.translate(str.maketrans('', '', string.punctuation))
        return new_txt

    def get_relevant_schemas(self, txt):
        relevant_schemas = []
        words = self.remove_punctuation(txt).split(' ')
        for word in words:
            for schema in self.schema_feed.schema_list:
                if schema.lower().__contains__(word.lower()):
                    relevant_schemas.append(schema)
        return [*set(relevant_schemas)]

    def add_relevant_schemas(self, txt):
        schemas_to_add = self.get_relevant_schemas(txt)
        for schema in schemas_to_add:
            txt += '\n' + self.schema_feed.schema_feed[schema]
        return txt

    def get_completion(self, prompt, gpt_params):
        env_config = dotenv_values('.env')
        openai.api_key = env_config['OpenAiKey']

        response = openai.Completion.create(
            model=gpt_params['model'],
            prompt=prompt,
            temperature=gpt_params['temperature'],
            max_tokens=gpt_params['max_tokens'],
            top_p=gpt_params['top_p'],
            frequency_penalty=gpt_params['frequency_penalty'],
            presence_penalty=gpt_params['presence_penalty']
        )

        return response