# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0 com uma pausa de 1 segundo entre eles

import time
for x in range(10, -1, -1):
    print(x)
    time.sleep(1)

time.sleep(1)
print('BUM! BUM! POOOW!')

# for x in reversed(range(0, 11)):
#     print(x)
#     time.sleep(1)

# # print(0)
# time.sleep(1)
# print('BUM! BUM! POOOW!')