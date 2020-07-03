try:
    age = int(input('Age: '))
    income = 2000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print("Age cannot be zero")
except ValueError:
    print("Invalid Value")

'''
Age: afjoaljm
Traceback (most recent call last):
  File "C:/Users/Administrator/PycharmProjects/HelloWorld/exception.py", line 1, in <module>
    age = int(input('Age: '))
ValueError: invalid literal for int() with base 10: 'afjoaljm'

Process finished with exit code 1

'''
