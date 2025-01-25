try:
    
    print("Introduce the limit of the prime numbers sequence: \n")
    
    data_enter = int(input("- "))

    if data_enter < 2:
    
        print("No prime numbers below 2.")
    
    else:
    
        prime_sequence = []

        for num in range(2, data_enter + 1):
    
            is_prime = True
    
            for divisor in range(2, int(num ** 0.5) + 1):
    
                if num % divisor == 0:
    
                    is_prime = False
    
                    break
            if is_prime:
    
                prime_sequence.append(num)

        print("Prime numbers sequence: ", prime_sequence)

except ValueError:
    
    print("You have not entered an integer number.")