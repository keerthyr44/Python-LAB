def count_even_odd(numbers):
    even_count=0
    odd_count=0

    for numbers in numbers:
        if numbers%2==0:
            even_count+=1
        else:
            odd_count+=1

    print(f"Even numbers:{even_count},Odd numbers:{odd_count}")

input_list=[1,2,3,4,5,6]
count_even_odd(input_list)
            
