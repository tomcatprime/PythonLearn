Function Transformations
"Function transformation" is just a more concise way to describe a specific type of higher order function. It's when a function takes a function (or functions) as input and returns a new function. Let's look at an example:



def multiply(x, y):
    return x * y

def add(x, y):
    return x + y

# self_math is a higher order function
# input: a function that takes two arguments and returns a value
# output: a new function that takes one argument and returns a value
def self_math(math_func):
    def inner_func(x):
        return math_func(x, x)
    return inner_func

square_func = self_math(multiply)
double_func = self_math(add)

print(square_func(5))
# prints 25

print(double_func(5))
# prints 10

The self_math function takes a function that operates on two different parameters (e.g. multiply or add) and returns a new function that operates on one parameter twice (e.g. square or double).

Assignment
Doc2Doc needs a good logging system so that users and developers alike can see what's going on under the hood. Complete the get_logger function.

It takes a formatter function as a parameter and returns a new function. Steps:

Define a new function, logger, inside get_logger (see self_math above as an example). It accepts two strings. You can just name them first and second if you like.
The logger function should not return anything. It should simply print the result of calling the given formatter function with the first and second strings as arguments.
Return the new logger function for the test suite to use.
Tip
The colon_delimit and dash_delimit functions are "formatters" that will be passed into our get_logger function by the tests. You don't need to touch them, but it's important to understand that when you call formatter() in the get_logger function, you're calling one of these functions.


def get_logger(formatter):
    def logger(first, second):
        print(formatter(first, second))
    return logger


# Don't edit below this line


def test(first, errors, formatter):
    print("Logs:")
    logger = get_logger(formatter)
    for err in errors:
        logger(first, err)
    print("====================================")


def colon_delimit(first, second):
    return f"{first}: {second}"


def dash_delimit(first, second):
    return f"{first} - {second}"


def main():
    db_errors = [
        "out of memory",
        "cpu is pegged",
        "networking issue",
        "invalid syntax",
    ]
    test("Doc2Doc FATAL", db_errors, colon_delimit)

    mail_errors = [
        "email too large",
        "non alphanumeric symbols found",
    ]
    test("Doc2Doc WARNING", mail_errors, dash_delimit)


main()


Assignment
Complete the doc_format_checker_and_converter function.

It takes a conversion_function and a list of valid_formats as parameters. It should return a new function that takes two parameters of its own:

filename: The name of the file to be converted
content: The content (body text) of the file to be converted
If the file extension of the filename is in the valid_formats list, then it should return the result of calling the conversion_function on the content.
Otherwise, it should raise a ValueError with the message invalid file format.
Tip
I used the .split() method on the filename to get the file extension. You can use the in keyword to check if a value is in a list.

The capitalize_content and reverse_content are "conversion functions" that will be passed into our doc_format_checker_and_converter function by the tests.

def doc_format_checker_and_converter(conversion_function, valid_formats):
    def inner_func(filename, content):
        new_file = filename.split('.')[-1]
        if new_file in valid_formats:
            return conversion_function(content)
        else:
            raise ValueError('invalid file format')
    return inner_func
        


# Don't edit below this line


def capitalize_content(content):
    return content.upper()


def reverse_content(content):
    return content[::-1]

