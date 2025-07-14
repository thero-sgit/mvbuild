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



class TestBuildProject(unittest.TestCase):
    @patch('subprocess.run', return_value = MagicMock(returncode = 0))
    def test_build_project_success(self, mock_run):
        build_project('com.example', 'my-app', 'false')
        #
        mock_run.assert_called_once()
        args = mock_run.call_args[0][0]

        self.assertIn('-DgroupId=com.example', args)
        self.assertIn('-DartifactId=my-app', args)
        self.assertIn('-DinteractiveMode=false', args)
    


if __name__ == '__main__':
    unittest.main()