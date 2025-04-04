import os
import sys

from pathlib import Path
from jinja2 import Template

TEMPLATE = Path(__file__).parent / "templates" / "airflow_local_settings.py.j2"

def init(home_dir: str|None=None):
    if home_dir is None:
        try:
            home_dir = os.environ["AIRFLOW_HOME"]
        except KeyError:
            raise ValueError("AIRFLOW_HOME is not set")
        
    home_dir = Path(home_dir)

    airflow_config_dir = home_dir / "config"
    dest = airflow_config_dir / "airflow_local_settings.py"

    if not airflow_config_dir.exists():
        raise FileNotFoundError(f"Airflow config directory not found: {airflow_config_dir}")

    with open(TEMPLATE) as f:
        content = Template(f.read()).render()

    if dest.exists():
        backup = dest.with_suffix(".bak")
        dest.rename(backup)
        print(f"[!] Existing airflow_local_settings.py backed up to: {backup}")

    with open(dest, "w") as f:
        f.write(content)
        print(f"[+] airflow_local_settings.py generated at: {dest}")

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Generate airflow_local_settings.py with ORJson")
    subparsers = parser.add_subparsers(dest="command")

    init_parser = subparsers.add_parser("init", help="Generate airflow_local_settings.py")
    init_parser.add_argument("-H", "--home-dir", help="Custom AIRFLOW_HOME directory")

    args = parser.parse_args()

    if args.command == "init":
        init(home_dir=args.home_dir)
    else:
        parser.print_help()
        sys.exit(1)
