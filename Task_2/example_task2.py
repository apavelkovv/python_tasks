from filter_func import filter_func
words = ['Гиперболический синус', 'кек', 'ок', 'апчхи']
print(filter_func(lambda x: ' ' not in x, words))
print(filter_func(lambda x: x[0] != 'а', words))
print(filter_func(lambda x: len(x) >= 5, words))
