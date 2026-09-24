#!/usr/bin/envpython3
# Created By:Deepak
# Date: 09/24/2026
# This program asks the user for the radius of
# a circle in mm. It then calculates and displays
# the circumference using tau.
import constants


def main():
    # get the radius from the user
    radius = float(input("Enter radius of the circle  (mm): "))

    # calculate the circumference
    circumference = constants.TAU * radius

    # display the circumference
    print("")
    print("circumference - {} mm".format(circumference))


if __name__ == "__main__":
    main()
