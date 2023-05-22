# A) Excel

In Excel, columns are label with alphabets from A to Z and after that it will use multiple letter AA - ZZ and so on.

Given an integer representing the column index, convert it into excel's column label.

## Input

-   The first line contains number of indexes, n
-   Next n line contains the index of the column, i

## Constraint

-   1 ≤ n ≤ 50
-   1 ≤ i ≤ 10^4

## Example

Input:

    4
    1
    27
    55
    714

Output:

    A
    AA
    BC
    AAL

# B) Not Another Math Question

There are X horizontal lines and Y vertical lines. These lines intersect and create some rectangles. Count how many rectangles (including sub rectangles) are there.

## Input

-   First line contains T, the number of test cases.
-   Each cases containes two integers X and Y separated by space

## Constraint

-   1 ≤ T ≤ 100
-   0 ≤ X, Y ≤ 10^5

## Example

Input:

    3
    2 3
    3 4
    2 2

Output:

    3
    18
    1

# C) Joe's Words

Calculate the sentences score. The score for the sentence is the sum of the 3 highest value word.

`Score = Sum of Index of that letter in the alphabet (1 indexed)`

## Input

-   First line containes an integer T for the test cases
-   Second line is the number of words, N for each test cases
-   Next line is a string of word for each N
-   The words are case insensitive

## Constraint

-   1 ≤ T ≤ 100
-   5 ≤ N ≤ 100

## Example

Input:

    2
    5
    Welcome
    to
    Prosolve
    National
    TwentyTwenty
    6
    Good
    luck
    and
    have
    fun
    everyone


Output:

    422
    445

# D) Let's Count Characters!

Given a sentence, find out the highest number of characters in a word that is inside of parenthesis in that sentence.

## Input

-   First line is the number of sentences, N
-   A string of sentence, s

## Constraint

-   1 ≤ N ≤ 50
-   String s contains, parenthesis, lower/upper case letters
-   Each words separated by underscore '\_'

## Example

Input:

    3
    _Jom__makan_(nasi_goreng_ayam)_dekat_(kedai_mamak_)
    _(i_like_)_durian
    (Please_answer_this_question)____in_(one_minutes)_ya

Output:

    6
    4
    8
