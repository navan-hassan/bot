from discord import TextChannel
from typing import Dict, List
from random import randint

async def send_auto_message(author: str, config: Dict[str, List[str]], channel: TextChannel):
		msg_list = config.get(author)
		if (msg_list is None):
			return
		if will_send_message():
			msg = msg_list[randint(0, 100) % len(msg_list)]
			await channel.send(msg)

def will_send_message():
	chance = randint(0, 1000)
	return chance < 300