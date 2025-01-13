import discord
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
GENAI_API_KEY = os.getenv('GENAI_API_KEY')
CLIENT_TOKEN = os.getenv('CLIENT_TOKEN')

genai.configure(api_key=GENAI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
     await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='With Nara'), status=discord.Status.idle)
     print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('hana'):
        prompt = message.content[len('hana '):]
        response = model.generate_content(prompt + " (JAWABAN HARUS DIBAWAH 2000 KATA)")
        content = response.text
        await message.channel.send(content)
        chat = model.start_chat(
            history=[
                {"role": "user", "parts": prompt},
                {"role": "model", "parts": content},
                ])

client.run(CLIENT_TOKEN)
