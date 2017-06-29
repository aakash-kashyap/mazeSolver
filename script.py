import numpy as np
import cv2

## The readImage function takes a file path as argument and returns image in binary form.
def readImage(filePath):
    #############  Add your Code here   ###############
    img = cv2.imread(filePath)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret,binaryImage = cv2.threshold(gray,200,255,0)
##    cv2.imshow('Binary Image',binaryImage)
    ###################################################
    return binaryImage

## The findNeighbours function takes a maze image and row and column coordinates of a cell as input arguments
## and returns a stack consisting of all the neighbours of the cell as output.
## Note :- Neighbour refers to all the adjacent cells one can traverse to from that cell provided only horizontal
## and vertical traversal is allowed.
def findNeighbours(img,row,column):
    neighbours = []
    #############  Add your Code here   ###############
    h,w = img.shape
    i=(len(img)/20)    
    sImg = img[row*(h/i) : (row*(h/i))+(h/i) , column*(w/i) :(column*(w/i))+(w/i)]
## coordinates to check open sides of the cell in all directions(north,south,east,west)
    ny=0
    nx=10
    ey= 10
    ex=19
    sy=19
    sx=10
    wy=10
    wx=0

    if(sImg[ny,nx] !=0):
        ##print "north"
        temp=(row-1,column)
        neighbours.append(temp)
             
    if(sImg[ey,ex] !=0):
        ##print "east"
        temp=(row,column+1)
        neighbours.append(temp)

    if(sImg[sy,sx] !=0):
        ##print "south"
        temp=(row+1,column)
        neighbours.append(temp)
        
    if(sImg[wy,wx] !=0):
        ##print "west"
        temp=(row,column-1)
        neighbours.append(temp)
    ###################################################
    return neighbours

##  colourCell function takes 4 arguments:-
##            img - input image
##            row - row coordinates of cell to be coloured
##            column - column coordinates of cell to be coloured
##            colourVal - the intensity of the colour.
##  colourCell basically highlights the given cell by painting it with the given colourVal. Care should be taken that
##  the function doesn't paint over the black walls and only paints the empty spaces. This function returns the image
##  with the painted cell.
def colourCell(img,row,column,colourVal):
    #############  Add your Code here   ###############
    h,w = img.shape
    i=(len(img)/20)        
    ret,thresh1 = cv2.threshold(img[row*(h/i):(row*(h/i))+h/i,column*(w/i) :(column*(w/i))+w/i ],0,colourVal,cv2.THRESH_BINARY)
    img[row*(h/i):(row*(h/i))+h/i,column*(w/i) :(column*(w/i))+w/i ]=thresh1 

    ###################################################
    return img

##  Main function takes the filepath of image as input.
##  You are not allowed to change any code in this function.
def main(filePath):
    img = readImage(filePath)
    coords = [(0,0),(9,9),(3,2),(4,7),(8,6)]
    string = ""
    for coordinate in coords:
        img = colourCell(img, coordinate[0], coordinate[1], 150)
        neighbours = findNeighbours(img, coordinate[0], coordinate[1])
        print neighbours
        string = string + str(neighbours) + "\n"
        for k in neighbours:
            img = colourCell(img, k[0], k[1], 230)
    if __name__ == '__main__':
        return img
    else:
        return string + "\t"
## Specify filepath of image here. The main function is called in this section.
if __name__ == '__main__':
    filePath = 'testMazes/maze06.jpg'
    img = main(filePath)
    cv2.imshow('canvas', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
