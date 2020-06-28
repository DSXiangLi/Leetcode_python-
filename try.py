pascal = [1]
for i in range( 1, 3 ):
    print(pascal)
    pascal = [sum( pair ) for pair in zip( [0] + pascal, pascal + [0] )]
