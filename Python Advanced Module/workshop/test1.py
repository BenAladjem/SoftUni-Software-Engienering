a =  [[1, 1, 1],
      [3, 4, 5],
      [6, 7, 8]]
# print(a.count(1))
# flag = False
# if a[0][0]==a[0][1]== a[0][2]:
#     flag = True
# print(flag)
# print(a[0][0])
# print(a[0][1])
# print(a[0][2])
#flag = False
def win_check(sign, matr):
    flag = False
    #[0, 0], [0, 1], [0, 2]
    if         (matr[0][0] == matr[0][1] == matr[0][2]) == sign\
            or (matr[1][0] == matr[1][1] == matr[1][2]) == sign\
            or (matr[2][0] == matr[2][1] == matr[2][2]) == sign\
            or (matr[0][0] == matr[1][0] == matr[2][0]) == sign\
            or (matr[0][1] == matr[1][1] == matr[2][1]) == sign\
            or (matr[0][2] == matr[1][2] == matr[2][2]) == sign\
            or (matr[0][0] == matr[1][1] == matr[2][2]) == sign\
            or (matr[0][2] == matr[1][1] == matr[2][0]) == sign:
        flag = True
    return flag

print(win_check(1,a))