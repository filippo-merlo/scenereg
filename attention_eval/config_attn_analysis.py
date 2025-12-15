import os

# Base directory containing datasets, cache folders, and evaluation outputs.
data_dir_path = '../data'

# Annotation file for the selected dataset.
dataset_path = os.path.join(data_dir_path, 'VISIONS/S1_boundingbox_critical_object.csv')
#dataset_path = os.path.join(data_dir_path, 'COOCO/COOCO_data.json')

# Directory containing all dataset images.
images_path = os.path.join(data_dir_path, 'VISIONS/VISIONS_images')
#images_path = os.path.join(data_dir_path, 'COOCO/COOCO_images')

# Directories for storing model checkpoints and cached intermediate files.
model_dir = os.path.join(data_dir_path, 'cache')
cache_dir = os.path.join(data_dir_path, 'cache')

# Directory where evaluation outputs are written.
output_dir = os.path.join(data_dir_path, 'attn_eval_output')

# Directory for temporary intermediate files.
temporary_save_dir = os.path.join(data_dir_path, 'temporary_save')

# Path to the precomputed average attention matrices for each dataset.
avg_vis_attn_matrix_path = os.path.join(output_dir, 'vis_attn_matrix_average_VISIONS.pt')
#avg_vis_attn_matrix_path = os.path.join(output_dir, 'vis_attn_matrix_average_COOCO.pt')


