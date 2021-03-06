Releasing Blogofobe
------

 * Do a platform test via tox:

   ```sh
   $ tox -r
   ```

 * Ensure that the docs build:

   ```sh
   $ cd docs
   $ make clean html
   ```

 * Change version number in:

   * blogofobe:

     * blogofobe/\_\_init\_\_.py
     * docs/conf.py

   * blogofobe_blog:

     * blogofobe_blog/\_\_init\_\_.py

 * Test upload to PyPI:

   ```sh
   $ python setup.py sdist register -r testpypi upload -r testpypi
   ```

 * Test installation in a pristine virtualenv:

   ```sh
   $ virtualenv --python=python3.2 blogofobe-testrel
   $ cd blogofobe-testrel
   $ source bin/activate
   $ pip install --extra-index-url http://testpypi.python.org/pypi \
        "blogofobe==<version>"
   $ pip install --extra-index-url http://testpypi.python.org/pypi \
        "blogofobe_blog==<version>"
   ```

   and then test building a site, even if it's the sample blog via::

   ```sh
   $ blogofobe init test_blog blog
   $ blogofobe build -s test_blog
   ```

 * Release to PyPI:

   ```sh
   $ python setup.py sdist register upload
   ```
