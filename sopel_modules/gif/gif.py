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
import codecs


def configure(config):
    pass


def setup(bot):
    if "Sopel-GifSearch" not in bot.memory:
        stderr("[Sopel-GifSearch] Starting Setup Procedure")
        bot.memory["Sopel-GifSearch"] = {"cache": {}}

        moduledir = os.path.dirname(os.path.abspath(__file__))
        api_dir = os.path.join(moduledir, 'gifapi')
        configs_dict = read_directory_json_to_dict([api_dir], "Gif API", "[Sopel-GifSearch] ")

    if botevents_installed:
        set_bot_event(bot, "gifsearch")


@module.commands('gif')
def hello_world(bot, trigger):
    bot.say('Hello, world!')


def read_directory_json_to_dict(directories, configtypename="Config File", stderrname=''):

    if not isinstance(directories, list):
        directories = [directories]

    configs_dict = {}
    filesprocess, fileopenfail, filecount = [], 0, 0
    for directory in directories:
        if os.path.exists(directory) and os.path.isdir(directory):
            if len(os.listdir(directory)) > 0:
                for file in os.listdir(directory):
                    filepath = os.path.join(directory, file)
                    if os.path.isfile(filepath):
                        filesprocess.append(filepath)

    for filepath in filesprocess:

        # Read dictionary from file, if not, enable an empty dict
        filereadgood = True
        inf = codecs.open(filepath, "r", encoding='utf-8')
        infread = inf.read()
        try:
            dict_from_file = eval(infread)
        except Exception as e:
            filereadgood = False
            stderr(stderrname + "Error loading %s: %s (%s)" % (configtypename, e, filepath))
            dict_from_file = dict()
        # Close File
        inf.close()

        if filereadgood and isinstance(dict_from_file, dict):
            filecount += 1
        else:
            fileopenfail += 1

    if filecount:
        stderr(stderrname + '\n\nRegistered %d %s files,' % (filecount, configtypename))
        stderr(stderrname + '%d %s files failed to load\n\n' % (fileopenfail, configtypename))
    else:
        stderr(stderrname + "Warning: Couldn't load any %s files" % (configtypename))

    return configs_dict
