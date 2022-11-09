import argparse
import sys
from rich import print
from .script import generate_md_file

def main():
    print("[bold green]Django Mermaid[/ bold green]")

    parser = argparse.ArgumentParser()
    parser.add_argument('Path', metavar='path', type=str, nargs='?', const=1, default=".", help='the path to project')
    args = parser.parse_args()
    if sys.argv[1]:
        project_name = sys.argv[1]
        generate_md_file(project_name)
    

if __name__ == "__main__":
    main()
