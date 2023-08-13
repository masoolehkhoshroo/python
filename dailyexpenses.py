from docopt import docopt
from api import init,add,show 
from tabulate import tabulate
usage='''
usage:
    spent_app.py --init
    spent_app.py  --show[<category>]
    spent_app.py  --add <amount> <catrgory> [<message>]
'''
args=docopt(usage)
if args['--init']:
    init()
    print('Your Table successfully Created')
if args['--show']:
    category=args['<category>']
    amount,results=show(category)
    print('Total expense:',amount)
    print(tabulate(results))
if args['__add']:
    try:
        amount=float(args['<amount>'])
        add(amount,args['<category>'],args['<message>'])
        print('item added')
    except:
        print(usage)
