from pathlib import Path

def read_version():
    return Path('VERSION').read_text().strip()

def greet(name: str) -> str:
    return f"Hello, {name}! Welcome to Willful App v{read_version()}."

if __name__ == '__main__':
    print(greet('Developer'))
