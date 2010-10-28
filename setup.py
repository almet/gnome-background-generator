from distutils.core import setup
import sys

if sys.version_info < (2,7):
    requires = ['argparse', ]

setup(
    name = "gnome-background-generator",
    version = '1.1',
    url = 'http://github.com/ametaireau/gnome-background-generator/',
    author = 'Alexis Metaireau',
    author_email = 'alexis@notmyidea.org',
    description = """A simple utility command line to generate a XML file for
                  dynamic gnome wallpapers""",
    long_description=open('README.rst').read(),
    requires = requires, 
    scripts = ['gnome-background-generator', 'gnome-wallpaper-select'],
    classifiers = ['Development Status :: 5 - Production/Stable',
                   'Environment :: Console',
                   'License :: OSI Approved :: GNU Affero General Public License v3',
                   'Environment :: X11 Applications :: Gnome',
                   'Operating System :: POSIX :: Linux',
                   'Programming Language :: Python',
                   ],
)
