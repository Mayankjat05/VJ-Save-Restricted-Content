import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "23159366"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "4623dd30dd1303bddb729eb0862262d9")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://mayank:mayank@cluster0.dood4ni.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
