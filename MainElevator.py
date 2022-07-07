from elevators.RestrictiveAutomaticElevator import *
from elevators.VeryInformativeAutomaticElevator import *
from elevators.outputDevice import *

# def restrict(resElev, arr_rest):
#     for k in arr_rest:
#         resElev.RestrictStorey(k)
#
# def create_Elev(dct_elev):
#     while True:
#         name_e = input('Введите название лифта: ')
#         choice = input('Создать: 1.VIAE 2.RAE\n')
#         storeys = int(input('Введите количество этажей: '))
#         try:
#             if choice == '1':
#                 dct_elev[name_e] = VeryInformativeAutomaticElevator(storeys)
#                 break
#             elif choice == '2':
#                 dct_elev[name_e] = RestrictiveAutomaticElevator(storeys)
#                 n = int(input('Введите количество запрещенных этажей: \n'))
#                 arr = [int(input('Запретить этаж: \n')) for i in range(n)]
#                 restrict(dct_elev[name_e], arr)
#                 break
#             else:
#                 print('Неверные данные')
#         except ValueError as e:
#             print(e)
#
#
# def show_and_choice(dct_elev):
#     while True:
#         for key in dct_elev:
#             print(key)
#         choice = input('Введите название лифта: ')
#         if choice in dct_elev:
#             return dct_elev[choice]


def main():
    device = FileDevice('in.txt')
    elev = InformativeAutomaticElevator(20, device)
    elev.move_to(10)
    device.close()

    # dct_elev = {}
    # print('Создаем первый лифт')
    # create_Elev(dct_elev)
    # while True:
    #     choice = input('1.Создать лифты 2.Прокатиться на лифте\n')
    #     if choice == '1':
    #         create_Elev(dct_elev)
    #     elif choice =='2':
    #         elev = show_and_choice(dct_elev)
    #         break
    # while True:
    #     storey = int(input('Введите этаж: '))
    #     try:
    #         elev.move_to(storey)
    #     except ValueError as e:
    #         print(e)


main()