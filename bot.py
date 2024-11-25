import asyncio
import discord
from message import send_auto_message
from configuration import get_general_voice_channel_id, get_token, vc_config_path, get_ffmpeg_path
from configuration import load_configuration
from configuration import messages_config
from vc_jingle import choose_sound, play_audio
from pokemon import get_pokemon_info


DISCORD_TOKEN = get_token()
intents = discord.Intents.all()
intents.message_content = True
bot = discord.Client(intents=intents)

VC_CONFIGURATION = load_configuration(vc_config_path())
FFMPEG_PATH = get_ffmpeg_path()
MESSAGES_CONFIGURATION = load_configuration(messages_config())
VC_GENERAL = get_general_voice_channel_id()

@bot.event
async def on_ready():
	guild_count = 0
	for guild in bot.guilds:
		print(f"- {guild.id} (name: {guild.name})")
		guild_count = guild_count + 1

	print("BOT is in " + str(guild_count) + " guilds.")


@bot.event
async def on_message(message):
	mention = f'<@{bot.user.id}>'
	print(mention)
	if mention in message.content:
		args = message.content.split(' ')
		print(args)
		if (args[1].lower() == "pokemon"):
			print("Getting Pokemon...")
			new_message = get_pokemon_info(args[2].lower())
			await message.channel.send(new_message)
	else:
		await send_auto_message(message.author.name, MESSAGES_CONFIGURATION, message.channel)
	

@bot.event
async def on_voice_state_update(member, before, after):
	if before.channel is not None and before.channel.id == VC_GENERAL:
		if len(before.channel.members) == 1 and len(bot.voice_clients) == 1:
			while bot.voice_clients[0].is_playing():
				await asyncio.sleep(1)
			await asyncio.sleep(1)
			if len(bot.voice_clients[0].channel.members) <= 1:
				vc = await bot.voice_clients[0].disconnect()

	if after.channel is not None and after.channel.id == VC_GENERAL:
		if len(bot.voice_clients) == 0:
			vc = await after.channel.connect(timeout=10, reconnect=True)
		else:
			if bot.voice_clients[0].is_playing():
				bot.voice_clients[0].stop()
		vc = bot.voice_clients[0]
		if len(bot.voice_clients) > 0 and not bot.voice_clients[0].is_playing():
			if before.channel is None and after.channel is not None:
				sound = choose_sound(member.name, VC_CONFIGURATION)
				await play_audio(vc, sound, FFMPEG_PATH)
			
if __name__ == "__main__":
	if DISCORD_TOKEN is not None:
		bot.run(DISCORD_TOKEN)
