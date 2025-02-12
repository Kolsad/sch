from itertools import product, permutations, combinations


cnt = []
for i in permutations('ДЕЙНПТЬЯ', 4):
    a = ''.join(i)
    if 'ЕЯ' not in a:
        cnt.append(a)
        print(i)

print(len(cnt))
