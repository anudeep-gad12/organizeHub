from config_manager import load_config
from sorter import sort_file
import os


def sort_all_files(dir):
  for item in os.listdir(dir):
    item_path = os.path.join(dir, item)
    if os.path.isfile(item_path):
      sort_file(item_path)  


def main():
  config = load_config('../config/settings.json')
  watch_dir = config['watch_folder']
  sort_all_files(watch_dir)

if __name__ == "__main__":
  main()