import re

def extract_fields(text_lines):
    records = []
    record = {}
    for line in text_lines:
        if "Application No." in line:
            if record:
                records.append(record)
                record = {}
            match = re.search(r'Application No.\D*(\d+)', line)
            if match:
                record["application_number"] = match.group(1)

        elif "Proprietor" in line:
            record["proprietor_name"] = line.split(":")[-1].strip()

        elif "Address" in line:
            record["proprietor_address"] = line.split(":")[-1].strip()

        elif "Mark Description" in line:
            record["mark_description"] = line.split(":")[-1].strip()

    if record:
        records.append(record)

    return records