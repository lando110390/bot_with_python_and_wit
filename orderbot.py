from wit import Wit
import os, time
import random
import sys

access_token = 'WFAMW43LPHLGGQ4QYIBNUJ5WEIBWL7OX'

# Khởi tạo đối tượng wit
client = Wit(access_token = access_token)

menu = '''
    Please, type the name.
    1. Cheese pizza
    2. Vege pizza
    3. Meat lovers pizza
    4. Pepperoni pizza
'''

greetFrist = 'Hi, May I help you to order pizza?'
B = '\n\n\n\n\n\n\n\n\n\n\n'
bface = '[-.-] '
print (B)
print (greetFrist)

typePizza = None
sizePizza = None

while True:
    message_text = input('=> ').strip()
    message_text = message_text.lower()

    resp = client.message(message_text)

    entity = None
    value = None

    try:
        entity = list(resp['entities'])[0]
        value = resp['entities'][entity][0]['value']
    except:
        pass

    response = bface;
    if entity == 'order':
        response += 'Ok. I will show you {} pizza'.format(str(value))
        response += '\n' + menu
    elif entity == 'pizza':
        response += 'Great. Please choose size: Large | Midium | Small'
        typePizza = str(value)
    elif entity == 'size':
        sizePizza = str(value)
        response += 'Thank for your order. Your pizza is ' + typePizza + ' with size ' + sizePizza
    else:
        response += 'Sorry. I don\'t understand'
    print (response)
