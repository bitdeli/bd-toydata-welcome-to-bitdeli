import bitdeli
from collections import Counter

sales = Counter()
for profile in bitdeli.profiles():
    for event in profile['events']:
        if event['event'] == 'buy':
            sales[event['product']] += event['price']

bitdeli.set_theme('lipstick')

bitdeli.Text(head='Welcome to Bitdeli',
             size=(12,2),
             color=2)

bitdeli.Text(head='This board is your playground. Modify it as you wish!',
            size=(12,1),
            color=2)

bitdeli.Bar(label='Revenue per item',
            data=sales,
            size=(10,4),
            color=3)

bitdeli.Text(label='Total revenue',
             head='$%d' % sum(sales.values()),
             size=(2,4),
             color=1)

bitdeli.Title('Welcome to Bitdeli')

bitdeli.Description("""
Our deli has sold $%d worth of pickles!
""" % sales['Pickles'])
