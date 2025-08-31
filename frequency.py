from collections import Counter

para = input("Enter a paragraph: \n").upper()
para = para.split()

frequency = Counter(para).most_common(3)

print(f"Word count: {frequency}")
