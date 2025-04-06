import os
import csv
import stem
import json
import random
import stem.control
from datetime import datetime
from urllib.parse import urlparse
from .config import BLACKLISTED_UAS, FAKE_UAS

def basedir(name="results"):
    """
    Returns the absolute path of a base directory under the current working directory.
    Creates the directory if it does not exist.

    Args:
        name (str): Folder name (e.g., 'downloads', 'results', 'logs').

    Returns:
        str: Absolute path to the created/verified base directory.
    """
    base_dir = os.path.join(os.getcwd(), name)
    os.makedirs(base_dir, exist_ok=True)
    return base_dir

def rotate_ua():
    """
    Returns a random user-agent from FAKE_UAS, avoiding blacklisted ones.
    """
    while True:
        agent = random.choice(FAKE_UAS)
        if not any(bad.lower() in agent.lower() for bad in BLACKLISTED_UAS):
            return agent

def _fallback_ua():
    return "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    
def export_data(data, export_as="json", class_name="Result", output_dir=None):
    """
    Exports data in json, csv, txt, or markdown format.
    """
    if output_dir is None:
        output_dir = os.path.join(os.getcwd(), "results")
    os.makedirs(output_dir, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{class_name}_{timestamp}.{export_as}"
    filepath = os.path.join(output_dir, filename)

    try:
        if export_as == "json":
            with open(filepath, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4, ensure_ascii=False)

        elif export_as == "csv":
            with open(filepath, "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(["engine", "title", "url", "description", "domain"])
                for engine, entries in data.items():
                    for entry in entries:
                        writer.writerow([
                            engine,
                            entry.get("title", ""),
                            entry.get("url", ""),
                            entry.get("description", ""),
                            entry.get("domain", "")
                        ])

        elif export_as == "markdown":
            with open(filepath, "w", encoding="utf-8") as f:
                for engine, entries in data.items():
                    f.write(f"## {engine}\n\n")
                    for entry in entries:
                        f.write(f"**{entry.get('title', 'No Title')}**  \n")
                        f.write(f"{entry.get('description', '')}  \n")
                        f.write(f"[Link]({entry.get('url', '')}) — `{entry.get('domain', '')}`\n\n")

        elif export_as == "txt":
            with open(filepath, "w", encoding="utf-8") as f:
                for engine, entries in data.items():
                    f.write(f"=== {engine} ===\n")
                    for entry in entries:
                        f.write(f"{entry.get('title', 'No Title')}\n")
                        f.write(f"{entry.get('description', '')}\n")
                        f.write(f"{entry.get('url', '')} ({entry.get('domain', '')})\n")
                        f.write("\n")
        else:
            return f"[Export Error] Unknown format: {export_as}"

        return filepath

    except Exception as e:
        return f"[Export Error] {e}"
    
def rotate_ip():
    try:
        with stem.control.Controller.from_port(port=9051) as c:
            c.authenticate()
            c.signal(stem.Signal.NEWNYM)
            return True
    except Exception as e:
        return {"error": str(e)}
