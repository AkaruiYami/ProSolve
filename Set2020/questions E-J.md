# E) Crypt

Given a hexadecimal string. Try to decode it and output the secret message hidden in it. Your only clue is, it was ecrypted by a secret key and luckily, you recovered the front-chunk from the original data.

## Input

- First line is a test case, T
- For each test case, the first input is a hexadecimal string, E
- Second line of input is an integer, KL that represent the length of the key
- Third line of input is another hexadecimal string, RP that represent the front-chunk of the original data

## Constraint

- 1 ≤ T ≤ 128
- 1 ≤ length(E) ≤ 1024
- 1 ≤ KL ≤ 16
- 1 ≤ length(RP) ≤ 1024
- KL ≤ length(RP)

## Example

Input:

	3
	20000000491a18450d59114806010014020b185d540c080708
	10
	54686973206973207468
	32010e061b164b0a0c46540006044907030c0a1203071b18
	10
	466967757265206f757420686f
	33070617491f1e06121315060d5301121d005955010648
	10
	476f6f64206c75636b2061

Output:

	This is the original data
	Figure out how this work
	Good luck and have fun!




