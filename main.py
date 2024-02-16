from highrise import BaseBot, Position
from highrise import __main__
from json import load, dump
from time import time, sleep
from highrise import *
from highrise.models import *
from highrise.webapi import *
from highrise.models_webapi import *
from datetime import timedelta
from highrise import BaseBot, User, Position, AnchorPosition
from highrise.__main__ import SessionMetadata
from highrise.models import (
    AnchorPosition,
    ChannelEvent,
    ChannelRequest,
    ChatEvent,
    ChatRequest,
    CurrencyItem,
    EmoteEvent,
    EmoteRequest,
    Error,
    FloorHitRequest,
    GetRoomUsersRequest,
    GetWalletRequest,
    IndicatorRequest,
    Item,
    Position,
    Reaction,
    ReactionEvent,
    ReactionRequest,
    SessionMetadata,
    TeleportRequest,
    TipReactionEvent,
    User,
    UserJoinedEvent,
    UserLeftEvent,
)
import multiprocessing
import random
import datetime
import os
import json
import asyncio
from highrise.models import AnchorPosition
from highrise import BaseBot, __main__

from highrise import BaseBot

from highrise import BaseBot, User, Position, AnchorPosition
from highrise.models import Position
import time
import random
from highrise import *
from highrise.models import *
import asyncio
dancs = [
    "emote-lust",
    "emote-superpose",
    "dance-tiktok10",
    "dance-weird",
    "emote-charging",
    "emote-snowball",
    "emote-hot",
    "emote-snowangel",
    "dance-russian",
    "emote-curtsy",
    "emote-bow",
    "dance-pennywise",
    "dance-blackpink",
    "emote-model",
    "dance-tiktok8",
    "dance-tiktok2",
    "dance-macarena",
    "emoji-gagging",
    "emoji-flex",
    "emoji-celebrate",
    "emoji-cursing",
    "idle-loop-sitfloor",
    "emote-yes",
    "emote-sad",
    "emote-no",
    "emote-laughing",
    "emote-kiss",
    "emote-hello",
    "emote-zombierun",
    "emote-pose8",
    "emote-pose7",
    "emote-pose5",
    "emote-pose3",
    "emote-pose1",
    "idle-dance-casual",
    "emote-cutey",
    "emote-astronaut",
    "idle-dance-tiktok4",
    "emote-punkguitar",
    "dance-icecream",
    "emote-gravity",
    "emote-fashionista",
    "idle-uwu",
    "dance-wrong"
]
valuesss = "ghjk"
user_ad = ["c1q", "C0ffe1nkA", "M4O1", "", "fjia"]
class MyBot(BaseBot):

  def __init__(self):
    self.dances = {
      "emote-lust": 4,
      "emote-superpose": 4,
      "dance-tiktok10": 8,
      "dance-weird": 21.5,
      "emote-charging": 7,
      "emote-snowball": 4,
      "emote-hot": 4.1,
      "emote-snowangel": 5.5,
      "dance-russian": 10,
      "emote-curtsy": 2.3,
      "emote-bow": 3,
      "dance-pennywise": 1,
      "dance-blackpink": 7,
      "emote-model": 5.5,
      "dance-tiktok8": 10.5,
      "dance-tiktok2": 10,
      "emoji-gagging": 5.5,
      "emoji-flex": 1.6,
      "emoji-celebrate": 2.6,
      "emoji-cursing": 2,
      "emote-yes": 2,
      "emote-sad": 4.3,
      "emote-laughing": 2.5,
      "emote-kiss": 3.2,
      "emote-hello": 2.3,
      "emote-zombierun": 9,
      "emote-pose8": 4,
      "emote-pose7": 4.3,
      "emote-pose5": 4.2,
      "emote-pose3": 4,
      "emote-pose1": 2.5,
      "idle-dance-casual": 9,
      "emote-cutey": 2.5,
      "emote-astronaut": 12.2,
      "idle-dance-tiktok4": 15,
      "emote-punkguitar": 8.1,
      "dance-icecream": 14.3,
      "emote-gravity": 6,
      "emote-fashionista": 5,
      "dance-wrong": 12.3,
    }
    self.in_area_users = set()
    self.dance_event = asyncio.Event()
    self.ord = None
    self.ter = []
    self.run = False
    self.d = []
    self.current_dance = None
  async def on_start(self, SessionMetadata: SessionMetadata) -> None:
    try:
        print("on")
        asyncio.create_task(self.send_continuous_dances())
    except Exception as e:
        print(f"error : {e}")
  async def send_continuous_dances(self):
    while True:
        valid_users = []
        users_positions = await self.highrise.get_room_users()
        for user, position in users_positions.content:
            if isinstance(position, Position):
                x_range = (0, 18)
                y_range = (0, 7)
                z_range = (0, 8)
                if (
                    x_range[0] <= position.x <= x_range[1]
                    and y_range[0] <= position.y <= y_range[1]
                    and z_range[0] <= position.z <= z_range[1]
                ):
                    valid_users.append(user)

        random_dance, duration = random.choice(list(self.dances.items()))
        duration = float(duration)

        async def send_emote_safely(user):
            try:
                await self.highrise.send_emote(random_dance, user.id)
            except Exception as e:
                print(f"Error sending dance to {user.id}: {e}")

        tasks = [asyncio.create_task(send_emote_safely(user)) for user in valid_users]
        await asyncio.gather(*tasks)
        await asyncio.sleep(duration - 0.5)
        valid_users = []

  async def on_user_join(self, user: User, position: Position | AnchorPosition) -> None:
    if user.username=="c1q":
        await self.highrise.send_whisper(user.id, "امنورنا🤍")
    pass

  async def print_message(self, message: str, user: User) -> None:
    try:
        dance_number = int(message.split()[0])
        if 1 <= dance_number <= len(dancs):
            current_dance = dancs[dance_number - 1]
            while True:
                try:
                    await self.highrise.send_emote(current_dance, user.id)
                    await asyncio.sleep(0.6)
                except Exception as e:
                    print(f"Chat Error: {e}")
                    break
    except ValueError:
        print("Invalid dance number format")

  async def on_chat(self, user: User, message: str) -> None:
    global valuesss
    if message.startswith("الحك") and user.username in user_ad:
      values = message.split()
      valuesss = values[1].replace("@", "")
    elif message.startswith("توقف") and user.username in user_ad:
      await self.highrise.chat("حسنا")
      valuesss = "#####"
      self.stopped = True
      return
    if message.startswith("هزو") and user.username in user_ad:
                random_dans = random.sample(dancs, 1)[0]
                list = await self.highrise.get_room_users()
                for user, position in list.content:
                    try:
                        await self.highrise.send_emote(random_dans, user.id)
                    except:
                        print("erorr")

    if message.isdigit() and len(message.split()) > 0:
        if not hasattr(self, 'print_tasks'):
            self.print_tasks = {}

        if hasattr(self, 'print_tasks') and user.id in self.print_tasks and not self.print_tasks[user.id].done():
            self.print_tasks[user.id].cancel()
            await asyncio.sleep(0.1)

        self.print_tasks[user.id] = asyncio.create_task(self.print_message(message, user))

    if message.startswith(("توقف", "stop", "ايقاف", "0")):
        try:
          if hasattr(self, 'print_tasks') and user.id in self.print_tasks and not self.print_tasks[user.id].done():
            self.print_tasks[user.id].cancel()
            await asyncio.sleep(1)
        except ValueError:
            print("Invalid dance number format")


    if message.startswith("نزلني") :
      await self.highrise.teleport(user.id, Position(x='9', y='4', z='1'))
    if message.startswith("انتقال") and user.username in user_ad:
        if user.username not in self.ter:
            self.ter.append(user.username)
        else:
            print("u r in")
    if message.startswith("مشي") and user.username in user_ad:
        if user.username in self.ter:
            self.ter.remove(user.username)
        else:
            print("u r not ")
    if message.startswith("VIP") : #and user.username in user_ad:
      await self.highrise.teleport(user.id, Position(x='13.5', y='11.2', z='17'))
    if message.startswith("927373829") and user.username == "c1q":
        list = await self.highrise.get_room_users()
        for user, position in list.content:
            try:
                await self.highrise.move_user_to_room(user.id, '655a7f15c9ad99cfd71031c0')
            except Exception as e:
                print(f"حدث خطأ: {e}")
    if user.username in user_ad:
        if message.startswith(("حظر", "بلوك","اطرد")):
            try:
                name_to_add = message1.split('@')[1]
                room_users = await self.highrise.get_room_users()
                username_targ = name_to_add
                for user, position in room_users.content:
                    if user.username == username_targ:
                        id_user = user.id
                        await self.highrise.moderate_room(id_user, "ban", action_length=1440)
            except Exception as e:
                print(f"Chat Error: {e}")
        if message.startswith("ميوت"):
            try:
                name_to_add = message1.split('@')[1]
                room_users = await self.highrise.get_room_users()
                username_targ = name_to_add
                for user, position in room_users.content:
                    if user.username == username_targ:
                        id_user = user.id
                        await self.highrise.moderate_room(id_user, "mute", action_length=1440)
            except Exception as e:
                print(f"Chat Error: {e}")

  async def on_user_move(self, user: User, destination: Position | AnchorPosition) -> None :
      if user.username=="c1q":
          print(destination)
      try:
          if user.username==valuesss:
                self.x = destination.x
                self.y = destination.y
                self.z = destination.z
                await self.highrise.walk_to(Position(self.x, self.y, self.z - 1))
          if user.username in self.ter:
              if isinstance(destination, AnchorPosition):
                  print(f"AnchorPosition(entity_id={destination.entity_id}, anchor_ix={destination.anchor_ix}")
              else:
                  await self.highrise.teleport(user.id, Position(x=destination.x, y=destination.y, z=destination.z))
      except Exception as e:
          print(f"Error : {e}")
  async def on_reaction(self, user: User, reaction: Reaction, receiver: User) -> None:
    if user.username == "c1q":
        if reaction == "thumbs" :
            try:
                await self.highrise.move_user_to_room(receiver.id, '')
                await self.highrise.chat(f"لم نتشرف بك ضيفا فلا تكرر زيارتنا ، لقد تم طرد المستخدم  {user.username}")
            except Exception as e:
                print(f"حدث خطأ: {e}")
    if user.username in user_ad:
        if reaction == "wave" :
            try:
                r_username = receiver.username
                print(f"receiver: {r_username}")
                list = await self.highrise.get_room_users()
                username_targ = user.username
                for user, position in list.content:
                    if user.username == username_targ:
                        print(f"User: {user.username}")
                        print(f"id: {user.id}")
                        positions = f"{position.x}, {position.y}, {position.z}"
                        await self.highrise.teleport(receiver.id, Position(x=position.x, y=position.y, z=position.z - 1))
            except Exception as e:
                print(f"حدث خطأ: {e}")