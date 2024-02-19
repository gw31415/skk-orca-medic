import os
import re

support = re.compile('^[\u3041-\u3096ー\\d!#$%&()*+,./:<=>?]+$')


def main():
    cwd = os.path.dirname(__file__)
    in_path = os.path.join(cwd, "..", "..", "assets", "medic.t")
    out_path = os.path.join(cwd, "..", "..", "medic.L")

    if os.path.exists(out_path):
        os.remove(out_path)
    out = open(out_path, "a", encoding="EUC-JP")

    for line in open(in_path, "r", encoding="EUC-JP"):
        if "#T35" not in line:  # assert the content is a word
            print(f"::Skipped:: not a word: {line.strip()}")
            continue
        [yomi, word] = line.split("#T35")
        [yomi, word] = [yomi.strip(), word.strip()]
        if not support.fullmatch(yomi):
            print(f"::Skipped:: yomi contains not-supported char: {yomi}")
            continue
        out.write(f"{yomi} /{word}/\n")
