
# CanAddress

CanAddress is a Python library for cleaning and parsing addresses. It standardizes addresses by converting them to a consistent format and splitting them into components such as street number, street name, city, province/state, and postal code.

## Features

- Clean and standardize addresses
- Split addresses into components
- Easily integrate with pandas DataFrames

## Installation

You can install CanAddress using pip:

```bash
pip install canaddress
```

## Usage

Here's a basic example of how to use CanAddress:

```python
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
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Author

- Avneesh Chaudhary
- Email: hey@avneeshchaudhary.com
