yes = tuple()
yes = ("да","д","ДА","Д","Да","yes","y","Y","YES","Yes","lf","Lf","LF")
no = tuple()
no = ("нет", "н","НЕТ","Н","Нет","не","Не","НЕ","no","n","NO","N","No","ytn","Ytn","YTN")
choice = "yes"
while choice not in no:
  while choice in yes:
    count = 1
    factorial = 1
    user_number = input('Введи положительное целое число, для которого нужно рассчитать факториал:\n')
    if user_number.isdigit():
      user_number=int(user_number)
      if user_number >=0:
        for count in range (1,user_number):
          factorial = factorial * (count+1)
          count = count + 1
        print (user_number, "! = ", factorial, sep="")
      else:
        print("Факториал можно рассчитать только для целого неотрицательного числа.")
    else:
      print("Факториал можно рассчитать только для целого неотрицательного числа.")
    choice = input("Хочешь рассчитать факториал для другого числа?\n")
print("Пока!")