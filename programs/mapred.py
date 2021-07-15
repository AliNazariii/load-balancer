import sys
import time

file = open(f"{sys.argv[1]}", "r")

words = []
for line in file:
  words += line.strip().split(" ")

mapreduce_map = dict()
for word in words:
    mapreduce_map[word] = mapreduce_map.get(word, 0) + 1

sorted_map = sorted(mapreduce_map.items(), key=lambda x: x[1], reverse=True)

for k, v in sorted_map:
    print(f"{k}, {v}")

time.sleep(10)