def printblock(start, duration, low, high, sample, value):
    if value != 0:
        result = ""
        for i in range(1, sample * 4 + 1, 2):
            result += ", %s %s" % (start + duration / sample / 4 * i, low if i % 4 == 1 else high)
            result += ", %s %s" % (start + duration / sample / 4 * i + 0.000000001, high if i % 4 == 1 else low)
        return result
    else:
        return f", {start + duration} {low}"


def printarray(array, blockwidth, low, high, sample):
    result = f"0 {low}"
    for i, v in enumerate(array):
        result += printblock(i * blockwidth, blockwidth, low, high, sample, v)
    return result


def printmatrix(matrix, sample=20):
    blockwidth = 1
    maxvoltage = 1
    voltagestep = maxvoltage / len(matrix)
    result = "output\n.option probe nomod brief\n\n"
    for i, array in enumerate(reversed(matrix)):
        result += f"vpwl{i} v{i} 0 pwl ({printarray(array, blockwidth, voltagestep * i, voltagestep * (i+1), sample)})\n.probe v(v{i})\n\n"

    result += f".tran {blockwidth / sample} {blockwidth * len(matrix[0])}\n.end\n"
    return result


if __name__ == "__main__":
    from readhzk16 import get_str_pointmap
    import sys
    string = sys.argv[1] if len(sys.argv) > 1 else "新年快乐哈哈哈"
    mat = get_str_pointmap(string)
    with open("output.sp", "w") as f:
        f.write(printmatrix(mat, 20))
