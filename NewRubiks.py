import random
import timeit

face1 = [['G1','G2','G3'],['G4','G5','G6'],['G7','G8','G9']]
face2 = [['R1','R2','R3'],['R4','R5','R6'],['R7','R8','R9']]
face3 = [['B1','B2','B3'],['B4','B5','B6'],['B7','B8','B9']]
face4 = [['O1','O2','O3'],['O4','O5','O6'],['O7','O8','O9']]
face5 = [['W1','W2','W3'],['W4','W5','W6'],['W7','W8','W9']]
face6 = [['Y1','Y2','Y3'],['Y4','Y5','Y6'],['Y7','Y8','Y9']]


def original():
    face1 = (('G1','G2','G3'),('G4','G5','G6'),('G7','G8','G9'))
    face2 = (('R1','R2','R3'),('R4','R5','R6'),('R7','R8','R9'))
    face3 = (('B1','B2','B3'),('B4','B5','B6'),('B7','B8','B9'))
    face4 = (('O1','O2','O3'),('O4','O5','O6'),('O7','O8','O9'))
    face5 = (('W1','W2','W3'),('W4','W5','W6'),('W7','W8','W9'))
    face6 = (('Y1','Y2','Y3'),('Y4','Y5','Y6'),('Y7','Y8','Y9'))

    return face1, face2, face3, face4, face5, face6

loginData = {'user':'password'} #better to use file? Won't be able to save new users with dictionary?


#instead of directions: rotate clockwise for each face. User just enters face number.
def face1Rotation(direction):
    #if direction == 'C':
        #face 2 changes: first column
        #face 3 changes: first row to last column, middle row to middle column and last row to first column
        #face 4 changes: last column
        #face 5 changes: first column
        #face 6 changes: first column
    #if direction == 'AC':
        #face 1 changes: first row to first column, second row to second column, third row to third column
        #face 2 changes: first column e.g. yellow
        #face 3 changes: no changes 
        #face 4 changes: last column e.g. white
        #face 5 changes: first column e.g. red
        #face 6 changes: first column e.g. orange

    #temp variables - columns
    #face1 
    G1 = face1[0][0]
    G2 = face1[0][1]
    G3 = face1[0][2]
    G4 = face1[1][0]
    G5 = face1[1][1]
    G6 = face1[1][2]
    G7 = face1[2][0]
    G8 = face1[2][1]
    G9 = face1[2][2]
    
    #first column
    temp1F2 = face2[0][0]
    temp2F2 = face2[1][0]
    temp3F2 = face2[2][0]
    #last column
    temp1F4 = face4[0][2]
    temp2F4 = face4[1][2]
    temp3F4 = face4[2][2]
    #first column
    temp1F5 = face5[0][0]
    temp2F5 = face5[1][0]
    temp3F5 = face5[2][0]
    #first column
    temp1F6 = face6[0][0]
    temp2F6 = face6[1][0]
    temp3F6 = face6[2][0]
    
    if direction == 'C':
        #change R1,R4,R7 e.g.
        #swap R1, R4, R7 with W1,W4,W7 using index positions
        
        #changes to face 1
        face1[0][2] = G1
        face1[1][2] = G2
        face1[2][2] = G3

        face1[0][1] = G4
        face1[1][1] = G5
        face1[2][1] = G6

        face1[0][0] = G7
        face1[1][0] = G8
        face1[2][0] = G9
        
        #changes to face 2
        face2[0][0] = face5[0][0]
        face2[1][0] = face5[1][0]
        face2[2][0] = face5[2][0]

        #changes to face 4
        face4[0][2] = face6[0][0]
        face4[1][2] = face6[1][0]
        face4[2][2] = face6[2][0]
        
        #changes to face 5
        face5[0][0] = temp1F4
        face5[1][0] = temp2F4
        face5[2][0] = temp3F4

        #changes to face 6
        face6[0][0] = temp1F2
        face6[1][0] = temp2F2
        face6[2][0] = temp3F2

        updatedNet(face1,face2,face3,face4,face5,face6) #how to keep this changed list consistent for all?
        
    if direction == 'AC':
        #changes to face 1
        face1[0][2] = G9
        face1[1][2] = G8
        face1[2][2] = G7

        face1[0][1] = G6
        face1[1][1] = G5
        face1[2][1] = G4

        face1[0][0] = G3
        face1[1][0] = G2
        face1[2][0] = G1
        
        #changes to face 2
        face2[0][0] = temp1F6
        face2[1][0] = temp2F6
        face2[2][0] = temp3F6

        #changes to face 4
        face4[0][2] = temp1F5
        face4[1][2] = temp2F5
        face4[2][2] = temp3F5

        #changes to face 5
        face5[0][0] = temp1F2
        face5[1][0] = temp2F2
        face5[2][0] = temp3F2

        #changes to face 6
        face6[0][0] = temp1F4
        face6[1][0] = temp2F4
        face6[2][0] = temp3F4

        updatedNet(face1,face2,face3,face4,face5,face6)
               
        
