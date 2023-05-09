#!/usr/bin/python3
figure = 0
while figure <= 89:
    if figure % 10 == 0:
        figure += 1 + figure // 10
    print("{:02d}".format(figure), end='\n' if figure == 89 else ", ")
    figure += 1
