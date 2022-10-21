# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 00:32:00 2022

@author: salva


Write a python program to find the total number of ways to make change for $1

Examples: 100 pennies, or 75 pennies and 5 nickels .....
"""
coins = (50, 25, 10, 5, 1)

howManyWays = 0

for fifty in range(3): #50 cent pieces
    for quarter in range(5): #25 cent pieces
        for dimes in range(11): #10 cent pieces
            for nickels in range(51): #5 cent pieces
                for pennies in range(101): #1 cent pieces
                    amt = fifty + quarter + dimes + nickels + pennies
                    if amt == 100:
                        howManyWays += 1
                        print(f'fifty={fifty} quarter={quarter} dimes={dimes} nickels={nickels} pennies={pennies}')
