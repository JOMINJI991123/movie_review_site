import os

movie_images_path = "static/images"
files = os.listdir(movie_images_path)
movie_images_count = len(files)

print(movie_images_count)