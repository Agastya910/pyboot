import argparse
from tinylist import TinyList
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("items", nargs="+", help = "strings to store")
    args = parser.parse_args()

    tl = TinyList()
    for it in args.items:
        tl.append(it)
    print(list(tl[i] for i in range(len(tl))))
    popped= tl.pop()
    print("pop ->", popped)
    print("remaining:", [tl[i] for i in range(len(tl))])

    tl.remove("b")
    print("after remove('b'):", [tl[i] for i in range(len(tl))])
    
if __name__=="__main__":
    main()