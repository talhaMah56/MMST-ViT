# from huggingface_hub import snapshot_download

# snapshot_download(repo_id="fudong03/Tiny-CropNet", repo_type="dataset")
from huggingface_hub import snapshot_download
import shutil
import os

# Define your desired directory
desired_dir = "/mnt/Tiny-CropNet"

# Create the desired directory if it does not exist
if not os.path.exists(desired_dir):
    os.makedirs(desired_dir)

# Download the dataset to the temporary directory
snapshot_download(
    repo_id="fudong03/Tiny-CropNet",
    repo_type="dataset",
    cache_dir=desired_dir  # Specify a temporary directory
)
