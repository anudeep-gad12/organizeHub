# Organize Hub

Sick of messy files? Let **Organize Hub** bring order to your chaos. This Python script sorts files based on their extensions using a slick configuration file. Say goodbye to clutter and hello to organization.

##  Installation

1. **Clone the Beast:**

    ```bash
    git clone https://github.com/anudeep-gad12/organizeHub
    ```

2. **Dive into the Source:**

    ```bash
    cd organizeHub/src
    ```

3. **Config Magic:**

    Ensure that you have a `settings.json` file in the `config` directory. This file should contain a `folder_mappings` object that maps file extensions to directories. Example:

    ```json
    {
      "folder_mappings": {
        ".txt": "text_files",
        ".jpg": "images"
      }
    }
    ```

##  Usage

Run the script with Python 3, passing the path to the file you want to sort as an argument:

```bash
python main.py /path/to/file
```

## Scheduling

**Automate your sorting with ease:**

For Windows: 
- Create a .bat file:
```bash
@echo off
cd /d "path\to\file-sorter\src"
python main.py
```
- Schedule it using Windows Task Scheduler to run this .bat file at your desired intervals.

For Linux and Mac: 
- Set up cron jobs to schedule the script. Example to run it daily at midnight:
```bash
0 0 * * * /usr/bin/python3 /path/to/organizeHub/src/main.py
```


- All actions are logged to sorter.log in the logs directory. Logs include timestamps, log levels, and messages, so you know exactly what's going down.








