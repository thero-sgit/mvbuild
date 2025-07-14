import subprocess
from argparse import ArgumentParser, Namespace

def main():
    args = parse_args()

    if args.command == 'build':
        build_project(group_id=args.id, artifact_id=args.n, interactive=args.i)


def parse_args() -> Namespace:
    parser = ArgumentParser(description="Tool to generate a Maven Project.")
    sub_parsers = parser.add_subparsers(dest='command', required=True)

    build_parser = sub_parsers.add_parser('build', help="Generate a Maven Project.")
    build_parser.add_argument('--id', help='Group ID (e.g., com.example)')
    build_parser.add_argument('--n', help='Project Name / Artifact ID')
    build_parser.add_argument('--i', choices=['true', 'false', 't', 'f'], default='false', help='Interactive mode: true/false (default: false)')

    return parser.parse_args()

        

def build_project(group_id: str, artifact_id: str, interactive: str):
    interactive = 'false' if interactive.lower() in ['f', 'false'] else 'true'

    command = [
        "mvn", "archetype:generate",
        f"-DgroupId={group_id}",
        f"-DartifactId={artifact_id}",
        f"-DarchetypeArtifactId=maven-archetype-quickstart",
        f"-DinteractiveMode={interactive}"
    ]

    print(f"Running Maven Command: \n{' '.join(command)}")

    try:
        subprocess.run(command, check=True)
        print(f"✅ Maven project '{artifact_id}' created successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")
    except FileNotFoundError:
        print("Maven (mvn) not found. Make sure it's installed and in your PATH")
    except Exception as e:
        print(f"Unexpected error: {e}")