def face2Rotation(direction):
    #if direction == 'C':
        #face 1 changes: last column e.g. yellow
        #face 2 changes: first row to last column, middle row to middle column and last row to first column
        #face 3 changes: first column e.g. white
        #face 4 changes: no changes
        #face 5 changes: last row e.g. green
        #face 6 changes: first row e.g. blue
    #if direction == 'AC':
        #face 1 changes: last column e.g. white
        #face 2 changes: first row to first column, second row to second column, third row to third column
        #face 3 changes: first column e.g. yellow
        #face 4 changes: no changes
        #face 5 changes: last row e.g. blue
        #face 6 changes: first row e.g. green

    #temp variables:
    #face1 
    R1 = face2[0][0]
    R2 = face2[0][1]
    R3 = face2[0][2]
    R4 = face2[1][0]
    R5 = face2[1][1]
    R6 = face2[1][2]
    R7 = face2[2][0]
    R8 = face2[2][1]
    R9 = face2[2][2]
    #last column
    temp1F1 = face1[0][2]
    temp2F1 = face1[1][2]
    temp3F1 = face1[2][2]
    #first column
    temp1F3 = face3[0][0]
    temp2F3 = face3[1][0]
    temp3F3 = face3[2][0]
    #last row
    temp1F5 = face5[2][0]
    temp2F5 = face5[2][1]
    temp3F5 = face5[2][2]
    #first row
    temp1F6 = face6[0][0]
    temp2F6 = face6[0][1]
    temp3F6 = face6[0][2]
    
    if direction == 'C':
        #changes to face 1:
        face1[0][2] = temp1F6
        face1[1][2] = temp2F6
        face1[2][2] = temp3F6

        #changes to face 2
        face2[0][2] = R1
        face2[1][2] = R2
        face2[2][2] = R3

        face2[0][1] = R4
        face2[1][1] = R5
        face2[2][1] = R6

        face2[0][0] = R7
        face2[1][0] = R8
        face2[2][0] = R9
        
        #changes to face 3:
        face3[0][0] = temp1F5
        face3[1][0] = temp2F5
        face3[2][0] = temp3F5

        #changes to face 5:
        face5[2][0] = temp1F1
        face5[2][1] = temp2F1
        face5[2][2] = temp3F1

        #changes to face 6:
        face6[0][0] = temp1F3
        face6[0][1] = temp2F3
        face6[0][2] = temp3F3
        
        updatedNet(face1,face2,face3,face4,face5,face6)

    if direction == 'AC':
        #changes to face 1:
        face1[0][2] = temp1F5
        face1[1][2] = temp2F5
        face1[2][2] = temp3F5
        
        #changes to face 2:
        face2[0][2] = R9
        face2[1][2] = R8
        face2[2][2] = R7
        
        face2[0][1] = R6
        face2[1][1] = R5
        face2[2][1] = R4

        face2[0][0] = R3
        face2[1][0] = R2
        face2[2][0] = R1

        #changes to face 3:
        face3[0][0] = temp1F6
        face3[1][0] = temp2F6
        face3[2][0] = temp3F6

        #changes to face 5:
        face5[2][0] = temp1F3
        face5[2][1] = temp2F3
        face5[2][2] = temp3F3
        
        #changes to face 6:
        face6[0][0] = temp1F1
        face6[0][1] = temp2F1
        face6[0][2] = temp3F1
        
        updatedNet(face1,face2,face3,face4,face5,face6)
    
