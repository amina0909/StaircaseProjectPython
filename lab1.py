"""
Name: Amina Edavalath
UCINetID: aedavala
"""

''' This functions asks the user for the number of steps
they want to climb, gets the value provided by the user
and returns it to the calling function. This function will
raise any exceptions related to none integer user inputs.'''

class IntegerOutOfRangeException(Exception):
    pass

class NoStaircaseSizeException(Exception):
    pass


def getUserInput():
    #your code belongs here
    numSteps = int(input("Please input your staircase size:\n"))
    #numSteps = input("Please input your staircase size:\n")
    if type(numSteps) == int:
        return numSteps
    elif numSteps == "DONE":
        return "DONE"
    else:
        raise ValueError("Invalid staircase value entered.")

''' This function takes the number of steps as an input parameter,
creates a string that contains the entire steps based on the user input
and returns the steps string to the calling function. This function will raise
any exceptions resulting from invalid integer values.
'''
def createSteps(stepCount):
    #your code belongs here
    base_stair = "+-+"
    side_stair = "| |"
    mid_row = "+-+-+"
    space = " "
    staircase = ""
   

    

    if 0 < stepCount < 1000:
        for i in range(1, stepCount+1):
            spaceCount = ((2*stepCount) - (2*i))
            if i == 1:
                staircase = staircase + f'{(spaceCount * space)}{base_stair}\n'
                staircase = staircase + f'{(spaceCount * space)}{side_stair}\n'
            else:
                staircase = staircase + f'{(spaceCount * space)}{mid_row}\n'
                staircase = staircase + f'{(spaceCount * space)}{side_stair}\n'
        staircase = staircase + base_stair
        return staircase
    elif stepCount == 0:
        #return "Your staircase has no steps to build."
        raise NoStaircaseSizeException 
    
    elif stepCount >= 1000:
        #return "The staircase is too tall to build."
        raise IntegerOutOfRangeException
    #else:
        #return "You have provided an invalid staircase size."
    

'''This function kicks off the running of your program. Once it starts
it will continuously run your program until the user explicitly chooses to
end the running of the program based on the requirements. This function returns
the string "Done Executing" when it ends. Additionally, all exceptions will be
handled (caught) within this function.'''
def runProgram():
    #your code belongs here
    while True:
        try:
            print(createSteps(getUserInput()))
        except ValueError:
            print("Invalid staircase value entered.")
        except IntegerOutOfRangeException:
            print("That staircase size is out of range.")
        except NoStaircaseSizeException:
            print("I cannot draw a staircase with no steps.")
    
'''Within this condition statement you are to write the code that kicks off
your program. When testing your code the code below this
should be the only code not in a function and must be within the if
statement. I will explain this if statement later in the course.'''
if __name__ == "__main__": 
    #your code belongs here
    runProgram()
