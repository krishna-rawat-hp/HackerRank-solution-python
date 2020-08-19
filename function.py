# Write a python function

def is_leap(year):
    leap = False
    
    if year%100 ==0 and year%400 != 0:
        leap = False
    elif(year%4 == 0):
        leap = True
    
    return leap

if __name__ == '__main__':
	year = int(input())
	result = is_leap(year)
	print(result)