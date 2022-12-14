import math

X = 5
Y = 7

print(X / Y)                                                #справжнє ділення
print(X // Y)                                               #ділення з округленням в меншу сторону

print(math.floor(2.5))                                      #найближче менше значення
print(math.floor(-2.5))
print(math.trunc(2.5))                                      #усічення дробної частини в сторону нуля
print(math.trunc(-2.5))

print(5 / 2, 5 / -2)
print(5 // 2, 5 // -2)                                      #усікання в меншу сторону: округлення до першого меншого цілого
print(5 / 2.0, 5 / -2)
print(5 // 2.0, 5 // -2.0)                                  #повторюється результат для чисел з плаваючою крапкою

print(5 / -2)                                               #зберігає остаток
print(5 // -2)                                              #округляє результат в меншу сторону
print(math.trunc(5 / -2))                                   #усікає замість округлення

print(5 / 2,',', 5 / 2.0,',', 5 / -2.0, ',', 5 / -2)        #справжнє ділення
print(5 // 2,',', 5 // 2.0,',', 5 // -2.0, ',', 5 // -2)    #ділення з заокругленням в меншу сторону