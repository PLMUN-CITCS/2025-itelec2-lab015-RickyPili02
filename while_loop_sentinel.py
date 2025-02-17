total_sum = 0

while True:
    user_input = input("Enter a number (or 'stop' to finish): ")
    
    if user_input.strip().lower() == "stop":
        break 
    
    try:
        total_sum += float(user_input)
    except ValueError:
        print("Invalid input. Please enter a number.")

print("Total sum:", total_sum)