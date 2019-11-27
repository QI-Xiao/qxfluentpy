import sys, re

WORD_RE = re.compile(r'\w+')

index = {}
with open('py3_1.txt', encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        print(line)
        for match in WORD_RE.finditer(line):
            # print(match)
            word = match.group()
            print('---------word:', word)
            column_no = match.start()+1
            # print('column_no', column_no)
            location = (line_no, column_no)

            # occurrences = index.get(word, [])
            # print(location, occurrences)
            #
            # occurrences.append(location)
            # print(location, occurrences)
            # index[word] = occurrences

            index.setdefault(word, []).append(location)

print(index)
# for word in sorted(index, key=str.upper):
#     print(word, index[word])
#
# text = 'abbaaabbbbaaaaa'
#
# pattern = 'ab'
#
# for match in re.finditer(pattern, text):
#     s = match.start()
#     e = match.end()
#     print('Found {!r} at {:d}:{:d}'.format(
#         text[s:e], s, e))


# import collections
#
# index2 = collections.defaultdict(list)
# print(index2)
# with open('py3_1.txt', encoding='utf-8') as fp:
#     for line_no, line in enumerate(fp, 1):
#         print('lineline', line)
#         for match in WORD_RE.finditer(line):
#             # print(match)
#             word = match.group()
#             print('---------word:', word)
#             column_no = match.start()+1
#             location = (line_no, column_no)
#             print(index2[word])
#             index2[word].append(location)
#
# for word in sorted(index2, key=str.upper):
#     print(word, index2[word])