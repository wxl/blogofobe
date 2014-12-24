# -*- coding: utf-8 -*-
"""Integration tests for blogofobe.
"""
import os
import shutil
from tempfile import mkdtemp
try:
    import unittest2 as unittest        # For Python 2.6
except ImportError:
    import unittest                     # flake8 ignore # NOQA
from ... import main


class TestblogofobeCommands(unittest.TestCase):
    """Intrgration tests for the blogofobe commands.
    """
    def _call_entry_point(self, *args):
        main.main(*args)

    def test_blogofobe_init_bare_site(self):
        """`blogofobe init src` initializes bare site w/ _config.py file
        """
        src_dir = mkdtemp()
        self.addCleanup(shutil.rmtree, src_dir)
        os.rmdir(src_dir)
        self._call_entry_point(['blogofobe', 'init', src_dir])
        self.assertEqual(os.listdir(src_dir), ['_config.py'])

    def test_blogofobe_build_bare_site(self):
        """`blogofobe build` on bare site creates _site directory
        """
        self.addCleanup(os.chdir, os.getcwd())
        src_dir = mkdtemp()
        self.addCleanup(shutil.rmtree, src_dir)
        os.rmdir(src_dir)
        self._call_entry_point(['blogofobe', 'init', src_dir])
        self._call_entry_point(['blogofobe', 'build', '-s', src_dir])
        self.assertIn('_site', os.listdir(src_dir))
