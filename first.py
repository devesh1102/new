
import numpy

def getNthUglyNo(n) :
    ans = 1
    for2 = []
    for3 = []
    for5 = []
    index2 = 1
    index3 = 1
    index5 = 1
    for i in range(1,150):
        minimum = min(index2, index3, index5)
        ans = index2*index3*index5;
        if minimum == index2:
            index2 = index2 * 2

            print i, ans,minimum
        elif  minimum == index3:
            index3 = index3 * 3

            print i, ans,minimum
        else:
            index5 = index5 * 5

            print i, ans,minimum


    return ans

def main():

    n = 1

    print getNthUglyNo(n)


if __name__ == '__main__':
    main()
