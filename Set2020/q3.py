import string

letters = string.ascii_lowercase

T = int(input())

words_score = []
for _ in range(T):
    N = int(input())
    words = [input() for _ in range(N)]

    find_index = lambda c: letters.index(c.lower()) + 1

    new_score = [sum(map(find_index, word)) for word in words]
    words_score.extend(new_score)
    words_score.sort(reverse=True)
    words_score = words_score[:3]
    print(sum(words_score))
