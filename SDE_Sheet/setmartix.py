def setMatrix(matrix):
          Rows = len(matrix)             # To intialize Rows variable
          Columns = len(matrix[0])       # To intialize Columns variable
          row,column = set(),set()


          # for finding zeroes element in rowsand columns
          for i in range(Rows):
                    for j in range(Columns):
                              if matrix[i][j]==0:
                                        row.add(i)          # Adding index to set  of row
                                        column.add(j)       # Adding index to set  of column
          
          # for updating rows,columns to zeroes
          for i in range(Rows):
                    for j in range(Columns):
                              if i in row  or j in column:
                                        matrix[i][j] = 0

          print( matrix )

mat=[[1,1,1,1],[1,0,1,0],[1,1,1,1]]       
setMatrix(mat)                                  
