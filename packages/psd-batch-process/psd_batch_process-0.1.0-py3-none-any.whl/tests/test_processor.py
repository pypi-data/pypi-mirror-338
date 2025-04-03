import unittest
from unittest.mock import MagicMock, patch, PropertyMock
import pandas as pd
from psd_batch_process.processor import PsdBatchProcessor
import os
import tempfile

class TestPsdBatchProcessor(unittest.TestCase):
    def setUp(self):
        self.processor = PsdBatchProcessor()
        
    def test_validate_dataframe(self):
        # Test valid DataFrame
        df = pd.DataFrame({
            'PhotoshopFile': ['file1', 'file2'],
            'Name': ['name1', 'name2'],
            'Cost': [1, 2]
        })
        text_columns = self.processor._validate_dataframe(df)
        self.assertEqual(set(text_columns), {'Name', 'Cost'})
        
        # Test DataFrame without PhotoshopFile column
        df_invalid = pd.DataFrame({
            'Name': ['name1', 'name2'],
            'Cost': [1, 2]
        })
        with self.assertRaises(ValueError):
            self.processor._validate_dataframe(df_invalid)
            
        # Test DataFrame with only PhotoshopFile column
        df_no_text = pd.DataFrame({
            'PhotoshopFile': ['file1', 'file2']
        })
        with self.assertRaises(ValueError):
            self.processor._validate_dataframe(df_no_text)
    
    @patch('win32com.client.Dispatch')
    def test_process_file(self, mock_dispatch):
        # Mock Photoshop application and document
        mock_doc = MagicMock()
        mock_layer = MagicMock()
        mock_layer.Name = 'TestLayer'
        mock_layer.Kind = 2  # Text layer
        
        # Create a mock TextItem
        mock_text_item = MagicMock()
        mock_layer.TextItem = mock_text_item
        
        mock_doc.ArtLayers = [mock_layer]
        
        mock_app = MagicMock()
        mock_app.Open.return_value = mock_doc
        mock_dispatch.return_value = mock_app
        
        # Create a temporary test file
        with tempfile.NamedTemporaryFile(suffix='.psd', delete=False) as tmp:
            tmp.write(b'dummy content')
            test_file = tmp.name
            
        try:
            # Test successful update
            updates = {'TestLayer': 'New Text'}
            result = self.processor.process_file(test_file, updates)
            self.assertTrue(result)
            
            # Verify the Contents was set
            self.assertEqual(mock_text_item.Contents, 'New Text')
            
            # Test non-existent layer
            updates = {'NonExistentLayer': 'New Text'}
            result = self.processor.process_file(test_file, updates)
            self.assertFalse(result)
            
        finally:
            # Clean up
            if os.path.exists(test_file):
                os.remove(test_file)
    
    def test_read_csv_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            self.processor._read_csv('nonexistent.csv')
    
    @patch('pandas.read_csv')
    def test_read_csv_encoding(self, mock_read_csv):
        # Create a temporary CSV file
        with tempfile.NamedTemporaryFile(suffix='.csv', delete=False) as tmp:
            tmp.write(b'dummy content')
            test_file = tmp.name
            
        try:
            # Mock successful read with second encoding
            def mock_read(path, encoding):
                if encoding == 'utf-8':
                    raise UnicodeDecodeError('utf-8', b'', 0, 1, 'invalid')
                return pd.DataFrame()
                
            mock_read_csv.side_effect = mock_read
            
            # Should succeed with second encoding
            result = self.processor._read_csv(test_file)
            self.assertIsInstance(result, pd.DataFrame)
            
            # Test all encodings fail
            mock_read_csv.side_effect = UnicodeDecodeError('utf-8', b'', 0, 1, 'invalid')
            with self.assertRaises(ValueError):
                self.processor._read_csv(test_file)
                
        finally:
            # Clean up
            if os.path.exists(test_file):
                os.remove(test_file)

if __name__ == '__main__':
    unittest.main()
