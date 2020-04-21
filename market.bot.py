# -*- coding: utf-8 -*-

from fbchat import Client
from fbchat.models import *
from config import *
from time import sleep
import random, re


class MarketBot(Client):
    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):

        if author_id != self.uid:

            if message_object.text == "Cet article est-il toujours disponible ?":
                sleep(random.randrange(10,25))
                self.send(Message(text=default_message), thread_id=thread_id, thread_type=thread_type)


            if message_object.text.find('livr') >= 0:
                sleep(random.randrange(10,25))
                self.send(Message(text=deliver_message), thread_id=thread_id, thread_type=thread_type)


client = MarketBot(email, password)
client.listen()