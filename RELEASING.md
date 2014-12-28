Releasing Blogofobe
------

* Do a platform test via tox:

   $ tox -r

* Ensure that the docs build:

   $ cd docs
   $ make clean html

* Change version number in:

  * Blogofobe:

    * blogofobe/__init__.py
    * docs/conf.py

  * blogofobe_blog:

    * blogofobe_blog/__init__.py

  * blogofobe.com:

    * _config.py

* Test upload to PyPI:

   $ python setup.py sdist register -r testpypi upload -r testpypi

* Test installation in a pristine virtualenv:

   $ virtualenv --python=python3.2 blogooble-testrel
   $ cd blogofobe-testrel
   $ source bin/activate
   $ pip install --extra-index-url http://testpypi.python.org/pypi \
          "Blogofobe==<version>"
   $ pip install --extra-index-url http://testpypi.python.org/pypi \
          "blogofobe_blog==<version>"

  and then test building a site, even if it's the sample blog via::

   $ blogofobe init test_blog blog
   $ blogofobe build -s test_blog

* Release to PyPI:

   $ python setup.py sdist register upload
