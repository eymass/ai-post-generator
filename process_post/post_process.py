import json

from process_products.process_images import ProcessImages


class PostProcess:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_json_file(self):
        with open(self.file_path, 'r') as file:
            data = json.load(file)
        return data

    def get_products(self, data):
        return data.get('products', [])

    def get_image_sources(self, data):
        images = data.get('images', [])
        return [image.get('src') for image in images]

    def extract_asin_from_product(self, product):
        return product.get('asin')

    def get_asins_from_products(self, products):
        asins = []
        for product in products:
            asin = self.extract_asin_from_product(product)
            if asin:
                asins.append(asin)
        return asins

    def process_post(self):
        data = self.read_json_file()
        products = self.get_products(data)
        sources = self.get_image_sources(data)

        # main images
        for src in sources:
            ProcessImages({"url": src, "name": src}).process_images()

        # thumbnail
        ProcessImages({"url": sources[0], "name": f"{sources[0]}_thumb"},
                      object_path="images/thumb",
                      sizes=[(100, 100)],
                      formats=['jpg', 'webp']).process_images()

        # products
        keys = self.get_asins_from_products(products)
        for key in keys:
            ProcessImages({"url": key, "name": key}, sizes=[(250, 250)]).process_images()


if __name__ == '__main__':
    post_processor = PostProcess('post.json')
    post_processor.process_post()
