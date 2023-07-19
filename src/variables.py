import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv("../.env"))

USERNAME = os.environ.get("user_name")
PASSWORD = os.environ.get("password")
JENKINSURL = os.environ.get("jenkins_url")