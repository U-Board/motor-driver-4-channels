// Класс для управления мотором
class Motor {
private:
  int pinA;
  int pinB;

public:
  // Конструктор класса
  Motor(int pinA, int pinB) : pinA(pinA), pinB(pinB) {
    pinMode(pinA, OUTPUT);
    pinMode(pinB, OUTPUT);
  }

  // Метод для движения мотора в одну сторону с заданной скоростью (0-255)
  void moveForward(int speed = 255) {
    analogWrite(pinA, speed);
    analogWrite(pinB, 0);
  }

  // Метод для движения мотора в другую сторону с заданной скоростью (0-255)
  void moveBackward(int speed = 255) {
    analogWrite(pinA, 0);
    analogWrite(pinB, speed);
  }

  // Метод для остановки мотора
  void stop() {
    analogWrite(pinA, 0);
    analogWrite(pinB, 0);
  }
};

// Создание экземпляров класса Motor для каждого мотора
Motor motor1(9, 10);  // Мотор 1
Motor motor2(11, 12); // Мотор 2
Motor motor3(3, 5);   // Мотор 3
Motor motor4(6, 7);   // Мотор 4

void setup() {
  // Инициализация пинов происходит в конструкторах класса Motor
}

void loop() {
  // Все моторы крутятся в одну сторону с полной скоростью
  motor1.moveForward();
  motor2.moveForward();
  motor3.moveForward();
  motor4.moveForward();
  delay(2000); // Двигаемся 2 секунды

  // Останавливаем все моторы
  motor1.stop();
  motor2.stop();
  motor3.stop();
  motor4.stop();
  delay(1000); // Пауза 1 секунда

  // Все моторы крутятся в другую сторону с половиной скорости
  motor1.moveBackward(128);
  motor2.moveBackward(128);
  motor3.moveBackward(128);
  motor4.moveBackward(128);
  delay(2000); // Двигаемся 2 секунды

  // Останавливаем все моторы
  motor1.stop();
  motor2.stop();
  motor3.stop();
  motor4.stop();
  delay(1000); // Пауза 1 секунда
}
