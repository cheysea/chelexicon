import random

rand = random.Random(100)
rand_list: list = []
for number in range(10):
    rand_list.append(random.randint(1, 100))
    print(rand_list[number])



def explained_enumerate(input_list: list):
    index: int = 0
    enumerated_dict: dict = {}
    for number in rand_list:
        enumerated_dict[index] = number
        index += 1
    return enumerated_dict

for key,value in explained_enumerate(rand_list).items():
    print(f"Key: {key}, Value: {value}")





#for index,number in enumerate(rand.sample(range(100), 10)):
#    print(f"Index: {index}, Number: {number}")