def face3Rotation(direction):
    #if direction == 'C':
        #face 1 changes: no changes
        #face 2 changes: last column e.g. yellow
        #face 3 changes: first row to last column, middle row to middle column and last row to first column
        #face 4 changes: last column e.g. white
        #face 5 changes: last column e.g. red
        #face 6 changes: last column e.g. orange    
    #if direction == 'AC':
        #face 1 changes: no changes
        #face 2 changes: last column e.g. white
        #face 3 changes: first row to first column, second row to second column, third row to third column
        #face 4 changes: last column e.g. yellow
        #face 5 changes: last column e.g. orange
        #face 6 changes: last column e.g. red    

    #temporary variables:
    #face 3
    B1 = face3[0][0]
    B2 = face3[0][1]
    B3 = face3[0][2]
    B4 = face3[1][0]
    B5 = face3[1][1]
    B6 = face3[1][2]
    B7 = face3[2][0]
    B8 = face3[2][1]
    B9 = face3[2][2]
    #last column
    temp1F2 = face2[0][2]
    temp2F2 = face2[1][2]
    temp3F2 = face2[2][2]
    #first column
    temp1F4 = face4[0][0]
    temp2F4 = face4[1][0]
    temp3F4 = face4[2][0]
    #last column
    temp1F5 = face5[0][2]
    temp2F5 = face5[1][2]
    temp3F5 = face5[2][2]
    #last column
    temp1F6 = face6[0][2]
    temp2F6 = face6[1][2]
    temp3F6 = face6[2][2]
    
    if direction == 'C':
        #changes to face 2:
        face2[0][2] = temp1F6
        face2[1][2] = temp2F6
        face2[2][2] = temp3F6

        #changes to face 3
        face3[0][2] = B1
        face3[1][2] = B2
        face3[2][2] = B3

        face3[0][1] = B4
        face3[1][1] = B5
        face3[2][1] = B6

        face3[0][0] = B7
        face3[1][0] = B8
        face3[2][0] = B9

        #changes to face 4:
        face4[0][0] = temp1F5
        face4[1][0] = temp2F5
        face4[2][0] = temp3F5

        #changes to face 5:
        face5[0][2] = temp1F2
        face5[1][2] = temp2F2
        face5[2][2] = temp3F2

        #changes to face 6:
        face6[0][2] = temp1F4
        face6[1][2] = temp2F4
        face6[2][2] = temp3F4

        updatedNet(face1,face2,face3,face4,face5,face6)

    if direction == 'AC':
        #changes to face 2:
        face2[0][2] = temp1F5
        face2[1][2] = temp2F5
        face2[2][2] = temp3F5
        
        #changes to face 3:
        face3[0][2] = B9
        face3[1][2] = B8
        face3[2][2] = B7

        face3[0][1] = B6
        face3[1][1] = B5
        face3[2][1] = B4

        face3[0][0] = B3
        face3[1][0] = B2
        face3[2][0] = B1

        #changes to face 4:
        face4[0][0] = temp1F6
        face4[1][0] = temp2F6
        face4[2][0] = temp3F6

        #changes to face 5:
        face5[0][2] = temp1F4
        face5[1][2] = temp2F4
        face5[2][2] = temp3F4

        #changes to face 6:
        face6[0][2] = temp1F2
        face6[1][2] = temp2F2
        face6[2][2] = temp3F2

        updatedNet(face1,face2,face3,face4,face5,face6)
        
