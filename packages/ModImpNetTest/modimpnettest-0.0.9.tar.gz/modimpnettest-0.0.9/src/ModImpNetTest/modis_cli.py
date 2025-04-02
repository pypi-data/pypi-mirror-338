import argparse
import sys

# from ModImpNetTest.modis_download_all import download_modis

def main():
    # Create the parser
    parser = argparse.ArgumentParser()
    # Add an argument
    # it will be stored as dest='f'
    parser.add_argument("-f", "--configfile",
                        default=None, type=str, required=True, dest='f',
                        help="Path to ModImpNet TOML configuration file.")

    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    else:
        args = parser.parse_args()
        # download_modis(args.f)
        print(f'Hello: {args.f}')
