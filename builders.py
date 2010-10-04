#!/usr/bin/env python
#-*- coding: utf8 -*-

# Copyright (c) 2010 Alexis Metaireau

from xml.dom.minidom import Document


class XmlBackgroundBuilder():
    """Build the xml file from a configuration object and a path.

    """
    def __init__(self, transition_time, display_time):
        """Constructor. Initialize path and conf.

        """
        self.transition_time = transition_time
        self.display_time = display_time

    def build_xml(self, pictures_list):
        """Return the backgroun.xml file.

        """
        doc = Document()
        background = doc.createElement('background')
        doc.appendChild(background)

        for pic in pictures_list:
            try:
                next = pictures_list[pictures_list.index(pic) + 1]
            except IndexError:
                next = pictures_list[0]

            static = doc.createElement('static')

            duration = doc.createElement('duration')
            duration.appendChild(doc.createTextNode("%s.0" % self.display_time))
            static.appendChild(duration)

            file = doc.createElement('file')
            file.appendChild(doc.createTextNode(pic))
            static.appendChild(file)

            background.appendChild(static)

            transition = doc.createElement('transition')

            duration = doc.createElement('duration')
            duration.appendChild(doc.createTextNode("%s.0" % self.transition_time))
            transition.appendChild(duration)

            fromel = doc.createElement('from')
            fromel.appendChild(doc.createTextNode(pic))
            transition.appendChild(fromel)

            to = doc.createElement('to')
            to.appendChild(doc.createTextNode(next))
            transition.appendChild(to)

            background.appendChild(transition)

        print doc.toxml()
