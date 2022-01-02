import pymongo
import requests
import os
import random

from dotenv import load_dotenv
from bs4 import BeautifulSoup

load_dotenv()

client = pymongo.MongoClient(os.getenv('DB_URL'))

# channels db
db_channels = client.channel_id

# chapter db
db_chapter = client.chapter

# chapters data
data_rz = db_chapter.data
data_kaguya = db_chapter.data_kaguya
data_onk = db_chapter.data_onk

# flip image urls db
db_flips = client.flips

# flip image urls data
flips = db_flips.data

# channels data
channels_rz = db_channels.data
channels_kaguya = db_channels.data_kaguya
channels_onk = db_channels.data_onk

async def send_messages(bot, channels, title, data, db_rec, anchor):
  if db_rec['title'] != title:
    data.find_one_and_update({'title':str(db_rec['title'])}, { '$set': { "title" : title} })
    for channel in channels.find():
          if bot.get_channel((channel['id'])):
            try:
              await (bot.get_channel(int(channel['id']))).send(f'Chapter {title} has been translated.\n{anchor}, I suppose!')
            except Exception as e:
              print(f"The channel with id {channel['id']} is private, I suppose!")

# sends the latest english translated chapter
async def commands_latest_chapter(ctx):
  page = requests.get('https://witchculttranslation.com/arc-7/')

  soup = BeautifulSoup(page.content, 'html.parser')

  most_recent_post = soup.find_all('h3', 'rpwe-title')[0]

  post_link = most_recent_post.find('a')

  try:
      if 'href' in post_link.attrs:
          latest_chapter_translated_link = post_link.get('href')
  except:
      pass

  title = most_recent_post.text
  await ctx.send(f'Latest translated chapter is {title}, I suppose!\n{latest_chapter_translated_link}')

# add the channel to the receiver list
async def commands_add_channel(id, series):
  channel_entry = {
    'id': id,
  }
  success_msg = "This text channel will receive notifications, I suppose!"
  failure_msg = "This text channel is already on the receiver list, in fact!"
  is_in_list = channels_rz.count_documents(channel_entry, limit = 1) != 0
  is_in_kaguya_list = channels_kaguya.count_documents(channel_entry, limit = 1) != 0
  is_in_onk_list = channels_onk.count_documents(channel_entry, limit = 1) != 0
  if (series == "rz" or series == "rezero"):
        if (not is_in_list):
          channels_rz.insert_one(channel_entry)
          return success_msg
        else:
          return failure_msg
  elif (series == "kaguya" or series == "kaguya-sama" or series == "ks"):
        if (not is_in_kaguya_list):
          channels_kaguya.insert_one(channel_entry)
          return success_msg
        else:
          return failure_msg
  elif (series == "onk" or series == "oshi-no-ko" or series == "oshi no ko"):
        if (not is_in_onk_list):
          channels_onk.insert_one(channel_entry)
          return success_msg
        else:
          return failure_msg
  elif (series == "" or series == " "):
        return "To what list do you want to add this channel, in fact?!"
  else:
        return "What is that, I suppose?!"

# remove the channel from the receiver list
async def commands_remove_channel(id, series):
  channel_entry = {
    'id': id,
  }
  success_msg = "This text channel will no longer receive notifications, I suppose!"
  failure_msg = "This text channel is not on the receiver list, in fact!"
  is_in_list = channels_rz.count_documents(channel_entry, limit = 1) != 0
  is_in_kaguya_list = channels_kaguya.count_documents(channel_entry, limit = 1) != 0
  is_in_onk_list = channels_onk.count_documents(channel_entry, limit = 1) != 0
  if (series == "rz" or series == "rezero"):
        if (is_in_list):
          channels_rz.find_one_and_delete(channel_entry)
          return success_msg
        else:
          return failure_msg
  elif (series == "kaguya" or series == "kaguya-sama" or series == "ks"):
        if (is_in_kaguya_list):
          channels_kaguya.find_one_and_delete(channel_entry)
          return success_msg
        else:
          return failure_msg
  elif (series == "onk" or series == "oshi-no-ko" or series == "oshi no ko"):
        if (is_in_onk_list):
          channels_onk.find_one_and_delete(channel_entry)
          return success_msg
        else:
          return failure_msg
  elif (series == "" or series == " "):
        return "From what list do you want to remove this channel, in fact?!"
  else:
        return "What is that, I suppose?!"

