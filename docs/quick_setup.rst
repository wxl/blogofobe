A Quick Tutorial
****************

.. note::
   This documents blogofobe's current stable release.

Ok, if you're impatient, this is the short *short* [#f1]_ version of
getting setup with blogofobe.

* Install blogofobe and the blogofobe_blog plugin,
  (see :ref:`install-blogofobe`).
  Use a Python virtualenv_ or :command:`sudo` as you wish.

  ::

    git clone git://github.com/wxl/blogofobe.git
    git clone git://github.com/wxl/blogofobe_blog.git
    cd blogofobe
    python setup.py install
    cd ../blogofobe_blog
    python setup.py install

  .. _virtualenv: http://www.virtualenv.org/

* Initialize a blog site in a directory call :file:`mysite`::

    blogofobe init mysite blog

* Build the site::

    blogofobe build -s mysite

* Serve the site::

    blogofobe serve -s mysite

* Open your web browser to http://localhost:8080 to see the rendered site.

* Explore the :command:`blogofobe` commands with :command:`blogofobe help`.

* Create some post files in the :file:`_posts` directory (see :ref:`posts`)

The next chapters explain this process in more detail.

.. rubric:: Footnotes

.. [#f1] * **Priest**: Do you?

 * **Vespa**: Yes.

 * **Priest**: Do *you*?

 * **Lone Star**: I do.

 * **Priest**: Good! Fine! You're married! Kiss Her!

.. _git: http://www.git-scm.org
