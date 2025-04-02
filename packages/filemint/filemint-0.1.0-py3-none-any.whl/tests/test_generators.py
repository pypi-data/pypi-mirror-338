"""Tests for the generators module."""

import os
import tempfile
import unittest
import csv

from filemint.generators import (
    generate_csv,
    generate_txt,
    generate_binary,
    generate_invalid_csv,
    generate_test_files,
)


class TestGenerators(unittest.TestCase):
    """Test the file generator functions."""
    
    def setUp(self):
        """Set up a temporary directory for test files."""
        self.test_dir = tempfile.mkdtemp()
    
    def tearDown(self):
        """Clean up temporary files."""
        # In a real implementation, you might want to remove
        # the temporary directory and its contents here
        pass
    
    def test_generate_csv(self):
        """Test generating a CSV file."""
        filename = "test.csv"
        num_rows = 5
        
        filepath = generate_csv(self.test_dir, filename, num_rows)
        
        # Check file exists
        self.assertTrue(os.path.exists(filepath))
        
        # Check file has correct structure
        with open(filepath, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            rows = list(reader)
            
            # Check header row
            self.assertEqual(rows[0], ['ID', 'Name', 'Value'])
            
            # Check data rows
            self.assertEqual(len(rows), num_rows + 1)  # +1 for header
            
            # Check ID values
            for i, row in enumerate(rows[1:], 1):
                self.assertEqual(int(row[0]), i)
    
    def test_generate_txt(self):
        """Test generating a TXT file."""
        filename = "test.txt"
        num_lines = 5
        
        filepath = generate_txt(self.test_dir, filename, num_lines)
        
        # Check file exists
        self.assertTrue(os.path.exists(filepath))
        
        # Check file has correct number of lines
        with open(filepath, 'r') as txtfile:
            lines = txtfile.readlines()
            self.assertEqual(len(lines), num_lines)
    
    def test_generate_binary(self):
        """Test generating a binary file."""
        filename = "test.bin"
        size_kb = 10
        
        filepath = generate_binary(self.test_dir, filename, size_kb)
        
        # Check file exists
        self.assertTrue(os.path.exists(filepath))
        
        # Check file has correct size
        file_size = os.path.getsize(filepath)
        self.assertEqual(file_size, size_kb * 1024)
    
    def test_generate_invalid_csv(self):
        """Test generating an invalid CSV file."""
        filename = "test_invalid.csv"
        
        filepath = generate_invalid_csv(self.test_dir, filename, num_rows=10)
        
        # Check file exists
        self.assertTrue(os.path.exists(filepath))
        
        # Check file has header row
        with open(filepath, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            first_row = next(reader)
            self.assertEqual(first_row, ['ID', 'Name', 'Value'])
    
    def test_generate_test_files(self):
        """Test generating multiple test files."""
        num_csv = 2
        num_txt = 2
        num_bin = 2
        num_invalid = 2
        
        filepaths = generate_test_files(
            self.test_dir,
            num_csv=num_csv,
            num_txt=num_txt,
            num_binary=num_bin,
            num_invalid=num_invalid,
        )
        
        # Check correct number of files were generated
        expected_count = num_csv + num_txt + num_bin + num_invalid
        self.assertEqual(len(filepaths), expected_count)
        
        # Check all files exist
        for filepath in filepaths:
            self.assertTrue(os.path.exists(filepath))


if __name__ == '__main__':
    unittest.main() 