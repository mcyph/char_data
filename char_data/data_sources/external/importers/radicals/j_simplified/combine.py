from toolkit.list_operations.rem_dupes import rem_dupes
from codecs import open

D = {}

for p in ('JSimplified.txt', 'JSimplified-2.txt'):
    for line in open(p, 'rb', 'utf-8'):
        D.setdefault(line.split()[0], []).extend(i for i in line.split()[1] if i != line.split()[0])

with open('out.txt', 'wb', 'utf-8') as f:
    for char, L in sorted(D.items()):
        print(char, ''.join(rem_dupes(L)))
        f.write('%s %s\n' % (char, ''.join(rem_dupes(L))))
