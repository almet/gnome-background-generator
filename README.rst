Gnome animated background generator
###################################

Gnome background can use XML files to make an animated background. 
This little script allows you to generate automaticaly your own XML background
changer file, easily, using the command line.

To generate the XML file, use `gnome-background-generator`::

    usage: gnome-background-generator [-h] [-p PATH] [-o OUTPUT]
                                  [-t TRANSITION_TIME] [-d DISPLAY_TIME] [-s]
                                  [-b]

    A simple command line tool to generate an XML file to use for gnome
    wallpapers, to have dynamic walls

    optional arguments:
      -h, --help            show this help message and exit
      -p PATH, --path PATH  Path to look for the pictures. If no output is
                            specified, will be used too for outputing the dynamic-
                            wallpaper.xml file. Default value is the current
                            directory (.)
      -o OUTPUT, --output OUTPUT
                            Output filename. If no filename is specified, a
                            dynamic-wallpaper.xml file will be generated in the
                            path containing the pictures. You can also use "-" to
                            display the xml in the stdout.
      -t TRANSITION_TIME, --transition-time TRANSITION_TIME
                            Time (in seconds) transitions must last (default value
                            is 2 seconds)
      -d DISPLAY_TIME, --display-time DISPLAY_TIME
                            Time (in seconds) a picture must be displayed. Default
                            value is 900 (15mn)
      -s, --set-background  '''try to set the background using gnome-appearance-
                            properties
      -b, --debug

There is also another command you can use to change your background to a random
file from a known directory::

    $ gnome-wallpaper-select /path/to/walls 

This second one is useful if combined with a cronjob :)
