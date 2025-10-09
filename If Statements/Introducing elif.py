# In this exercise, it's related to biology about where
# most of the cells in your body contain your full genetic code in DNA
# Part of a single strand is something like: AGTAGCGTCCTTAGTTACAGGATGGCTTAT...
# and it will be paired with another strand where A = T vice versa, C = G vice versa, and so on
# TCATCGCAGGAATCAATGTCCTACCGAATA...

# Let's create a function where we will replace every character with if statements
dna = 'AGTAGCGTC'
opposite_dna = ''
for char in dna:
    if char == 'A':
        char = 'T'
    if char == 'T':
        char = 'A'
    if char == 'G':
        char = 'C'
    if char == 'C':
        char = 'G'
    opposite_dna += char
print(opposite_dna) # Outputs: AGAAGGAG
# The output isn't right, due to continuation of passing condition from one another
# that keeps on getting its condition met resulting to unexpected result

# In that case, we need to use an else keyword
dna2 = 'AGTAGCGTC'
opposite_dna2 = ''
for char2 in dna2:
    if char2 == 'A':
        char2 = 'T'
    else:
        if char2 == 'T':
            char2 = 'A'
    
    if char2 == 'G':
        char2 = 'C'
    else:
        if char2 == 'C':
            char2 = 'G'
    opposite_dna2 += char2
print(opposite_dna2) # Output TCATCGCAG which is correct

# But this can also be rewritten with elif keyword
dna3 = 'AGTAGCGTC'
opposite_dna3 = ''
for char3 in dna3:
    if char3 == 'A':
        char3 = 'T'
    elif char3 == 'T':
        char3 = 'A'
    elif char3 == 'G':
        char3 = 'C'
    elif char3 == 'C':
        char3 = 'G'
    opposite_dna3 += char3 # Output TCATCGCAG
print(opposite_dna3)