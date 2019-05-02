# Quality Control Module

import pandas as pd
import sys
import csv

def quality_control (infile, outfile="out.csv"):

    # read in input file, adjective dictionary
    inp = pd.read_csv(infile)
    adj_dictionary = pd.read_csv("adj.txt", names=['adj'])['adj'].tolist()
    dictionary = [x.lower() for x in adj_dictionary if x == x]

    # open output file
    out = open(outfile, "w")
    writer = csv.writer(out)
    writer.writerow(["hit_id", "worker_id", "image_url", "seen", "prompt", "type_test", "emot0", "emot1", "emot2", "pers0", "pers1", "pers2", "phys0", "phys1", "phys2"])

    adj_types = ["emot", "pers", "phys"]

    # iterate over input rows
    for _, row in inp.iterrows():

        # check if type test is passed
        if (row["Input.prompt"] == row["Answer.type_test"]):

            # remove duplicates from responses TODO: Do we want to do this?
            emot_adjectives = set([row["Answer.emot{}".format(x)].lower() for x in range(3)])
            pers_adjectives = set([row["Answer.pers{}".format(x)].lower() for x in range(3)])
            phys_adjectives = set([row["Answer.phys{}".format(x)].lower() for x in range(3)])

            adjectives = {'emot' : emot_adjectives, 'pers' : pers_adjectives, 'phys' : phys_adjectives}
            
            # check if given words are real and are adjectives
            valid = {}
            for x in range(3):
                for adjective in adj_types:
                    valid["{}{}".format(adjective, x)] = ""

            for adj_set in adjectives.keys():
                i = 0
                for word in adjectives[adj_set]:
                    if (word in dictionary):
                        valid["{}{}".format(adj_set, i)] = word
                        i += 1

            # check if seen
            seen = row["Answer.seen.on"]
            
            # write valid responses to output file
            writer.writerow([row["HITId"], row["WorkerId"], row["Input.image_url"], seen, row["Input.prompt"], row["Answer.type_test"], valid["emot0"], valid["emot1"], valid["emot2"], valid["pers0"], valid["pers1"], valid["pers2"], valid["phys0"], valid["phys1"], valid["phys2"]])

    out.close()
    return

# require command line specification of filenames
if (len(sys.argv) == 3):
    in_filename = sys.argv[1]
    out_filename = sys.argv[2]
else:
    print("Bad input - Must be of format 'python qc.py IN_FILE OUT_FILE'")
    exit(1)

quality_control(in_filename, out_filename)
