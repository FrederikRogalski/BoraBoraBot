from selenium import webdriver
import os
import time
import random
import re
import argparse
from subprocess import Popen
import re
import asyncio
import threading

parser = argparse.ArgumentParser(description='Process some integers.')


parser.add_argument('--discord', default=None, help='Enables Discord Bot. Needs Discord token.', type=str)
parser.add_argument('--name', default=None, help='Name to log in to Moodle like <name>@lehre.dhbw.mosbach.de.', type=str)
parser.add_argument('--passwd', default=None, help='Password for Moodle.', type=str)
parser.add_argument('--test', action='store_true', help='Test the bot.')
parser.add_argument('--quiet', action='store_true', help='Deactivates the voice of BoraBora.')
parser.add_argument('--noText', action='store_true', help='Deactivates writing of BoraBora.')
parser.add_argument('--audio', default="./audio", help="A folder with mp3 files to play from.")

args = parser.parse_args()

class LandBot():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.allreadySeen = ['Anwesenheitstests']

    def abfrage(self):
        self.driver.get(
            'https://moodle.mosbach.dhbw.de/course/view.php?id=12679')
        assert "login" in self.driver.current_url
        name = self.driver.find_element_by_xpath('//*[@id="username"]')
        kennwort = self.driver.find_element_by_xpath('//*[@id="password"]')
        button = self.driver.find_element_by_xpath('//*[@id="loginbtn"]')
        name.send_keys(f'{args.name}@lehre.mosbach.dhbw.de')
        kennwort.send_keys(args.passwd)
        button.click()
        time.sleep(0.5+random.random())

    def check(self):
        found = re.findall('.nwesenheitstest[a-zA-Z0-9]*', self.driver.page_source)
        #import pdb; pdb.set_trace()
        new = [x for x in found if x not in self.allreadySeen]
        if len(new) > 0:
            self.allreadySeen.append(new[0])
            return True
        else:
            return False

def borabora(bot):
    count = 0
    while True:
        print(count, ". Abfrage")
        try:
            bot.abfrage()
        except:
            pass

        time.sleep(5+random.random())
        if bot.check():
            if bot.allreadySeen[-1]!="Anwesenheitstests":
                print("Found Anwesenheitstest")
                #cmd = """osascript -e 'tell app "System Events" to display dialog "Anwesenheitstest!"'"""
                #cmd = ['osascript', '-e', 'tell app "System Events" to display dialog "Anwesenheitstest!"']
                #Popen(cmd)
                break
        time.sleep(5+random.random())
        count += 1
    return bot.allreadySeen[-1]

if args.discord != None:
    import discord
    client = discord.Client()

    async def startAudio(channel, mp3):
        audio_source = discord.FFmpegPCMAudio(os.path.join(args.audio, mp3))
        while True:
            try:
                await asyncio.sleep(1)
                vc = await asyncio.wait_for(channel.connect(), 1.0)
                break
            except:
                print(f"connecting issues...{channel}")
        vc.play(audio_source)
        while vc.is_playing():
            await asyncio.sleep(1)
        while True:
            try:
                await asyncio.sleep(1)
                await asyncio.wait_for(vc.disconnect(), 1.0)
                break
            except:
                print(f"disconneceting issue{channel}")
        print("finished")

    async def distribute(channels):
        mp3s = [x for x in os.listdir(args.audio) if len(x) >= 4 and x[-4:]=='.mp3']
        if len(mp3s) == 0:
            raise FileNotFoundError(f"The specified directory {args.audio} doesn't contain a single mp3 file.")
        await asyncio.gather(*[startAudio(channel, random.choice(mp3s)) for channel in channels])



    @client.event
    async def on_ready():
        print(f'{client.user} has connected to Discord!')
        if not args.test:
            bot = LandBot()
        while True:
            if not args.test:
                test = borabora(bot)
            else:
                test = "testAnwesenheitstest"
                time.sleep(random.random()*5)
            if test == "Anwesenheitstests":
                continue
            text_channel_list = []
            voice_channel_list = []
            for guild in client.guilds:
                for channel in guild.text_channels:
                    text_channel_list.append(channel)
                for channel in guild.voice_channels:
                    voice_channel_list.append(channel)
                    break
            if args.noText == False:
                for channel in text_channel_list:
                    await channel.send(f"Anwesenheitstest: {test}!\nhttps://moodle.mosbach.dhbw.de/course/view.php?id=12679")
            if args.quiet == False:
                await distribute(voice_channel_list)

    client.run(args.discord)
else:
    borabora()



