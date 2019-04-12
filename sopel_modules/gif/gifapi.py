# coding=utf-8

from __future__ import unicode_literals, absolute_import, division, print_function

from .gifsearch import *

config_prefix = '^\.(.*)'


def setup(bot):
    global config_prefix
    config_prefix = bot.config.core.prefix


@module.rule(config_prefix)
def gifapi_triggers(bot, trigger):
    triggerargs, prefixcommand = sopel_triggerargs(bot, trigger, 'prefix_command')

    if prefixcommand not in bot.memory["Sopel-GifSearch"]['valid_gif_api_dict'].keys():
        return

    if triggerargs == []:
        return bot.osd("Please present a query to search.")

    query = spicemanip.main(triggerargs, 0)
    searchapis = bot.memory["Sopel-GifSearch"]['valid_gif_api_dict'].keys()
    searchdict = {"query": query, "gifsearch": searchapis}

    gifdict = getGif(bot, searchdict)

    if gifdict["error"]:
        bot.osd(gifdict["error"])
    else:
        bot.osd(str(gifdict['gifapi'].title() + " Result (" + str(query) + " #" + str(gifdict["returnnum"]) + "): " + str(gifdict["returnurl"])))
