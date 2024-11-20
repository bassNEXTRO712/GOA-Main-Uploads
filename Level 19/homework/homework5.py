#შექმენით რიცხვების სია, გადაუარეთ მას for loop-ით, გაიგეთ
#  რამდენი ლუწი და რამდენი კენტი რიცხვი გვაქვს სიაში და დაბეჭდეთ მათი რაოდენობა

#numbers = [102,204,201,701,2029,28383,22838,19283,]
#luwebi = []
#kentebi = []
#x = len(numbers)
#for x in range(x + 1):
#    print(x)
#if numbers % 2 == 0:
#    numbers.append(luwebi)
#else:
#    numbers.append(kentebi)    




numbers = [1,2,3,4,5,6,7,8,9,10,12]

even_count = 0
odd_count = 0

for number in numbers:
        if number % 2 == 0:
                even_count += 1
        else:
                odd_count += 1


print("Even numbers count:", even_count)
print("Odd numbers count:", odd_count)