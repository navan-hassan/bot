from asyncio import sleep
from random import randint
from typing import Dict, List
from discord import FFmpegPCMAudio, VoiceClient, ClientException



def choose_sound(username: str, config: Dict[str, List[str]]):
	song_list = config.get(username)
	if song_list is None:
		return "ERROR"
	else:
		index = randint(0, 1000) % len(song_list)
		return song_list[index]

async def play_audio(vc: VoiceClient, sound_filepath: str, exe_filepath: str):
	try:
		audio = FFmpegPCMAudio(source=sound_filepath, executable=exe_filepath)
		vc.play(audio)
		while vc.is_playing():
			await sleep(1)
		await vc.disconnect()
	except ClientException as e:
		print(e)
		print("ERROR: COULD NOT CREATE FFmpeg SUBPROCESS")
