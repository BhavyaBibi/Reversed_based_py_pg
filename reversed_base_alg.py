# first we want to create the algorithm for this programing

# this is an pyramid printing of star program is this

rows = int(input('Enter the number of rows:'))

for a in range(rows,0,-1):
    for b in range(rows-a):
        print(' ',end='')

    for b in range(2*a-1):
        print('*', end='')
    print()
    