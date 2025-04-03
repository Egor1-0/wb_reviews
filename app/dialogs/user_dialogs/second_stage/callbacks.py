import io
import logging
import os

import aiofiles
from aiogram.types import CallbackQuery, Message, InputFile, InputMediaPhoto, InputMediaAnimation, InputMediaVideo, \
    FSInputFile
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.input import MessageInput, ManagedTextInput
from aiogram_dialog.widgets.kbd import Button

from config import config
from database.daos import PromotionDao, ParticipationDao
from keyboards.admin import get_accept_reject_first_stage_keyboard, get_accept_reject_second_stage_keyboard
from states.user import FirstStage


async def save_photo_and_video_review(message: Message, widget: MessageInput, dialog_manager: DialogManager):
    if message.photo:
        dialog_manager.dialog_data['photo_review_id'] = message.photo[-1].file_id
    if message.video:
        dialog_manager.dialog_data['video_review_id'] = message.video.file_id
    if message.animation:
        dialog_manager.dialog_data['animation_review_id'] = message.animation.file_id

    await dialog_manager.next()


async def save_screenshot_review(message: Message, widget: MessageInput, dialog_manager: DialogManager):
    dialog_manager.dialog_data['screenshot_review_id'] = message.photo[-1].file_id
    await dialog_manager.next()


async def save_article(message: Message, widget: ManagedTextInput, dialog_manager: DialogManager, data: str):
    dialog_manager.dialog_data['article'] = message.text
    await dialog_manager.next()


async def save_nickname(message: Message, widget: ManagedTextInput, dialog_manager: DialogManager, data: str):
    dialog_manager.dialog_data['nickname'] = message.text
    await dialog_manager.next()


async def save_phone_number(message: Message, widget: ManagedTextInput, dialog_manager: DialogManager, data: str):
    dialog_manager.dialog_data['phone_number'] = message.text
    await dialog_manager.next()


async def save_details_for_transfer(message: Message, widget: ManagedTextInput, dialog_manager: DialogManager,
                                    data: str):
    details_for_transfer = message.text
    photo_review_id = dialog_manager.dialog_data.get('photo_review_id')
    video_review_id = dialog_manager.dialog_data.get('video_review_id')
    animation_review_id = dialog_manager.dialog_data.get('animation_review_id')
    screenshot_review_id = dialog_manager.dialog_data['screenshot_review_id']
    article = dialog_manager.dialog_data['article']
    nickname = dialog_manager.dialog_data['nickname']
    phone_number = dialog_manager.dialog_data['phone_number']
    promotion_id = int(dialog_manager.start_data['promotion_id'])

    promotion = await PromotionDao.find_by_id(dialog_manager.middleware_data['session'],
                                              promotion_id)
    await ParticipationDao.update(dialog_manager.middleware_data['session'],
                                  {'user_id': message.from_user.id, 'promotion_id': promotion_id},
                                  {'phone_number': phone_number, 'wb_nickname': nickname,
                                   'details_for_transfer': details_for_transfer})

    text = (f'Юзер: {'@' + message.from_user.username + f' ({message.from_user.id})'
    if message.from_user.username else message.from_user.id} прошел второй этап по акции {promotion.name}. '
            f'Проверьте, все ли в порядке с данными и переведите кешбэк пользователю. \nДанные:\n'
            f'Артикул товара: {article}\nИмя пользователя на WB: {nickname}\nНомер телефона пользователя: '
            f'{phone_number}\nРеквизиты пользователя для перевода: {details_for_transfer}')

    media = [InputMediaPhoto(media=screenshot_review_id)]

    if photo_review_id:
        media.append(InputMediaPhoto(media=photo_review_id))
    if video_review_id:
        media.append(InputMediaVideo(media=video_review_id))
    if animation_review_id:
        animation = await message.bot.get_file(animation_review_id)
        animation_file = await message.bot.download_file(animation.file_path)
        animation_bytes = io.BytesIO(animation_file.read())
        async with aiofiles.open(f'{animation_review_id}.mp4', mode='wb') as file:
            await file.write(animation_bytes.getvalue())
        media.append(InputMediaVideo(media=FSInputFile(f'{animation_review_id}.mp4')))

    group = await message.bot.send_media_group(chat_id=config.bot.ADMINISTRATION, media=[*media])

    await message.bot.send_message(config.bot.ADMINISTRATION, text=text,
                                   reply_markup=get_accept_reject_second_stage_keyboard(message.from_user.id,
                                                                                        promotion_id),
                                   reply_to_message_id=group[0].message_id)

    await message.answer('Данные предоставлены модерации. Если все в порядке - вам придет уведомление, что '
                         'кешбэк переведен на указанные реквизиты')
    if animation_review_id:
        os.remove(f'{animation_review_id}.mp4')
    await dialog_manager.done()
