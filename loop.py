# Desenhando um triângulo de altura 5
import time

altura = 5
while True:
    for i in range(altura):
        print(" " * (altura - i - 1) + "*" * (2*i + 1))
    for i in range(altura):
        print(" " * i + "*" * (2 * (altura - i) - 1))

    time.sleep()