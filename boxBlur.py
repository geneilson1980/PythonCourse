# Last night you partied a little too hard. Now there's a black and white photo of you that's about to go viral! You can't let this ruin your reputation, so you want to apply the box blur algorithm to the photo to hide its content.

# The pixels in the input image are represented as integers. The algorithm distorts the input image in the following way: Every pixel x in the output image has a value equal to the average value of the pixel values from the 3 × 3 square that has its center at x, including x itself. All the pixels on the border of x are then removed.

# Return the blurred image as an integer, with the fractions rounded down.

def boxBlur(image):
    sumValues = 0
    average = 0
    newList = []
    rowSize = len(image)-2
    colSize = len(image[0])
    ref = 1
    i = 0
    j = 0
    while i < rowSize:
        newList.append([])
        while j < colSize:
            a = image[i][j]
            b = image[i+1][j]
            c = image[i+2][j]
            sumValues = sumValues + image[i][j] + image[i+1][j] + image[i+2][j]
            if ref == 3:
                average = int(sumValues / 9)
                newList[i].append(average)
                ref = 1
                sumValues = 0
                if j == colSize -1:
                    break
                j = j -1
                continue
            else:
                ref += 1
            j += 1
        i += 1
        j = 0
    return newList

image = [[1,1,1], 
        [1,7,1], 
        [1,1,1]]

result = boxBlur(image)
print(result)