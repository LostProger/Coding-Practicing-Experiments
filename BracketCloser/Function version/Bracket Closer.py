def pairdelete(line):
    """Deletes pairs of brackets in line line until there are none left."""
    length = len(line) + 1
    while length > len(line):
        length = len(line)
        if line.find("()") > -1:
            line = line.replace("()", "")

        if line.find("[]") > -1:
            line = line.replace("[]", "")

        if line.find("{}") > -1:
            line = line.replace("{}", "")

    return line


def findcenter(line):
    """Finds potential highest-level brackets.
    If there are 2 of them - returns their position and 2.
    If there is only one such bracket - returns it's position and 1 (if it's a right bracket) or -1.
    Otherwise returns -1 for both position and type."""
    for i in [")(", ")[", "){", "][", "](", "]{", "}{", "}(", "}["]:
        pos = line.find(i)
        if pos > -1:
            return [pos, 2]

    searchr = max([line.rfind(")"), line.rfind("]"), line.rfind("}")])
    if searchr > -1:
        return [searchr, 1]

    found = []
    for i in ["(", "[", "{"]:
        if line.find(i) > -1:
            found.append(line.find(i))
        if found:
            return [min[found], -1]
    return [-1, -1]


def build(line):
    """Reverses brackets in a given line."""
    swap = {"[": "]",
            "]": "[",
            "(": ")",
            ")": "(",
            "{": "}",
            "}": "{"}
    line = line[::-1]
    out = ''
    for i in line:
        out += swap[i]
    return out


inputstring = input()
if inputstring == "":
    pass
elif "(]" in inputstring \
        or "(}" in inputstring \
        or "[)" in inputstring \
        or "[}" in inputstring \
        or "{)" in inputstring \
        or "{]" in inputstring:
    print("IMPOSSIBLE")
else:
    new = pairdelete(inputstring)
    [split, sign] = findcenter(new)
    if split > -1:
        if sign == -1:
            left = ""
            right = build(new)
        elif sign == 1:
            left = build(new)
            right = ""
        else:                               # we need to complete input with 2 strings from each end
            left = build(new[:split + 1])
            right = build(new[split + 1:])
        print(left + inputstring + right)

"""
Sample Input 1:

}[[([{[]}

Sample Output 1:

{}[[([{[]}])]]

Sample Input 2:

{][[[[{}[]

Sample Output 2:

IMPOSSIBLE
"""