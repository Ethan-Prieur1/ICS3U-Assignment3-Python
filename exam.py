#!/usr/bin/env python3

# Created by Ethan Prieur
# Created on April 2022
# This is a program that checks if the user can take an exam


def main():
    # This function is the main function

    # Input
    held = int(input("Enter The Number of Classes That Were Held: "))
    attended = int(input("Enter The Number of Classes You've Attended: "))

    # Process & Output
    percent = attended / held * 100
    if percent >= 75:
        print(
            "You've attended {0:,.2f}% of classes. You Can Take The Exam".format(
                percent
            )
        )
    else:
        print(
            "You've attended {0:,.2f}% of classes. You really think we’d let a troublemaker like you take the exam?".format(
                percent
            )
        )

    print("\nDone.")


if __name__ == "__main__":
    main()
