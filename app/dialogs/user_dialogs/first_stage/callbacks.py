from aiogram.types import CallbackQuery, Message, InputFile, InputMediaPhoto
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Button

from config import config
from database.daos import PromotionDao, ParticipationDao
from database.schemas.participation import CreateParticipation
from database.schemas.status import Status
from keyboards.admin import get_accept_reject_first_stage_keyboard
from states.user import FirstStage


async def save_promotion_id(callback: CallbackQuery, button: Button, dialog_manager: DialogManager, data: str):
    dialog_manager.dialog_data['promotion_id'] = data
    create_promotion = CreateParticipation(
        user_id=callback.from_user.id,
        promotion_id=int(data),
        status=Status.FIRST_STAGE
    )
    await ParticipationDao.create(dialog_manager.middleware_data['session'], create_promotion)
    await dialog_manager.switch_to(FirstStage.find_by_keywords)


async def save_find_by_keywords_photo(message: Message, widget: MessageInput, dialog_manager: DialogManager):
    dialog_manager.dialog_data['find_by_keywords_photo_id'] = message.photo[-1].file_id
    await dialog_manager.next()


async def save_basket_with_competitors_photo(message: Message, widget: MessageInput, dialog_manager: DialogManager):
    dialog_manager.dialog_data['basket_with_competitors_photo_id'] = message.photo[-1].file_id
    await dialog_manager.next()


async def save_basket_without_competitors_photo(message: Message, widget: MessageInput, dialog_manager: DialogManager):
    dialog_manager.dialog_data['basket_without_competitors_photo_id'] = message.photo[-1].file_id
    await dialog_manager.next()


async def save_order_with_address_photo(message: Message, widget: MessageInput, dialog_manager: DialogManager):
    dialog_manager.dialog_data['order_with_address_photo_id'] = message.photo[-1].file_id
    await dialog_manager.next()


async def save_like_shop_and_product_photo(message: Message, widget: MessageInput, dialog_manager: DialogManager):
    like_shop_and_product_photo_id = message.photo[-1].file_id
    find_by_keywords_photo_id = dialog_manager.dialog_data['find_by_keywords_photo_id']
    basket_with_competitors_photo_id = dialog_manager.dialog_data['basket_with_competitors_photo_id']
    basket_without_competitors_photo_id = dialog_manager.dialog_data['basket_without_competitors_photo_id']
    order_with_address_photo_id = dialog_manager.dialog_data['order_with_address_photo_id']

    promotion = await PromotionDao.find_by_id(dialog_manager.middleware_data['session'],
                                              int(dialog_manager.dialog_data['promotion_id']))

    text = (f'Юзер: {'@' + message.from_user.username + f' ({message.from_user.id})' 
            if message.from_user.id else message.from_user.id} хочет участвовать в акции по товару {promotion.name}. '
            f'Проверьте, все ли в порядке со скришотами')

    group = await message.bot.send_media_group(chat_id=config.bot.ADMINISTRATION,
                                               media=[
                                                   InputMediaPhoto(media=like_shop_and_product_photo_id),
                                                   InputMediaPhoto(media=find_by_keywords_photo_id),
                                                   InputMediaPhoto(media=basket_with_competitors_photo_id),
                                                   InputMediaPhoto(media=basket_without_competitors_photo_id),
                                                   InputMediaPhoto(media=order_with_address_photo_id)
                                               ],
                                               )
    await message.bot.send_message(config.bot.ADMINISTRATION, text=text,
                                   reply_markup=get_accept_reject_first_stage_keyboard(message.from_user.id, promotion.id),
                                   reply_to_message_id=group[0].message_id)
    await message.answer(
        'Данные предоставлены модерации. Если все в порядке - вам придет уведомление, что можете создавать заказ')
    await dialog_manager.done()
