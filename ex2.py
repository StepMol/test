import sys


def main(s="Hello"):
    # Находит и выводит повторяющиеся символы в строке.
    # По умолчанию в слове "Hello"
    l = len(s)
    arr = []
    if l == 0:
        return False
    for i in range(l):
        st_prev = s[:i]
        st_next = s[i+1:]
        if s[i] in st_prev or s[i] in st_next:
            if s[i] not in arr:
                arr.append(s[i])
    return arr


if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(*main(sys.argv[1]))
    else:
        print(*main())
