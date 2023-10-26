from functools import reduce

nums = [2,5,9,8,4,7,5,6,3,2]

evens = list(filter(lambda n : n % 2 == 0,nums))
doubles =list(map(lambda n : n * 2 , evens ))
sum =reduce(lambda a,b : a + b , doubles)

print(evens)
print(doubles)
print(sum)