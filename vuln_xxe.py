import xml.etree.ElementTree as ET

def parse_xml_config(xml_data):
    """
    VULNERABLE: XML External Entity (XXE) - CWE-611
    Attacker can read files or cause DoS
    """
    # Using unsafe XML parser - vulnerable to XXE!
    parser = ET.XMLParser()
    tree = ET.fromstring(xml_data, parser=parser)
    
    return tree.find('config').text
