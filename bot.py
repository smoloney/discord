import os
import discord
import random
import requests
import json
from selenium import webdriver

from dotenv import load_dotenv
load_dotenv()
TOKEN=
GUILD = os.getenv('bottestserver')

def getTournament():
    parameters = {
        "api_key":
    }

    apiCall = requests.get(" http://api.challonge.com/v1/tournaments.json", params=parameters)
    data = apiCall.json()
    if len(data) > 1:
        idx = len(data) - 1
    else:
        idx = 0
    return data[idx]['tournament']['full_challonge_url']

def getResults():
    

client = discord.Client()
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    if message.content == '!99':
        response = random.choice(quotes)
        await message.channel.send(response)
    if message.content == '!bracket':
        response = getTournament()
        await message.channel.send(response)

client.run(TOKEN)
