def multiplication_table(number):
    """
    Ex. multiplication_table(6) returns "6 12 18 24 30 36 42 48 54 60 66 72 "
    :param number: An integer
    :return: A string of 12 values representing the mulitiplication table of the parameter number.
    """
    list_of_numbers=""
    # the list of numbers will look like: 6, 12, 18, 24, etc if a 6 is passed into the function
    for x in range(1,2):
        multipled_number=str(x*number)
        list_of_numbers += multipled_number+""
    print("The concatenated list is", list_of_numbers)


if __name__ == '__main__':
    multiplication_table(12)
    # Make sure to delete this line when writing your function.