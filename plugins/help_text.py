#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @vloggerdeven_TG
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os
import time

# the secret configuration specific things
if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

# the Strings used for this "thing"
from translation import Translation

import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)
from pyrogram import filters 
from pyrogram import Client as Mai_bOTs

#from helper_funcs.chat_base import TRChatBase
from helper_funcs.display_progress import progress_for_pyrogram

from pyrogram.errors import UserNotParticipant, UserBannedInChannel 
from pyrogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
# https://stackoverflow.com/a/37631799/4723940
from PIL import Image
from database.database import *
from database.db import *


@Mai_bOTs.on_message(pyrogram.filters.command(["help"]))
async def help_user(bot, update):
    update_channel = Config.UPDATE_CHANNEL
    if update_channel:
        try:
            user = await bot.get_chat_member(update_channel, update.chat.id)
            if user.status == "kicked":
               await update.reply_text("SORRY, YOU'RE BANNED!")
               return
        except UserNotParticipant:
            await update.reply_text(
                text="**DUE TO THE HUGE TRAFFIC ONLY CHANNEL MEMBERS CAN USE THIS BOT. YOU NEED TO JOIN THE BELLOW MENTIONED CHANNEL BEFORE USING ME!**",
                reply_markup=InlineKeyboardMarkup([
                    [ InlineKeyboardButton(text="🔰 JOIN CHANNEL 🔰", url=f"https://t.me/{update_channel}")]
              ])
            )
            return
        else:
            await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HELP_USER,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('📝 RENAME', callback_data = "rnme"),
                    InlineKeyboardButton('📂 FILE TO VIDEO', callback_data = "f2v")
                ],
                [
                    InlineKeyboardButton('📄 CUSTOM THUMBNAIL', callback_data = "cthumb"),
                    InlineKeyboardButton('🏷️ CUSTOM CAPTION', callback_data = "ccaption")
                ],
                [
                    InlineKeyboardButton('👨‍💻 SOURCE', url='https://github.com/TitterBuck/CMGRENAMERBOT')
                ]
            ]
        )   
    )       

@Mai_bOTs.on_message(pyrogram.filters.command(["start"]))
async def start_me(bot, update):
    if update.from_user.id in Config.BANNED_USERS:
        await update.reply_text("YOU'RE BANNED!")
        return
    update_channel = Config.UPDATE_CHANNEL
    if update_channel:
        try:
            user = await bot.get_chat_member(update_channel, update.chat.id)
            if user.status == "kicked":
               await update.reply_text("SORRY, YOU'RE BEEN FLOODING ME. SO MY OWNER REMOVED YOU FROM USING ME. IF YOU THINK IT'S AN ERROR, CONTACT : @TitterBuck")
               return
        except UserNotParticipant:
            await update.reply_text(
                text="**DUE TO THE HUGE TRAFFIC ONLY CHANNEL MEMBERS CAN USE THIS BOT. YOU NEED TO JOIN THE BELLOW MENTIONED CHANNEL BEFORE USING ME!**",
                reply_markup=InlineKeyboardMarkup([
                    [ InlineKeyboardButton(text="🔰 JOIN CHANNEL 🔰", url=f"https://t.me/{update_channel}")]
              ])
            )
            return
        else:
            await update.reply_text(Translation.START_TEXT.format(update.from_user.first_name),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                        InlineKeyboardButton("⚙️ HELP", callback_data = "ghelp")
                ],
                [
                    InlineKeyboardButton('🗞️ UPDATES', url='https://t.me/Cinemagram_Links'),
                    InlineKeyboardButton('📽️ MOVIES', url='https://t.me/+ImlrofNsB78yYjll')
                ],
                [
                    InlineKeyboardButton('🛠️ DEVOLOPER', url='https://t.me/TitterBuck'),
                    InlineKeyboardButton('📔 ABOUT', callback_data = "about")
                ]
            ]
        ),
        reply_to_message_id=update.message_id
    )
            return 

