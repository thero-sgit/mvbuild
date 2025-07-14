import unittest
from unittest.mock import patch, MagicMock
import sys

from mvbuild.src.main import *

class TestParseArgs(unittest.TestCase):
    @patch.object(sys, 'argv', ['mv', 'build', '--id', 'com.example', '--n', 'my-app', '--f', 'false'])
    def test_parse_args_valid(self):
        args = parse_args()
        #
        self.assertEqual(args.command, 'build')
        self.assertEqual(args.id, 'com.example')
        self.assertEqual(args.n, 'mu-app')
        self.assertIn(args.i, ['f', 'false'])