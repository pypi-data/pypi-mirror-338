import win32com.client
import pandas as pd
import os
from pathlib import Path
from typing import List, Dict, Optional
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class PsdBatchProcessor:
    """Batch processor for updating text layers in PSD files using CSV data."""
    
    def __init__(self):
        self._ps_app = None
        self.encodings = ['utf-8', 'utf-8-sig', 'gbk', 'gb2312']
    
    def _connect_photoshop(self) -> None:
        """Initialize connection to Photoshop application."""
        try:
            self._ps_app = win32com.client.Dispatch("Photoshop.Application")
        except Exception as e:
            raise ConnectionError(f"Failed to connect to Photoshop: {e}")
    
    def _read_csv(self, csv_path: str) -> pd.DataFrame:
        """Read CSV file with multiple encoding attempts."""
        if not os.path.exists(csv_path):
            raise FileNotFoundError(f"CSV file not found: {csv_path}")
            
        for encoding in self.encodings:
            try:
                df = pd.read_csv(csv_path, encoding=encoding)
                logger.info(f"Successfully read CSV with {encoding} encoding")
                return df
            except UnicodeDecodeError:
                continue
                
        raise ValueError("Could not read CSV file with any of the attempted encodings")
    
    def _validate_dataframe(self, df: pd.DataFrame) -> List[str]:
        """Validate DataFrame and return text columns."""
        if 'PhotoshopFile' not in df.columns:
            raise ValueError("CSV must contain 'PhotoshopFile' column")
        
        text_columns = [col for col in df.columns if col != 'PhotoshopFile' 
                       and not col.startswith('Unnamed:')]
        
        if not text_columns:
            raise ValueError("CSV must contain at least one column for text layer updates")
            
        return text_columns
    
    def _update_text_layers(self, doc, text_columns: List[str], row: pd.Series) -> bool:
        """Update text layers in the document."""
        text_layers = {layer.Name: layer for layer in doc.ArtLayers 
                      if layer.Kind == 2}  # 2 = text layer
        
        updates_made = False
        for column in text_columns:
            if column in text_layers:
                value = str(row[column])
                text_layers[column].TextItem.Contents = value
                updates_made = True
                logger.info(f"Updated layer '{column}' with value: {value}")
        
        return updates_made
    
    def process_file(self, psd_path: str, text_updates: Dict[str, str]) -> bool:
        """Process a single PSD file."""
        if not os.path.exists(psd_path):
            logger.error(f"File not found: {psd_path}")
            return False
            
        if not self._ps_app:
            self._connect_photoshop()
            
        try:
            doc = self._ps_app.Open(psd_path)
            text_layers = {layer.Name: layer for layer in doc.ArtLayers 
                         if layer.Kind == 2}
            
            updates_made = False
            for layer_name, new_text in text_updates.items():
                if layer_name in text_layers:
                    text_layers[layer_name].TextItem.Contents = str(new_text)
                    updates_made = True
            
            if updates_made:
                doc.Save()
                logger.info(f"Successfully saved {psd_path}")
            
            doc.Close()
            return updates_made
            
        except Exception as e:
            logger.error(f"Error processing {psd_path}: {e}")
            try:
                doc.Close()
            except:
                pass
            return False
    
    def process_csv(self, csv_path: str) -> Dict[str, bool]:
        """Process all PSD files specified in the CSV."""
        try:
            df = self._read_csv(csv_path)
            text_columns = self._validate_dataframe(df)
            
            if not self._ps_app:
                self._connect_photoshop()
            
            results = {}
            for index, row in df.iterrows():
                psd_path = str(row['PhotoshopFile']) + ".psd"
                psd_path = psd_path.replace('/', '\\')
                
                updates = {col: row[col] for col in text_columns}
                success = self.process_file(psd_path, updates)
                results[psd_path] = success
                
            return results
            
        except Exception as e:
            logger.error(f"Error processing CSV: {e}")
            raise
