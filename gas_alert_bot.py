import discord
from discord import app_commands           
import requests
import asyncio
import threading
import time

ETHERSCAN_URL = "https://api.etherscan.io/api?module=proxy&action=eth_gasPrice&apikey=ETHERSCAN_API_TOKEN"

intents = discord.Intents.default()  
client = discord.Client(intents=intents) 
tree = app_commands.CommandTree(client) 

def check_gas_price(interaction, target_price):
    while True:
        try :
            response = requests.get(ETHERSCAN_URL).json()
            current_gas_price = int(response["result"], 16) / 10**9  # Convert from Wei to Gwei
        except :
            current_gas_price = 1000
        if current_gas_price <= target_price:
            asyncio.run_coroutine_threadsafe(interaction.channel.send(
                f'<@{interaction.user.id}>, Gas price has dropped to or below your specified price ({target_price} Gwei)!'), client.loop)
            break
        else:
            time.sleep(60)  # Check every 60 seconds

@tree.command(name = "gasalert", description = "Set the gas price to trigger the alert")
@app_commands.describe(price = "gas price")
async def gasalert(interaction:discord.Interaction, price:app_commands.Range[int,1,100]):
    await interaction.response.defer(ephemeral=True)
    threading.Thread(target=check_gas_price, args=(interaction, price)).start()
    await interaction.followup.send(f"Price set, you will be notified when the gas price reaches {price}!",ephemeral=True)

@client.event
async def on_ready():
    print("Name: {}".format(client.user.name))
    await tree.sync()
    print("Ready!")

client.run('discord-token')  # Bot tokeninizi buraya girin
