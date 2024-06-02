import pandas as pd
from canaddress import AddressParser

# Sample data
data = {
        'Property_Address': [
            '1801  3077 WESTON ROAD, TORONTO, ONTARIO M9M3A1',
            '711  4673 JANE STREET, TORONTO, ONTARIO M3N2L1',
            '105  55 NEPTUNE DRIVE, TORONTO, ONTARIO M6A1X2',
            '104  5949 YONGE STREET, TORONTO, ONTARIO M2M3V8'
        ]
    }
df = pd.DataFrame(data)

# Initialize the AddressParser
parser = AddressParser(df, 'Property_Address')

# Clean and process the data
parser.clean_and_process_data()

# Display the cleaned and processed data
print(parser.display_data())
