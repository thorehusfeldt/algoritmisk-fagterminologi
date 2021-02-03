import yaml
import subprocess
import os
import shutil
import re
from pathlib import Path

P = subprocess.run(["cue",  "vet",  "_data/words.yml",  "--schema", "words", "_data/wordlist.cue"], check=False)
if P.returncode == 0:
    print("validated successfully")
else:
    print(P.stdout)

with open("_data/words.yml", "r") as f:
    words = yaml.load(f, Loader=yaml.FullLoader)

def slugify(s: str):
    s = s.translate(str.maketrans({"é": "e", "ø": "o", "æ": "ae", "å": "a" }))
    return re.sub(" ", "-", s)

word_dir = Path("_words")
shutil.rmtree(word_dir)
os.mkdir(word_dir)
for w in words:
    with open(word_dir / f"{slugify(w['title'])}.md", "w") as f:
        print ("---", file=f)
        yaml.dump(w, f, allow_unicode=True)
        print ("---", file=f)
