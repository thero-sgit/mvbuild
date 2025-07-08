import subprocess
from argparse import ArgumentParser

def main():
    parser = ArgumentParser()
    sub_parsers = parser.add_subparsers(dest='command', required=True)

    build_parser = sub_parsers.add_parser('build')
    build_parser.add_argument('--id', help='Group ID')
    build_parser.add_argument('--n', help='Project Name.')
    build_parser.add_argument('--i', help='Interactive mode (true/false).', required=False)

    args = parser.parse_args()

    if args.command == 'build':
        if hasattr(args, 'i'):
            i = (args.i).lower().strip() if (args.i).lower().strip() == 'true' else 'false'
            build_project(args.id, args.n, i)
        #
        else:
            build_project(args.id, args.n)



def build_project(group_id: str, artifact_id: str, interactive: str = 'false'):
    

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
