# scores.py  (LOCAL BRANCH)
import sys

scores = list(map(float, input("Enter scores separated by space: ").split()))

total = sum(scores)
average = total / len(scores)
maximum = max(scores)
minimum = min(scores)

print("Sum of scores:", total)
print("Average of scores:", average)
print("Maximum score:", maximum)
print("Minimum score:", minimum)
