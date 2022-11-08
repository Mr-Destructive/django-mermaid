import argparse
from rich import print
from .script import generate_md_file

def main():
    print("[bold green]Django Mermaid[/ bold green]")

    parser = argparse.ArgumentParser()
    parser.add_argument('Path', metavar='path', type=str, nargs='?', const=1, default=".", help='the path to project')
    args = parser.parse_args()
    generate_md_file()
    

if __name__ == "__main__":
    main()
