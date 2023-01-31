import re

pattern1 = "[A-Z][a-z]+"
pattern2 = "TATAA[ACGT]{3}TT"
pattern3 = "[0-9]{2}.[^0-9]{2}"
pattern4 = "TATAA[ACGT]{3}TT.*"
p5 = "((TATAA[ACGT]{3}TT)*.(TATAA[ACGT]{3}TT)){1,}"

if __name__ == '__main__':
    print(re.match(pattern1, "Apple"))
    print(re.search(pattern2, "ACGACGTTTACACGGATATAAGGGTTACGCGCTGTATAATGTGATCAGCTGATTCGAA"))
    print(re.search(pattern2, "ACGACGTTTACACGGAAATAAGGGTTACGCGCTGTATAATGTGATCAGCTGATTCGAA"))
    print(re.search(p5, "SDADTATAAGGGTTDHHDTATAAGGGTTASFASFDTATAAGGGTT"))