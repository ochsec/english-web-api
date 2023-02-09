import string

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
                if word.lower().__contains__(schema.lower()):
                    relevant_schemas.append(schema)
        return [*set(relevant_schemas)]

    def add_relevant_schemas(self, txt):
        schemas_to_add = self.get_relevant_schemas(txt)
        for schema in schemas_to_add:
            txt += '\n' + self.schema_feed.schema_feed[schema]
        return txt

