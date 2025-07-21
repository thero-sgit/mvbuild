import subprocess
from argparse import ArgumentParser, Namespace
from pathlib import Path

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

        # write to pom
        write_to_pom(group_id, artifact_id)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")
    except FileNotFoundError:
        print("Maven (mvn) not found. Make sure it's installed and in your PATH")
    except Exception as e:
        print(f"Unexpected error: {e}")


def write_to_pom(group_id: str, artifact_id: str):
    pom_cotent = f'''<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0
                             http://maven.apache.org/xsd/maven-4.0.0.xsd">
  <modelVersion>4.0.0</modelVersion>

  <groupId>{group_id}</groupId>
  <artifactId>{artifact_id}</artifactId>
  <version>1.0.0</version>
  <packaging>jar</packaging>

  <name>{artifact_id}</name>

  <properties>
    <maven.compiler.source>21</maven.compiler.source>
    <maven.compiler.target>21</maven.compiler.target>
    <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
  </properties>

  <dependencies>
    <!-- JUnit 5 for testing -->
    <dependency>
      <groupId>org.junit.jupiter</groupId>
      <artifactId>junit-jupiter</artifactId>
      <version>5.10.1</version>
      <scope>test</scope>
    </dependency>
  </dependencies>

  <build>
    <plugins>
      <!-- Maven Compiler Plugin -->
      <plugin>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-compiler-plugin</artifactId>
        <version>3.11.0</version>
        <configuration>
          <release>21</release>
        </configuration>
      </plugin>

      <!-- Maven Surefire Plugin for running tests -->
      <plugin>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-surefire-plugin</artifactId>
        <version>3.2.5</version>
      </plugin>
    </plugins>
  </build>
</project>
'''
    #
    pom_path = f'{Path.cwd()}/{artifact_id}/pom.xml'

    try:
        print('\nPreparing pom.xml:\n   Writing to pom.xml...')
        with open(pom_path, "w", encoding='utf-8') as pom_file:
            pom_file.write(pom_cotent)

        print(' Done!')
    except:
        print('Something went wrong!')