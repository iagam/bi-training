from dotenv import load_dotenv
load_dotenv("/home/ubuntu/bi-training/.env")

ANALYTICS_DB_USERNAME = os.environ["ANALYTICS_DB_USERNAME"]
ANALYTICS_DB_PASSWORD = os.environ["ANALYTICS_DB_PASSWORD"]
ANALYTICS_DB_HOST = os.environ["ANALYTICS_DB_HOST"]
ANALYTICS_DB_NAME = os.environ["ANALYTICS_DB_NAME"]
