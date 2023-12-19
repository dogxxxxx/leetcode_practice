from typing import List

"""
Method 1:
This method iterates through the image to calculate a smoothed version of it.

The time complexity is O(m*n), where m and n represent the number of rows and columns in the image, respectively.
The space complexity is O(m*n), as it requires a similar-sized structure to store the results.
"""


class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        rows = len(img)
        columns = len(img[0])
        result = [[None] * columns for _ in range(rows)]
        for i in range(rows):
            for j in range(columns):
                sums = 0
                count = 0
                for r in range(max(0, i - 1), min(rows, i + 2)):
                    for c in range(max(0, j - 1), min(columns, j + 2)):
                        sums += img[r][c]
                        count += 1
                result[i][j] = int(sums / count)
        return result


if __name__ == "__main__":
    sol = Solution()
    img = [[100, 200, 100], [200, 50, 200], [100, 200, 100]]
    result = sol.imageSmoother(img)
    print(result)
