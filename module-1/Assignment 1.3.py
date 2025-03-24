#Kristopher Kuenning
#3/23/2025
#Module 1.3

def Beer (bottles):
    # Function that countdown and prints the song lyrics
    while bottles > 0:
        if bottles > 1:
            print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
            print(f"Take one down and pass it around, {bottles - 1} bottles of beer on the wall.\n")
        else:
            print("1 bottle of beer on the wall, 1 bottle of beer.")
            print("Take one down and pass it around, no more bottles of beer on the wall.\n")
        bottles -= 1

    # At the end of the countdown buy more beer
    print("No more bottles of beer on the wall, no more bottles of beer.")
    print("Go to the store and buy some more, 99 bottles of beer on the wall.")

def main():
    # Ask for user input
    bottles = int(input("How many bottles of beer are on the wall? "))
    Beer (bottles)


# Run the program
if __name__ == "__main__":
    main()
