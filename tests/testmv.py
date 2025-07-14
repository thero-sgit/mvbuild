import unittest
from unittest.mock import patch, MagicMock
import sys

from mvbuild.src.main import *

class TestParseArgs(unittest.TestCase):
    @patch.object(sys, 'argv', ['mv', 'build', '--id', 'com.example', '--n', 'my-app', '--i', 'false'])
    def test_parse_args_valid(self):
        args = parse_args()
        #
        self.assertEqual(args.command, 'build')
        self.assertEqual(args.id, 'com.example')
        self.assertEqual(args.n, 'my-app')
        self.assertIn(args.i, ['f', 'false'])

    
    @patch.object(sys, 'argv', ['mv', 'build', '--id', 'com.example', '--n', 'my-app', '--i', 'true'])
    def test_parse_args_valid_2(self):
        args = parse_args()
        #
        self.assertEqual(args.command, 'build')
        self.assertEqual(args.id, 'com.example')
        self.assertEqual(args.n, 'my-app')
        self.assertIn(args.i, ['t', 'true'])


    @patch.object(sys, 'argv', ['mv', 'build', '--id', 'com.example', '--n', 'my-app'])
    def test_parse_args_defaults(self):
        args = parse_args()
        #
        self.assertIn(args.i, ['f', 'false'])


if __name__ == '__main__':
    unittest.main()