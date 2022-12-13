#!/usr/bin/env python3

# Created By: Kestrel Bryce
# Date: Dec. 13, 2022
# This program asks for the base
# and height of a square
# pyramid and calculates its
# volume using a function

import math


# volume function
def calculate_volume(height_cm, base_cm):
    try:
        # checking that height_cm is a float
        height_cm_float = float(height_cm)

        # checking that it's bigger than zero
        if height_cm_float > 0:
            try:
                # checking that base_cm is a float
                base_cm_float = float(base_cm)

                # checking that it's bigger than zero
                if base_cm_float > 0:
                    # initializing pyramid_volume
                    pyramid_volume = base_cm_float * (height_cm_float / 3)
                    # returning pyramid_volume
                    return pyramid_volume
                else:
                    # negative message
                    print("\n")
                    print("Please enter a positive base.")
            except ValueError:
                # string message
                print("\n")
                print("Please enter a valid base.")
        else:
            # negative message
            print("\n")
            print("Please enter a positive height.")
    except ValueError:
        # string message
        print("\n")
        print(("Please enter a valid height."))


def main():
    # introductory paragraph
    print("This program asks how many numbers")
    print("you want to add together, gets that")
    print("numbers of integers from the user,")
    print("and displays the sum")
    print("")

    # input
    # getting height_string
    height_cm = input("Enter the height in cm: ")
    # getting base_string
    base_cm = input("Enter the base in cm: ")

    # calling function
    pyramid_volume = calculate_volume(height_cm, base_cm)

    # printing results
    print("Your volume is {:,.2f}".format(pyramid_volume), end="")
    print(" cm3.")


if __name__ == "__main__":
    main()
