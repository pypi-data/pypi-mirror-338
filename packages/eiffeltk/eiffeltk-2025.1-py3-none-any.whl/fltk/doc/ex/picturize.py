from pathlib import Path
from re import search, sub
import subprocess
import sys


def version(n):
    if n == 1:
        return ''
    else:
        return '-'+str(n)


def picturize(filename):
    path = Path(filename)
    stem = path.stem
    mod_path = stem + ".mod.py"
    with open(filename) as of:
        lines = of.readlines()
    n=0
    w = h = 0
    with open(mod_path, 'w') as of:
        for line in lines:
            if "cree_fenetre" in line:
                match = search(r'cree_fenetre\((.*),(.*)\)', line)
                w, h = match.groups()
            if 'attend_' in line:
                n += 1
                line = sub(r"attend_.*?\(\)",
                           r"capture_ecran('" + stem + version(n) + "')",
                           line)
                call = 'rectangle(0, 0, {}, {}, couleur="grey")\n'
                of.write(call.format(int(w) - 1, int(h) - 1))
            of.write(line)

    subprocess.call("python3 " + mod_path, shell=True)
    # subprocess.call("rm " + mod_path, shell=True)
            
            
if __name__ == '__main__':
    for name in sys.argv[1:]:
        picturize(name)
