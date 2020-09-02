import math

book_count = int(input("How many books do you have in your basket? "))
book_prices = []
for i in range(0, book_count):
    book_prices.append(float(input("What is the price of the book number " + str(i + 1) + "? ")))


def total_price(prices):
    return math.fsum(prices)


print("a) Total price: $" + str(total_price(book_prices)))


def average_price(prices):
    return total_price(prices) / len(prices)


print("b) Average price: $" + str(average_price(book_prices)))


def least_expensive(prices):
    return min(prices)


print("c) Price of the least expensive book: $" + str(least_expensive(book_prices)))


def most_expensive(prices):
    return max(prices)


print("d) Price of the most expensive book: $" + str(most_expensive(book_prices)))


def count_cheaper(prices, threshold):
    count = 0
    for i in prices:
        if i < threshold: count += 1
    return count


print("e) Number of books cheaper than $" + str(10) + ": " + str(count_cheaper(book_prices, 10)))


def pct_cheaper(prices, threshold):
    count = 0
    for i in prices:
        if i < threshold: count += 1
    return count / len(prices) * 100


print("f) Percentage of books cheaper than $" + str(10) + ": " + str(pct_cheaper(book_prices, 10)) + "%")