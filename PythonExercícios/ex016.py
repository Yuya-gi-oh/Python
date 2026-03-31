import emoji
import math

num=float(input('Digite um valor: '))
print(emoji.emojize('O valor digitado foi {} e a sua porção inteira é {}:sunglasses: :sparkles: :sunglasses: :sparkles:.'.format(num,math.trunc(num))))
