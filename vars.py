

from os import environ

API_ID = int(environ.get("API_ID", "26331872"))
API_HASH = environ.get("API_HASH", "c93589620441707c37c5683a02eea54e")
BOT_TOKEN = environ.get("BOT_TOKEN", " ")

# Force Subscribe Configuration
FORCE_SUB_CHANNEL = environ.get("FORCE_SUB_CHANNEL", "roxybasicneedbot1")  # Channel username without @, 
FORCE_SUB_CHANNEL_LINK = environ.get("FORCE_SUB_CHANNEL_LINK", "https://t.me/roxybasicneedbot1")  # Channel link

# Admin Configuration
ADMINS = list(map(int, environ.get("ADMINS", "8413546109").split()))

# Optional: Bot Owner ID
OWNER_ID = int(environ.get("OWNER_ID", "8413546109"))

# Database URL (if you want to add database support later)
DATABASE_URL = environ.get("DATABASE_URL", "")


