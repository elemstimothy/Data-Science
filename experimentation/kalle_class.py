def main():
    # Write code here
    class Person():
        def __init__(self, age, weight, height, first_name, last_name, catch_phrase ):
            self.age = age
            self.weight = weight
            self.height = height
            self.first_name = first_name
            self.last_name = last_name
            self.catch_phrase = catch_phrase
            

    user = Person(25, 90, 188, 'John', 'Bonham', 'One, Two, Three, Four')
    print(user.weight)

    class Bottle():
        def __init__(self, volume, color, cap_color) -> None:
            self.volume = volume
            self.color = color
            self.cap_color = cap_color

    melk = Bottle(1, 'White', 'Red')
    print(melk.volume)
             

if __name__ == '__main__':
    main()