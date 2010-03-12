#!/usr/bin/env python
#-*- coding: utf8 -*-

# Copyright (c) 2010 Alexis Metaireau
# Part of this file are (c) 2009 Bruno Bord

import os
from xdg.BaseDirectory import xdg_config_home
from ConfigParser import SafeConfigParser

class Configuration():
    """Configuration file"""
    
    def __init__(self, options=None):
        self.debug = False
        if options:
            self.debug = options.debug
            
        config_dir = xdg_config_home
        self.conf_dir = os.path.join(config_dir,self.project_name)
        self.config = SafeConfigParser()
        self.conf_file = os.path.join(self.conf_dir, '%s.conf' % self.project_name)
        
        # variable definition here
        for (option, value) in self.available_options.items():
            setattr(self, option, value)
        
        if not os.path.isfile(self.conf_file):
            if self.debug:
                print "Configuration file not found, creating it"
            self.write()
        self.read()
        #overwrite configuration with options if present.
        for option in self.available_options:
            if hasattr(options, option):
                attr = getattr(options, option, False)
                if attr:
                    setattr(self, option, attr)
        
    def write(self):
        "Write settings in the configuration file"
        if self.debug:
            print "Writing configuration file"

        if not os.path.isdir(self.conf_dir):
            os.makedirs(self.conf_dir)

        if not self.config.has_section('general'):
            self.config.add_section('general')
        # setting Feed URL
        for option in self.available_options:     
            self.config.set('general', option, getattr(self, option))

        # finally writing the file.
        with open(self.conf_file, 'wb') as configfile:
            self.config.write(configfile)
            configfile.close()

    def read(self):
        "Reading settings from configuration file"
        if self.debug:
            print "Reading configuration file", self.conf_file
        self.config.read(self.conf_file)
        for option in self.available_options:
            setattr(self, option, self.config.get('general', option))