def face4Rotation(direction):
    #if direction == 'C':
        #face 1 changes: first column e.g. white
        #face 2 changes: no changes
        #face 3 changes: last column e.g. yellow
        #face 4: first row to last column, middle row to middle column and last row to first column
        #face 5 changes: first row e.g. blue
        #face 6 changes: last row e.g. green    
    #if direction == 'AC':
        #face 1 changes: first column e.g. yellow
        #face 2 changes: no changes
        #face 3 changes: last column e.g. white
        #face 4 changes: first row to first column, second row to second column, third row to third column
        #face 5 changes: first row e.g. green
        #face 6 changes: last row e.g. blue   

    #temp  variables:
    #face 4
    O1 = face4[0][0]
    O2 = face4[0][1]
    O3 = face4[0][2]
    O4 = face4[1][0]
    O5 = face4[1][1]
    O6 = face4[1][2]
    O7 = face4[2][0]
    O8 = face4[2][1]
    O9 = face4[2][2]
    #first column
    temp1F1 = face1[0][0]
    temp2F1 = face1[1][0]
    temp3F1 = face1[2][0]
    #last column
    temp1F3 = face3[0][2]
    temp2F3 = face3[1][2]
    temp3F3 = face3[2][2]
    #first row
    temp1F5 = face5[0][0]
    temp2F5 = face5[0][1]
    temp3F5 = face5[0][2]
    #last row
    temp1F6 = face6[2][0]
    temp2F6 = face6[2][1]
    temp3F6 = face6[2][2]

    if direction == 'C':
        #changes to face 1:
        face1[0][0] = temp1F5 
        face1[1][0] = temp2F5
        face1[2][0] = temp3F5

        #changes to face 3:
        face3[0][2] = temp1F6
        face3[1][2] = temp2F6
        face3[2][2] = temp3F6

        #changes to face 4
        face4[0][2] = O1
        face4[1][2] = O2
        face4[2][2] = O3
        
        face4[0][1] = O4
        face4[1][1] = O5
        face4[2][1] = O6

        face4[0][0] = O7
        face4[1][0] = O8
        face4[2][0] = O9

        #changes to face 5:
        face5[0][0] = temp1F3
        face5[0][1] = temp2F3
        face5[0][2] = temp3F3

        #changes to face 6:
        face6[2][0] = temp1F1
        face6[2][1] = temp2F1
        face6[2][2] = temp3F1

        updatedNet(face1,face2,face3,face4,face5,face6)

    if direction == 'AC':
        #changes to face 1
        face1[0][0] = temp1F6 
        face1[1][0] = temp2F6
        face1[2][0] = temp3F6

        #changes to face 3:
        face3[0][2] = temp1F5
        face3[1][2] = temp2F5
        face3[2][2] = temp3F5

        #changes to face 4
        face4[0][2] = O9
        face4[1][2] = O8
        face4[2][2] = O7

        face4[0][1] = O6
        face4[1][1] = O5
        face4[2][1] = O4
        
        face4[0][0] = O3
        face4[1][0] = O2
        face4[2][0] = O1
        
        #changes to face 5:
        face5[0][0] = temp1F1
        face5[0][1] = temp2F1
        face5[0][2] = temp3F1

        #changes to face 6:
        face6[2][0] = temp1F3
        face6[2][1] = temp2F3
        face6[2][2] = temp3F3

        updatedNet(face1,face2,face3,face4,face5,face6)
                
                
