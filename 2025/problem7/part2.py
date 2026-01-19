from typing import List
from utils import FileIO as iO


def main():
    example = iO.parse('input.txt', {'separator': '\n'})
    return count_timelines_with_exits(example)


def count_timelines_with_exits(grid: List[str]) -> int:
    rows = len(grid)
    cols = len(grid[0])
    
    #Find S
    try:
        sc = grid[0].index('S')
    except IndexError:
        raise ValueError("Start 'S' not found in first row")

    curr = [0] * cols
    curr[sc] = 1
    exits = 0
    
    for r in range(rows):
        next_row = [0] * cols
        
        for c in range(cols):
            ways_here = curr[c]
            
            if ways_here == 0:
                continue
            
            cell = grid[r][c]
            
            if cell in ['.', 'S']:
                if r + 1 < rows:
                    next_row[c] = next_row[c] + ways_here
                else:
                    exits = exits + ways_here
            elif cell == '^':
                if r + 1 < rows:
                    if c - 1 >= 0:
                        next_row[c - 1] = next_row[c - 1] + ways_here
                    if c+ 1 < cols:
                        next_row[c + 1] = next_row[c + 1] + ways_here
                else:
                    if c - 1 >= 0:
                        exits = exits + ways_here
                    if c + 1 < cols:
                        exits = exits + ways_here
        curr = next_row
        print("   ".join([str(c) for c in curr]))
    
    return exits
    

if __name__ == '__main__':
    print(main())