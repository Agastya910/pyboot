import argparse

# positional argument
p = argparse.ArgumentParser()
# p.add_argument("filename")
# args = p.parse_args(["data.csv"])
# print(args.filename)
# optinal flag
# p.add_argument("--verbose", "-v", action="store_true")
# args = p.parse_args(["-v"])
# print(args.verbose) #true


p.add_argument("items", nargs="+")  # one or more
p.add_argument("--opt", nargs="*")  # 0 or more
p.add_argument("--exact", nargs=3)  # exactly 3
p.add_argument("--maybe", nargs="?")  # 0 or 1
