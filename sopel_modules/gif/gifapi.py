# coding=utf-8

from __future__ import unicode_literals, absolute_import, division, print_function

from .gifsearch import *


@module.commands('gifb')
def gif_trigger(bot, trigger):
    triggerargs = sopel_triggerargs(bot, trigger)
    if triggerargs == []:
        return bot.osd("Please present a query to search.")

    query = spicemanip.main(trigger.args[1], 0)
    searchapis = bot.memory["Sopel-GifSearch"]['valid_gif_api_dict'].keys()
    searchdict = {"query": query, "gifsearch": searchapis}

    gifdict = getGif(bot, searchdict)

    if gifdict["error"]:
        bot.osd(gifdict["error"])
    else:
        bot.osd(str(gifdict['gifapi'].title() + " Result (" + str(query) + " #" + str(gifdict["returnnum"]) + "): " + str(gifdict["returnurl"])))
