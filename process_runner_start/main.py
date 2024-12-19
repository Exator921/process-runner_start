import sys
import os
import subprocess


def detect_project_type():
    """Detects the project type based on common files."""
    patterns = {
        'node': ['package.json'],
        'java': ['pom.xml', '*.java'],
        'ruby': ['Gemfile'],
        'go': ['go.mod'],
        'elixir': ['mix.exs'],
        'python': ['requirements.txt'],
    }
    for project_type, files in patterns.items():
        for file in files:
            if '*' in file:  # Handle wildcard patterns
                if any(f.endswith(file.lstrip('*')) for f in os.listdir()):
                    return project_type
            elif os.path.exists(file):
                return project_type
    return None


def start_project(project_type):
    """Runs the start command for the given project type."""
    commands = {
        'node': ['npm', 'run', 'start'],
        'java': ['mvn', 'compile', 'exec:java'],
        'ruby': ['bundle', 'exec', 'ruby', 'main.rb'],
        'go': ['go', 'run', '.'],
        'elixir': ['mix', 'run'],
        'python': ['python', 'main.py'],
    }
    command = commands.get(project_type)
    if not command:
        print(f"Unknown or unsupported project type: {project_type}")
        return

    try:
        print(f"Running {project_type} project...")
        subprocess.run(command, check=True)
    except FileNotFoundError as e:
        print(f"Error: Required tool not found for {project_type}. Make sure it's installed and in your PATH.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to start {project_type} project: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


def main():
    if len(sys.argv) <= 1 or sys.argv[1].lower() != "start":
        print("Usage: process-runner_start start")
        return

    project_type = detect_project_type()
    if project_type:
        print(f"Detected {project_type} project.")
        start_project(project_type)
    else:
        print("Could not detect project type. Ensure you're in the project root directory or have files corresponding to a project type. (ex: package.json for Node.js projects)")


if __name__ == '__main__':
    main()
