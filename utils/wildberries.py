import asyncio
import json
import logging
from dataclasses import dataclass
from typing import List

import aiohttp

logger = logging.getLogger('wildberries')


@dataclass
class CardInfo:
    id: int
    info: dict
    error: str = None


def get_cards_info(card_ids: List[int]) -> List[CardInfo]:
    try:
        responses = asyncio.run(gather_data(card_ids))
    except Exception as err:
        logger.error(f'get_cards_info; asyncio.run(gather_data(card_ids)); err: {err}')
        raise err
    return responses


async def get_card_data(session, cart_id: int) -> CardInfo:
    url = f"https://card.wb.ru/cards/detail?locale=ru&lang=ru&curr=rub&nm={cart_id}"

    async with session.get(url=url) as response:
        response_text = await response.text()
        card_data_json = json.loads(response_text)
        card_info_obj_error = None
        try:
            card_data = card_data_json['data']['products'][0]
        except (KeyError, IndexError) as err:
            logger.warning(f"wildberries.get_card_data; err: {err}")
            card_info_obj_error = 'Unparsed'
            card_data = None

        card_info_obj = CardInfo(
            id=cart_id,
            info=card_data,
            error=card_info_obj_error
        )
        return card_info_obj


async def gather_data(cards_ids: list):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for cart_id in cards_ids:
            task = asyncio.create_task(get_card_data(session, cart_id))
            tasks.append(task)
        return await asyncio.gather(*tasks)