def face5Rotation(direction):
    #if direction == 'C':
        #face 1 changes: first row e.g. red
        #face 2 changes: first row e.g. blue
        #face 3 changes: first row e.g. orange
        #face 4 changes: first row e.g. green
        #face 5 changes: first row to last column, middle row to middle column and last row to first column
        #face 6 changes: no changes  
    #if direction == 'AC':
        #face 1 changes: first row e.g. orange
        #face 2 changes: first row e.g. green
        #face 3 changes: first row e.g. red
        #face 4 changes: first row e.g. blue
        #face 5 changes: first row to first column, second row to second column, third row to third column
        #face 6 changes: no changes  

    #temp variables:
    #face 5
    W1 = face5[0][0]
    W2 = face5[0][1]
    W3 = face5[0][2]
    W4 = face5[1][0]
    W5 = face5[1][1]
    W6 = face5[1][2]
    W7 = face5[2][0]
    W8 = face5[2][1]
    W9 = face5[2][2]
    #first row
    temp1F1 = face1[0][0]
    temp2F1 = face1[0][1]
    temp3F1 = face1[0][2]
    #first row
    temp1F2 = face2[0][0]
    temp2F2 = face2[0][1]
    temp3F2 = face2[0][2]
    #first row
    temp1F3 = face3[0][0]
    temp2F3 = face3[0][1]
    temp3F3 = face3[0][2]
    #first row
    temp1F4 = face4[0][0]
    temp2F4 = face4[0][1]
    temp3F4 = face4[0][2]    

    if direction == 'C':
        #changes to face 1:
        face1[0][0] = temp1F2
        face1[0][1] = temp2F2
        face1[0][2] = temp3F2

        #changes to face 2:
        face2[0][0] = temp1F3
        face2[0][1] = temp2F3
        face2[0][2] = temp3F3

        #changes to face 3:
        face3[0][0] = temp1F4
        face3[0][1] = temp2F4
        face3[0][2] = temp3F4

        #changes to face 4:
        face4[0][0] = temp1F1
        face4[0][1] = temp2F1
        face4[0][2] = temp3F1

        #changes to face 5
        face5[0][2] = W1
        face5[1][2] = W2
        face5[2][2] = W3
        
        face5[0][1] = W4
        face5[1][1] = W5
        face5[2][1] = W6

        face5[0][0] = W7
        face5[1][0] = W8
        face5[2][0] = W9


        updatedNet(face1,face2,face3,face4,face5,face6)

    if direction == 'AC':
        #changes to face 1:
        face1[0][0] = temp1F4
        face1[0][1] = temp2F4
        face1[0][2] = temp3F4

        #changes to face 2:
        face2[0][0] = temp1F1
        face2[0][1] = temp2F1
        face2[0][2] = temp3F1

        #changes to face 3:
        face3[0][0] = temp1F2
        face3[0][1] = temp2F2
        face3[0][2] = temp3F2

        #changes to face 4:
        face4[0][0] = temp1F3
        face4[0][1] = temp2F3
        face4[0][2] = temp3F3

        #changes to face 5
        face5[0][2] = W9
        face5[1][2] = W8
        face5[2][2] = W7

        face5[0][1] = W6
        face5[1][1] = W5
        face5[2][1] = W4

        face5[0][0] = W3
        face5[1][0] = W2
        face5[2][0] = W1
        
        updatedNet(face1,face2,face3,face4,face5,face6)        
        
    
