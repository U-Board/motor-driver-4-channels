from machine import Pin, PWM
import math
import time


class Motor:
    def __init__(self, pins, freq=10000, max_duty=10000):
        self.pin_1 = PWM(Pin(pins[0], Pin.OUT), freq=freq)
        self.pin_2 = PWM(Pin(pins[1], Pin.OUT), freq=freq)
        self.freq = freq
        self.max_duty = max_duty

    def set_duty(self, duty: int):
        if abs(duty) > self.max_duty:
            duty = math.copysign(self.max_duty, duty)
        if duty < 0:
            self.pin_1.duty_u16(abs(int(duty)))
            self.pin_2.duty_u16(0)
        else:
            self.pin_1.duty_u16(0)
            self.pin_2.duty_u16(abs(int(duty)))

    def stop(self, emergency):
        if emergency:
            self.pin_1.duty_u16(self.max_duty)
            self.pin_2.duty_u16(self.max_duty)
            return
        self.pin_1.duty_u16(0)
        self.pin_2.duty_u16(0)


if __name__ == '__main__':
    motors = [
        Motor([2, 3]),
        Motor([0, 1]),
        Motor([6, 7]),
        Motor([4, 5])
    ]
    while True:
        for motor in motors:
            motor.set_duty(7000)
        time.sleep(2000)

        for motor in motors:
            motor.set_duty(-7000)
        time.sleep(2000)

        for motor in motors:
            motor.stop(True)
        time.sleep(2000)

