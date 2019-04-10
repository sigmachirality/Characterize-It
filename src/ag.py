# Aggregation Module

import pandas as pd
import csv

def aggregate (infile, outfile="out.csv"):

    # read in from input file
    inp = pd.read_csv(infile)

    # open output file
    out = open(outfile, "w")
    writer = csv.writer(out)
    writer.writerow(["image_url", "adjective0", "adjective1", "adjective2", "adjective3", "adjective4"])

    freq = {}

    # build dictionary of common responses and frequencies
    for _, row in inp.iterrows():

        if (row["image_url"] not in freq):
            freq[row["image_url"]] = {}

        for i in range(10):
            if (row["adjective{}".format(i)] == row["adjective{}".format(i)] and row["adjective{}".format(i)] != ""):
                if (row["adjective{}".format(i)] not in freq[row["image_url"]]):
                    freq[row["image_url"]][row["adjective{}".format(i)]] = 0
                
                freq[row["image_url"]][row["adjective{}".format(i)]] += 1

    # write top 5 adjectives for each image to the output file
    for key in freq.keys():
        sorted_freqs = sorted(freq[key].items(), key=lambda kv: kv[1], reverse=True)
        writer.writerow([key, sorted_freqs[0][0], sorted_freqs[1][0], sorted_freqs[2][0], sorted_freqs[3][0], sorted_freqs[4][0]])

    out.close()
    return

aggregate("qc_out.csv", "ag_out.csv")