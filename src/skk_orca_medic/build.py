import os


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
        if "/" in line:
            print(f"::Skipped:: not formattable: {line.strip()}")
            continue
        [yomi, word] = line.split("#T35")
        [yomi, word] = [yomi.strip(), word.strip()]
        out.write(f"{yomi}/{word}/\n")
