def diagonal_difference(matrix):
    n=len(matrix)
    sum_main1=0
    sum_secondary1=0
    
    for i in range(n):
        sum_main1 += matrix[i][i]
        sum_secondary1 += matrix[i][n - 1 - i]
    return abs(sum_main1 - sum_secondary1)
#----------------------------------------------------
matrix_1 =[        
     [1,2,3],
     [4,5,6 ],
     [9,8,9]
    
    ]

#///////////////////////////
matrix_2 =[
    [11,2,4],
    [4,5,6],
    [10,8,-12]
    ]
print("Input 1 Result:" ,diagonal_difference(matrix_1))
print("Input 2 Result:" ,diagonal_difference(matrix_2))