# coding=utf-8

from __future__ import unicode_literals, absolute_import, division, print_function

from sopel import module
from sopel.tools import stderr

try:
    from sopel_modules.botevents.botevents import *
    botevents_installed = True
except ImportError:
    botevents_installed = False

import os


def configure(config):
    pass


def setup(bot):
    if "Sopel-GifSearch" not in bot.memory:
        stderr("[Sopel-GifSearch] Starting Setup Procedure")
        bot.memory["Sopel-GifSearch"] = {"cache": {}}

        moduledir = os.path.dirname(os.path.abspath(__file__))
        api_dir = os.path.join(moduledir, 'gifapi')
        stderr(str(api_dir))

    if botevents_installed:
        set_bot_event(bot, "gifsearch")


@module.commands('gif')
def hello_world(bot, trigger):
    bot.say('Hello, world!')