# task that removes non existing(deleted) channels every 10 seconds
async def tasks_filter_channels(bot):
  for channel in channels_rz.find():
    if not bot.get_channel((channel['id'])):
      channel_entry = {
        'id': channel['id'],
      }
      channels_rz.find_one_and_delete(channel_entry)
  for channel in channels_kaguya.find():
    if not bot.get_channel((channel['id'])):
      channel_entry = {
        'id': channel['id'],
      }
      channels_kaguya.find_one_and_delete(channel_entry)
  for channel in channels_onk.find():
    if not bot.get_channel((channel['id'])):
      channel_entry = {
        'id': channel['id'],
      }
      channels_onk.find_one_and_delete(channel_entry)

# task that checks chapter every 10 seconds
async def tasks_check_chapter(bot):
  try:
    is_wct_down = False
    is_guya_down = False
    try:
      page = requests.get('https://witchculttranslation.com/arc-7/', timeout=5)
    except requests.Timeout:
      print("WitchCultTranslation down!")
      is_wct_down = True
      sleep(1)
    try:
      page_kaguya = requests.get('https://guya.moe/read/manga/Kaguya-Wants-To-Be-Confessed-To/', timeout=5)
    except requests.Timeout:
      print("Guya.Moe down!")
      is_guya_down = True
      sleep(1)
    try:
      page_onk = requests.get('https://guya.moe/read/manga/Oshi-no-Ko/', timeout=5)
    except requests.Timeout:
      print("Guya.moe down!")
      is_guya_down = True
      sleep(1)

    if (not is_wct_down):
      # web scraping for re zero
      soup = BeautifulSoup(page.content, 'html.parser')
      most_recent_post = soup.find_all('h3', 'rpwe-title')[0]

      post_link = most_recent_post.find('a')

      most_recent_post = most_recent_post.text
      most_recent_post_array = most_recent_post.split()

      most_recent_post_str = ""

      for i in range(0, 4):
          most_recent_post_str += most_recent_post_array[i] + " "

      most_recent_post_str = most_recent_post_str.strip()

      if 'href' in post_link.attrs:
          latest_chapter_translated_link = post_link.get('href')

      last_chapter = db_chapter.data.find_one()
      
      await send_messages(bot, channels_rz, most_recent_post_str, data_rz, last_chapter, latest_chapter_translated_link)
      
    if (not is_guya_down):
      # web scraping for kaguya-sama
      soup_kaguya = BeautifulSoup(page_kaguya.content, 'html.parser')
  
      most_recent_kaguya_chapter = soup_kaguya.find_all('td', 'chapter-title')[0]
  
      kaguya_chapter_link = most_recent_kaguya_chapter.find('a')
  
      
      if 'href' in post_link.attrs:
        kaguya_chapter_anchor = 'https://guya.moe'
        kaguya_chapter_anchor += kaguya_chapter_link.get('href')
        
      most_recent_kaguya_chapter_title = kaguya_chapter_link.text
  
      most_recent_kaguya_chapter_array = most_recent_kaguya_chapter_title.split()
  
      most_recent_kaguya_chapter_str = ""
  
      for i in range(0, len(most_recent_kaguya_chapter_array)):
        most_recent_kaguya_chapter_str += most_recent_kaguya_chapter_array[i] + " "
  
      most_recent_kaguya_chapter_str = most_recent_kaguya_chapter_str.strip()
  
      last_kaguya_chapter = db_chapter.data_kaguya.find_one()
      
      await send_messages(bot, channels_kaguya, most_recent_kaguya_chapter_str, data_kaguya, last_kaguya_chapter, kaguya_chapter_anchor)
  
      # web scraping for oshi no ko
      soup_onk = BeautifulSoup(page_onk.content, 'html.parser')
  
      most_recent_onk_chapter = soup_onk.find_all('td', 'chapter-title')[0]
  
      onk_chapter_link = most_recent_onk_chapter.find('a')
  
      if 'href' in post_link.attrs:
        onk_chapter_anchor = 'https://guya.moe'
        onk_chapter_anchor += onk_chapter_link.get('href')
        
      most_recent_onk_chapter_title = onk_chapter_link.text
  
      most_recent_onk_chapter_array = most_recent_onk_chapter_title.split()
  
      most_recent_onk_chapter_str = ""
  
      for i in range(0, len(most_recent_onk_chapter_array)):
        most_recent_onk_chapter_str += most_recent_onk_chapter_array[i] + " "
  
      most_recent_onk_chapter_str = most_recent_onk_chapter_str.strip()
  
      last_onk_chapter = db_chapter.data_onk.find_one()
  
      await send_messages(bot, channels_onk, most_recent_onk_chapter_str, data_onk, last_onk_chapter, onk_chapter_anchor)
      
  except:
      pass
  
            
# flip command        
async def commands_flip(ctx):
  pipe = [{ '$sample': { 'size': 1 } }]
  flip = list(flips.aggregate(pipeline=pipe))[0]['url']
  await ctx.send(flip)