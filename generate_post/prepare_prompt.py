import json

sentence_only_json = "do not include in your response any other words, " \
            "just the json object, your response will be parsed automatically as json string"
sentence_new_only = "in your response, include only the new json object, " \
                         "do not add the whole post object that you already sent"

sentence_product_only = "Your response should be only the new json object of the new product " \
                        "- do not include the whole post object"

sentence_before_after = "do not include any sentences before or after the json."


class PromptGenerator:

    def __init__(self, topic):
        self.topic = topic

    def get_prompt(self):
        with open('structure.json') as f:
            dict_str = json.loads(f.read())
        f = open("context", "r")
        intro = f.read()
        context = f"{intro}. Each post has this json structure: {str(dict_str)}"
        prompt = f"{context} I want to create a post in the above json object structure, about '{self.topic}'"
        prompt2 = f"{prompt} give me the post json object, as for the products and comments," \
                  f" leave them for now as empty arrays e.g. 'products': [], 'comments': []"
        return f"{prompt2} {sentence_only_json}"

    @staticmethod
    def get_product_prompt(i):
        return f"Please give a product no.{i+1} item as a standalone json object. " \
               f"{sentence_before_after}"  \
               f"{sentence_product_only}."

    @staticmethod
    def get_comments_prompt(n):
        return f"Please provide {n} standalone comments as a json array. " \
               f"do not include the whole post object. " \
               f"{sentence_before_after}"

