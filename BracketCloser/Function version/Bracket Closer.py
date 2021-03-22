def pairdelete(t):
    length = len(t)+1
    while length > len(t):
        length = len(t)
        if t.find("()") > -1:
            t = t.replace("()", "")
        if t.find("[]") > -1:
            t = t.replace("[]", "")
        
        if t.find("{}") > -1:
            t = t.replace("{}", "")
        
    return t

def findcenter(a):
    for i in [")(", ")[", "){", "][", "](", "]{", "}{", "}(", "}["]:
        pos = a.find(i)
        if pos > -1:
            return [pos, 2]
    
    searchr = max([a.rfind(")"), a.rfind("]"), a.rfind("}")])
    if searchr > -1:
        return [searchr, 1]

    found = []
    searchl = -1
    for i in ["(", "[", "{"]:
        if a.find(i) > -1:
            found.append(a.find(i))
        if found != []:
            searchl = min[found]
            return [searchl, -1]
    return [-1, -1]

def build(b):
    swap = {"[":"]", "]":"[", "(":")", ")":"(", "{":"}", "}":"{"}
    b = b[::-1]
    out = ''
    for i in b:
        out += swap[i]
    return out
    
s = input()
if s == "":
    pass
elif "(]" in s or "(}" in s or "[)" in s or "[}" in s or "{)" in s or "{]" in s:
    print("IMPOSSIBLE")
else:
    new = pairdelete(s)
    [split, sign] = findcenter(new)
    if split > -1:
        if sign == -1:
            left = ""
            right = build(new)
        elif sign == 1:
            left = build(new)
            right = ""
        else:
            left = build(new[:split+1])
            right = build(new[split+2:])
        print(left+s+right)
