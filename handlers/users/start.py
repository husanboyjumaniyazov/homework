from aiogram import Router, types, F
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.enums.parse_mode import ParseMode
from aiogram.client.session.middlewares.request_logging import logger
from loader import db, bot
from data.config import ADMINS
from utils.extra_datas import make_title

router = Router()



@router.message(CommandStart())
async def do_start(message: types.Message):
    """
            MARKDOWN V2                     |     HTML
    link:   [Google](https://google.com/)   |     <a href='https://google.com/'>Google</a>
    bold:   *Qalin text*                    |     <b>Qalin text</b>
    italic: _Yotiq shriftdagi text_         |     <i>Yotiq shriftdagi text</i>



                    **************     Note     **************
    Markdownda _ * [ ] ( ) ~ ` > # + - = | { } . ! belgilari to'g'ridan to'g'ri ishlatilmaydi!!!
    Bu belgilarni ishlatish uchun oldidan \ qo'yish esdan chiqmasin. Masalan  \.  ko'rinishi . belgisini ishlatish uchun yozilgan.
    """

    telegram_id = message.from_user.id
    full_name = message.from_user.full_name
    username = message.from_user.username
    user = None
    try:
        user = await db.add_user(telegram_id=telegram_id, full_name=full_name, username=username)
    except Exception as error:
        logger.info(error)
    if user:
        count = await db.count_users()
        msg = (f"[{make_title(user['full_name'])}](tg://user?id={user['telegram_id']}) bazaga qo'shildi\.\nBazada {count} ta foydalanuvchi bor\.")
    else:
        msg = f"[{make_title(full_name)}](tg://user?id={telegram_id}) bazaga oldin qo'shilgan"
    for admin in ADMINS:
        try:
            await bot.send_message(
                chat_id=admin,
                text=msg,
                parse_mode=ParseMode.MARKDOWN_V2
            )
        except Exception as error:
            logger.info(f"Data did not send to admin: {admin}. Error: {error}")
    await message.answer(f"Assalomu alaykum {make_title(full_name)}\!", parse_mode=ParseMode.MARKDOWN_V2)



@router.message(F.photo)
async def handle_photo(message: Message):
    """Foto handler"""
    photo = message.photo[-1]
    file_info = await bot.get_file(photo.file_id)

    await message.answer(
        f"📷 <b>Foto qabul qilindi!</b>\n\n"
        f"🆔 File ID: <code>{photo.file_id}</code>\n"
        f"📏 O'lcham: {photo.width}x{photo.height}\n"
        f"💾 Hajmi: {photo.file_size // 1024} KB\n"
        f"📂 Path: <code>{file_info.file_path}</code>\n\n"
        f"Caption: {message.caption or 'Yoq'}"
    )

    await message.answer_photo(
        photo.file_id,
        caption="Bu sizning rasmingiz! ✨"
    )


@router.message(F.video)
async def handle_video(message: Message):
    """Video handler"""
    video = message.video

    await message.answer(
        f"🎥 <b>Video qabul qilindi!</b>\n\n"
        f"🆔 File ID: <code>{video.file_id}</code>\n"
        f"📏 O'lcham: {video.width}x{video.height}\n"
        f"⏱️ Davomiyligi: {video.duration} soniya\n"
        f"💾 Hajmi: {video.file_size // 1024 // 1024} MB\n\n"
        f"Caption: {message.caption or 'Yoq'}"
    )


@router.message(F.audio)
async def handle_audio(message: Message):
    """Audio handler"""
    audio = message.audio

    await message.answer(
        f"🎵 <b>Audio qabul qilindi!</b>\n\n"
        f"🎤 Ijrochi: {audio.performer or 'Nomalum'}\n"
        f"🎼 Nomi: {audio.title or 'Nomalum'}\n"
        f"⏱️ Davomiyligi: {audio.duration} soniya\n"
        f"💾 Hajmi: {audio.file_size // 1024 // 1024} MB"
    )


@router.message(F.voice)
async def handle_voice(message: Message):
    """Ovozli xabar handler"""
    voice = message.voice

    await message.answer(
        f"🎤 <b>Ovozli xabar qabul qilindi!</b>\n\n"
        f"⏱️ Davomiyligi: {voice.duration} soniya\n"
        f"💾 Hajmi: {voice.file_size // 1024} KB\n\n"
        f"Ovozingiz juda yoqimli! 😊"
    )


@router.message(F.video_note)
async def handle_video_note(message: Message):
    """Video xabar handler"""
    video_note = message.video_note

    await message.answer(
        f"🎬 <b>Video xabar qabul qilindi!</b>\n\n"
        f"⏱️ Davomiyligi: {video_note.duration} soniya\n"
        f"📏 O'lcham: {video_note.length}x{video_note.length}\n"
        f"💾 Hajmi: {video_note.file_size // 1024} KB\n\n"
        f"Ajoyib video xabar! 🎥"
    )


@router.message(F.document)
async def handle_document(message: Message):
    """Hujjat handler"""
    document = message.document