def face6Rotation(direction):
    #if direction == 'C':
        #face 1 changes: last row e.g. orange
        #face 2 changes: last row e.g. green
        #face 3 changes: last row e.g. red
        #face 4 changes: last row e.g. blue
        #face 5 changes: no changes
        #face 6 changes: first row to last column, middle row to middle column and last row to first column
    #if direction == 'AC':
        #face 1 changes: last row e.g. red
        #face 2 changes: last row e.g. blue
        #face 3 changes: last row e.g. orange
        #face 4 changes: last row e.g. green
        #face 5 changes: no changes
        #face 6 changes: first row to first column, second row to second column, third row to third column
    
    #temp variables:
    #face 6
    Y1 = face6[0][0]
    Y2 = face6[0][1]
    Y3 = face6[0][2]
    Y4 = face6[1][0]
    Y5 = face6[1][1]
    Y6 = face6[1][2]
    Y7 = face6[2][0]
    Y8 = face6[2][1]
    Y9 = face6[2][2]
    #last row
    temp1F1 = face1[2][0]
    temp2F1 = face1[2][1]
    temp3F1 = face1[2][2]
    #last row
    temp1F2 = face2[2][0]
    temp2F2 = face2[2][1]
    temp3F2 = face2[2][2]
    #last row
    temp1F3 = face3[2][0]
    temp2F3 = face3[2][1]
    temp3F3 = face3[2][2]
    #last row
    temp1F4 = face4[2][0]
    temp2F4 = face4[2][1]
    temp3F4 = face4[2][2]
    
    if direction == 'C':
        #changes to face 1:
        face1[2][0] = temp1F4
        face1[2][1] = temp2F4
        face1[2][2] = temp3F4

        #changes to face 2:
        face2[2][0] = temp1F1
        face2[2][1] = temp2F1
        face2[2][2] = temp3F1

        #changes to face 3:
        face3[2][0] = temp1F2
        face3[2][1] = temp2F2
        face3[2][2] = temp3F2

        #changes to face 4:
        face4[2][0] = temp1F3
        face4[2][1] = temp2F3
        face4[2][2] = temp3F3

        #changes to face 6
        face6[0][2] = Y1
        face6[1][2] = Y2
        face6[2][2] = Y3
        
        face6[0][1] = Y4
        face6[1][1] = Y5
        face6[2][1] = Y6

        face6[0][0] = Y7
        face6[1][0] = Y8
        face6[2][0] = Y9

        updatedNet(face1,face2,face3,face4,face5,face6)

    if direction == 'AC':
        #changes to face 1:
        face1[2][0] = temp1F2
        face1[2][1] = temp2F2
        face1[2][2] = temp3F2

        #changes to face 2:
        face2[2][0] = temp1F3
        face2[2][1] = temp2F3
        face2[2][2] = temp3F3

        #changes to face 3:
        face3[2][0] = temp1F4
        face3[2][1] = temp2F4
        face3[2][2] = temp3F4

        #changes to face 4:
        face4[2][0] = temp1F1
        face4[2][1] = temp2F1
        face4[2][2] = temp3F1
        
        #changes to face 6
        face6[0][2] = Y9
        face6[1][2] = Y8
        face6[2][2] = Y7

        face6[0][1] = Y6
        face6[1][1] = Y5
        face6[2][1] = Y4

        face6[0][0] = Y3
        face6[1][0] = Y2
        face6[2][0] = Y1

        updatedNet(face1,face2,face3,face4,face5,face6)        

    
def shuffle():
    #cannot shuffle: middle (G5, R5, B5, O5, W5, Y5) always stays the same - squares surrounding it can change;
    #shuffle: rows and columns with the ones in other faces
    #after shuffling, updatedNet()?
##    shuffle = random.shuffle(face1) - doesn't work
##    print(shuffle)

    #unravel lists into one big list, shuffle and then re-structure them?

    data = []
    for record in face1:
        for i in record:
            data.append(i)
    for record in face2:
        for i in record:
            data.append(i)

##    reordered = []
##    for record in data:
##        new = data.random()
##        reordred.append(new)
##
##    print(reordered)

    #list of rotations - use random generator to 'randomly' shuffle?
    rotations = [face1[0],face1[2],[face1[0][0],face1[1][0],face1[2][0]], [face1[0][2],face1[1][2], face1[2][2]],
                 face2[0],face2[2],[face2[0][0],face2[1][0],face2[2][0]], [face2[0][2],face2[1][2], face2[2][2]],
                 face3[0],face3[2],[face3[0][0],face3[1][0],face3[2][0]], [face3[0][2],face3[1][2], face3[2][2]],
                 face4[0],face4[2],[face4[0][0],face4[1][0],face4[2][0]], [face4[0][2],face4[1][2], face4[2][2]],
                 face5[0],face5[2],[face5[0][0],face5[1][0],face5[2][0]], [face5[0][2],face5[1][2], face5[2][2]],
                 face6[0],face6[2],[face6[0][0],face6[1][0],face6[2][0]], [face6[0][2],face6[1][2], face6[2][2]]]

    #not face[1] as middle cube has to stay the same
        
    
    pass


def solveCube():
    shuffle()
    #display shuffled cube and use this for the rotations - not the temp variables at start

    #start and stop timer when done etc (for leaderboard)
    while checkSolved() is False:
