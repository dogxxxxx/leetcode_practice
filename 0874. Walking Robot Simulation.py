from typing import List
"""
Method 1:
Save obstacles into a set for quick search.
"""

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        result = 0
        index = 0
        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        x = 0
        y = 0
        obstacles_set = set(map(tuple, obstacles))

        for command in commands:
            if command == -1:
                index = (index + 1) % 4
            elif command == -2:
                index = (index - 1) % 4
            else:
                for i in range(command):
                    new_x = x + direction[index][0]
                    new_y = y + direction[index][1]
                    if (new_x, new_y) in obstacles_set:
                        break
                    x, y = new_x, new_y
                    result = max(result, x*x + y*y)
        return result
    

if __name__ == "__main__":
    commands = [4,-1,3]
    obstacles = []
    result = Solution().robotSim(commands=commands, obstacles=obstacles)
    print(result)
