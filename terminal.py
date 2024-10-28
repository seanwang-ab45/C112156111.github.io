def calculate_sum(numbers):
    return sum(numbers)

if __name__ == "__main__":
    numbers = input("請輸入數字，以逗號分隔: ").split(',')
    numbers = [int(num) for num in numbers]
    total = calculate_sum(numbers)
    print(f"數字總和是: {total}")