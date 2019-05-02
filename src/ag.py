# Aggregation Module

import pandas as pd
import sys
import csv

def aggregate (infile, outfile="out.csv"):

    # read in from input file
    inp = pd.read_csv(infile)

    # open output file
    out = open(outfile, "w")
    writer = csv.writer(out)

    # TODO: need to update output format
    writer.writerow(["image_url", "adjective0", "adjective1", "adjective2", "adjective3", "adjective4"])

    adj_types = ["emot", "pers", "phys"]

    freq = {}

    # build dictionary of common responses and frequencies
    for _, row in inp.iterrows():

        if (row["image_url"] not in freq):
            freq[row["image_url"]] = {}
            for adjective in adj_types:
                freq[row["image_url"]][adjective] = {}

        for adjective in adj_types:
            for i in range(3):
                if (row["{}{}".format(adjective, i)] == row["{}{}".format(adjective, i)] and row["{}{}".format(adjective, i)] != ""):
                    if (row["{}{}".format(adjective, i)] not in freq[row["image_url"]][adjective]):
                        freq[row["image_url"]][adjective][row["{}{}".format(adjective, i)]] = 0
                    
                    freq[row["image_url"]][adjective][row["{}{}".format(adjective, i)]] += 1

    # write top 5 adjectives for each image to the output file TODO: need to update output format
    for key in freq.keys():
        sorted_freqs = sorted(freq[key].items(), key=lambda kv: kv[1], reverse=True)
        writer.writerow([key, sorted_freqs[0][0], sorted_freqs[1][0], sorted_freqs[2][0], sorted_freqs[3][0], sorted_freqs[4][0]])

    out.close()
    return

# require command line specification of filenames
if (len(sys.argv) == 3):
    in_filename = sys.argv[1]
    out_filename = sys.argv[2]
else:
    print("Bad input - Must be of format 'python ag.py IN_FILE OUT_FILE'")
    exit(1)

aggregate(in_filename, out_filename)