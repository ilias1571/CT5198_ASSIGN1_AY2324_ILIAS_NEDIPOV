import math

def get_customer_counts(days):
    customer_count = []
    for day in range(1, days + 1):
        while True:
            try:
                customers = int(input(f"Enter the number of customers for day {day}: "))
                if customers < 0:
                    raise ValueError("Number of customers cannot be negative.")
                break
            except ValueError:
                print("Invalid input. Please enter a valid positive integer.")
        customer_count.append(customers)
    return customer_count

def calculate_statistics(customer_count):
    max_customers = max(customer_count)
    min_customers = min(customer_count)
    avg_customers = math.ceil(sum(customer_count) / len(customer_count))
    return max_customers, min_customers, avg_customers

def main():
    # Use the get_customer_counts function to get the list of customer counts
    customer_count = get_customer_counts(7)

    # Use the calculate_statistics function to determine max, min, and average
    max_customers, min_customers, avg_customers = calculate_statistics(customer_count)

    # Print the results
    print("\nResults:")
    print(f"Maximum number of customers: {max_customers}")
    print(f"Minimum number of customers: {min_customers}")
    print(f"Average number of customers: {avg_customers}")

    # Add this line to prevent the console window from closing immediately
    input("Press Enter to exit...")

if __name__ == "__main__":
    main()
