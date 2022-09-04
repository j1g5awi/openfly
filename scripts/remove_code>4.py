from pathlib import Path
for 码表 in Path().glob("*.dict.yaml"):
    if 码表.name in ["flypy.dict.yaml", "openfly.dict.yaml", "openfly.symbols.dict.yaml", "openfly.embedded.hint.dict.yaml"]:
        continue
    with open(码表, "r") as f:
        raw = f.read()
        output = raw[: raw.find("...") + 4]
        raw = raw[raw.find("...") + 4 : -1]
        dict = [
            (line.split("\t", 1)[0], line.split("\t", 1)[1])
            for line in raw.split("\n")
            ]
        for char, code in dict:
            if len(char) > 4:
                print(char, code)
            else:
                output += f"{char}\t{code}\n"
    with open(码表, "w") as f:
        f.write(output)
