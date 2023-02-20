def fibonacci(count):
   list = [0, 1]

   any(map(lambda _:list.append(sum(list[-2:])),
         range(2, count)))

   return list[:count]
