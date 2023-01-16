#1
# class OS_user:
#     def about(self):
#         print("I using PC")
# class Windows_user(OS_user):
#     def about1(self):
#         print("I using Windows")
# class Windo7(Windows_user):
#     def about2(self):
#         print("I am using Windows 7 Ultimate")
# class Linux_user(OS_user):
#     def about1(self):
#         print('I like Arch Linux')
# class KDE_user(Linux_user):
#     def about2(self):
#         print('I use KDE Plasma for Arch Linux')
# class admin(OS_user):
#     def about2(self):
#         print('I am admin for this pc.')
# class idk(admin, KDE_user):
#     def __init__(self):
#         super().about1()
#         super().about()
# user = idk()

#2



#3
# class Car:
#     def __init__(self):
#         print('i have 4 wheels')
# class Ferrari(Car):
#     def __init__(self):
#         super().__init__()
#         print('i have 3 'r' on ferrari')
# class Opel(Car):
#     def __init__(self):
#         super().__init__()
#         print('i have lightning on my logo')
# class Ferrari812(Ferrari):
#     def __init__(self):
#         super().__init__()
#         print('The 812 Superfast has a 6,496 cc (6.5 L) F140 GA V12, an enlarged version of the 6.3-litre engine used in the F12berlinetta. It generates a power output of 800 PS (588 kW; 789 hp) at 8,500 rpm and 718 N⋅m (530 lb⋅ft) \nof torque at 7,000 rpm.[7][8] According to Ferrari in 2018, the 812 Superfasts engine was, at the time, the most powerful naturally \naspirated production car engine ever made. It does not feature turbocharging or hybrid technology.\nCars built in 2019 or before were not fitted with petrol particulate filters, whereas\ncars built in 2020 or after are now fitted with the emissions device.')
# class Opel_ast(Opel):
#     def __init__(self):
#         super().__init__()
#         print('The Opel Astra is a compact car/small family car (C-segment) developed and produced by the German automaker Opel \nsince 1991, currently at its sixth generation. It was first launched in September 1991 as a direct replacement to the Opel Kadett. As of 2022, the car slots between the smaller Corsa supermini and the larger Insignia large family car. Initially, the \nAstra was available in hatchback, saloon, and estate (station wagon; known as the Astra Caravan, \nlater the Sports Tourer) forms. A panel van (sedan delivery; Astravan) and a convertible (Astra Cabrio) also appeared in the early 1990s. These body styles were later followed by a coupé (the Astra GTC) in 2004, and the sporty Astra OPC appeared in 2005.\n The Twin Top retractable hardtop convertible replaced the soft top convertible in 2006, while the Caravan \nwas renamed to Astra Sports Tourer since 2009.')
# print('--------------------Ferrari 812--------------------')
# f812 = Ferrari812()
# print('--------------------------------------------------\n')
# print('--------------------Opel Astra-------------------')
# oast = Opel_ast()
# print('-------------------------------------------------')

# 6
import icecream
import inspect
import sys
print(inspect.ismodule(icecream))
print(inspect.isclass(icecream))
print(inspect.isfunction(icecream))
print(inspect.getmodule(icecream))
print(callable(icecream))
for module_name, module_path in sys.modules.items():
    print(module_name, module_path)