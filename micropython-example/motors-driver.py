from machine import Pin, PWM
import math
import time

class Motor:
    # Инициализация мотора с заданными пинами, частотой и максимальной мощностью
    def __init__(self, pins, freq=10000, max_duty=10000):
        self.pin_1 = PWM(Pin(pins[0], Pin.OUT), freq=freq)  # Инициализация первого пина как PWM
        self.pin_2 = PWM(Pin(pins[1], Pin.OUT), freq=freq)  # Инициализация второго пина как PWM
        self.freq = freq  # Частота PWM
        self.max_duty = max_duty  # Максимальная мощность (дюти-цикл)

    # Установка мощности мотора
    def set_duty(self, duty: int):
        if abs(duty) > self.max_duty:
            duty = math.copysign(self.max_duty, duty)  # Ограничение мощности максимальным значением
        if duty < 0:
            self.pin_1.duty_u16(abs(int(duty)))  # Установка дюти-цикла на первом пине для обратного вращения
            self.pin_2.duty_u16(0)  # Отключение второго пина
        else:
            self.pin_1.duty_u16(0)  # Отключение первого пина
            self.pin_2.duty_u16(abs(int(duty)))  # Установка дюти-цикла на втором пине для прямого вращения

    # Остановка мотора
    def stop(self, emergency):
        if emergency:
            self.pin_1.duty_u16(self.max_duty)  # Полная мощность на первом пине для экстренной остановки
            self.pin_2.duty_u16(self.max_duty)  # Полная мощность на втором пине для экстренной остановки
            return
        self.pin_1.duty_u16(0)  # Отключение первого пина
        self.pin_2.duty_u16(0)  # Отключение второго пина

# Основная программа
if __name__ == '__main__':
    motors = [
        Motor([2, 3]),  # Создание объекта мотора с пинами 2 и 3
        Motor([0, 1]),  # Создание объекта мотора с пинами 0 и 1
        Motor([6, 7]),  # Создание объекта мотора с пинами 6 и 7
        Motor([4, 5])   # Создание объекта мотора с пинами 4 и 5
    ]
    while True:
        for motor in motors:
            motor.set_duty(7000)  # Вращение всех моторов вперед с мощностью 7000
        time.sleep(2000)  # Пауза 2 секунды
        for motor in motors:
            motor.set_duty(-7000)  # Вращение всех моторов назад с мощностью 7000
        time.sleep(2000)  # Пауза 2 секунды
        for motor in motors:
            motor.stop(True)  # Экстренная остановка всех моторов
        time.sleep(2000)  # Пауза 2 секунды