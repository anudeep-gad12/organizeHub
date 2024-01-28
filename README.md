# File Sorter

This Python script sorts files based on their extensions. It uses a configuration file to determine where to move files of each type.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/anudeep-gad12/organizeHub
cd src

```

2. Ensure that you have a settings.json file in the config directory. This file should contain a folder_mappings object that maps file extensions to directories. For example:

```json
{
  "folder_mappings": {
    ".txt": "text_files",
    ".jpg": "images"
  }
}
```

3. Run the script with Python 3, passing the path to the file you want to sort as an argument:

```python
python3 sorter.py <file-path>
```

4. If you'd like to schedule it

For Windows: Create a .bat file and use Windows task scheduler to run this .bat file.

```
@echo off
cd /d "path\to\file-sorter\src"
python main.py

```

For Linux and Mac: setup cron jobs

Logging
The script logs its activity to a file named sorter.log in the logs directory. The log includes timestamps, log levels, and messages.
