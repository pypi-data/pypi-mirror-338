#!/usr/bin/env python3
"""
Unit tests for BM25 search functionality in discord_mcp_server.py.
"""

import unittest
import os
import tempfile
import shutil
import json
from datetime import datetime, timezone
from pathlib import Path

# Try to import the required modules, skip tests if not available
try:
    import sys
    sys.path.insert(0, os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
    import bm25s
    import numpy as np
    from discord_mcp_server import DiscordMessageDB, format_search_results
    BM25_SEARCH_AVAILABLE = True
except ImportError:
    BM25_SEARCH_AVAILABLE = False

@unittest.skipIf(not BM25_SEARCH_AVAILABLE, "BM25 search module not available")
class TestBM25Search(unittest.TestCase):
    """Test the BM25 search functionality in discord_mcp_server.py."""
    
    def setUp(self):
        """Set up test environment."""
        # Create temporary directories for testing
        self.temp_dir = tempfile.mkdtemp()
        self.data_dir = os.path.join(self.temp_dir, "discord_data")
        os.makedirs(self.data_dir, exist_ok=True)
        
        # Create a test exports directory
        exports_dir = os.path.join(self.data_dir, "exports")
        os.makedirs(exports_dir, exist_ok=True)
        
        # Create a test export file
        export_data = {
            "guild": {
                "id": "67890",
                "name": "Test Server"
            },
            "channel": {
                "id": "12345",
                "name": "test-channel",
                "type": "text"
            },
            "messages": [
                {
                    "id": "1",
                    "content": "Hello world",
                    "timestamp": "2023-01-01T12:00:00Z",
                    "author": {
                        "id": "user1",
                        "username": "User One"
                    }
                },
                {
                    "id": "2",
                    "content": "This is a test message about AI and machine learning",
                    "timestamp": "2023-01-02T12:00:00Z",
                    "author": {
                        "id": "user2",
                        "username": "User Two"
                    }
                },
                {
                    "id": "3",
                    "content": "Keyword search is useful for finding relevant messages",
                    "timestamp": "2023-01-03T12:00:00Z",
                    "author": {
                        "id": "user1",
                        "username": "User One"
                    }
                }
            ]
        }
        
        with open(os.path.join(exports_dir, "test-channel.json"), "w") as f:
            json.dump(export_data, f)
        
        # Initialize message database
        self.message_db = DiscordMessageDB(self.data_dir)
    
    def tearDown(self):
        """Clean up test environment."""
        shutil.rmtree(self.temp_dir)
    
    def test_load_data(self):
        """Test loading of exported message data."""
        # Data should already be loaded in setUp
        self.assertEqual(len(self.message_db.channels), 1)
        self.assertEqual(len(self.message_db.messages.get("12345", {})), 3)
        self.assertEqual(len(self.message_db.users), 2)
    
    def test_search_messages_keyword(self):
        """Test basic keyword searching."""
        # Search for a keyword
        results = self.message_db.search_messages(query="machine")
        
        # Should find the second message
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["id"], "2")
    
    def test_search_messages_user_filter(self):
        """Test filtering by user."""
        # Search with user filter
        results = self.message_db.search_messages(user="User One")
        
        # Should find the first and third messages
        self.assertEqual(len(results), 2)
        self.assertIn(results[0]["id"], ["1", "3"])
        self.assertIn(results[1]["id"], ["1", "3"])
    
    def test_search_messages_date_filter(self):
        """Test filtering by date."""
        # Create a specific date for filtering
        start_date = datetime.fromisoformat("2023-01-02T00:00:00+00:00")
        
        # Search with date filter
        results = self.message_db.search_messages(start_date=start_date)
        
        # Should find the second and third messages
        self.assertEqual(len(results), 2)
        self.assertIn(results[0]["id"], ["2", "3"])
        self.assertIn(results[1]["id"], ["2", "3"])
    
    def test_format_message(self):
        """Test message formatting."""
        # Get a message to format
        message = next(iter(self.message_db.messages.get("12345", {}).values()))
        
        # Format it
        formatted = self.message_db.format_message(message)
        
        # Check that formatting contains expected elements
        self.assertIn(message["author"]["username"], formatted)
        self.assertIn(message["content"], formatted)
        self.assertIn(message["channel_name"], formatted)
    
    def test_format_search_results(self):
        """Test formatting search results."""
        # Create a sample result with relevance scores
        results = [
            {
                "id": "1",
                "content": "Test message",
                "timestamp": "2023-01-01T12:00:00Z",
                "author": {
                    "username": "TestUser"
                },
                "channel": "test-channel",
                "channel_id": "12345",
                "relevance": 0.85
            }
        ]
        
        # Format the results
        formatted = format_search_results(results)
        
        # Check that the formatting contains expected elements
        self.assertIn("TestUser", formatted)
        self.assertIn("Test message", formatted)
        self.assertIn("test-channel", formatted)
        self.assertIn("Relevance: 0.85", formatted)
    
    def test_bm25_tokenization(self):
        """Test basic BM25 tokenization."""
        # Test the tokenization function from bm25s
        contents = ["This is a test", "Another test message"]
        tokens = bm25s.tokenize(contents)
        
        # Check basic properties
        self.assertEqual(len(tokens), 2)
        self.assertIn("test", tokens[0])
        self.assertIn("test", tokens[1])

if __name__ == "__main__":
    unittest.main()