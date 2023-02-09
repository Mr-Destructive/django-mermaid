import argparse
import sys
from rich import print
from .script import generate_md_file, generate_model_file
from .script import gnerate_model_file

def main():
    print("[bold green]Django Mermaid[/ bold green]")

    parser = argparse.ArgumentParser()
    parser.add_argument('Path', metavar='path', type=str, nargs='?', const=1, default=".", help='the path to project')
    args = parser.parse_args()
    if sys.argv[1]:
        project_name = sys.argv[1]
        generate_md_file(project_name)
    
def generate_model():
    print("[bold green]Django Mermaid[/ bold green]")

    parser = argparse.ArgumentParser()
    parser.add_argument('Path', metavar='path', type=str, nargs='?', const=1, default=".", help='the path to project')
    parser.add_argument('Path', metavar='mermaid_file', type=str, nargs='?', const=1, default=".", help='the path to mermaid file')
    args = parser.parse_args()
    if sys.argv[1]:
        project_name = sys.argv[1]
        mermaid_diagram = sys.argv[2]
        generate_model_file(project_name, mermaid_diagram)

