
# the smallest part of the problem is:
# finding places along the guard path
# , where one can turn right 90 degrees, and you hit an obstacle on the same face as in the normal path
# ie an X then an obstacle

# guard move
# at each square, check the 90 degree offshoot clockwise
# for index in row (or column) check if current index is an X and next is an #
# if so current square is a potential blocker position, add 1 to count

from src.day_6.task_one import GuardMap




def main():
    pass

if __name__ == '__main__':
    main()