# -*- coding: utf-8 -*-

import discord
from discord import Message, embeds
import webscraping
import img_desing
import time as tm
import sqlite3
import os
from discord.ext import commands
from PIL import Image
from discord import Webhook, AsyncWebhookAdapter, RequestsWebhookAdapter, File
# Token for Bot
bot_token = "XXX"
# Webhook ID and Token
id = 123123
token = "XXX"
# Creating Webhook
mwebhook = discord.Webhook.partial(id= id, token= token, adapter=RequestsWebhookAdapter())
# Bot Settings
client = commands.Bot(command_prefix="")
# Start Fonc
@client.event
async def on_ready():
    print("I'm ready to FLY")
# Main Bot Func
@client.command()
async def heyobot(message):
    # Taking diffrent channel_id for sending image and taking url!
    img_channel = await client.fetch_channel(channel_id=123123123)
    while True:
        # Web scraping
        x = webscraping.Main_Events()
        print("Web scrabbing complete!")
        if x != []:
            for i in range(0,len(x[0])):
                # Creating Image and save
                r_img = img_desing.img_main(x[i])
                print("Image desing complete!")
                r_img.save(fp="./Main/Saved/saved.png")
                print("Image Saved!")
                # Creating a file named 'file'
                file = discord.File("./Main/Saved/saved.png")
                # Separating webscraping data
                EventID, Killer_Profile, Killer_Equipment, Victim_Profile, Victim_Equipment, Victim_Inventory, TotalKillFame, Participants = x[i]
                # Taking killer and Victim name's
                title = Killer_Profile[0][2]+" has killed "+Victim_Profile[0][2]
                # Creating Evend Url
                url = img_desing.make_url(EventID)
                # My Description
                description = "This bot made by Heyopa. Version 0.0.2"
                # Checking who the killer is, if it's from us embed will be green.if it's not will be red.
                if Killer_Profile[0][1] == "Iron Hand" or Victim_Profile[0][1] == "Iron Hand":
                    # Sending 'file' named file to discord
                    img_url = await img_channel.send(file=file)
                    # Creating embed
                    my_img = discord.Embed(title=title, url=url, colour=0x00FF00)
                    # Taking our image url and added in to embed
                    my_img.set_image(url=img_url.attachments[0].url)
                    my_img.set_footer(text=description)
                    # Sending Embed
                    mwebhook.send(embed=my_img)
                    print("Image deleted successfully")
                else:
                    img_url = await img_channel.send(file=file)
                    my_img = discord.Embed(title=title, url=url, colour=0xff0000)
                    my_img.set_image(url=img_url.attachments[0].url)
                    my_img.set_footer(text=description)
                    mwebhook.send(embed=my_img)
                    print("Image deleted successfully")
        print("Waiting next scraping!")
        tm.sleep(5)

client.run("XXX")
