# Auto Correction Discord Self Bot
# Copyright (c) 2021 houseofkraft

# This software requires a version below Python 3.7.0 and has been tested on discord.py 1.0.0
# however you might be able to go higher. This is a self-bot and they are technically banned on Discord,
# please use this at your own risk! You also need spellchecker for this to run properly.

from spellchecker import SpellChecker
import discord
import asyncio
import time

client = discord.Client()
spell = SpellChecker()

# Add your ID and Token below!
AUTHOR_ID = 1
TOKEN = "Insert Token Here!"
OVERRIDE_KEY = "/"

@client.event
async def on_message(message):
    global con
    con = message.content
    if not message.author.id == AUTHOR_ID: return

    word_list = con.split(" ")

    if OVERRIDE_KEY in word_list[len(word_list) - 1]:
        # You want to ignore auto-correct then, and do nothing.
        word_bad = True
        con = con.replace(OVERRIDE_KEY, "")
    else:
        bad_words = spell.unknown(word_list)
        word_bad = False
        for word in bad_words:
            correction = spell.correction(word)

            if not word == correction:
                # Sometimes, the bad word equals the corrected word and it does nothing, ignore if
                # this happens.
                word_bad = True
                con = con.replace(word, spell.correction(word))

    if word_bad:
        time.sleep(1)
        await message.edit(content=con)


client.run(TOKEN, bot=False)
