import os, shutil
from pyrogram import Client, filters
from pyrogram.types.bots_and_keyboards import InlineKeyboardMarkup
from translation import Translation


@Client.on_message(filters.private & filters.command('starts'))
def _start(bot, update):
    update.reply_text(
        Translation.START_TEXT.format(str(update.from_user.first_name)), reply_markup=InlineKeyboardMarkup(Translation.start_buttons)
    )


@Client.on_message(filters.private & filters.command('help'))
def _help(bot, update):
    update.reply_text(Translation.HELP_TEXT)


@Client.on_message(filters.private & filters.command('cleandir'))
def _cleandir(bot, update):
    dirx = './Manga/'
    if os.path.isdir(dirx):
        shutil.rmtree(dirx)
        update.reply_text(Translation.CLEANDIR_SUCCESS)
    else:
        update.reply_text(Translation.CLEANDIR_UNSUCCESS)

@Client.on_message(filters.private & filters.command('top'))
def _tes(bot, update):
    update.reply_text

@Client.on_message(filters.private & filters.command('browse'))
def _tes(bot, update):
    update.reply_text

@Client.on_message(filters.private & filters.command('anime'))
def _tes(bot, update):
    update.reply_text

@Client.on_message(filters.private & filters.command('menu'))
def _tes(bot, update):
    update.reply_text

@Client.on_message(filters.private & filters.command('manga'))
def _tes(bot, update):
    update.reply_text

@Client.on_message(filters.private & filters.command('character'))
def _tes(bot, update):
    update.reply_text

@Client.on_message(filters.private & filters.command('quote'))
def _tes(bot, update):
    update.reply_text

@Client.on_message(filters.private & filters.command('anilist'))
def _tes(bot, update):
    update.reply_text

@Client.on_message(filters.private & filters.command('auth'))
def _tes(bot, update):
    update.reply_text

@Client.on_message(filters.private & filters.command('schedule'))
def _tes(bot, update):
    update.reply_text

@Client.on_message(filters.private & filters.command('airing'))
def _tes(bot, update):
    update.reply_text

@Client.on_message(filters.private & filters.command('manga_s'))
def _tes(bot, update):
    update.reply_text

@Client.on_message(filters.private & filters.command('getgenres'))
def _tes(bot, update):
    update.reply_text    

@Client.on_message(filters.private & filters.command('gettags'))
def _tes(bot, update):
    update.reply_text

@Client.on_message(filters.private & filters.command('watch'))
def _tes(bot, update):
    update.reply_text

@Client.on_message(filters.private & filters.command('wallpaper'))
def _tes(bot, update):
    update.reply_text

@Client.on_message(filters.private & filters.command('waifu'))
def _tes(bot, update):
    update.reply_text

@Client.on_message(filters.private & filters.command('reverse'))
def _tes(bot, update):
    update.reply_text     

@Client.on_message(filters.private & filters.command('favourites'))
def _tes(bot, update):
    update.reply_text

@Client.on_message(filters.private & filters.command('me'))
def _tes(bot, update):
    update.reply_text

@Client.on_message(filters.private & filters.command('flex'))
def _tes(bot, update):
    update.reply_text

@Client.on_message(filters.private & filters.command('user'))
def _tes(bot, update):
    update.reply_text              
@Client.on_message(filters.private & filters.command('ping'))
def _tes(bot, update):
    update.reply_text

@Client.on_message(filters.private & filters.command('fillers'))
def _tes(bot, update):
    update.reply_text

@Client.on_message(filters.private & filters.command('logout'))
def _tes(bot, update):
    update.reply_text    
@Client.on_message(filters.private & filters.command('top'))
def _tes(bot, update):
    update.reply_text

@Client.on_message(filters.private & filters.command('top'))
def _tes(bot, update):
    update.reply_text

@Client.on_message(filters.private & filters.command('top'))
def _tes(bot, update):
    update.reply_text                     