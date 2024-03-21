import logger

import telegram
import telegram.ext as tg
from telegram import Bot, Update
from telegram.constants import ParseMode
from telegram.ext import Application, ApplicationBuilder


TOKEN = "6105124264:AAFt9rKVqHkP774bQUqwf47eBsM0DQ57Y_I"BOT_ID = dispatcher.bot.id
BOT_NAME = dispatcher.bot.first_name
BOT_USERNAME = dispatcher.bot.username

TOKEN = "6105124264:AAFt9rKVqHkP774bQUqwf47eBsM0DQ57Y_I"

DB_NAME = ""
MONGO_DB_URI = ""

dispatcher = Application.builder().token(TOKEN).build()
function = dispatcher.add_handler

logging.basicConfig(
  level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

app = Client("Mikobot", api_id=API_ID, api_hash=API_HASH, bot_token=TOKEN)
tbot = TelegramClient(MemorySession(), API_ID, API_HASH)
# <=======================================================================================================>

# <=============================================== GETTING BOT INFO ========================================================>
# Get bot information
print("[INFO]: Getting Bot Info...")
BOT_ID = dispatcher.bot.id
BOT_NAME = dispatcher.bot.first_name
BOT_USERNAME = dispatcher.bot.username




