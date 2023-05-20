import string

letters = string.ascii_uppercase

n_col = int(input())

for _ in range(n_col):
    i_col = int(input())

    r = ""
    while i_col > 0:
        i_col, i_letter = divmod(i_col, 26)
        r += letters[i_letter - 1]

    print(r[::-1])
