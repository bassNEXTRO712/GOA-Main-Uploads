#შექმენით რიცხვების დიაპაზონი 1-დან 100-მდე, შეამოწმეთ თუ რიცხვი იყოფა 3-ზე დაბეჭდეთ
#  "Fizz" და გვერდზე მიუწერეთ რიცხვი. თუ რიცხვი იყოფა 5-ზე დაბეჭდეთ "Buzz
# " და გვერდზე მიუწერეთ რიცხვი, ხოლო თუ იყოფა 3-ზეც და 5-ზეც დაბეჭდეთ 
# "FizzBuzz" და გვერდზე მიუწერეთ რიცხვი


user_num = int(input("Enter Your Number For (1,100) : "))
if user_num % 3 == 0:
    print("Fizz" )
elif user_num % 5 == 0 :
    print("Buzz")
else:
 user_num % 3 
print("FizBuzz")        