##        print('Enter x to go back to main menu')
        face = input('\nEnter face number: ')
        direction = input('Enter direction: ')
        direction = direction.upper()

        while face not in '123456':
            print('Invalid input. Please try again.')
            face = input('Enter face number: ')
        while direction not in ['C','AC']:
            direction = input('Enter direction: ')
            direction = direction.upper()

        if face == '1':
            face1Rotation(direction)
        if face == '2':
            face2Rotation(direction)
        if face == '3':
            face3Rotation(direction)
        if face == '4':
            face4Rotation(direction)
        if face == '5':
            face5Rotation(direction)
        if face == '6':
            face6Rotation(direction)
##        if face == 'x' or 'X':
##            break

    #exit loop option to go back to main menu

def undoMove():
    print('TIP: to undo a move, just enter the same face and change the direction to anti-clockwise')

def displayNet():
    print('\nINSTRUCTIONS')
    print('R = red \nB = blue \nO = orange \nG = green \nW = white \nY = yellow')
    print('Enter the face you want to rotate')
    print('Enter the direction of rotation (c for clockwise or ac for anti-clockwise)')
    print('For example, to rotate the red face clockwise, enter "2 c"\n')
    

    print('Here is the net:')

    
    net = [
        '            __________           ',
        '           |W1  W2  W3|          ',
        '           |          |          ',
        '           |W4  W5  W6|          ',
        '           |          |          ',
        '           |W7  W8  W9|          ',
        ' __________|__________|__________ __________ ',
        '|G1  G2  G3|R1  R2  R3|B1  B2  B3|O1  O2  O3|',
        '|          |          |          |          |',
        '|G4  G5  G6|R4  R5  R6|B4  B5  B6|O4  O5  O6|',
        '|          |          |          |          |',
        '|G7  G8  G9|R7  R8  R9|B7  B8  B9|O7  O8  O9|',
        '|__________|__________|__________|__________|',
        '           |Y1  Y2  Y3|          ',
        '           |          |          ',
        '           |Y4  Y5  Y6|          ',
        '           |          |          ',
        '           |Y7  Y8  Y9|          ',
        '           |__________|          ',
                                            ]

    for record in net:
        print(record)
    print('\n')

    net2 = [
        '            __________           ',
        '           |          |          ',
        '           |          |          ',
        '           |    5     |          ',
        '           |          |          ',
        '           |          |          ',
        ' __________|__________|__________ __________ ',
        '|          |          |          |          |',
        '|          |          |          |          |',
        '|     1    |    2     |     3    |     4    |',
        '|          |          |          |          |',
        '|          |          |          |          |',
        '|__________|__________|__________|__________|',
        '           |          |          ',
        '           |          |          ',
        '           |    6     |          ',
        '           |          |          ',
        '           |          |          ',
        '           |__________|          ',
                                            ]

    for record in net2:
        print(record)
    print('\n')         

def updatedNet(face1,face2,face3,face4,face5,face6):

        
    print(
    '             __________           \n',
    '           | {0} {1} {2} |          \n'.format(face5[0][0],face5[0][1],face5[0][2]),
    '           |          |          \n',
    '           | {0} {1} {2} |          \n'.format(face5[1][0],face5[1][1],face5[1][2]),
    '           |          |          \n',
    '           | {0} {1} {2} |          \n'.format(face5[2][0],face5[2][1],face5[2][2]),
    ' __________|__________|__________ __________ \n',
    '| {0} {1} {2} | {3} {4} {5} | {6} {7} {8} | {9} {10} {11} |\n'.format(face1[0][0],face1[0][1],face1[0][2],face2[0][0],face2[0][1],face2[0][2],face3[0][0],face3[0][1],face3[0][2],face4[0][0],face4[0][1],face4[0][2]),
    '|          |          |          |          |\n',
    '| {0} {1} {2} | {3} {4} {5} | {6} {7} {8} | {9} {10} {11} |\n'.format(face1[1][0],face1[1][1],face1[1][2],face2[1][0],face2[1][1],face2[1][2],face3[1][0],face3[1][1],face3[1][2],face4[1][0],face4[1][1],face4[1][2]),
    '|          |          |          |          |\n',
    '| {0} {1} {2} | {3} {4} {5} | {6} {7} {8} | {9} {10} {11} |\n'.format(face1[2][0],face1[2][1],face1[2][2],face2[2][0],face2[2][1],face2[2][2],face3[2][0],face3[2][1],face3[2][2],face4[2][0],face4[2][1],face4[2][2]),
    '|__________|__________|__________|__________|\n',
    '           | {0} {1} {2} |          \n'.format(face6[0][0],face6[0][1],face6[0][2]),
    '           |          |          \n',
    '           | {0} {1} {2} |          \n'.format(face6[1][0],face6[1][1],face6[1][2]),
    '           |          |          \n',
    '           | {0} {1} {2} |          \n'.format(face6[2][0],face6[2][1],face6[2][2]),
    '           |__________|          \n',
                                        )

    #show net with colours
    #replacement fields?
    


