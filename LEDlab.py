digits = [
    ["###", "# #", "# #", "# #", "###"],  # 0
    ["  #", "  #", "  #", "  #", "  #"],  # 1
    ["###", "  #", "###", "#  ", "###"],  # 2
    ["###", "  #", "###", "  #", "###"],  # 3
    ["# #", "# #", "###", "  #", "  #"],  # 4
    ["###", "#  ", "###", "  #", "###"],  # 5
    ["###", "#  ", "###", "# #", "###"],  # 6
    ["###", "  #", "  #", "  #", "  #"],  # 7
    ["###", "# #", "###", "# #", "###"],  # 8
    ["###", "# #", "###", "  #", "###"]   # 9
]

def print_number(num):
    num_str = str(num)
    lines = ["" for _ in range(5)]
    
    for digit in num_str:
        for i in range(5):
            lines[i] += digits[int(digit)][i] + "  "
    
    for line in lines:
        print(line)

if __name__ == "__main__":
    num = input("Enter a non-negative integer: ")
    if num.isdigit():
        print_number(num)
    else:
        print("Invalid input. Please enter a non-negative integer.")
