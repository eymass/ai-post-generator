import datetime
import os
import openai
import json

from generate_post.execute_conversation import ConversationExecutor


class PostGenerator:
    def __init__(self, post_key, topic, products_count):
        openai.api_key = os.environ['OPENAI_API_KEY']
        if openai.api_key == "":
            print("OPENAI_API_KEY is not set")
            exit(1)
        self.post_key = post_key
        self.products_count = products_count
        self.topic = topic

    def generate_post_content(self):
        return ConversationExecutor(api_key=openai.api_key,
                                    products_count=self.products_count)\
            .generate_post_json(self.topic)

    def add_static_data(self, post):
        post["date"] = datetime.datetime.now().isoformat()
        post["formattedDate"] = datetime.datetime.now().strftime("%m/%d/%Y")
        post["thumbnail"] = {"src": f"thumb/{self.post_key}_thumb"}
        post["images"] = [{"src": f"{self.post_key}1"}, {"src": f"{self.post_key}2"}]
        return post

    @staticmethod
    def save_to_json(post_object, file_name):
        with open(file_name, "w") as outfile:
            json.dump(post_object, outfile, indent=4)

    def create_post(self):
        output_file_name = f"{self.post_key}.json".lower()
        post_content = self.generate_post_content()
        updated_post = self.add_static_data(post_content)
        print(updated_post)
        self.save_to_json(updated_post, output_file_name)
