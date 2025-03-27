import random

def generate_random_numbers(count, start, end):
    """Generate a list of random numbers."""
    return [random.randint(start, end) for _ in range(count)]

def calculate_average(numbers):
    """Calculate the average of a list of numbers."""
    return sum(numbers) / len(numbers) if numbers else 0

def find_max_and_min(numbers):
    """Find the maximum and minimum numbers in a list."""
    return max(numbers), min(numbers)

def main():
    random_numbers = generate_random_numbers(10, 1, 100)
    print("Random Numbers:", random_numbers)

    average = calculate_average(random_numbers)
    print("Average:", average)

    max_num, min_num = find_max_and_min(random_numbers)
    print("Maximum:", max_num)
    print("Minimum:", min_num)

if __name__ == "__main__":
    main()