def checkSolved():

##    if face1 and face2 and face3 and face4 and face5 and face6 == original():
##        print('Congratulations! You have solved the Rubik\'s Cube')
##        return True
##    else:
##        print('Keep trying!')
    
    #tempFaces == faces
    #if solved - output congratulatory message, otherwise a motivating one etc.
    #return Boolean values
    return False


def login():
    existing = input('\nAre you an existing user (y or n)?: ') #validate
    existing = existing.lower()
    loggedIn = False
    while loggedIn == False:
        if existing == 'y':
            username = input('Enter username: ')
            password = input('Enter password: ')
            for user in loginData.keys():
                if username == user:
                    for passw in loginData.values():
                        if password == passw:
                            print('Login successful')
                            loggedIn = True
                        else:
                            print('Incorrect username or password')
                else:
                    print('Not an existing user')
        else:
            create = input('Create new account (y or n)?: ') #validate
            if create == 'y':
                username = input('Enter username: ')
                if username not in loginData.keys(): #need 2 add to dict
                    password = input('Enter password: ')
                    loggedIn = True
            else:
                pass
                         
def leaderboard():
    pass

def FiveMins():
    #start for 5 mins
    #solveCube
    #(WHILE LOOP) stop when 5 mins are up + output message

##    T = timeit.timeit(lambda:solveCube(),number = 1)
##    print(T)     
    pass

def TenMins():
    pass

def timedVersion():
    print('Enter 5 for 5 minutes to solve the cube')
    print('Enter 10 for 10 minutes to solve the cube')
    option = input('Enter time: ')
    while option not in ['5','10']:
        print('Please try again.')
        option = input('Enter time: ')

    if option == '5':
        FiveMins()

    if option == '10':
        TenMins()

def main():
    print('****** RUBIK\'S CUBE SIMULATION ******\n')
    print('MENU OPTIONS')
    print('1: Display Instructions')
    print('2: Start Solving')
    print('3: Login')
    print('4: Check Leaderboards')
    print('Q: Quit')

    run = True
    while run:
        menuOption = input('Enter Menu Option: ')
        menuOption = menuOption.upper()
        while menuOption not in '1234Q':
            print('Invalid option. Please try again.')
            menuOption = input('Enter Menu Option: ')
            menuOption = menuOption.upper()


        if menuOption == '1':
            displayNet()
        if menuOption == '2':
            print('\nEnter A for standard version')
            print('Enter B for timed version')
            option = input('Enter option: ')
            option = option.upper()
            while option not in 'AB':
                print('Invalid option. Please try again.')
                option = input('Enter option: ')
                option = option.upper()

            if option == 'A':
                solveCube()
            else:
                timedVersion()
    
            #shuffle cube
        if menuOption == '3':
            login()
            #if logged in, store time/score to username for leaderboard
        if menuOption == '4':
            pass
        if menuOption == 'Q':
            print('Quitting...')
            run = False
    
        
main()




















