rating = float(input())


def grade(r):
    if 2.00 <= r <= 2.99:
        return "Fail"
    elif 3.00 <= r <= 3.49:
        return "Poor"
    elif 3.50 <= r <= 4.49:
        return  "Good"
    elif 4.50 <= r <= 5.49:
        return "Very Good"
    elif 5.50 <= r <= 6.00:
        return "Excellent"


print(grade(rating))
