from time import sleep
import emoji
print('Lançamento do foguete em:')
for c in range(10,0,-1):
    print(c)
    sleep(1)
print(emoji.emojize('Boom!:rocket:'))
