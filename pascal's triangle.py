lass Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle=[]
        #Making sure each row begins with 1
        for r in range(numRows):
            row=[1]
            #Filling the inner elements
            for c in range(1,r):
                left_above=triangle[r-1][c-1]
                right_above=triangle[r-1][c]
                row.append(left_above+right_above)

            if r>0:
                row.append(1)

            triangle.append(row)
        
        return triangle
            
