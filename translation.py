class Translation(object):
    START_TEXT = """<b>๐ HELLO {} ๐ฅฐ, \n\n๐คฉ I'M A SIMPLE RENAMER + FILE TO VIDEO CONVERTER BOT WITH PERMENENT THUMBNAIL AND COSTUME CAPTION SUPPORT \n\n๐ฉ SENT ANY TELEGRAM FILE OR VIDEO TO USE ME</b>"""

    BANNED_USER_TEXT = "<b>SORRY! YOU ARE BANNED FROM USING THIS BOT ๐ซ. CONTACT @TitterBuck [ADMIN] FOR DETAILS...๐จโ๐ป</b>" 
    DOWNLOAD_START = "<b>๐ฅ DOWNLOADING TO MY SERVER โฃโฃโฃโกโก PLEASE WAIT ๐</b>"
    UPLOAD_START = "<b>โ DOWNLOADING COMPLETED. ๐ค UPLOADING TO TELEGRAM โฃโฃโฃโกโก</b>"
    AFTER_SUCCESSFUL_UPLOAD_MSG = "<b>THANKYOU FOR USING ME ๐. HAVE A NICE DAY ๐ฅฐ \n\n@Cinemagram_Links</b>"
    SAVED_CUSTOM_THUMB_NAIL = "<b>YOUR PERMENENT THUMBANAIL SAVED SUCCESSFULLY โ๏ธ</b>"
    DEL_ETED_CUSTOM_THUMB_NAIL = "<b>YOUR THUMBANAIL DELETED SUCCESSFULLY ๐ฎ</b>"
    SAVED_RECVD_DOC_FILE = "<b>FILE DOWNLOADED SUCCESSFULLY โ๏ธ</b>"
    REPLY_TO_DOC_FOR_RENAME_FILE = "<b>PLEASE REPLY TO AN FILE WITH /rename FIL NAME EXTENSION TO RENAME A FILE ๐ฐ</b>"
    REPLY_TO_FILE_FOR_CONVERT = "<b>PLEASE REPLY TO AN FILE WITH /c2v TO CONVERT IT INTO STREAMABLE VIDEO FILE ๐ฐ</b>"
    CUSTOM_CAPTION_UL_FILE = " "
    NO_THUMB_FOUND = "<b>NO THUMBANAIL FOUND ๐ง. PLEASE SENT ME A IMAGE FOR YOUR PERMENENT THUMBANAIL ๐ฉ</b>"
    IFLONG_FILE_NAME = """<b>๐ณ PLEASE DECREASE THE NUMBER OF LETTERS ๐คฏ</b>"""
    ABOUT_ME = """<b>
โฃ MY NAME : <a href='t.me/CMG_Rename_Bot'>CMG RENAME BOT</a>

โฃ CREATOR : <a href='https://t.me/TitterBuck'>โฌ ๐ป๐ผ๐ผโ๐ธ๐ โฌ</a>

โฃ LANGUAGE : <a href='https://www.python.org/'>PYTHON-3</a>

โฃ LIBRARY : <a href='https://docs.pyrogram.org/'>PYROGRAM</a>

โฃ SERVER : <a href='https://dashboard.heroku.com/'>HEROKU</a>

โฃ SOURCE : <a href='https://github.com/TitterBuck/CMGRENAMERBOT'>CLICK HERE</a>
</b>"""
    HELP_USER = """<b>HERE IS THE HELP FOR MY COMMANDS ๐ค</b>"""
    RENAME_HELP = """<b>HERE IS THE AVAILABLE COMMAND FOR RENAME A FILE ๐ \n\nREPLAY TO AN FILE OR VIDEO WITH <code>/rename Filename.Extension</code> FOR RENAMING</b>"""
    C2V_HELP = """<b>HERE IS THE AVAILABLE COMMAND FOR FILE TO VIDEO โฎ๏ธ \n\nREPLAY TO AN FILE WITH <code>/c2v</code> TO CONVERT IT INTO VIDEO</b>"""
    THUMBNAIL_HELP = """<b>HERE IS THE AVAILABLE COMMAND FOR CUSTOM THUMBNAIL ๐ \n\n โฃ SENT A PHOTO TO SET THE COSTUME THUMBANAIL \n โฃ <code>/showthumb</code> : FOR SHOWING THE CURRENT THUMBANAIL  \n โฃ <code>/delthumb</code> : FOR DELETING THE CURRENT THUMBNAIL</b>"""
    CCAPTION_HELP = """<b>HERE IS THE AVAILABLE COMMANDS FOR CUSTOM CAPTION ๐ \n\n โฃ <code>/scaption</code> : USE THIS COMMAND FOR SAVE YOUR CUSTOM CAPTION \n USAGE : <code>/scaption your caption text</code> \n\n [YOU CAN USE <code>{filename}</code> FOR SHOWING NEW FILE NAME IN THE CAPTION]</b>"""
