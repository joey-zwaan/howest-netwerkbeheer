import argparse

parser = argparse.ArgumentParser(description="een beschrijving")
parser.add_argument("-n", default=1 ,help="een getal", type=int)
# parser.add_argument("hoi", help="een getal", type=int)
args = parser.parse_args()
print(args)
print(args.n)