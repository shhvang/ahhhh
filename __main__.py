import logging

from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler

from IO import *

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
  """Send a message when the command /start is issued."""
  user = update.effective_user
  await update.message.reply_html(
      rf"Hi {user.mention_html()}!",
  )

async def help(update: Update,
     context: ContextTypes.DEFAULT_TYPE) -> None:
  """Send a message when the command /help is issued."""
  await update.message.reply_text("Help!")


def main():
  function(CommandHandler("start", start))
  function(CommandHandler("help", get_help))

if __name__ == "__main__":
  try:
      LOGGER.info("Successfully loaded modules: " + str(ALL_MODULES))
      tbot.start(bot_token=TOKEN)
      app.start()
      main()
  except KeyboardInterrupt:
      pass
  except Exception:
      err = traceback.format_exc()
      LOGGER.info(err)
  finally:
      try:
          if loop.is_running():
              loop.stop()
      finally:
          loop.close()
      LOGGER.info(
          "------------------------ Stopped Services ------------------------"
      )