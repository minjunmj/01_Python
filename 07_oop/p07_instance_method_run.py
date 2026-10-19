class Car:

    wheels = 4

    def __init__(self, color, model):
        self.color = color
        self.model = model
        self.speed = 0

    def accelerate(self, value):
        if value>0:
            self.speed += value

    def deceleration(self, value):
        if value > 0:
            self.speed = max(0, self.speed-value)

    def stop(self):
        self.speed = 0

    def show_info(self):
        print(f"모델명: {self.model}")
        print(f"색상: {self.color}")
        print(f"속도: {self.speed}km/h")
        print(f"바퀴: {self.wheels}")

def main():
    car1 = Car("흰색", '그랜져')
    car2 = Car("빨간색", "테슬라")
    Car.wheels = 5
    car1.accelerate(80)
    car1.deceleration(30)
    car2.accelerate(40)

    print("=== 첫 번째 자동차 ===")
    car1.show_info()

    print("=== 두 번째 자동차 ===")
    car2.show_info()
    

if __name__ == "__main__":
    main()