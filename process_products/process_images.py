import os
import boto3
from PIL import Image


class ProcessImages:
    def __init__(self, image, object_path="images/posts",
                 sizes=[(360, 180), (720, 360), (1200, 600)],
                 formats=['jpg', 'webp'],
                 image_name=""):
        self.image = image
        self.image_name = image_name
        self.sizes = sizes
        self.formats = formats
        self.object_path = object_path

    def process_images(self):
        images = []
        for idx, size in enumerate(self.sizes):
            for fmt in self.formats:
                image_key = f"{self.image_name}.{fmt}"
                if len(self.sizes) > 1 and idx > 0:
                    image_key = f"{self.image_name}_{idx+1}x.{fmt}"
                local_output_image = f"images_out/{image_key}"
                s3_file_path = f"{self.object_path}/{image_key}"
                self.resize_image(self.image, local_output_image, size[0], size[1])
                images.append(self.upload_to_s3(local_output_image, s3_file_path))
        return images

    def resize_image(self, image, output_image_path, new_width, new_height):
        original_width, original_height = image.size
        aspect_ratio = float(original_width) / float(original_height)

        intermediate_height = int(new_width / aspect_ratio)
        intermediate_image = image.resize((new_width, intermediate_height), Image.ANTIALIAS)

        y_offset = (intermediate_height - new_height) // 2
        cropped_image = intermediate_image.crop((0, y_offset, new_width, new_height + y_offset))
        cropped_image.save(output_image_path)

    def upload_to_s3(self, file_path, s3_key):
        bucket_name = os.environ['AWS_S3_BUCKET']
        s3 = boto3.client('s3')
        s3.upload_file(file_path, bucket_name, s3_key)
        url = f"https://{bucket_name}.s3.amazonaws.com/{s3_key}"
        print(f"File uploaded to: {url}")
        return url


