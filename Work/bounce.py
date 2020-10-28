# bounce.py
#
# Exercise 1.5

ball_height = 100
gravity = 0.6

for i in range(10):
    ball_height *= gravity
    print(i + 1, round(ball_height, 4))