==========
ASSIGNMENT
==========

In this repository you'll find code for an application which aims to support
various transposition ciphers. Since the application uses a plugin architecture
each cipher should be introduced as a standalone plugin.
Your tasks for this assignment are:

- create plugins for the following transposition ciphers (see `Plugin interface`_):
    - `Vigenere cipher <https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher>`_
    - `Rail fence cipher <https://en.wikipedia.org/wiki/Rail_fence_cipher>`_

- provide implementation to all the ``IMPLEMENT ME!`` marked sections you'll
  find in this repository so that the application can actually do something
  (see `CLI Interface`_)

Installation
============

For this project, no dependencies are needed, so the following is all that is
needed:

::

    $ python3 setup.py install --user

or

::

    $ python3 setup.py develop --user

.. note:: You can also install to a virtual environment if you prefer.


Implementation
==============

Plugin interface
----------------

Each plugin needs to be implemented as a standalone package located inside
the ``transpose/plugins`` directory. In order for the plugin to work and be
hooked into the main application properly, you'll have to implement the
``Plugin`` interface which:

- inherits from the provided ``PluginCore`` abstract class
- the ``Plugin`` class should be instantiated when the plugin's package
  module is loaded
- when ``Plugin`` is being instantiated it has to register its CLI options
  with the main singleton CLI parser

Cipher modules
--------------

The plugin also comes with the cipher implementation itself. You'll have to
create the ``Vigenere`` and ``RailFence`` classes in the respective plugin
modules. Both classes inherit from the ``Cipher`` abstract class.

CLI interface
-------------
Each of the ciphers has some specifics for which you'll need to provide all
necessary CLI options in order for the algorithms to work - you'll need to use
the main ``Parser`` instance when you're plugin is being registered.

Note that some common CLI options are already provided by the skeleton (and
your solution will inherit them automatically), so check the code before
wasting time on re-implementing the whole CLI parser!

If everything is hooked up correctly the end result CLI interface should look
like the following:

::

    $ transpose --help

    usage: transpose [-h] CIPHER ...

    transposition cipher tool

    positional arguments:
      CIPHER
        vigenere  Vigenere cipher
        rail_fence
                  Rail fence cipher

    optional arguments:
      -h, --help  show this help message and exit


    $ transpose vigenere --help

    usage: transpose vigenere [-h] (-c | -d) --key KEY text

    positional arguments:
      text           Text to encrypt/decrypt

    optional arguments:
      -h, --help     show this help message and exit
      -c, --encrypt  encrypt message
      -d, --decrypt  decrypt message
      ...

TO RUN TESTS
-----
::

    $ python3 -m unittest tests

NOTES
-----

- no external libraries are permitted, for this exercise you'll only need
  modules from the standard Python library
- the alphabet for the Vigenere cipher should support all printable ASCII
  characters not just the default A-Z characters you see in Wikipedia
- your solution should include some suitable error checking
- bonus points if you also provide some sort of unit tests! :)
