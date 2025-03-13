import math


def prime(num):
    if num <= 1:
        return
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return
    return True


def sum_of_prime(start, end):
    return sum(num for num in range(start, end + 1) if prime(num))


def length_converter(value, direction):
    if direction.upper() == 'M':
        return round(value * 3.28084, 2)
    elif direction.upper() == 'F':
        return round(value / 3.28084, 2)
    else:
        raise ValueError("Direction must be 'M' or 'F'")


def consonant_count(text):
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    return sum(1 for char in text if char in consonants)


def min_max_finder(numbers):
    if not numbers:
        raise ValueError("No numbers provided")
    return min(numbers), max(numbers)


def palindrome(text):
    clean_text = ''.join(char.lower() for char in text if char.isalnum())
    return clean_text == clean_text[::-1]


def word_counter(file_path, words):
    counts = {word: 0 for word in words}
    try:
        with open(file_path, 'r') as file:
            text = file.read().lower()
            for word in words:
                counts[word] = text.count(word.lower())
    except FileNotFoundError:
        raise FileNotFoundError("The file was not found")
    return counts


def main():
    while True:
        print("\nMenu:")
        print("1. Prime number sum calcalutor")
        print("2. Length conversion")
        print("3. Consonant counter")
        print("4. Min-max finder")
        print("5. Check for palindrome")
        print("6. Word counter")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            start = int(input("Enter start of range: "))
            end = int(input("Enter end of range: "))
            result = sum_of_prime(start, end)
            print(f"sum of prime numbers between {start} and {end}: {result}")

        elif choice == '2':
            value = float(input("Enter the value: "))
            direction = input(
                "Enter conversion direction (M for meters to feet, F for feet to meters): ")
            result = length_converter(value, direction)
            print(f"Converted length: {result}")

        elif choice == '3':
            text = input("Enter a text: ")
            result = consonant_count(text)
            print(f"Number of consonants: {result}")

        elif choice == '4':
            numbers = list(
                map(float, input("Enter number seperated by a single space: ").split()))
            min_num, max_num = min_max_finder(numbers)
            print(f"Smallest: {min_num}, Largest: {max_num}")

        elif choice == '5':
            text = input("Enter a text: ")
            result = palindrome(text)
            print(f"Palindrome: {result}")

        elif choice == '6':
            file_path = input("Enter the path to the text file: ")
            words = ["the", "was", "and"]
            try:
                counts = word_counter(file_path, words)
                for word, count in counts.items():
                    print(f"'{word}' count: {count}")
            except FileNotFoundError as e:
                print(e)

        elif choice == '7':
            print("Exiting the program")
            break

        else:
            print("Invalid choice. Choose a number between 1 and 7 ")


if __name__ == "__main__":
    main()