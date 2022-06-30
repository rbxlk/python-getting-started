import sys

with open(sys.argv[1], mode='rt', encoding='utf-8') as f:
    for line in f:
        sys.stdout.write(line)