@Mai_bOTs.on_callback_query()
async def cb_handler(client: Mai_bOTs , query: CallbackQuery):
    data = query.data
    if data == "rnme":
        await query.message.edit_text(
            text=Translation.RENAME_HELP,
            disable_web_page_preview = True,
            reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('⏪️ BACK', callback_data = "ghelp"),
                    InlineKeyboardButton("🔐 CLOSE", callback_data = "close")
                ]
            ]
        )
     )
    elif data == "f2v":
        await query.message.edit_text(
            text=Translation.C2V_HELP,
            disable_web_page_preview = True,
            reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('⏪️ BACK', callback_data = "ghelp"),
                    InlineKeyboardButton("🔐 CLOSE", callback_data = "close")
                ]
            ]
        )
     )
    elif data == "ccaption":
        await query.message.edit_text(
            text=Translation.CCAPTION_HELP,
            disable_web_page_preview = True,
            reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('📃 SHOW CURRENT CAPTION', callback_data = "shw_caption"),
                    InlineKeyboardButton("🚮 DELETE CAPTION", callback_data = "d_caption")
                ],
                [
                    InlineKeyboardButton('⏪️ BACK', callback_data = "ghelp"),
                    InlineKeyboardButton('🔐 CLOSE', callback_data = "close")
                ]
            ]
        )
     )
    elif data == "cthumb":
        await query.message.edit_text(
            text=Translation.THUMBNAIL_HELP,
            disable_web_page_preview = True,
            reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('⏪️ BACK', callback_data = "ghelp"),
                    InlineKeyboardButton("🔐 CLOSE", callback_data = "close")
                ]
            ]
        )
     )
    elif data == "closeme":
        await query.message.delete()
        try:
            await query.message.reply_text(
                text = "<b>PROCESS CANCELLED🚫</b>"
     )
        except:
            pass 
    elif data == "ghelp":
        await query.message.edit_text(
            text=Translation.HELP_USER,
            disable_web_page_preview = True,
            reply_markup=InlineKeyboardMarkup(
            [   
                [
                    InlineKeyboardButton('📝 RENAME', callback_data = "rnme"),
                    InlineKeyboardButton('📂 FILE TO VIDEO', callback_data = "f2v")
                ],
                [
                    InlineKeyboardButton('📄 CUSTOM THUMBNAIL', callback_data = "cthumb"),
                    InlineKeyboardButton('🏷️ CUSTOM CAPTION', callback_data = "ccaption")
                ],
                [
                    InlineKeyboardButton('👨‍💻 SOURCE', url='https://github.com/TitterBuck/CMGRENAMERBOT')
                ]
            ]     
        )   
    )       

    elif data =="shw_caption":
             try:
                caption = await get_caption(query.from_user.id)
                c_text = caption.caption
             except:
                c_text = "<b>SORRY BUT YOU HAVEN'T ADDED ANY CAPTION YET. PLEASE SET YOUR CAPTION THROUGH /scaption COMMAND</b>" 
             await query.message.edit(
                  text=f"<b>YOUR CUSTOM CAPTION :</b> \n\n{c_text} ",
                  parse_mode="html", 
                  disable_web_page_preview=True, 
                  reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('⏪️ BACK', callback_data = "ccaption"),
                    InlineKeyboardButton("🔐 CLOSE", callback_data = "close")
               ]
            ]
        )
     )
    elif data == "about":
        await query.message.edit_text(
            text=Translation.ABOUT_ME,
            disable_web_page_preview = True,
            reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('⏪️ BACK', callback_data = "ghelp"),
                    InlineKeyboardButton("🔐 CLOSE", callback_data = "close")
                ]
            ]
        )
     )
    elif data == "d_caption":
        try:
           await del_caption(query.from_user.id)   
        except:
            pass
        await query.message.edit_text(
            text="<b>CAPTION DELETED SUCCESSFULLY✅️</b>",
            disable_web_page_preview = True,
            reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('⏪️ BACK', callback_data = "ccaption"),
                    InlineKeyboardButton("🔐 CLOSE", callback_data = "close")
                ]
            ]
        )
     )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
