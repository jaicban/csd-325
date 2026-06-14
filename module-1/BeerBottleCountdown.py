# Jerrold Icban
# June 14, 2026
# CSD325 Module 1.3 Assignment

# The purpose of this program is to count down the bottles of beer
# remaining on the wall, based on what the user initially inputs.

def sing_bottles_song(number_of_bottles):
    # This counts down the bottles of beer song from the user's starting number.

    for bottles in range(number_of_bottles, 0, -1):  # This'll count backwards from the user's starting value down to 1.
        if bottles == 1:
            print("🎵1 bottle of beer on the wall, 1 bottle of beer.🎵")
        else:
            print(f"🎵{bottles} bottles of beer on the wall, {bottles} bottles of beer.🎵")

        remaining_bottles = bottles - 1 # This'll show how many bottles remain after taking one down.

        if remaining_bottles == 1: # For grammatical purposes, this will show when only one bottle remains.
            print("🎵You take one down and pass it around, 1 bottle of beer on the wall.🎵")
        else:
            print(f"🎵You take one down and pass it around, {remaining_bottles} bottle(s) of beer on the wall.🎵")

        print()

def main():
    # This part shows the beginning of the program when running it.
    # Additionally, some emojis and spaces were added to the program for aesthetic purposes.
    # Just for fun as well as refreshing and relearning the Python program.
    
    print("🍺🍺🍺🍺🍺🍺🍺🍺🍺🍺🍺🍺🍺🍺🍺🍺🍺🍺🍺🍺🍺🍺🍺🍺🍺")
    print(" ")
    print("WELCOME TO THE BEER ON THE WALL COUNTDOWN SONG PROGRAM!")
    print("                    LET'S BEGIN!                       ") 
    print(" ")
    print("🍺🍺🍺🍺🍺🍺🍺🍺🍺🍺🍺🍺🍺🍺🍺🍺🍺🍺🍺🍺🍺🍺🍺🍺🍺")
    print(" ")
    bottles = int(input("User, please enter the number of bottles of beer you want to start off with on the wall -->>  "))
    sing_bottles_song(bottles)
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print(" ")
    print("There are no more bottles of beer remaining on the wall.")
    print("So, now it's time to make another run to the package store!")
    print(" ")
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    

main()

# References

# W3Schools Python Tutorial. https://www.w3schools.com/python/
# Oliver, Robert. Python QuickStart Guide
