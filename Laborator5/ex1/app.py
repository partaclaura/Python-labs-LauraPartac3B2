# a) Write a module named utils.py that contains one function called process_item.
# The function will have one parameter, x, and will return the least prime number
# greater than x. When run, the module will request an input from the user, convert
# it to a number and it will display the output of the process_item function.

# b) Write a module named app.py. When this module is run, it will run in an infinite loop,
# waiting for inputs from the user. The program will convert the input to a number and process
# it using the function process_item implemented in utils.py. You will have to import this
# function in your module. The program stops when the user enters the message "q".

from utils import process_item

if __name__ == '__main__':
    run_process = True
    while run_process:
        user_input = input("Give input: ")
        if user_input == 'q':
            run_process = False
        else:
            print("Least prime number > input: ", process_item(int(user_input)))
