#!/usr/bin/env python3
"""
Unit tests for the discord_exporter module.
"""

import unittest
import os
import tempfile
import shutil
from pathlib import Path

# Try to import the discord_exporter module, skip tests if not available
try:
    import sys
    sys.path.insert(0, os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
    from discord_exporter import DiscordExporter
    DISCORD_EXPORTER_AVAILABLE = True
except ImportError:
    DISCORD_EXPORTER_AVAILABLE = False

@unittest.skipIf(not DISCORD_EXPORTER_AVAILABLE, "Discord exporter module not available")
class TestDiscordExporter(unittest.TestCase):
    """Test the DiscordExporter class."""
    
    def setUp(self):
        """Set up test environment."""
        # Create temporary directory for testing
        self.temp_dir = tempfile.mkdtemp()
        self.output_dir = os.path.join(self.temp_dir, "exports")
        os.makedirs(self.output_dir, exist_ok=True)
        
        # Initialize exporter without token for testing
        self.exporter = DiscordExporter(output_dir=self.output_dir)
    
    def tearDown(self):
        """Clean up test environment."""
        shutil.rmtree(self.temp_dir)
    
    def test_init(self):
        """Test initializing the exporter."""
        self.assertEqual(self.exporter.output_dir, Path(self.output_dir))
        self.assertIsNone(self.exporter.token)
    
    def test_check_dotnet(self):
        """Test checking for .NET runtime."""
        # This just tests that the method runs without error
        # The actual result depends on whether .NET is installed
        result = self.exporter.check_dotnet()
        # Result should be a boolean
        self.assertIsInstance(result, bool)
    
    def test_download_dce(self):
        """Test the download_dce method."""
        # Skip actual download in tests
        self.exporter.dce_dir.mkdir(parents=True, exist_ok=True)
        self.exporter.dce_cli_path = self.exporter.dce_dir / "DiscordChatExporter.Cli.dll"
        # Create a dummy file
        with open(self.exporter.dce_cli_path, 'w') as f:
            f.write("dummy")
        
        # Check if download is skipped when file exists
        result = self.exporter.download_dce()
        self.assertTrue(result)
        self.assertTrue(self.exporter.dce_cli_path.exists())
    
    def test_get_token_instructions(self):
        """Test getting token instructions."""
        instructions = self.exporter.get_token_instructions()
        self.assertIsInstance(instructions, str)
        self.assertIn("Discord token", instructions)

if __name__ == "__main__":
    unittest.main()