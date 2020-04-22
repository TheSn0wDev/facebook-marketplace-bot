# -*- coding: utf-8 -*-

from fbchat import Client
from fbchat.models import *
from config import *
from time import sleep
import random, re


class MarketBot(Client):
    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):

        if author_id != self.uid:

            if (message_object.text == "Cet article est-il toujours disponible ?") or (message_object.text == "Cet article m’intéresse.") or (message_object.text == "Is this still available?") or (message_object.text == "Est-ce toujours disponible ?") or (message_object.text == "Isto está disponível?"):
                sleep(random.randrange(5,15))
                self.markAsDelivered(thread_id, message_object.uid)
                self.markAsRead(thread_id)
                self.setTypingStatus(TypingStatus.TYPING, thread_id=thread_id, thread_type=thread_type)
                sleep(random.randrange(10,25))
                self.send(Message(text=default_message), thread_id=thread_id, thread_type=thread_type)

            if message_object.text.find('livr') >= 0:
                sleep(random.randrange(5,15))
                self.markAsDelivered(thread_id, message_object.uid)
                self.markAsRead(thread_id)
                self.setTypingStatus(TypingStatus.TYPING, thread_id=thread_id, thread_type=thread_type)
                sleep(random.randrange(10,25))
                self.send(Message(text=deliver_message), thread_id=thread_id, thread_type=thread_type)

            if (message_object.text.find('etat') >= 0) or (message_object.text.find('état') >= 0):
                sleep(random.randrange(5,15))
                self.markAsDelivered(thread_id, message_object.uid)
                self.markAsRead(thread_id)
                self.setTypingStatus(TypingStatus.TYPING, thread_id=thread_id, thread_type=thread_type)
                sleep(random.randrange(10,20))
                self.send(Message(text=status_phone_message), thread_id=thread_id, thread_type=thread_type)

            if message_object.text.lower() == "ok":
                sleep(random.randrange(5,15))
                self.markAsDelivered(thread_id, message_object.uid)
                self.markAsRead(thread_id)
                self.reactToMessage(message_object.uid, MessageReaction.YES)


client = MarketBot(email, password)
client.listen()