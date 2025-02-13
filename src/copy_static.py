import os
import shutil

def copy_static_files(source_dir, dest_dir):
    if os.path.exists(dest_dir):
        print(f"Removing existing directory: {dest_dir}") # Debug print
        shutil.rmtree(dest_dir)
    print(f"Creating root directory: {dest_dir}") # Debug print
    os.mkdir(dest_dir)
    for item in os.listdir(source_dir):
        source_path = os.path.join(source_dir, item)
        dest_path = os.path.join(dest_dir, item)
        _copy_item(source_path, dest_path)

def _copy_item(source_path, dest_path):
    if os.path.isfile(source_path):
        print(f"Copying file: {source_path} -> {dest_path}") # Debug print
        shutil.copy(source_path, dest_path)
    elif os.path.isdir(source_path):
        print(f"Creating directory: {dest_path}") # Debug print
        os.mkdir(dest_path)
        for item in os.listdir(source_path):
            _copy_item(os.path.join(source_path, item), os.path.join(dest_path, item))
        