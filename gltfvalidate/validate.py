import os
import subprocess
import json
import colorama as c

VALIDATE_BINARY = "gltf_validator.exe"

SEVERITY_COLOUR_MAP = [
	"",
	c.Fore.BLUE,
	c.Fore.YELLOW,
	c.Fore.RED
]
SEVERITY_PREFIX_MAP = [
	"[i]",
	"[i]",
	"[!]",
	"[x]"
]

def validate(file: str) -> dict:
	return json.loads(subprocess.run([os.path.join(os.path.abspath(os.path.dirname(__file__)), VALIDATE_BINARY), file, "-o"], stdout=subprocess.PIPE).stdout)

def pprint(file: str):
	d = validate(file)
	for m in d["issues"]["messages"]:
		print(f"{SEVERITY_COLOUR_MAP[m["severity"] - 1]}{SEVERITY_PREFIX_MAP[m["severity"] - 1]} {c.Style.BRIGHT}{m["code"]}{c.Style.NORMAL}")
		print((" " * 6) + m["message"])
		print(c.Style.DIM + (" " * 6) + m["pointer"])
		print(c.Style.RESET_ALL)