import random
import itertools
from operator import itemgetter

# Constants
MAXCOMBIS = 10000
VALUES_COL1 = ['MCO']
VALUES_COL2 = ['QCLSRC', 'QSRC']
VALUES_LANG = ['RPGLE', 'COBOL', 'CL', 'C', 'CPP', 'JAVA', 'SQL']  
COMBINATION_LENGTH = 4
TWO_LETTER_COMBINATIONS = ['AB', 'CD', 'EF', 'GH','12', '34', '56', '78', '90', 'AB', 'CD', 'EF', 'GH', 'IJ', 'KL']
NUM_LINES = 1000000

# Generate all unique combinations of the two-letter combinations
all_combinations = list(itertools.permutations(TWO_LETTER_COMBINATIONS, COMBINATION_LENGTH))
all_combinations = [''.join(comb) for comb in all_combinations]
random.shuffle(all_combinations)

# Limit to first 10,000 combinations (if there are more)

if len(all_combinations) > MAXCOMBIS:
    all_combinations = all_combinations[:10000]

# Generate data
data = []
line_count = {}
lang_val = {}

for i in range(NUM_LINES):
    col1_value = random.choice(VALUES_COL1)
    col2_value = random.choice(VALUES_COL2)
    col3_value = random.choice(all_combinations)

    # Determine n (the numeric column)
    key = (col1_value, col2_value, col3_value)
    # If key is not in the dictionary, add it with a value of 1
    if key not in line_count:
        line_count[key] = 1
        lang_val[key] = random.choice(VALUES_LANG)
    else:
        line_count[key] += 1

    if line_count[key]<=20000:
    
        n_value=line_count[key]

        # Generate metadata column (6 digit number)
        metadata_value = '{:06d}'.format(random.randint(0, 999999))

        # Generate xyzdata column (random text up to 100 characters)
        xyzdata_length = random.randint(1, 100)
        xyzdata_value = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 ', k=xyzdata_length))
        lang_value=lang_val[key]
        data.append((col1_value, col2_value, col3_value, lang_value, n_value, metadata_value, xyzdata_value))

# Sort the data
sorted_data = sorted(data, key=itemgetter(0, 1, 2, 3, 4, 5))

# Open file to write data
with open('test.txt', 'w') as f:
    # Write header
    f.write("System\tLibrary\tObject\tLang\tSequence\tMetadata\tXYZData\n")
    
    # Write sorted data
    for row in sorted_data:
        f.write('\t'.join(map(str, row)) + '\n')

print("File generated successfully with {} lines.".format(NUM_LINES + 1))  # +1 for the header
