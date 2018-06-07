def log(message, *args):
    if not args:
        print(message)
    else:
        args_str = ', '.join(str(x) for x in args)
        print('%s: %s' % (message, args_str))

log('My numbers are', [1, 2])
log('Hi there')
log('What about this? ', 'Peter', 'Woo')
list = ['item1', 'item2', 'item3']
log('What about these lists here:', *list)




