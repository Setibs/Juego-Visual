import keyboard
import time
dot = "."
print(dot)
while True:
    print(dot)
    for x in dot:
        if keyboard.is_pressed("space"):
            while keyboard.is_pressed("space"):
                if len(dot) < 119: #Límite para una terminal minimizada, ajustar a gusto del consumidor
                    dot += "."
                    print(dot)
                else:
                    print(dot)
                time.sleep(0.015)
        elif keyboard.is_pressed("s"):
            if len(dot) == 1:
                print("\nHave a good day!")
                exit()
            else:
                for y in dot:
                    dot = dot[:-1]
                    print(dot)
                    time.sleep(0.015)
                print("Have a good day!")
                exit()
        elif len(dot) == 1:
            time.sleep(0.015)
            continue
        else:
            dot = dot[:-1]
            print(dot)
            time.sleep(0.015)

