# Day 5
# Problem: Online Shopping
# Platform: HackerRank
# Topic: Python Basics / Arithmetic & Conditional Statements
# Language: Python

# Input: Flipkart prices and discount
F1 = float(input())  # Original price
F2 = float(input())  # Discount %
F3 = float(input())  # Delivery charge

# Input: Snapdeal prices and discount
S1 = float(input())
S2 = float(input())
S3 = float(input())

# Input: Amazon prices and discount
A1 = float(input())
A2 = float(input())
A3 = float(input())

# Calculate final price for Flipkart
flipkart = F1 - (F1 * F2 / 100) + F3
flipkart = int(flipkart)

# Calculate final price for Snapdeal
snapdeal = S1 - (S1 * S2 / 100) + S3
snapdeal = int(snapdeal)

# Calculate final price for Amazon
amazon = A1 - (A1 * A2 / 100) + A3
amazon = int(amazon)

# Print final prices
print(f"In Flipkart: Rs.{flipkart}")
print(f"In Snapdeal: Rs.{snapdeal}")
print(f"In Amazon: Rs.{amazon}")

# Decide the best option
min_price = min(flipkart, snapdeal, amazon)

if min_price == flipkart:
    print("Choose Flipkart")
elif min_price == snapdeal:
    print("Choose Snapdeal")
else:
    print("Choose Amazon")
