import os
import subprocess
import json
import colorama as c

VALIDATE_BINARY = "gltf_validator.exe"

SEVERITY_COLOUR_MAP = [
	c.Fore.RED,
	c.Fore.YELLOW,
	c.Fore.BLUE,
	""
]
SEVERITY_PREFIX_MAP = [
	"[x]",
	"[!]",
	"[i]",
	"[i]"
]

def validate(file: str) -> dict:
	args = [
		os.path.join(os.path.abspath(os.path.dirname(__file__)), VALIDATE_BINARY),
		file,
		"-o",
		"-c",
  		(os.path.join(os.path.abspath(os.path.dirname(__file__)), "config.yml"))
	]
	d = json.loads(subprocess.run(args, stdout=subprocess.PIPE).stdout)
	d["issues"]["messages"].sort(key=lambda x: x["severity"])
	return d

def pprint(file: str):
	d = validate(file)
	for m in d["issues"]["messages"]:
		print(f"{SEVERITY_COLOUR_MAP[m["severity"]]}{SEVERITY_PREFIX_MAP[m["severity"]]} {c.Style.BRIGHT}{m["code"]}{c.Style.NORMAL}")
		print((" " * 6) + m["message"])
		print(c.Style.DIM + (" " * 6) + m["pointer"])
		print(c.Style.RESET_ALL)
	sp = len(str(max(d["issues"]["numErrors"], d["issues"]["numWarnings"], d["issues"]["numInfos"], d["issues"]["numHints"]))) + 1
	print(f"{SEVERITY_COLOUR_MAP[0]}{c.Style.BRIGHT}{d["issues"]["numErrors"]}{c.Style.NORMAL}{" " * (sp - len(str(d["issues"]["numErrors"])))}Errors{c.Style.RESET_ALL}")
	print(f"{SEVERITY_COLOUR_MAP[1]}{c.Style.BRIGHT}{d["issues"]["numWarnings"]}{c.Style.NORMAL}{" " * (sp - len(str(d["issues"]["numWarnings"])))}Warnings{c.Style.RESET_ALL}")
	print(f"{SEVERITY_COLOUR_MAP[2]}{c.Style.BRIGHT}{d["issues"]["numInfos"]}{c.Style.NORMAL}{" " * (sp - len(str(d["issues"]["numInfos"])))}Infos{c.Style.RESET_ALL}")
	print(f"{SEVERITY_COLOUR_MAP[3]}{c.Style.BRIGHT}{d["issues"]["numHints"]}{c.Style.NORMAL}{" " * (sp - len(str(d["issues"]["numHints"])))}Hints{c.Style.RESET_ALL}")

pprint("D:\\dev\\MPFanGame\\minigames\\PaintballGame\\env\\attempt1.glb")