import sys
from generate_post.generate_post import PostGenerator

if len(sys.argv) < 3:
    print("Usage: python generate_post.py <post_topic> <post_key> <products_count>")
    exit(1)
p_topic = sys.argv[0]
p_key = sys.argv[1]
p_count = sys.argv[2]
PostGenerator(topic=p_topic, post_key=p_key, products_count=p_count).create_post()
