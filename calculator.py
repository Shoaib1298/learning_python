def divide(x, y):
    return float(x / y)


if __name__ == "__main__":
    # x = float(input("give x : "))
    # y = float(input("give y : "))

    #! input function takes even a int as string.
    #  int(s) converts "ab" to ab where a and b are ints
    # * note the nesting of functions
    # * note that in this + is addition not concatination

    # z = round(x+y,3)
    # print(f"the sum is {x+y:,} and is rounded to {z:,}")

    # * funt(number[,ndigits]) means that ndigits is an optional arg.
    # * way to bring commas in the final number to make it more redable

    """
    --functions :

    -To define a function
        we use def (),
            -sequencal and inline arguments.
            -giving defalut arguments.
            #! I am not very confident in changing the predefined argument ex if name was predined as name ="world" and changing it
            #! in functions argument as name = "shoaib" or just "shoaib".
    -Top to bottom and left to right and from in to out
    -Start defining main() function
    -a function once called can do two thigs
        -have a side effect (avoid this side effects try to return, just to make testing easy)
        -return a value
    --Writing unit tests
     -Assert asserts that for assert boo that boo ==ture otherwise we get an assertion errror

    """

    x = int(input("give x"))
    y = int(input("give y"))
    print(divide(x, y))
