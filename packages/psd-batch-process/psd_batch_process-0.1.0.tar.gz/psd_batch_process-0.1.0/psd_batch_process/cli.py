import argparse
import sys
from .processor import PsdBatchProcessor
import logging

def main():
    parser = argparse.ArgumentParser(description='Batch update text layers in PSD files using CSV data.')
    parser.add_argument('csv_path', help='Path to the CSV file containing the text updates')
    parser.add_argument('--verbose', '-v', action='store_true', help='Enable verbose logging')
    
    args = parser.parse_args()
    
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)
    
    try:
        processor = PsdBatchProcessor()
        results = processor.process_csv(args.csv_path)
        
        success_count = sum(1 for success in results.values() if success)
        print(f"\nProcessing complete: {success_count}/{len(results)} files updated successfully")
        
        if success_count < len(results):
            sys.exit(1)
            
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()
