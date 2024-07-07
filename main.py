import argparse

# Parsing
def parse_arguments():
    parser = argparse.ArgumentParser(description='Date Processing')
    parser.add_argument('input', type=str, help='Input filepath')
    parser.add_argument('output', type=str, help='Output filepath')
    args = parser.parse_args()
    return args


def main():
    print("-====    Main function    ====-")

if __name__ == '__main__':
    main()