# /// script
# dependencies = [
#   "lorem",
# ]
# ///
import random
import itertools
from datetime import datetime, timedelta
import lorem

# Constants
LIBRARIES = ['MCOD995000', 'MCOSREF', 'MCOD995001', 'OTHSREF', 'MCOD995002', 'OLYSREF']
FILE_TYPES = ['QSRC', 'QCLSRC']
MEMBER_COUNT = 2000
TYPES = ['RPG', 'COBOL', 'CLP']
LINES_PER_MEMBER = 40

def generate_random_member_name():
    """Generate a random uppercase alphanumeric member name of max 10 chars"""
    length = random.randint(6, 10)
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    return ''.join(random.choices(chars, k=length))

def generate_random_date():
    """Generate a random date in 2024"""
    start_date = datetime(2024, 1, 1)
    end_date = datetime(2024, 12, 31)
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + timedelta(days=random_number_of_days)
    return random_date.strftime('%Y-%m-%d')

# Generate data
data = []
used_combinations = set()  # Track used (lib, fil, typ, mbr) combinations

for lib in LIBRARIES:
    for fil in FILE_TYPES:
        for _ in range(MEMBER_COUNT):
            # Generate unique member for this lib-fil-typ combination
            typ = random.choice(TYPES)
            while True:
                mbr = generate_random_member_name()
                if (lib, fil, typ, mbr) not in used_combinations:
                    used_combinations.add((lib, fil, typ, mbr))
                    break
            
            for seq in range(1, LINES_PER_MEMBER + 1):
                text_data = lorem.sentence()[:70]
                
                row = [
                    lib,           # LIB
                    fil,           # FIL
                    mbr,           # MBR
                    typ,           # TYP
                    str(seq),      # SEQ
                    generate_random_date(),  # DATE
                    text_data,     # DATA
                    '-',           # LASTUSED
                    '0'            # TIMESUSED
                ]
                data.append(row)

# Sort the data by LIB, FIL, MBR, SEQ
sorted_data = sorted(data, key=lambda x: (x[0], x[1], x[2], int(x[4])))

# Write to file
with open('test.txt', 'w') as f:
    # Write header
    headers = ['LIB', 'FIL', 'MBR', 'TYP', 'SEQ', 'DATE', 'DATA', 'LASTUSED', 'TIMESUSED']
    f.write('\t'.join(headers) + '\n')
    
    # Write data
    for row in sorted_data:
        f.write('\t'.join(map(str, row)) + '\n')

total_lines = len(sorted_data)
print(f"File generated successfully with {total_lines + 1} lines.")  # +1 for header
print(f"Generated {len(used_combinations)} unique members across {len(LIBRARIES)} libraries and {len(FILE_TYPES)} file types.")
