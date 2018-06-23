#!/usr/bin/python
#coding=UTF-8
import logging
import os, re, sys;
from urllib import parse;
from datetime import datetime, timedelta;

# from pymongo import MongoClient
from telegram.error import BadRequest
from telegram.ext import Updater, CommandHandler, RegexHandler
from telegram.ext import MessageHandler, Filters

def get_your_id(bot, update):
	print("get_your_id")

def main(*args, **kargs):
	updater = Updater("579796202:AAGQuScRkOsChEsA9aEWfZT2aS-UyEPsb-Y")
	updater.dispatcher.add_handler(CommandHandler("id", get_your_id))

	updater.start_polling()
	updater.idle()

if __name__ == '__main__':
	main(port=60030)