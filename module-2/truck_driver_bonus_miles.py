def calculate_bonus():

    print('Welcome, Truck Driver!')
    print('')

    # Enter the miles driven for the day
    miles = int(input('Enter the miles driven for the day: '))

    print('')

    # If the miles are 500 or more, the driver gets a bonus
    if miles >= 500:

        print('Congratulations, you earned an additional')
        print('$125 bonus incentive!')

    else:

        print('500 miles or more is required')
        print('to receive the incentive bonus.')


def main():

    calculate_bonus()


main()
