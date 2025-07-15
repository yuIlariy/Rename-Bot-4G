import os



# Required Variables Config
API_ID = int(os.environ.get("API_ID", ""))
API_HASH = os.environ.get("API_HASH", "")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
ADMIN = int(os.environ.get("ADMIN", "6318135266"))


# Premium 4GB Renaming Client Config
STRING_SESSION = os.environ.get("STRING_SESSION", "")


# Log & Force Channel Config
FORCE_SUBS = os.environ.get("FORCE_SUBS", "modstorexd")
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001925329161"))


# Mongo DB Database Config
DATABASE_URL = os.environ.get("DATABASE_URL", "")
DATABASE_NAME = os.environ.get("DATABASE_NAME", "ubots")


# Other Variables Config
START_PIC = os.environ.get("START_PIC", "https://i.ibb.co/fzgHjXQn/1752254564132.png")
