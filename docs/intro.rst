Introduction
************

* Definition: **Blogophile** (n):
   A person who is fond of or obsessed with blogs or blogging.

* Definition: **blogofobe** (n):
   A static website compiler and blog engine, written and extended in `Python`_. You know, for people that are scared of blogging because of the complexity of the tools out there.


Welcome to blogofobe
====================

blogofobe is a static website compiler, primarily (though not exclusively) designed to be a simple blogging engine. It requires no database and no special hosting environment. You customize a set of templates with `Mako <http://www.maktotemplates.org>`_, create posts in a markup language of your choice (see :ref:`post-content`) and blogofobe renders your entire website as static HTML and Atom/RSS feeds which you can then upload to any old web server you like. 

Why you should consider blogofobe
=================================

* blogofobe is **free open-source** software, released under a non-enforced `MIT License`_.
* blogofobe sites are **fast**, the web server doesn't need to do any database lookups nor any template rendering.
* blogofobe sites are **inexpensive** to host. Any web server can host a blogofobe blog.
* blogofobe is **modern**, supporting all the common blogging features:

 * Categories and Tags.
 * Comments, Trackbacks, and Social Networking mentions (Twitter,
   Reddit, FriendFeed etc), all with effective spam filtering using
   `Disqus <http://www.disqus.com>`_.
 * RSS and Atom feeds, one for all your posts, as well as one per
   category. Easily create additional feeds for custom content.
 * Syntax highlighting for source code listings.
 * Ability to create or share your own plugins in your own
   userspace (see :ref:`Filters <filters>` and :ref:`Controllers <controllers>`)

* blogofobe is **secure**, there's nothing executable on the server `to exploit <http://wordpress.org/news/2010/12/3-0-4-update/>`_.
* blogofobe works **offline**, with a built-in web server you can work on your site from anywhere.
* blogofobe is **file based**, so you can edit it with your favorite text editor, not some crappy web interface.
* Seamless :ref:`Git Integration <vcs-integration>`. Publish to your blog with a simple ``git push``. This also makes **backups** dirt simple.

.. _MIT License: http://github.com/wxl/blogofobe/LICENSE.txt

.. _install-blogofobe:

Installing blogofobe
====================

Python Versions
---------------

blogofobe is being developed under Python_ 3.2
and tested with Python 2.6, 2.7, and 3.2.

.. _Python: http://www.python.org/


Prerequisites
-------------

Apart from one of the Python versions listed above,
you will also need one of the Python packaging libraries that supports
:mod:`setuptools` style entry points; i.e. distribute_ or setuptools_.

.. _distribute: http://pypi.python.org/pypi/distribute
.. _setuptools: http://pypi.python.org/pypi/setuptools

Using a Python virtualenv_ is strongly recommended to segregate
blogofobe and the packages it depends on from your system Python
installation.
It has the added advantage of taking are of the packaging library issue
for you too.

.. _virtualenv: http://www.virtualenv.org/


Installing the Stable Release
-----------------------------

Download and install blogofobe and the blogofobe_blog plugin with::

  easy_install blogofobe
  easy_install blogofobe_blog

or use your favourite :command:`pip` or :command:`python setup.py` incantation.
The releases are hosted on PyPI and can be downloaded from
http://pypi.python.org/pypi/blogofobe
and http://pypi.python.org/pypi/blogofobe_blog.

If you prefer to use the development repos from Github,
or want to hack on blogofobe and blogofobe_blog,
please see the :ref:`ForDevelopers-section` section.
