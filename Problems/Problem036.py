import sys
sys.path.append(".\\")

from Services.Palindromes import generatePalindromes, isPalindrome
from Services.Binaries import GenerateBinaryAsString

palins = generatePalindromes(1000000)

sum = 0
for i in palins:
    binrep = GenerateBinaryAsString(i)
    if(isPalindrome(binrep)):
        sum += i
print(sum)

