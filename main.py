import argparse
import json
import xmltodict
import yaml

# Parsing
def parse_arguments():
    parser = argparse.ArgumentParser(description='Date Processing')
    parser.add_argument('input', type=str, help='Input filepath')
    parser.add_argument('output', type=str, help='Output filepath')
    args = parser.parse_args()
    return args

# Loads

# Load type handler
def load_file(filepath):
    if filepath.endswith('.json'):
        return load_json(filepath)
    elif filepath.endswith('.xml'):
        return load_xml(filepath)
    elif filepath.endswith('.yaml') or filepath.endswith('.yml'):
        return load_yaml(filepath)
    else:
        raise ValueError('Nieobsługiwany format pliku.')

# json
def load_json(filepath):
    with open(filepath, 'r') as file:
        data = json.load(file)
    return data

# xml
def load_xml(filepath):
    with open(filepath, 'r') as file:
        data = xmltodict.parse(file.read())
    return data

# yaml
def load_yaml(filepath):
    with open(filepath, 'r') as file:
        data = yaml.safe_load(file)
    return data

def main():
    print("-====    Main function    ====-")

if __name__ == '__main__':
    main()
