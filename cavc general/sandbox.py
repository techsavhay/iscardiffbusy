# Taking inputs for length, width, and height
length = int(input('Enter the length: '))
width = int(input('Enter the width: '))
height = int(input('Enter the height: '))

# Function to calculate the volume of a rectangular prism
def volume(length, width, height):
    return length * width * height

# Calculating the volume
vol = volume(length, width, height)

# Printing the volume
print(f'The volume of the rectangular prism is {vol} cubic feet.')
