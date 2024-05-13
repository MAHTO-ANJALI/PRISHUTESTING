import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH", "")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 5400))

SONG_DOWNLOAD_DURATION = int(
    getenv("SONG_DOWNLOAD_DURATION_LIMIT", "5400")
)
# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", "-1002077359484"))

# Get this value from @AnjaliMusicFourBot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", "6260080241"))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/MAHTO-ANJALI/PRISHUTESTING",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "http://t.me/AnjalixSupportxGroup")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/AnjalixSupportxGroup")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", "false"))
AUTO_SUGGESTION_MODE = getenv("AUTO_SUGGESTION_MODE", "false")
AUTO_SUGGESTION_TIME = int(
    getenv("AUTO_SUGGESTION_TIME", "5400"))
# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "")


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))

CLEANMODE_DELETE_MINS = int(
    getenv("CLEANMODE_MINS", "5"))
# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @Venom_string_robot on Telegram
STRING1 = getenv("STRING_SESSION", "")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}
chatstats = {}
userstats = {}
clean = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://te.legra.ph/file/48f3942d08a08eb4a93e7.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://te.legra.ph/file/6d4dc4b24fd867cb6edb2.jpg"
)
PLAYLIST_IMG_URL = "https://telegra.ph/file/1dca3157eb1d637846d87.jpg"
STATS_IMG_URL = "https://telegra.ph/file/eb054ff3c5c532ba7c0b2.jpg"
TELEGRAM_AUDIO_URL = "https://telegra.ph/file/29c8494278f990e910893.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/3df34a720f2d6d08f57c9.jpg"
STREAM_IMG_URL = "https://telegra.ph/file/f6fcad691d6948d7a89af.jpg"
SOUNCLOUD_IMG_URL = "https://telegra.ph/file/61ecec3d3f8d1123998db.jpg"
YOUTUBE_IMG_URL = "https://telegra.ph/file/ae2ce86d990c42710c52c.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/file/7bc63654994a5d41bddf5.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/file/d68695ad86852583f1ce4.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/ade24dc9e43fbe5f73a04.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00"))

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
