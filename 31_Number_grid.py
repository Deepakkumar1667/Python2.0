import os 
os.system("")

BLACK = "\033[38;2;0;0;0m" 
BLACK_BG = "\033[48;2;0;0;0m"
GREEN = "\033[38;2;54;255;15m" 
RESET = "\033[0m"

FONT = {
    "0" : ["01110", "10001", "10011", "10101", "11001", "10001", "01110"],
    "1" : ["00100", "01100", "00100", "00100", "00100", "00100", "01110"],
    "2" : ["01110", "10001", "00001", "01110", "00100", "01000", "11111"],
    "3" : ["11110", "00001", "00001", "01110", "00001", "00001", "11110"],
    "4" : ["00010", "00110", "01010", "10010", "11111", "00010", "00010"],
    "5" : ["11111", "10000", "11110", "00001", "00001", "10001", "01110"],
    "6" : ["00110", "01000", "10000", "11110", "10001", "10001", "01110"],
    "7" : ["11111", "00001", "00010", "00100", "01000", "01000", "01000"],
    "8" : ["01110", "10001", "10001", "01110", "10001", "10001", "01110"],
    "9" : ["01110", "10001", "10001", "01111", "00001", "00010", "01100"]
}

SCALE = 3
ROWS = 28 
GAP = 2

def make_grid(number_str):
    n = len(number_str)
    total_w = n * 5 * SCALE + (n - 1 ) * GAP 
    cols = max(28, total_w + 8)
    left = (cols - total_w ) // 2
    top = (ROWS - 7 * SCALE) // 2 

    grid = [[0.0] * cols for _ in range(ROWS)]

    for i, ch in enumerate(number_str):
        x0 = left + i * (5 * SCALE + GAP)
        for r in range(7):
            for c in range(5):
                if FONT[ch][r][c] == "1":
                    for dr in range(SCALE):
                        for dc in range(SCALE):
                            grid[top + r * SCALE + dr][x0 + c * SCALE + dc] = 1.0

    return grid

def print_grid(grid):
    for row in grid:
        line = []
        for v in row:
            color = BLACK if v == 1.0 else GREEN

            line.append(f"{BLACK_BG}{color}{int(v)}{RESET}")

        print(" ".join(line))

while True:
    text = input("Enter your number: ")
    if text.isdigit() and 0 <= int(text) <= 100:
        break
    print("Wrong input!")

number_str = str(int(text))
print_grid(make_grid(number_str))