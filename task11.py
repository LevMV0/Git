#1
def power(a, n):
    if n == 0:
        return 1
    else:
        return a * power(a, n - 1)
a = int(input("Vvedit chyslo: "))
n = int(input("Vvedit stupin: "))
print(power(a,n))
#2

#3
import random
numbers = [random.randint(-100, 100) for _ in range(100)]
def find_min_sequence(numbers, index=0, best_index=0, best_sum=None):
    if index > len(numbers) - 10:
        return best_index
    current_sum = sum(numbers[index:index+10])
    if best_sum is None or current_sum < best_sum:
        best_sum = current_sum
        best_index = index
    return find_min_sequence(numbers, index + 1, best_index, best_sum)
position = find_min_sequence(numbers)
print("Spysok:", numbers)
print("Posiziya:", position)
print("Poslidovnist:", numbers[position:position+10])
print("Suma:", sum(numbers[position:position+10]))