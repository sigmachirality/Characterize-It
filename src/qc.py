# Quality Control Module

import pandas as pd
import csv

def quality_control (infile, outfile="out.csv"):

    # read in input file
    inp = pd.read_csv(infile)

    # open output file
    out = open(outfile, "w")
    writer = csv.writer(out)
    writer.writerow(["hit_id", "worker_id", "image_url", "seen", "prompt", "type_test", "adjective0", "adjective1", "adjective2", "adjective3", "adjective4", "adjective5", "adjective6", "adjective7", "adjective8", "adjective9"])

    # iterate over input rows
    for _, row in inp.iterrows():

        # check if type test is passed
        if (row["Input.prompt"] == row["Answer.type_test"]):

            # remove duplicates from responses TODO: Do we want to do this?
            adjectives = set([row["Answer.adjective{}".format(x)] for x in range(10)])

            # check if given words are real and are adjectives
            valid = {}
            for x in range(10):
                valid["adjective{}".format(x)] = ""

            i = 0
            for word in adjectives:
                if (True): # TODO: add dictionary checking - currently accepts all words
                    valid["adjective{}".format(i)] = word
                i += 1

            # check if seen
            seen = row["Answer.seen.on"]
            
            # write valid responses to output file
            writer.writerow([row["HITId"], row["WorkerId"], row["Input.image_url"], seen, row["Input.prompt"], row["Answer.type_test"], valid["adjective0"], valid["adjective1"], valid["adjective2"], valid["adjective3"], valid["adjective4"], valid["adjective5"], valid["adjective6"], valid["adjective7"], valid["adjective8"], valid["adjective9"]])

    out.close()
    return

quality_control("sample_output.csv", "qc_out.csv")
