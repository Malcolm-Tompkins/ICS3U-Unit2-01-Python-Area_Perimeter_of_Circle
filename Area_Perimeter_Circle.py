#!/usr/bin/env/ python3

# Created by Malcolm Tompkins
# Created on April 26, 2021
# Calculates the perimeter and area of a circle with a radius of 15mm

import math


def main():
    print("Dimensions of circle:")
    print("Radius(R) = 15mm\n")
    print("Area is:{}mm".format(math.pi * 15 ** 2))
    print("Perimeter is: {}mm".format(math.pi * 15 * 2))


if __name__ == "__main__":
    main()
