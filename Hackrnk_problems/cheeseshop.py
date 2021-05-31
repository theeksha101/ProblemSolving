def cheeseshop(kind, arg, keywords):
    print("Do you have any", kind)
    print("I'm sorry, we're all out of ", kind)
    for args in arg:
        print(arg)
    for kw in keywords:
        print(kw, ":", keywords[kw])


cheeseshop("limburger", "it's a very runny",
           "it's really very very runny",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")