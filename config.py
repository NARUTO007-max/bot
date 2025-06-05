import re
from os import getenv
# ------------------------------------
# ------------------------------------
from dotenv import load_dotenv
from pyrogram import filters
# ------------------------------------
# ------------------------------------
load_dotenv()
# ------------------------------------
# -----------------------------------------------------
API_ID = int(getenv("API_ID", "21218274"))
API_HASH = getenv("API_HASH", "3474a18b61897c672d315fb330edb213")
BOT_TOKEN = getenv("BOT_TOKEN", "7207574948:AAGRV7Te9gcinmy9hLnPvAOiEzcOYgllDns")
BOT_ID = getenv("BOT_ID", "7207574948")
# -------------------------------------------------------
OWNER_USERNAME = getenv("OWNER_USERNAME","Uzumaki_X_Naruto_6")
# --------------------------------------------------------
BOT_USERNAME = getenv("BOT_USERNAME" , "Gvhhhgbot")
# --------------------------------------------------------
BOT_NAME = getenv("BOT_NAME" , "testbot")
# ---------------------------------------------------------
ASSUSERNAME = getenv("ASSUSERNAME" , "Hinata_assisbot")
# ---------------------------------------------------------


#---------------------------------------------------------------
#---------------------------------------------------------------
MONGO_DB_URI = getenv("mongodb+srv://sufyan532011:2010@dbz.28ftn.mongodb.net/?retryWrites=true&w=majority&appName=DBZ")
API_KEY = getenv("AIzaSyC8wdE5fLjCo3xiW9NmddHyxZaKenpEJ7Q")
#---------------------------------------------------------------
#---------------------------------------------------------------

# ----------------------------------------------------------------
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 17000))
# ----------------------------------------------------------------

# ----------------------------------------------------------------
LOGGER_ID = int(getenv("-1002535643821"))
CLONE_LOGGER = LOGGER_ID
# ----------------------------------------------------------------
# ----------------------------------------------------------------
OWNER_ID = int(getenv("OWNER_ID", 7576729648))
# -----------------------------------------------------------------
# -----------------------------------------------------------------
# config.py
# ----------------------------------------------------------------
# ----------------------------------------------------------------
# ----------------------------------------------------------------
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# ----------------------------------------------------------------
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
# ----------------------------------------------------------------
# ----------------------------------------------------------------
# ----------------------------------------------------------------
SOURCE = getenv("SOURCE", "https://github.com/TeamProBots/Clonify")
UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/TeamProBots/Clonify",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)
# --------------------------------------------------------------------
# --------------------------------------------------------------------
# --------------------------------------------------------------------
# --------------------------------------------------------------------



# ------------------------------------------------------------------------
# -------------------------------------------------------------------------
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/bey_war_updates")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/ProBotGc")
CHAT = getenv("CHAT", "https://t.me/ProBotGc")
# ------------------------------------------------------------------------------
# -------------------------------------------------------------------------------







# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "False")
AUTO_LEAVE_ASSISTANT_TIME = int(getenv("ASSISTANT_LEAVE_TIME", "9000"))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION", "9999999"))
SONG_DOWNLOAD_DURATION_LIMIT = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "9999999"))
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "1c21247d714244ddbb09925dac565aed")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "709e1a2969664491b58200860623ef19")
# ----------------------------------------------------------------------------------




# -----------------------------------------------------------------------------------
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))
# ------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "5242880000"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "5242880000"))
# --------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------



# ------------------------------------
# ------------------------------------
# ------------------------------------
# ------------------------------------
STRING1 = getenv("STRING_SESSION", "BQFDw-IAcCq6t61I2Ag8RKFsJfTJ2bpgNGxKzk6Hsmbs2SOeGH0a-GxcsKX0mAyX9YL5wQ-0xwp0fstrHvnp7DBH3Zk_bjH9Pn3mFDPZTGbfEEKGwlFY03EF1INP9hIfvl7JhMKoj0HFhXDbxany59OJeBtaViHlMacaeRJRCvh9d7MzzHrsaVCdgQDBBJ4Mf4c-3QpD1Ixom0KyuH6h9Ta69aLdsaQmVS9yAeZWD8rNRKEO696IrNyadaKIfptryW7o8Q4DGfCtdExJ-RQLq7POqL9jhfSAeHy9nOGRWzcvZIwiQqdseDwfBf3F8IxozNmmIRSuxCu3igRepVK133aGU6K0uQAAAAHk57-wAQ")
STRING2 = getenv("STRING_SESSION2", None)
BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

# ------------------------------------
# ------------------------------------
# ------------------------------------
# ------------------------------------

# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------

STREAMI_PICS = [
"https://i.ibb.co/whgkNq6n/start-img-1.jpg",
"https://i.ibb.co/q32FdssH/start-img-2.jpg",

]

START_IMG_URL = getenv(
    "START_IMG_URL", "https://i.ibb.co/xPjc7tv/help-menu.jpg"
)

HELP_IMG_URL = getenv(
    "HELP_IMG_URL", "https://i.ibb.co/xPjc7tv/help-menu.jpg"
)

PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://i.ibb.co/VWnm6f3f/ping.jpg"
)
PLAYLIST_IMG_URL = "https://i.ibb.co/gL3ykkyh/play-music.jpg"
STATS_IMG_URL = "https://i.ibb.co/pBqPtFYn/statistics.jpg"
TELEGRAM_AUDIO_URL = "https://i.ibb.co/gL3ykkyh/play-music.jpg"
TELEGRAM_VIDEO_URL = "https://i.ibb.co/gL3ykkyh/play-music.jpg"
STREAM_IMG_URL = "https://i.ibb.co/0VKCS20y/stream.jpg"
SOUNCLOUD_IMG_URL = "https://i.ibb.co/S4sPf3q8/soundcloud.jpg"
YOUTUBE_IMG_URL = "https://i.ibb.co/xShkBVBK/youtube.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://i.ibb.co/XZfMS8Db/spotify.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://i.ibb.co/XZfMS8Db/spotify.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://i.ibb.co/XZfMS8Db/spotify.jpg"

# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))

# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# ------------------------------------------------------------------------------
if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
# ---------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------


GREET = [
    "💞", "🥂", "🔍", "🧪", "🥂", "⚡️", "🔥", "🦋", "🎩", "🌈", "🍷", "🥂", "🦋", "🥃", "🥤", "🕊️",
    "🦋", "🦋", "🕊️", "⚡️", "🕊️", "⚡️", "⚡️", "🥂", "💌", "🥂", "🥂", "🧨"
]

# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------