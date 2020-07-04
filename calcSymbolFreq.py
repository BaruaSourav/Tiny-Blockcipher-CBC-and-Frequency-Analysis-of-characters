import pandas as pd
import sys
import csv

def main():
    filename = sys.argv[1]
    symbolFreqDF = pd.read_csv(filename,sep='\t')
    symbolStat = pd.DataFrame(columns=["Char", "Total Observations", "Relative Frequency"])
    symbolStat["Char"] = symbolFreqDF["Char"]
    symbolStat["Total Observations"] = symbolFreqDF.sum(axis = 1)
    sumOfTotalObservations = symbolStat["Total Observations"].sum()
    symbolStat["Relative Frequency"] = (symbolStat["Total Observations"]/sumOfTotalObservations) * 100
    symbolStat.at[1,"Char"] = '"'

    print("Result Table \n")
    print("#######################################")
    print(symbolStat.to_string())
    symbolStat.to_csv("charFrequencyAnalysis.tsv", sep="\t", index=False,float_format='%.4f')

if __name__ == '__main__':
    main()