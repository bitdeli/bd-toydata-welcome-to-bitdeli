from bitdeli import profiles, set_theme, Title, Description
from bitdeli.widgets import Text, Bar
from collections import Counter

sales = Counter()
for profile in profiles():
    for event in profile['events']:
        if event['event'] == 'buy':
            sales[event['product']] += event['price']

set_theme('lipstick')

Text(head='Welcome to Bitdeli',
     size=(12,2),
     color=2)

Text(head='This board is your playground. Modify it as you wish!',
     size=(12,1),
     color=2)

Bar(label='Revenue per item',
    data=sales,
    size=(10,4),
    color=3)

Text(label='Total revenue',
     head='$%d' % sum(sales.values()),
     size=(2,4),
     color=1)

Title('Welcome to Bitdeli')

Description("""
Our deli has sold $%d worth of pickles!
""" % sales['Pickles'])
