Dynamic background generator
############################

This package propose two ways to dynamically change your desktop automatically.
One is by generating a XML file, that can be used by any GNOME desktop
compatible system (such as GNOME 2 and 3, Unity, MATE and Cinnamon), and the other
one is a little script you can run to randomly select a picture from a path.

Using XML files
===============

GNOME background compatible desktop environment can use XML files to make an
animated background. 
This little script allows you to automatically generate your own XML background
changer file, easily, using the command line.

To generate the XML file, use `gnome-background-generator`::

    usage: gnome-background-generator [-h] [-v] [-o OUTPUT]
                                  [-r] [-t TRANSITION_TIME] [-d DISPLAY_TIME]
                                  [-R] [-f] [directory [directory ...]]

    A simple command line tool to generate an XML file to use for gnome
    wallpapers, to have dynamic walls

    positional arguments:
      directory             Directory path that should be searched for image files

    optional arguments:
      -h, --help            show this help message and exit
      -r, --randomize       Randomly shuffle scanned images
      -R, --recursive       Recursivly scan the given directories
      -f, --follow-symlinks
                            Follow symbolic links when scanning directories
                            recursivly (implies --recursive)
      -o OUTPUT, --output OUTPUT
                            Output filename. If no filename is specified, a
                            dynamic-wallpaper.xml file will be generated in the
                            path containing the pictures. You can also use "-" to
                            display the xml in the stdout
      -t TRANSITION_TIME, --transition-time TRANSITION_TIME
                            Time (in seconds) transitions must last [Default: 2]
      -d DISPLAY_TIME, --display-time DISPLAY_TIME
                            Time (in seconds) a picture must be displayed
                            [Default: 900 (15min)]
      -v, --debug

Examples
--------

1. Generate a file named `dynamic-background.xml` from all images in the current directory:
   ``gnome-background-generator``
2. Generate a file named `background.xml` in the current directory using all images in
   the directories "foo" and "bar" and all their subdirectories (even symlinked ones)
   in random order with a 5 second transition and a 15 second display time:
   ``gnome-background-generator -o background.xml -r -t 5 -d 15 -R -f foo bar``

Gnome 3 Background Settings
===========================

We need to add the new dynamic-background.xml file generated above to the gnome-background-properties manifest.

1. Create a new directory::

   $ mkdir -p ~/.local/share/gnome-background-properties

2. Add a new file in this directory named `custom.xml` with this content::

    <?xml version="1.0" encoding="UTF-8"?>
    <!DOCTYPE wallpapers SYSTEM "gnome-wp-list.dtd">
    <wallpapers>
     <wallpaper deleted="false">
       <name>Gnome Background Generator Wallpapers</name>
       <filename>/path/to/dynamic-wallpaper.xml</filename>
       <options>zoom</options>
     </wallpaper>
    </wallpapers>

Next we need to reference our dynamic-background.xml file from the Gnome 3 Settings

1. Open the "Activities" overview and start typing "Settings"
2. Click on "Background"
3. Select either the "Background" or "Lock Screen"
4. Find your dynamic background entry and select it

Changing your desktop randomly
==============================

There is also another command you can use to change your background to a random
file from a known directory::

    $ gnome-wallpaper-select /path/to/walls 

This second one is useful if combined with a cronjob; Unfortunately, it's
sometimes a hard process because crontabs use dbus, and this conflicts with the
use of `gconftool-2`.

Here is a simple tutorial on how to make it work::

    $ wget http://github.com/ametaireau/gnome-background-generator/raw/master/xdbus -O ~/.Xdbus
    $ crontab -e

And then add ::

    */4 * * * * . ~/.Xdbus; /usr/local/bin/gnome-wallpaper-select ~/Images/walls
