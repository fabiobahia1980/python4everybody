largest = None
smallest = None

while True:
    try:
        num = raw_input("Enter a number: ")
        # num = int(num) -> except before break not good :-/
        if num == "done" : break
        num = int(num)
        #print num
        if largest is None or num > 0:
            largest = num
        if smallest is None or num < smallest:
            smallest = num

    except:

        print "Invalid input"

print "Maximum is", largest
print "Minimum is", smallest
