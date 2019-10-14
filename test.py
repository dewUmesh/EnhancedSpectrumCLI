def zero():

        return 'zero'
def one():
        return 'one'
def indirect(i):
        switcher={
                'dataflow list':zero,
                'dataflow export':one("input"),
                2:lambda:'two'
                }
        func=switcher.get(i,lambda :'Invalid')
        return func()

print(indirect("dataflow list"))
