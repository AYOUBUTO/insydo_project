__author__ = 'Apolikamixitos'


"""
    Get the longest substring from a list of strings
"""


def longest_substring(list_strings):

    track = {}

    for idx, line in enumerate(list_strings):
        subs = line.split(" ")

        # Split each line substrings
        for sub in subs:
            track[sub]=[idx] #The index line where it's found

            #We keep searching in other lines Except the one where we found the sub
            for idx_other, other_line in enumerate(list_strings):
                other_subs = other_line.split(" ")

                for other_sub in other_subs:

                    if sub != other_sub and sub in other_sub[0:len(sub)]:
                        #Track iterations
                        if idx_other not in track[sub]:
                            track[sub].append(idx_other)

    #Filtering the results
    longest_sub = ''
    for key, list_idx_lines in track.items():
        #Get subs that are found in at least 2 lines
        if len(list_idx_lines) > 1:
            if len(key) > len(longest_sub):
                longest_sub = key

    return longest_sub