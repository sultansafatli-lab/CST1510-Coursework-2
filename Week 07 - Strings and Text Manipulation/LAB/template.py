"""
RECORD CHECK  -  my version
===========================

Name  :  Sultan
Lane  :  AI 
Date  :  13/11/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# 1. Write parse_line(raw_line) that cleans and parses one raw, messy line
#    into a dict. Handle inconsistent spacing and case - that is the whole
#    point of this week.
#
#    Typical and above: also write status_of(...), shaped for your lane
#    (e.g. OVER LIMIT / WARNING / OK, or FLAGGED / OK). Give both a
#    one-line docstring.


def parse_line(raw_line):
    """Cleans and parses a survey record into a dictionary."""

    line = raw_line.strip().lower()

    survey, rest = line.split(",", 1)

    survey = survey.strip()

    data = {
        "survey": survey
        }

    pieces = rest.split(",")

    for piece in pieces:
        key, value = piece.split("=")

        key = key.strip()
        value = float(value.strip())

        data[key] = value

    return data

def status_of(record):
    """Checks whether a survey rating should be flagged."""

    if record["rating"] <= 2:
        return "FLAGGED"
    else:
        return "OK"



# ====================================================================== INPUT
# 2. Your raw, messy records - at least 5, deliberately varied in spacing
#    and case. Match the shape to your lane:
#
#    AI / Data Science : "  Survey_2026 , rating=4 , age=23  "
#    Cyber Security     : "SRC=10.0.0.5,ATTEMPTS=12,RESULT=FAILED"
#    IT                  : "  Srv-01 , used=87 , total=100  "
#
#    Excellent: save these lines to a file and load them with open() /
#    a for loop over the file, instead of writing them directly here.

raw_records = []

with open("survey_records.txt", "r") as file:
    for line in file:
        raw_records.append(line)


# =============================================================== PROCESS + OUTPUT
# 3. Parse and report on every record.
#
#    Threshold : parse each record, print the cleaned dict.
#    Typical   : also call status_of(...) for each, print it alongside.
#    Excellent : print a one-line summary at the end - how many records,
#                how many flagged.

record_count = 0
flagged_count = 0

for raw_record in raw_records:

    data = parse_line(raw_record)

    print(data)

    status = status_of(data)

    print(status)

    record_count += 1

    if status == "FLAGGED":
        flagged_count += 1


print(f"Total records: {record_count}")
print(f"Flagged records: {flagged_count}")


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it against at least 5 genuinely messy raw records
#    [ ] Run it with a value that will not convert to a number - write the
#        error down
#    [ ] Check every function does one job, with a docstring
