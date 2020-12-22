from pathlib import Path

ROOT = (Path(__file__).parent / "..").resolve()

comment = False

with open(ROOT / "export.md", 'w') as outfile:
	for path in ROOT.rglob('suite/*.md'):  # todo: replace suite with "scenarios"
		with open(path) as file:
			for line in file:
				# if empty line, skip it
				if not line.strip():
					continue
				# if comment, skip it
				if line.startswith("```"):
					if comment:
						comment = False
						continue
					comment = True
				if comment:
					continue
				# if content, add space so it looks better in testpad
				if not line.startswith("#"):
					line = "  " + line
				outfile.write(line)
				print(line, end="")
			comment = False

print("DONE")
