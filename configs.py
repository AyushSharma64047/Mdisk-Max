# (c) @RoyalKrrishna

import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", 12345))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    BOT_SESSION_NAME = os.environ.get("BOT_SESSION_NAME", "MdiskSearchBot")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", "")
    CHANNEL_ID = int(os.environ.get("CHANNEL_ID", -100))
    BOT_USERNAME = os.environ.get("BOT_USERNAME")
    BOT_OWNER = int(os.environ.get("BOT_OWNER"))
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-100")
    ABOUT_BOT_TEXT = """<b>This is Mdisk Search Bot.

🤖 My Name: <a href='https://t.me/Mdisk_Links_Sender_Bot'>Mdisk Search Robot</a>

📝 Language : <a href='https://www.python.org'> Python V3</a>

📚 Library: <a href='https://docs.pyrogram.org'> Pyrogram</a>

📡 Server: <a href='https://heroku.com'>Heroku</a>

👨‍💻 Created By: <a href='https://t.me/z_harbour'>ZHarbour</a></b>
"""

    ABOUT_HELP_TEXT = """<b>👨‍💻 Developer : <a href='https://t.me/z_harbour'>Aayush</a>

Source: Closed </b>
"""

    HOME_TEXT = """

<b>Yo! {}😇,

I'm Mdisk Link Search Robo.</a>

I Can Search🔍 Mobiz-Seriez-Shows❗

Just Drop A Name With Correct Spelling And See My Powers ⚡⚡

<a>If You Didn't Found Ur Result, Please Try Requesting Here👉<i>@blackest_harbour</i> </a></b>

"""

    START_MSG = """

<b>Yo! Dear {}😇,

I'm Mdisk Link Search Robo.</a>

I Can Search🔍 Mobiz-Seriz-Showz❗

Just Drop A Name With Correct Spelling And See My Powers ⚡

<a>If You Didn't Found Ur Result Try Requesting Here👉<u> @blackest_harbour <u> </a></b>

"""
