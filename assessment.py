"""
## Question

In a university, your attendance determines whether you will be allowed to attend your graduation ceremony.
You are not allowed to miss classes for four or more consecutive days.
Your graduation ceremony is on the last day of the academic year, which is the Nth day.

Your task is to determine the following:

1. The number of ways to attend classes over N days.
2. The probability that you will miss your graduation ceremony.
Represent the solution in the string format as "Answer of (2) / Answer of (1)", don't actually divide or reduce the fraction to decimal

Test cases:
    for 5 days: 14/29
    for 10 days: 372/773



Logic Used:
    Taking N=5, there are 32 possible combinations (2^N combinations).
    The possible combinations are ['AAAAA', 'AAAAP', 'AAAPA', 'AAAPP', 'AAPAA', 'AAPAP', 'AAPPA', 'AAPPP',
                                   'APAAA', 'APAAP', 'APAPA', 'APAPP', 'APPAA', 'APPAP', 'APPPA', 'APPPP',
                                   'PAAAA', 'PAAAP', 'PAAPA', 'PAAPP', 'PAPAA', 'PAPAP', 'PAPPA', 'PAPPP',
                                   'PPAAA', 'PPAAP', 'PPAPA', 'PPAPP', 'PPPAA', 'PPPAP', 'PPPPA', 'PPPPP']

    Out of these combinations, due to the constraint that 4 classes can't be missed consecutively, 3 combinations has to be ruled out. ['AAAAA', 'AAAAP', 'PAAAA']
    So the number of ways of attending classes over N days is 32-3 = 29

    Out of the 29 combinations, in 14 combinations says that the kid is absent on the last day.

    So the probability of missing the graduation ceremony is 14/29.



Code Flow:
    The code takes in the total number of days (ie, value for N) and generates all the possible combinations in a tree generation manner.
    We save the leaf nodes values(combination of length N) to an array. The calculations of probability are based on the values of this array.

    We then check for 4 consecutive absent(AAAA) in the combinations and take the count the other combinations. This will be the total number of
    ways of attending classes inorder to be eligible for attending graduation ceremony. Out of this we will check for the count of combinations in
    which the kid is absent on the day of graduation ceremony.

    The ratio of these counts is the solution.

"""



def generate_tree(value, root=None):
    """
        Recursive method to generate the possible combinations of attending the class.
    """
    global eligible_days, not_possible_from_eligible, total_days

    if not root:
        root = value
    else:
        root = root + value

    if total_days == len(root):
        combination_arr.append(root)
        if 'AAAA' not in root:
            eligible_days += 1
            if root[-1] == 'A':
                not_possible_from_eligible += 1
    else:
        generate_tree('A', root)
        generate_tree('P', root)



if __name__ == '__main__':
    #Fetching total number of days
    total_days = ""
    while isinstance(total_days, str):
        try:
            total_days = int(input("Enter total days : "))
        except ValueError as e:
            print("Enter a valid number..!")

    combination_arr = []
    eligible_days = 0
    not_possible_from_eligible = 0

    #generating the possible N combinations
    generate_tree('A')
    generate_tree('P')

    print("Probability of missing the graduation ceremony is ", str(not_possible_from_eligible) + '/' + str(eligible_days))

