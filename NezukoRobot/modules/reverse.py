import os

from GoogleSearch import Search
from telegram import (InlineKeyboardButton, InlineKeyboardMarkup,
                      MessageEntity, Update)
from telegram.ext import CallbackContext
from NezukoRobot import dispatcher
from NezukoRobot.modules.disable import DisableAbleCommandHandler


def grs(update: Update, context: CallbackContext):
    message = update.effective_message
    args = context.args
    
    if args:
        if len(args) <= 1:
            url = args[0]
            if url.startswith(("https://", "http://")):
                msg = message.reply_text("Uploading url to google..")

                result = Search(url=url)
                name = result["output"]
                link = result["similar"]
                
                msg.edit_text("ara ara matte ...")
                msg.edit_text(
                text=f"{name}",
                reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    text="Similar",
                                    url=link,
                                ),
                            ],
                        ],
                    )
                )
                return
        else:
            message.reply_text("Command must be used with a reply to an image or should give url")
    
    elif message.reply_to_message and message.reply_to_message.photo:
        edit = message.reply_text("Downloading Image")

        photo = message.reply_to_message.photo[-1]
        file = context.bot.get_file(photo.file_id)
        file.download("reverse.jpg")

        edit.edit_text("Downloaded Image, uploading to google...")

        result = Search(file_path="reverse.jpg")
        edit.edit_text("Uploaded to google, fetching results...")
        name = result["output"]
        link = result["similar"]

        edit.edit_text(
            text=f"{name}",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="Similar",
                            url=link,
                        ),
                    ],
                ],
            )
        )
        return
    else:
        message.reply_text("Command should be used with replying to an image or url should given.")

GRS_HANDLER = DisableAbleCommandHandler("grs", grs, run_async=True)
dispatcher.add_handler(GRS_HANDLER)

__help__ = """
Reverse search any image using google image search.
Usage:
    - sending /reverse by replying to any image
    - /reverse https://sample.com/sample.jpg
    - /grs wAifu or Husbandro
"""

__mod_name__ = "Reverse"
