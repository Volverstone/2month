inp = input("input").lower()
engl =  ("qwertyuiop[]asdfghjkl;'zxcvbnm,./`")
russ = ("йцукенгшщзхъфывапролджэячсмитьбю.ё")
all =  dict(zip(map(ord,russ),engl))
all2 =  dict(zip(map(ord,engl),russ))
for word in engl:
    if word in inp:
        print(inp.translate(all2))
        break
for word in russ:
    if word in inp:
        print(inp.translate(all))
        break
    # else:
    #     print(inp.translate(all))
    #     break





