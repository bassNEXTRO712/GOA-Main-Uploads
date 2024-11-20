#6) შექმენით სია, სადაც გექნებათ 1-ანები და 0-ანები, შექმენით ახალი სია, 
# რომელიც თავიდან იქნება ცარიელი. for loop-ით გადაუარეთ პირველ სიას
#  და თუ საიტერაციო ცვლადის მნიშვნელობა იქნება 1, ახალ სიაში ჩაამატეთ
#  True, სხვა შემთხვევაში False. საბოლოოდ დაბეჭდეთ ახალი სია

numbers = [1,0,1,0,1,0,1,0,1,0,1,0,1,0]
second_numbers = []
for num in numbers:
    if num == 1:
        second_numbers.append("True")
    else:
        second_numbers.append("False")
        
    print(second_numbers)
    
