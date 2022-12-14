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
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", -100)
    ABOUT_BOT_TEXT = """<b>This is Mdisk Search Bot.

๐ค My Name: <a href='https://t.me/Mdisk_Links_Sender_Bot'>Mdisk Search Robot</a>

๐ Language : <a href='https://www.python.org'> Python V3</a>

๐ Library: <a href='https://docs.pyrogram.org'> Pyrogram</a>

๐ก Server: <a href='https://heroku.com'>Heroku</a>

๐จโ๐ป Created By: <a href='https://t.me/z_harbour'>ZHarbour</a></b>
"""

    ABOUT_HELP_TEXT = """<b>๐จโ๐ป Developer : <a href='https://t.me/z_harbour'>Aayush</a>

Source: Closed </b>
"""

    HOME_TEXT = """

<b>Yo! {}๐,

I'm Mdisk Link Search Robo.</a>

I Can Search๐ Mobiz-Seriez-Showsโ

Just Drop A Name With Correct Spelling And See My Powers โกโก

<a>If You Didn't Found Ur Result, Please Try Requesting Here๐<i>@blackest_harbour</i> </a></b>

"""

    START_MSG = """

<b>Yo! Dear {}๐,

I'm Mdisk Link Search Robo.</a>

I Can Search๐ Mobiz-Seriz-Showzโ

Just Drop A Name With Correct Spelling And See My Powers โก

<a>If You Didn't Found Ur Result Try Requesting Here๐<u> @blackest_harbour <u> </a></b>

"""
