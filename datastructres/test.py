# lst_a = [
#     'crossin 3 2 11 \n',
#     'liubei 2 4 30 \n',
#     'guanyu 5 7 49 \n',
#     'zhangfei 3 3 33'
# ]
#
# dic_a = {}
#
# for i in lst_a:
#     data = i.strip().split()
#     print(data[0], data[1:], data)
#
#     dic_a[data[0]] = data[1:]
#
# print()
# print('dic_a',dic_a)


dic_a = {
    'crossin': ['3', '2', '11'],
    'liubei': ['2', '4', '30'],
    'guanyu': ['5', '7', '49'],
    'zhangfei': ['3', '3', '33']
}

print("dic_a.get('crossin'):", dic_a.get('crossin'))
print("dic_a.get('Jack'):", dic_a.get('Jack'))





