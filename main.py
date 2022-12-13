# Imports
import random
import base64

# Picks a random number between 0-1000 and stores it to RandomNumber. String variable saved as well.
RandomNumber = random.randint(0, 1001)
RandomNumberString = str(RandomNumber)

# Flag value
EncodedFlag = "JHtzb25vZmFiaWNoP30="

# While testing print the number
# print(RandomNumberString)

# Saves input as int to SelectedNumber
SelectedNumber = int(input("Enter a number between 0 - 1000: "))

# Counter for amount of tries
count = 1

# While input does not equal the random number, loop
while RandomNumber != SelectedNumber:

    if SelectedNumber < RandomNumber:
        SelectedNumber = int(input("Try a larger number: "))
        count = count+1

    elif SelectedNumber > RandomNumber:
        SelectedNumber = int(input("Try a smaller number: "))
        count = count+1

    else:
        break

# Converts "count" and "RandomNumber" to string
CountString = str(count)
RandomNumberString = str(RandomNumber)

# Prints endgame result
print("\nCongratulations, you guessed the correct number in " + CountString + " attempt(s)!")
print("You get " + RandomNumberString + " cookies!\n")

# Checks counter to check if flag should be given
if count < 10:
    # Decodes the EncodedFlag variable
    DecodedFlag = base64.b64decode(EncodedFlag).decode('utf-8')
    print("Well done, you finished the secret. The flag is:\n" + DecodedFlag)

else:
    print("Use less than 10 attempts to access the secret.")







