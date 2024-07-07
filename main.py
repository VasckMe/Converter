import json
import xmltodict
import yaml

def save_json(data, filepath):
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)
    print(f'Dane zapisane do pliku: {filepath}')

def save_xml(data, filepath):
    with open(filepath, 'w') as file:
        xml_str = xmltodict.unparse(data, pretty=True)
        file.write(xml_str)
    print(f'Dane zapisane do pliku: {filepath}')

def save_yaml(data, filepath):
    with open(filepath, 'w') as file:
        yaml.dump(data, file)
    print(f'Dane zapisane do pliku: {filepath}')

def save_file(data, filepath):
    if filepath.endswith('.json'):
        save_json(data, filepath)
    elif filepath.endswith('.xml'):
        save_xml(data, filepath)
    elif filepath.endswith('.yaml') or filepath.endswith('.yml'):
        save_yaml(data, filepath)
    else:
        raise ValueError('Nieobsługiwany format pliku.')

def main():
    print("-====    Main function    ====-")

if __name__ == '__main__':
    main()