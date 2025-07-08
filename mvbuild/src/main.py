import subprocess
from argparse import ArgumentParser

def main():
    parser = ArgumentParser()
    sub_parsers = parser.add_subparsers(dest='command', required=True)

    build_parser = sub_parsers.add_parser('build')
    build_parser.add_argument('--id', help='Group ID')
    build_parser.add_argument('--n', help='Project Name.')
    build_parser.add_argument('--i', help='Interactive mode (true/false).')

    args = parser.parse_args()

    if args.command == 'build':
        try:
            assert args.i.lower().strip() in ['t', 'f', 'true', 'false']
            #
            build_project(args.id, args.n, args.i)
        #
        except Exception as e:
            raise e
        




def build_project(group_id: str, artifact_id: str, interactive: str):
    interactive = 'false' if interactive in ['f', 'false'] else 'true'

    command = [
        "mvn", "archetype:generate",
        f"-DgroupId={group_id}",
        f"-DartifactId={artifact_id}",
        f"-DarchetypeArtifactId=maven-archetype-quickstart",
        f"-DinteractiveMode={interactive}"
    ]

    try:
        subprocess.run(command, check=True)
        print(f"✅ Maven project '{artifact_id}' created successfully.")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error occurred: {e}")
