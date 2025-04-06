import re

def parse_address(address):
    # Very basic parsing for demo — you can expand later!
    pattern = r'(?P<building_number>\d+[A-Z]?)\s(?P<street>[\w\s]+),\s(?P<city>[\w\s]+),?\s?(?P<postcode>[A-Z]{1,2}\d{1,2}[A-Z]?\s?\d[A-Z]{2})'
    match = re.search(pattern, address)
    if match:
        return {
            "building_number": match.group("building_number"),
            "street": match.group("street"),
            "city": match.group("city"),
            "postcode": match.group("postcode"),
            "country": "United Kingdom"
        }
    return {}
