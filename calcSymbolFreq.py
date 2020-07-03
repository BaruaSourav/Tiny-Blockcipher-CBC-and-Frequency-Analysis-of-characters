import pandas as pd
import sys

def main():
    for args in sys.argv:
        print(str(args))
    filename = sys.argv[1]
    symbolFreqDF = pd.read_csv(filename,sep='\t')
    print(symbolFreqDF)


if __name__ == '__main__':
    main()