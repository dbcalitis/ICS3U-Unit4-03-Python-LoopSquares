#!/usr/bin/env python3

# Created by: Daria Bernice Calitis
# Created on: Oct 2021
# This program squares all numbers from 0 to the user_input (inclusive)


def main():
    # This function squares all numbers from 0 to the given integer
    # input
    user_input = input("Enter an integer >= 0: ")

    # process & output
    try:
        user_input = int(user_input)
        # it starts with 0 and ends with the given integer.
        if user_input >= 0:
            for counter in range(user_input + 1):  # includes the given integer
                print("{0}² = {1}".format(counter, counter ** 2))
        else:
            print("You did not enter a positive integer.")
    except (Exception):
        print("You did not enter an integer.")

    print("\nDone.")


if __name__ == "__main__":
    main()
