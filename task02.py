x=""
while(True):
    print("First (q to quit)")
    x=input()
    if x=='q'or x=='Q':
        break
    x=int(x)
    print("Second:")
    y=int(input())
    print(f"sum {x+y} product {x*y} average {(x+y)/2}")

print("bye")