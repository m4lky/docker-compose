import sys
import subprocess
import logging
from pathlib import Path


def get_yaml():
    return [
        p.name
        for p in Path.cwd().iterdir()
        if p.is_file() and p.suffix.lower() in {".yml", ".yaml"}
    ]

def docker_compose_up(yaml_list):
    for i in yaml_list:
        up = ["docker", "compose", "-f", i, "up", "-d"]
        subprocess.run(up, check=True)

def docker_compose_down(yaml_list):
    for i in yaml_list:
        down = ["docker", "compose", "-f", i, "down"]
        subprocess.run(down, check=True)

def main():
    yaml_list = get_yaml()
    print(yaml_list)
    docker_compose_up(yaml_list)
    
if __name__ == "__main__":
    main()


