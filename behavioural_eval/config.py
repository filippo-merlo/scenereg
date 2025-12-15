import os

# Base directory containing the dataset, model cache, and evaluation outputs.
data_dir_path = '../data'

# Path to the COOCO dataset annotation file.
dataset_path = os.path.join(data_dir_path, 'COOCO/COOCO_data.json')

# Directory containing all COOCO images.
images_path = os.path.join(data_dir_path, 'COOCO/COOCO_images')

# Directories for storing downloaded HuggingFace models and cached files.
model_dir = os.path.join(data_dir_path, 'cache')
cache_dir = os.path.join(data_dir_path, 'cache')

# Directory where evaluation outputs are stored.
output_dir = os.path.join(data_dir_path, 'eval_output')

# Directory used for storing temporary intermediate files.
temporary_save_dir = os.path.join(data_dir_path, 'temporary_save')
