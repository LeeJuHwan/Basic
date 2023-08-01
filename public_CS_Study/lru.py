LIMIT = 4

li = [1, 3, 0, 3, 5, 6, 3]
page = []
for i in li:
    page.insert(0, i)
    if page.count(i) >= 2:
        page = sorted(set(page), key=lambda x: page.index(x))
    if len(page) == LIMIT:
        page.pop()
    print(page)
