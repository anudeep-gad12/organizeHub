import os
import shutil
from config_manager import load_config
import logging

logging.basicConfig(filename='../logs/sorter.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(name)s %(message)s')


def sort_file(file_path):
  config = load_config('../config/settings.json')
  root, file_extension = os.path.splitext(file_path)
  file_name = os.path.basename(root)
  destination_dir = config['folder_mappings'].get(file_extension)


  try:

    if destination_dir is None:
      destination_dir = config['other_folder']
      shutil.move(file_path, destination_dir)
      logging.info("File moved to: %s", destination_dir)


  
    new_path = os.path.join(destination_dir, file_name + file_extension)
  
    counter = 1
    while os.path.exists(new_path):
      new_file_name = f"{file_name}_{counter}{file_extension}"
      new_path = os.path.join(destination_dir, new_file_name)
      counter += 1

    shutil.move(file_path, new_path)
    logging.info("File moved to: %s", destination_dir)

  except FileNotFoundError as e:
        logging.error(f"FileNotFoundError: {e}")
  except PermissionError as e:
      logging.error(f"PermissionError: {e}")
  except Exception as e:
      logging.error(f"Exception: {e}")






