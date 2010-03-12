#!/usr/bin/env python
#-*- coding: utf8 -*-

# Copyright (c) 2010 Alexis Metaireau
# Part of this file are Copyrighted (c) 2009 Bruno Bord

"Generates a .XML file for gnome wallpapers"

from config import Configuration
from builders import XmlBackgroundBuilder

from optparse import OptionParser
import os

class GenBackgroundConfiguration(Configuration):
    project_name = 'genbackground'
    available_options = {
        'transition_time': '15', #15 seconds for a transition
        'display_time': '900', #15mn per picture
    }    
    authorized_extensions = ('jpg', 'png', 'jpeg')

class Main(object):
    "Main class. Handles the whole process"

    def __init__(self):
        # first things first, retreive options
        self.options, self.args = self.get_options()
        # configuration reading / writing
        self.configuration = GenBackgroundConfiguration(options=self.options)

    def get_options(self):
        "Retrieves the options using OptionParser"
        usage = '%prog [options]'
        parser = OptionParser(usage=usage)
        parser.add_option('-d', '--debug', action='store_true', default=False,
            help="display debug messages on the standard output")
        parser.add_option('-p', '--path', action='store', default=".",
            help="set the path to look for pictures."""
        )
        # options that may overwrite the configuration
        parser.add_option('-t', '--transition_time', default=None, type="int",
            help="set the transition time, overwriting the configuration value"
        )
        parser.add_option('--display-time', default=None, type="int",
            help="""set the display time for a picture, overwriting the 
            configuration value"""
        )

        return parser.parse_args()

    def generate_xml(self):
        "Generate the XML, according to preferences"
        builder = XmlBackgroundBuilder(
            self.configuration.transition_time,
            self.configuration.display_time, 
        )
        
        builder.build_xml(self.get_pictures_list(
            self.options.path, 
            self.configuration.authorized_extensions
        ))
        
    def get_pictures_list(self, path, authorized_extensions):
        """Return the list of pictures in a specific directory.
        
        """
        pictures_list = []
        for filename in os.listdir(path):
             if filename.split('.')[-1] in authorized_extensions:
                 pictures_list.append('%s%s' % (path, filename))
        return pictures_list
            
if __name__ == "__main__":
    main = Main()
    main.generate_xml()
