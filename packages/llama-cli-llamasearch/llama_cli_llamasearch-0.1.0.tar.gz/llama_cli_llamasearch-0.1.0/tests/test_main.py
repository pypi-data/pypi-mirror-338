"""
Tests for the llama-cli main module
"""
import os
import sys
import unittest
from unittest.mock import patch

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.llama_cli import __version__
from src.llama_cli.main import app


class TestLlamaCli(unittest.TestCase):
    """Test cases for the Llama CLI main functionality"""

    def test_version(self):
        """Test that version is correctly defined"""
        self.assertIsNotNone(__version__)
        self.assertTrue(isinstance(__version__, str))
    
    @patch('typer.Typer.command')
    def test_main_app(self, mock_command):
        """Test that the main app is correctly initialized"""
        self.assertIsNotNone(app)
        self.assertEqual(app.info.name, "llama")
        self.assertTrue("Command-line interface for LlamaSearch.ai tools" in app.info.help)


if __name__ == '__main__':
    unittest.main() 