from ofxparse import OfxParser
import csv

def convert_ofx_to_csv(ofx_file_path, csv_file_path):
    # Parse OFX file
    with open(ofx_file_path, 'rb') as ofx_file:
        ofx = OfxParser.parse(ofx_file)

    # Write data to CSV file
    with open(csv_file_path, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)

        # Extract header from OFX file dynamically
        header = get_dynamic_header(ofx)
        writer.writerow(header)

        # Write transaction data
        for transaction in ofx.account.statement.transactions:
            # Create a row based on the dynamic header
            row = [getattr(transaction, field, '') for field in header]
            writer.writerow(row)

def get_dynamic_header(ofx):
    # Extract unique fields from transactions dynamically
    header = set()
    for transaction in ofx.account.statement.transactions:
        header.update(vars(transaction).keys())
    
    # Convert the set to a list (maintaining order if needed)
    header = list(header)
    
    # Sort the header list for consistency
    header.sort()
    
    return header


if __name__ == "__main__":

    ofx_file_path = "./input.ofx";
    csv_file_path = "./output.csv";
    convert_ofx_to_csv(ofx_file_path, csv_file_path)


