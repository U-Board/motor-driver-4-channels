![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![PyCharm](https://img.shields.io/badge/pycharm-143?style=for-the-badge&logo=pycharm&logoColor=black&color=black&labelColor=green)
![C++](https://img.shields.io/badge/c++-%2300599C.svg?style=for-the-badge&logo=c%2B%2B&logoColor=white)
![CMake](https://img.shields.io/badge/CMake-%23008FBA.svg?style=for-the-badge&logo=cmake&logoColor=white)
![Espressif](https://img.shields.io/badge/espressif-E7352C.svg?style=for-the-badge&logo=espressif&logoColor=white)
![Arduino](https://img.shields.io/badge/-Arduino-00979D?style=for-the-badge&logo=Arduino&logoColor=white)

***
<img width="1280" height="720" alt="image" src="https://github.com/user-attachments/assets/d0dcd142-c622-491b-a1c0-6c1b9a823f20" />
***

# UBoard Quad Motors Module

Быстрый старт по работе с 4-канальным драйвером DC-моторов*

UBoard Quad Motors Module — четырёхканальный драйвер коллекторных DC-моторов на базе SS6285M. Модуль позволяет независимо управлять четырьмя двигателями: задавать направление вращения, скорость и режим торможения.

Управление выполняется обычными GPIO микроконтроллера или одноплатного компьютера. Для каждого двигателя используются два цифровых входа управления.

Модуль рассчитан на питание двигателей 3–33 В и ток нагрузки до 6 А на канал. Управляющая часть работает с логическими уровнями 3,3–5 В и гальванически изолирована от силовой части.

1. Разъёмы платы

На плате расположены четыре силовых выхода:

Motor 1 / Motor 2 / Motor 3 / Motor 4

Каждый выход предназначен для подключения одного DC-мотора.

Питание двигателей подключается через центральный силовой разъём:

Контакт	Назначение
VIN	Питание двигателей, 3–33 В
GND	Минус источника питания

Например, при использовании двигателей на 12 В к VIN подключается +12 V, а к GND — минус источника питания.

Напряжение источника необходимо выбирать исходя из допустимого напряжения подключённых двигателей.

2. Управляющие входы

Каждый мотор управляется двумя сигналами:

INxA и INxB

где x — номер двигателя.

Например, для первого двигателя:

IN1A
IN1B

для второго:

IN2A
IN2B

и так далее до Motor 4.

На управляющих разъёмах также доступны:

GND
VCC

VCC — питание логической части 3,3–5 В.

*3. Управление направлением*

Направление вращения задаётся состояниями входов A и B.

INxA	INxB	Состояние двигателя
0	0	Свободный ход
1	0	Вращение в одну сторону
0	1	Вращение в обратную сторону
1	1	Торможение

*Подробные примеры можно найти внутри репозитория* 
