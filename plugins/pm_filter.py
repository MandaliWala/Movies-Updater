import asyncio
import re
import math
from pyrogram.errors.exceptions.bad_request_400 import MediaEmpty, PhotoInvalidDimensions, WebpageMediaEmpty
from Script import script
import pyrogram
from info import * #SUBSCRIPTION, PAYPICS, START_IMG, SETTINGS, URL, STICKERS_IDS,PREMIUM_POINT,MAX_BTN, BIN_CHANNEL, USERNAME, URL, ADMINS,REACTIONS, LANGUAGES, QUALITIES, YEARS, SEASONS, AUTH_CHANNEL, SUPPORT_GROUP, IMDB, IMDB_TEMPLATE, LOG_CHANNEL, LOG_VR_CHANNEL, TUTORIAL, FILE_CAPTION, SHORTENER_WEBSITE, SHORTENER_API, SHORTENER_WEBSITE2, SHORTENER_API2, DELETE_TIME
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, InputMediaPhoto, ChatPermissions, WebAppInfo, InputMediaAnimation, InputMediaPhoto
from pyrogram import Client, filters, enums
from pyrogram.errors import * #FloodWait, UserIsBlocked, MessageNotModified, PeerIdInvalid, ChatAdminRequired
from utils import temp, get_settings, is_check_admin, get_status, get_size, save_group_settings, is_req_subscribed, get_poster, get_status, get_readable_time , imdb , formate_file_name
from database.users_chats_db import db
from database.ia_filterdb import Media, get_search_results, get_bad_files, get_file_details
import random
lock = asyncio.Lock()
import traceback
from fuzzywuzzy import process
BUTTONS = {}
FILES_ID = {}
CAP = {}

# zishan [
from database.config_db import mdb
import logging
from urllib.parse import quote_plus
from Jisshu.util.file_properties import get_name, get_hash, get_media_file_size
logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)
# ] codes add


	    
async def ai_spell_check(wrong_name):
    async def search_movie(wrong_name):
        search_results = imdb.search_movie(wrong_name)
        movie_list = [movie['title'] for movie in search_results]
        return movie_list
    movie_list = await search_movie(wrong_name)
    if not movie_list:
        return
    for _ in range(5):
        closest_match = process.extractOne(wrong_name, movie_list)
        if not closest_match or closest_match[1] <= 80:
            return 
        movie = closest_match[0]
        files, offset, total_results = await get_search_results(movie)
        if files:
            return movie
        movie_list.remove(movie)
    return
