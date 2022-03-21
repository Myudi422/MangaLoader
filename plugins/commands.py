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
def _tes1(bot, update):
    update.reply_text

@Client.on_message(filters.private & filters.command('anime'))
def _tes2(bot, update):
    update.reply_text

@Client.on_message(filters.private & filters.command('menu'))
def _tes3(bot, update):
    update.reply_text

@Client.on_message(filters.private & filters.command('manga'))
def _tes4(bot, update):
    update.reply_text

@Client.on_message(filters.private & filters.command('character'))
def _tes5(bot, update):
    update.reply_text

@Client.on_message(filters.private & filters.command('quote'))
def _tes6(bot, update):
    update.reply_text

@Client.on_message(filters.private & filters.command('anilist'))
def _tes7(bot, update):
    update.reply_text

@Client.on_message(filters.private & filters.command('auth'))
def _tes8(bot, update):
    update.reply_text

@Client.on_message(filters.private & filters.command('schedule'))
def _tes9(bot, update):
    update.reply_text

@Client.on_message(filters.private & filters.command('airing'))
def _tes10(bot, update):
    update.reply_text

@Client.on_message(filters.private & filters.command('manga_s'))
def _tes11(bot, update):
    update.reply_text

@Client.on_message(filters.private & filters.command('getgenres'))
def _tes12(bot, update):
    update.reply_text    

@Client.on_message(filters.private & filters.command('gettags'))
def _tes13(bot, update):
    update.reply_text

@Client.on_message(filters.private & filters.command('watch'))
def _tes14(bot, update):
    update.reply_text

@Client.on_message(filters.private & filters.command('wallpaper'))
def _tes15(bot, update):
    update.reply_text

@Client.on_message(filters.private & filters.command('waifu'))
def _tes16(bot, update):
    update.reply_text

@Client.on_message(filters.private & filters.command('reverse'))
def _tes17(bot, update):
    update.reply_text     

@Client.on_message(filters.private & filters.command('favourites'))
def _tes18(bot, update):
    update.reply_text

@Client.on_message(filters.private & filters.command('me'))
def _tes19(bot, update):
    update.reply_text

@Client.on_message(filters.private & filters.command('flex'))
def _tes20(bot, update):
    update.reply_text

@Client.on_message(filters.private & filters.command('user'))
def _tes21(bot, update):
    update.reply_text              
@Client.on_message(filters.private & filters.command('ping'))
def _tes22(bot, update):
    update.reply_text

@Client.on_message(filters.private & filters.command('fillers'))
def _tes23(bot, update):
    update.reply_text

@Client.on_message(filters.private & filters.command('logout'))
def _tes24(bot, update):
    update.reply_text    
@Client.on_message(filters.private & filters.command('top'))
def _tes25(bot, update):
    update.reply_text

@Client.on_message(filters.private & filters.command('top'))
def _tes26(bot, update):
    update.reply_text

@Client.on_message(filters.private & filters.command('top'))
def _tes27(bot, update):
    update.reply_text                     