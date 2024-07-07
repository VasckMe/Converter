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
        raise ValueError('Load Error: The format is out of the service')

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

# Saves

# Save type handler
def save_file(data, filepath):
    if filepath.endswith('.json'):
        save_json(data, filepath)
    elif filepath.endswith('.xml'):
        save_xml(data, filepath)
    elif filepath.endswith('.yaml') or filepath.endswith('.yml'):
        save_yaml(data, filepath)
    else:
        raise ValueError('Save Error: The format is out of the service')

# json
def save_json(data, filepath):
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)
    print(f'Data saved to file: {filepath}')

# xml
def save_xml(data, filepath):
    with open(filepath, 'w') as file:
        xml_str = xmltodict.unparse(data, pretty=True)
        file.write(xml_str)
    print(f'Data saved to file: {filepath}')

# yml
def save_yaml(data, filepath):
    with open(filepath, 'w') as file:
        yaml.dump(data, file)
    print(f'Data saved to file: {filepath}')

# Main

def main():
    args = parse_arguments()
    try:
        data = load_file(args.input)
        save_file(data, args.output)
    except Exception as e:
        print(f'Oops, error: {e}')

if __name__ == '__main__':
    main()
