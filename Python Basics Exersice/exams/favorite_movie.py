film = ''
count = 1
best_sum = 0
best_movie = ''
while film !="STOP":
    movie_sum = 0
    name = film
    long = len(name)
    for i in name:
        movie_sum+=ord(i)
        if ord(i) > 64 and ord(i) < 91:
            movie_sum-=long
        elif ord(i)>96 and ord(i)<123:
            movie_sum-=long*2
    if best_sum<movie_sum:
        best_sum=movie_sum
        best_movie=name
    count+=1
    if count > 8:
        print("The limit is reached.")
        break
    film = input()
print("The best movie for you is %s with %d ASCII sum."%(best_movie,best_sum))
