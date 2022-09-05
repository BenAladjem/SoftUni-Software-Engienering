

import unittest

"""
    grid = [
        [1, 1, 2, 2, 2, 1, 1, 1],
        [1, 1, 2, 2, 2, 1, 0, 0],
        [0, 1, 1, 2, 2, 1, 1, 0],
        [0, 1, 1, 0, 2, 1, 0, 0],
        [0, 3, 3, 0, 0, 1, 2, 2],
        [0, 3, 0, 0, 3, 2, 2, 0],
        [0, 3, 3, 3, 3, 0, 0, 0],
    ]

This grid of integers represents countries. Each countries land is a contiguous
block of the same integer. The size of a country is the number of grid cells
contained within its border. 

Notes: 

Non-connected blocks of colour are separate countries
Diagonally adjacent blocks are not connected
"""
grid = [
        [1, 1, 2, 2, 2, 1, 1, 1],
        [1, 1, 2, 2, 2, 1, 0, 0],
        [0, 1, 1, 2, 2, 1, 1, 0],
        [0, 1, 1, 0, 2, 1, 0, 0],
        [0, 3, 3, 0, 0, 1, 2, 2],
        [0, 3, 0, 0, 3, 2, 2, 0],
        [0, 3, 3, 3, 3, 0, 0, 0],
    ]



def countries(grid):
    visited = []
    def one(row, col, m, t, visited, country):
        sell = []
        sell.append(row)
        sell.append(col)
        if row < 0 or row >= len(m) or col < 0 or col >= len(m[0]):
            return 0
        if m[row][col] != t:
            return 0
        if sell in visited:
            return 0
        visited.append(sell)
        country.append(sell)
        result = 1
        result += one(row - 1, col, m, t, visited, country)
        result += one(row + 1, col, m, t, visited, country)
        result += one(row, col - 1, m, t, visited, country)
        result += one(row, col + 1, m, t, visited, country)
        return result

    global name_country
    max_country = 0
    rows = len(grid)
    cols = len(grid[0])
    result = []

    country = []
    count = 0
    for r in range(rows):
        for c in range(cols):
            sell = []
            sell.append(r)
            sell.append(c)
            t = grid[r][c]
            x = 0
            if not sell in country:
                x = one(r, c, grid, t, visited, country)
                count +=1
            if max_country < x:
                max_country = x
                name_country = grid[r][c]
    result.append(count)
    result.append(name_country)
    return result




def count_countries(grid):
    return countries(grid)[0]

def largest_country(grid):
    return countries(grid)[-1]

print(count_countries(grid))
print(largest_country(grid))


class TestCountries(unittest.TestCase):
    def test_count_countries_with_one_country(self):
        self.assertEqual(count_countries([[0]]), 1)

    def test_count_countries_with_two_countries(self):
        self.assertEqual(
            count_countries(
                [[0, 0],
                 [1, 1]]
            ),
            2
        )

    def test_count_countries_diagonally_unconnected(self):
        self.assertEqual(
            count_countries(
                [[1, 0],
                 [0, 1]],
            ),
            4
        )

    def test_largest_country(self):
        self.assertEqual(
            largest_country(
                [[1, 1, 1, 1],
                 [1, 2 ,2, 2],
                 [1, 1, 1, 1],
                 [0, 0, 0, 0]]
            ),
            1
        )

if __name__ == '__main__':
    unittest.main()
