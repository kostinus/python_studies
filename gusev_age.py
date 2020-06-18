"""Python class AGE"""

kinder = range(0,6)
school = range(6,18)
university = range(18,24)

age = input("Сколько тебе лет, дорогой пользователь?\n")

try:
  age=float(age)
  if age in kinder:
    print("Тебе пора в детский сад.")
  elif age in school:
    print("Тебе пора в школу.")
  elif age in university:
    print("Тебе пора в институт.")
  else:
    print("Тебе пора на работу.")
except ValueError:
  print("Такого не бывает.")

#else:
 # print("Такого возраста не бывает.")