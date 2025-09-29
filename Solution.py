#first we import the necessary libraries
from collections import Counter
import bs4
from bs4 import BeautifulSoup

#then we read the HTML file
with open("webpage.html", "r", encoding="utf-8") as file:
    content = file.read()
 
 #now we parse the HTML content   
parsed_content = BeautifulSoup(content, "html.parser")

data = {}
rows = parsed_content.find_all("tr")
for row in rows[1:]:
    cols = row.find_all("td")
    days = cols[0].text.strip()
    colors = cols[1].text.strip()
    data[days] = colors
    
# print(data), to see the extracted data, it has been commented out.
#why list? explain
all_colors = []
for days, colors in data.items():
    color_list = [color.strip() for color in colors.split(",")]
    #fixing spelling mistakes, which i noticed
    color_list = ["BLUE" if color in ["BLEW"] else color for color in color_list]
    color_list = ["ASH" if color in ["ARSH"] else color for color in color_list]
    all_colors.extend(color_list)
    
# print(all_colors) to comfirm if data is correct, it has been commented out.

from collections import Counter

#mean, mode, median, variance
counter = Counter(all_colors)
mean_color = counter.most_common(1)[0][0]
print("Mean Color:", mean_color)

most_worn = counter.most_common(1)[0]
print("Most Worn Color:", most_worn[0], "with", most_worn[1], "times")

sorted_colors = sorted(all_colors)
mid = len(sorted_colors) // 2
median_color = sorted_colors[mid]
print("Median Color:", median_color)

color_to_num = {c: i for i, c in enumerate(set(all_colors))}
nums = [color_to_num[c] for c in all_colors]

mean_val = sum(nums) / len(nums)
variance = sum((x - mean_val) ** 2 for x in nums) / len(nums)
print("Variance:", variance)


#probability of a color(red)
p_red = all_colors.count("RED") / len(all_colors)
print("Probability of RED:", p_red)

#code under this line is for recursion, binary to decimal conversion, and fibonacci sum, were attempted with the help of AI
def recursive_search(lst, target, i=0):
    if i >= len(lst):
        return -1
    if lst[i] == target:
        return i
    return recursive_search(lst, target, i+1)

print("Index of RED:", recursive_search(all_colors, "RED"))

import random
binary_str = "".join(random.choice("01") for _ in range(8))
decimal_val = int(binary_str, 2)
print("Binary:", binary_str, "Decimal:", decimal_val)

def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

n = 10
fib_sum = sum(fib(i) for i in range(n))
print(f"Sum of first {n} Fibonacci numbers:", fib_sum)
