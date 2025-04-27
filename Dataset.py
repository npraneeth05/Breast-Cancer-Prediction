pip install kaggle

import os
from kaggle.api.kaggle_api_extended import KaggleApi

# Set up Kaggle credentials (skip if you already set it up globally)
os.environ['KAGGLE_USERNAME'] = 'your_username'
os.environ['KAGGLE_KEY'] = 'your_key'

# Authenticate Kaggle API
api = KaggleApi()
api.authenticate()

# Download and unzip the dataset
api.dataset_download_files(
    'aryashah2k/breast-ultrasound-images-dataset',  # Dataset identifier
    path='./data',    # Save path
    unzip=True        # Automatically unzip
)
