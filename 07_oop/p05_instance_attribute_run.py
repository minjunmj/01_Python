class Car:

    def __init__(self, color, model):
        self.color = color
        self.model = model
        self.speed = 0

def main():
    car1 = Car("흰색", "그랜저")
    car2 = Car("빨간색", "테슬라")

    print(car1.color)
    print(car2.color)


if __name__ == "__main__":
    main()