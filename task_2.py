#Написать программу, которая должна найти и вывести повторяющийся символ в слове «Hello»

hello = "Hello"

for i in hello:
    if hello.count(i) > 1:
        print("Повторяющийся символ:", i)
        break
else:
    print("Нет повторяющихся символов")
