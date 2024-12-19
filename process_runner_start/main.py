import sys
import os
import subprocess

def main():
    import sys
    args = sys.argv[1:]

    if len(args) == 0:
        print("Usage: process-runner start")
        return

    if args[0] == "start":
        print("Starting your project...")
        # Add logic to detect and run the user's project
    else:
        print(f"Unknown command: {args[0]}")


def detect_project_type():
    """Detects the project type based on common files."""
    if os.path.exists('package.json'):
        return 'node'
    elif os.path.exists('pom.xml'):
        return 'java'
    elif os.path.exists('Gemfile'):
        return 'ruby'
    elif os.path.exists('go.mod'):
        return 'go'
    elif os.path.exists('mix.exs'):
        return 'elixir'
    elif os.path.exists('requirements.txt'):
        return 'python'
    else:
        return None

def start_project(project_type):
    """Runs the start command for the given project type."""
    try:
        if project_type == 'node':
            subprocess.run(['npm', 'start'])
        elif project_type == 'java':
            subprocess.run(['mvn', 'compile', 'exec:java'])
        elif project_type == 'ruby':
            subprocess.run(['bundle', 'exec', 'ruby', 'main.rb'])
        elif project_type == 'go':
            subprocess.run(['go', 'run', '.'])
        elif project_type == 'elixir':
            subprocess.run(['mix', 'run'])
        elif project_type == 'python':
            subprocess.run(['python', 'main.py'])
        else:
            print('Unknown project type or missing start command.')
    except Exception as e:
        print(f"Failed to start project: {e}")

def main():
    if len(sys.argv) > 1 and sys.argv[1].lower() == "start":
        project_type = detect_project_type()
        if project_type:
            print(f"Detected {project_type} project.")
            start_project(project_type)
        else:
            print("Could not detect project type.")
    else:
        print("Usage: process-runner start")

if __name__ == '__main__':
    main()
