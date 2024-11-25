from os import getenv
from json import load
from typing import Dict, List
from dotenv import load_dotenv

load_dotenv()

def get_general_voice_channel_id() -> int | None:
	try:
		channel_id = getenv("GENERAL_VC_ID")
		if channel_id is None:
			return channel_id
		return int(channel_id)
	except Exception as e:
		print("ERROR Could not load VC ID")
		print(e)
		return None
	
def vc_config_path() -> str | None:
	vc_config = getenv("VC_CONFIG")
	return vc_config

def messages_config() -> str | None:
	return getenv("MESSAGES_CONFIG")

def get_token() -> str | None:
	token = getenv("DISCORD_TOKEN")
	return token

def get_ffmpeg_path() -> str | None:
	return getenv("FFMPEG_PATH")

if __name__ == "__main__":
	id = get_general_voice_channel_id()
	print(id)
	print(type(id))

def load_vc_configuration(filepath: str) -> Dict[str, List[str]]:
	config_dictionary = {}
	with open(filepath) as config_file:
		config_dictionary = load(config_file)
	return config_dictionary

def load_configuration(filepath: str | None) -> Dict[str, List[str]] | None:
	config_dictionary = {}
	if filepath is None:
		return None
	else:
		with open(filepath) as config_file:
			config_dictionary = load(config_file)
		return config_dictionary