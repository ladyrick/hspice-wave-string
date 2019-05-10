def get_char_pointmap(character):
    bytecode = character.encode("gb2312")
    offset = (94 * (bytecode[0] - 0xa1) + bytecode[1] - 0xa1) * 32

    with open("hzk16", "rb") as f:
        f.seek(offset, 0)
        hzk = f.read(32)

    mat = []

    def byte2arr(b):
        return [b >> o & 1 for o in reversed(range(8))]

    for i in range(16):
        row = byte2arr(hzk[i * 2]) + byte2arr(hzk[i * 2 + 1])
        mat.append(row)

    return mat


def get_str_pointmap(string, surround=1):
    head = (len(string) * (16 + surround) + 1) * [0]
    mat = [head[:]]
    pms = [get_char_pointmap(c) for c in string]
    for i in range(16):
        row = [0] * surround
        for pm in pms:
            row += pm[i] + [0] * surround
        mat.append(row)
    mat.append(head[:])
    return mat


if __name__ == "__main__":
    mat = get_str_pointmap("我爱你")
    for row in mat:
        for p in row:
            print("@" if p else ".", end="")
        print()
