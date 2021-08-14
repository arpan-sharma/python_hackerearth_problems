


# Q:- et's learn about list comprehensions! You are given three integers and representing the dimensions of a cuboid along with an integer . Print a list of all possible coordinates given by on a 3D grid where the sum of is not equal to . Here,

# . Please use list comprehensions rather than multiple loops, as a learning exercise.

# Example

# Sample Input 0

# 1
# 1
# 1
# 2

# Sample Output 0

# [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]




if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    print ([[a,b,c] for a in range(0,x+1) for b in range(0,y+1) for c in range(0,z+1) if a + b + c != n ])