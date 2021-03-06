
import sys
import struct

# Open our input file which is defined by the first commandline argument
# then dump it into a list of bytes
infile = open("./eyes/frame_00_delay-0.1s.jpg", "rb")  # b is for binary
contents = bytearray(infile.read())
infile.close()

# Get the size of this image
data = [contents[2], contents[3], contents[4], contents[5]]
fileSize = struct.unpack("I", bytearray(data))

print("Size of file:", fileSize[0])

# Get the header offset amount
data = [contents[10], contents[11], contents[12], contents[13]]
offset = struct.unpack("I", bytearray(data))

print("Offset:", offset[0])

# Get the number of colors used
data = [contents[46], contents[47], contents[48], contents[49]]
colorsUsed = struct.unpack("I", bytearray(data))

print("Number of colors used:", colorsUsed[0])

# Create color definition array and init the array of color values
colorIndex = bytearray(colorsUsed[0])
for i in range(colorsUsed[0]):
    colorIndex.append(0)

# Assign the colors to the array
startOfDefinitions = 54
for i in range(colorsUsed[0]):
    colorIndex[i] = contents[startOfDefinitions + (i * 4)]

# Print the color definitions
# for i in range(colorsUsed[0]):
    # print hexlify(colorIndex[i])

# Make a string to hold the output of our script
arraySize = int((len(contents) - offset[0]) / 2)
outputString = "/* This was generated using the SparkFun BMPtoArray python script" + '\r'
outputString += " See https://github.com/sparkfun/BMPtoArray for more info */" + '\r\r'
outputString += "static const unsigned char myGraphic[" + str(
    arraySize) + "] PROGMEM = {" + '\r'

# Start coverting spots to values
# Start at the offset and go to the end of the file
for i in range(offset[0], fileSize[0], 2):
    colorCode1 = contents[i]
    actualColor1 = colorIndex[colorCode1]  # Look up this code in the table

    colorCode2 = contents[i + 1]
    actualColor2 = colorIndex[colorCode2]  # Look up this code in the table

    # Take two bytes, squeeze them to 4 bits
    # Then combine them into one byte
    compressedByte = (actualColor1 >> 4) | (actualColor2 & 0xF0)

    # Add this value to the string
    outputString += hex(compressedByte) + ", "

    # Break the array into a new line every 8 entries
    if i % 16 == 0:
        outputString += '\r'

# Once we've reached the end of our input string, pull the last two
# characters off (the last comma and space) since we don't need
# them. Top it off with a closing bracket and a semicolon.
outputString = outputString[:-2]
outputString += "};"

# Write the output string to our output file
outfile = open("output.txt", "w")
outfile.write(outputString)
outfile.close()

print("output.txt complete")
print("Copy and paste this array into a image.h or other header file")
