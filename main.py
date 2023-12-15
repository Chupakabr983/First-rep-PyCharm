# # print("Введите число:")
# # a = int(input())
# # b = int(input())
# # c = int(input())
# # print(a + b + c)
# # print("Сумма чисел", a, ",", b, "и", c, "равна:", a + b + c, "!", "Рассчет закончен,а ты иди гулять,двоечник!")
# print("Как тебя зовут?")
# a = input()
# print ("Привет,", a, ",приятно познакомиться!")


# Модуль 7. Текстовые файлы.

# f = open("text.txt", mode="w" encoding="utf-8") - записать
# f = open("text.txt", mode="a") - добавить
# f = open("text.txt", mode="r") - прочитать
# for x in range(10):
#     f.write("123123\n") - сделать запись в текстов документе
#
# f.close()


# f = open("text.txt", mode="r")

# print(f.read()) - весь файл читает
# print(f.readline()) - показывает первую строку, если два раза покажет первую и вторую строку и тд...
# print(f.readlines()) - список строк


# f = open("text.txt", mode="r")
# data = f.read()
# f.close()
#
# f = open("text2.txt", mode="w")
# f.write(data)
# f.close()


# Задание 1:

# f = open("EX_1.txt", mode="w")
# f.write("wergjoeirgj ejrgopigj epjrgj\n weifhiweufhiweuhf0923754\n wehui89237lkxq\n rj2309iru 312\n tgdrt\n faf")
# f.close()
#
# f = open("EX_1.txt", mode="r")
# qwerty = f.readlines()
# f.close()
#
# f = open("EX_1_mod.txt", mode="w")
# for i in qwerty:
#     if len(i.strip('\n')) >= 7:
#         f.write(i + ' ')
#
# f.close()


# Задание 2:

# f = open("EX_2.txt", mode='w')
# f.write("qwerty\n qwertyuiop\n asdfghjkl\n zxcvbnm")
# f.close()
#
# f = open("EX_2.txt", mode="r")
# qwerty = f.read()
# f.close()
#
# f = open("EX_2_mod.txt", mode="w")
# for i in qwerty:
#     f.write(i)
# f.close()

# Задание 3:

# f = open("EX_3.txt", mode='w')
# f.write("qwerty\nqwertyuiop\nasdfghjkl\nzxcvbnm")
# f.close()
#
# f = open("EX_3.txt", mode="r")
# qwerty = f.readlines()
# f.close()
#
# f = open("EX_3_mod.txt", mode="w")
# for i in reversed(qwerty):
#     f.write(i.strip() + "\n")
# f.close()

# Задание 4:

# f = open("EX_4.txt", mode='w')
# f.write("qwerty\nqwertyuiop\nasdfghjkl\nzxcvbnm")
# f.close()
#
# f = open("EX_4.txt", mode="r")
# qwerty = f.readlines()
# f.close()
#
# f = open("EX_4_mod.txt", mode="w")
#
# for i in qwerty:
#         f.write(i.__add__("**************"))
# f.close()
jhk,jh,k