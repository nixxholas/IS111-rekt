import q4

# Test case 1 - Pangram
sentence = "The quick brown fox jumps over the lazy dog."
print(q4.is_pangram(sentence))

# Test case 2 - Not a Pangram
sentence = "The quick brown fox jumps over the lazy cat."
print(q4.is_pangram(sentence))

# Test case 3 
sentence = "Pack my box with five dozen liquor jugs."
print(q4.is_pangram(sentence))

# Test case 4 
sentence = "The five boxing wizards jump quickly."
print(q4.is_pangram(sentence))

# Test case 5
sentence = "Mr. Jock, TV quiz Ph.D., bags few lynx."
print(q4.is_pangram(sentence))

