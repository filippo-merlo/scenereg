import os
import json

def load_dataset(dataset_path):
    # Load and preprocess data
    with open(dataset_path, 'r') as f:
        return json.load(f)

def get_images_names_path(images_path):
    # Load and preprocess images
    images_n_p = {}
    for filename in os.listdir(images_path):
        if filename.endswith('.jpg'):
            images_n_p[filename] = os.path.join(images_path, filename)
    return images_n_p

