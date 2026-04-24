import kagglehub

# Download latest version
path = kagglehub.dataset_download("aadigupta1601/lapd-crime-data-2020-2024")

print("Path to dataset files:", path)