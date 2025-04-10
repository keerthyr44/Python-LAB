def sum_of_even_numbers(start,end):
    total_sum=0
    for num in range(start,end+1):
        if num%2==0:
            total_sum+=num
    return total_sum


start=int(input("Enter the start value:"))
end=int(input("Enter the end value:"))

result=sum_of_even_numbers(start,end)
print(f"The Sum of even numbers in the range[{start},{end}]is:{result}")
