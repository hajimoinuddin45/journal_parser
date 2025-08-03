def test_sample_field_extraction():
    sample_lines = ["Application No.: 123456", "Proprietor: XYZ Pvt Ltd"]
    results = extract_fields(sample_lines)
    assert results[0]['application_number'] == '123456'