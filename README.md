Steps to Install and run in new environment

1: Clone the code
    Command: `git clone https://github.com/ganesh35palkar/Weather.git`

2: Move To Folder Code
    Command cd `Weather`

3: Install pip
    Command: `sudo apt-get install python-pip`

4: Run requirement file
    Command: `pip install -r requirements.txt`

5. Change username password and db name in settings if required

6:Run Migrations:
    command: `./manage.py migrate`


Data Loading script

1. Load data directly from JSON files of S3
    `./manage.py loadDataset`

2. Load data from S3 JSON files and load in our system through via APIs
    `./manage.py loadDatasetAPI http://localhost:8000`

2. Verify data of S3 JSON files with data in our system through via APIs
    `./manage.py verifyDatasetAPI http://localhost:8000`

