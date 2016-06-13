# more practice

def main():
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    b = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    print("list overlap = %s" % list_overlap(a, b))

def list_overlap(a, b):
    overlap = []
    for num1 in a:
        for num2 in b:
            if num1==num2:
                overlap.append(num1)
                break
    return overlap

if __name__ == "__main__":
    main()