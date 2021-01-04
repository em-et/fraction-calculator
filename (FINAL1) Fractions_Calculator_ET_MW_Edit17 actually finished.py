from math import gcd as mathgcd
from time import sleep as timesleep
from click import clear as clicknclear
# WELCOME TO THE COMMENTS. HERE YOU CAN READ WHAT MOST THINGS DO IN THE CODE.
# insert fixes the weird problem
#1 imports 'from math import gcd as math.gcd' imports the greatest common divisor for simplifying fractions
#2 imports 'sleep' is the 'wait' function in python (makes the code pause for however long specified)
def oops():
    clicknclear()
    print('Please check what you have typed in and try again.')
    timesleep(1.5)
    print("Restarting...")
    timesleep(.5)
    clicknclear()
    start()

def reset():
    print("Resetting...")
    timesleep(.5)
    clicknclear()
    start()

print("Starting Program...")

#3 Makes the program wait
timesleep(.5)

ermaxcrown = ('''

10                10                10
01  E            r M a          x   01
10    I       n        c       .    10
01     01   01          01  01      01
10       10               10        10
01                                  01
10              □                □  10
01                                  01
10                        ____      10
01                                  01
10                                  10
010010 011001010110110101101001 100110
''')

print(ermaxcrown)

#4 it defines the variable to 'goto' the code
def start():

#5 it stores the operation
    operation = input('Please enter the operation you want to do [+, -, * (Multiplication), / (Division)]: ')

#6 it just separates
    print('------------------------------------------------------------------------------------------')
    if operation == '+' or operation == '*' or operation == '/' or operation == '-':
        num1example = ('''     

                    |             
                    |             
                   \_/            
                              
                    ?             ?
                  -----    ''' + operation + '''    -----
                    ?             ?

                   ''')
        print(num1example)

        numerator1 = int(input('''                 -----------        -------
Please enter the |numerator| of the |first| fraction as seen above, or type 'reset' to reset: '''))


        print('------------------------------------------------------------------------------------------')

        denom1example = ('''  
                              
                    ''' + str(numerator1) + '''             ?
                  -----    ''' + operation + '''    -----
                    ?             ?
                    _
                   / \     
                    |
                    |
                        ''')
        print(denom1example)

        denominator1 = int(input('''                 -------------        -------
Please enter the |denominator| of the |first| fraction as seen above, or type 'reset' to reset: '''))


        print('''------------------------------------------------------------------------------------------
        ''')

#7 it stores if the fraction will be negative
        frac1neg = input('''Do you want the fraction to be negative? (y/n) Type 'reset' to reset.''')
        
        if frac1neg == 'reset':
            reset()
        if frac1neg == 'n':
            frac1neg = '+'
        elif frac1neg == 'y':
            frac1neg = '-'
        else:
            oops()
        
        print('''
------------------------------------------------------------------------------------------''')

        num2example = ('''

                                  |
                                  |
                                 \_/
                              
                    ''' + str(numerator1) + '''             ?
                ''' + frac1neg + ''' -----    ''' + operation + '''    -----
                    ''' + str(denominator1) + '''             ?
                    
                        ''')
        print(num2example)

        numerator2 = int(input('''                 -----------        --------
Please enter the |numerator| of the |second| fraction as seen above, or type 'reset' to reset: '''))
        

        print('------------------------------------------------------------------------------------------')

        denom2example = ('''        

                    ''' + str(numerator1) + '''             ''' + str(numerator2) + '''
                 ''' + frac1neg + ''' -----    ''' + operation + '''    -----
                    ''' + str(denominator1) + '''             ?
                                  _
                                 / \   
                                  |
                                  |
                        ''')
        print(denom2example)

        denominator2 = int(input('''                -------------        --------
Please enter the |denominator| of the |second| fraction as seen above, or type 'reset' to reset: '''))


        print('''------------------------------------------------------------------------------------------
        ''')

        frac2neg = input('''Do you want the fraction to be negative? (y/n) Type 'reset' to reset.''')

        if frac2neg == 'reset':
            reset()
        if frac2neg == 'n':
            frac2neg = '+'
        elif frac2neg == 'y':
            frac2neg = '-'
        else:
            oops()

        print('''
------------------------------------------------------------------------------------------''')

        timesleep(.5)
        print("Calculating Your Answer...")
        timesleep(.5)
        print('------------------------------------------------------------------------------------------')

        final_input = ('''Your input:
                              
                              
                    ''' + str(numerator1) + '''             ''' + str(numerator2) + '''
                 ''' + frac1neg + ''' -----    ''' + operation + '''   ''' + frac2neg + ''' -----
                    ''' + str(denominator1) + '''             ''' + str(denominator2) + '''
                                     
                        ''')
        print(final_input)
        timesleep(.5)
        print('------------------------------------------------------------------------------------------')
        #7 zeroes out the variables
        add_num_simple = 0
        add_denom_simple = 0
        add_num_not_equal_denom = 0
        add_denom_not_equal_denom = 0
        sub_num_simple = 0
        sub_denom_simple = 0
        sub_denom_not_equal_denom = 0
        sub_num_not_equal_denom = 0
        multi_num1_X_num2 = 0
        multi_denom1_X_denom2 = 0
        div_num_final = 0
        div_denom_final = 0
        finalfracneg = ''

        if frac1neg == '+':
            frac1neg = 'n'
        elif frac1neg == '-':
            frac1neg = 'y'
        
        if frac2neg == '+':
            frac2neg = 'n'
        elif frac2neg == '-':
            frac2neg = 'y'

        #8 TL;DR: Da math
        if operation == '+':
            if denominator1 == denominator2:
                add_num_simple = numerator1 + numerator2
                add_denom_simple = denominator1
                #9 TL;DR: Decides if the FRACTION will be positive or negative

                #10 if 'add_denom_simple' is negative and the other one isn't
                if '-' not in str(add_num_simple) and '-' in str(add_denom_simple):
                    #11 TL;DR: Checks what is negative or not to find the result
                    #12 if the first and second fractions are negative then 'finalfracneg' is minus
                    if frac1neg == 'y' and frac2neg == 'y':
                        finalfracneg = '-'
                    #13 if the first is positive and the second is negative the 'finalfracneg' is +
                    elif frac1neg == 'n' and frac2neg == 'y':
                        finalfracneg = '+'
                    #14 if the first is negative and the second is positive the 'finalfracneg' is still +
                    elif frac1neg == 'y' and frac2neg == 'n':
                        finalfracneg = '+'
                    #15 if the first and second fractions are positive then 'finalfracneg' is minus too
                    elif frac1neg == 'n' and frac2neg == 'n':
                        finalfracneg = '-'
                if '-'  in str(add_num_simple) and '-' not in str(add_denom_simple):
                    if frac1neg == 'y' and frac2neg == 'y':
                        finalfracneg = '-'
                    elif frac1neg == 'n' and frac2neg == 'y':
                        finalfracneg = '+'
                    elif frac1neg == 'y' and frac2neg == 'n':
                        finalfracneg = '+'
                    elif frac1neg == 'n' and frac2neg == 'n':
                        finalfracneg = '-'
                elif '-' in str(add_num_simple) and '-' in str(add_denom_simple):
                    if frac1neg == 'y' and frac2neg == 'y':
                        finalfracneg = '+'
                    elif frac1neg == 'n' and frac2neg == 'y':
                        finalfracneg = '-'
                    elif frac1neg == 'y' and frac2neg == 'n':
                        finalfracneg = '-'
                    elif frac1neg == 'n' and frac2neg == 'n':
                        finalfracneg = '+'
                    #16 Removes - if there is
                    if '-' in str(add_num_simple):
                        add_num_simple = str(add_num_simple).replace('-', '')
                    if '-' in str(add_denom_simple):
                        add_denom_simple = str(add_denom_simple).replace('-', '')
                print('''Your result is:
		    
                   ''' + str(add_num_simple) + '''
	                ''' + finalfracneg + ''' -----
                   ''' + str(add_denom_simple) + ''' ''')
            else:
                  add_num1_not_equal_denom = numerator1 * denominator2
                  add_denom_not_equal_denom = denominator1 * denominator2
                  add_num2_not_equal_denom = numerator2 * denominator1
                  add_num_not_equal_denom = add_num1_not_equal_denom + add_num2_not_equal_denom
                  if '-' not in str(add_num_not_equal_denom) and '-' in str(add_denom_not_equal_denom):
                      if frac1neg == 'y' and frac2neg == 'y':
                          finalfracneg = '-'
                      elif frac1neg == 'n' and frac2neg == 'y':
                          finalfracneg = '+'
                      elif frac1neg == 'y' and frac2neg == 'n':
                          finalfracneg = '+'
                      elif frac1neg == 'n' and frac2neg == 'n':
                          finalfracneg = '-'
                  if '-'  in str(add_num_not_equal_denom) and '-' not in str(add_denom_not_equal_denom):
                      if frac1neg == 'y' and frac2neg == 'y':
                          finalfracneg = '-'
                      elif frac1neg == 'n' and frac2neg == 'y':
                          finalfracneg = '+'
                      elif frac1neg == 'y' and frac2neg == 'n':
                          finalfracneg = '+'
                      elif frac1neg == 'n' and frac2neg == 'n':
                          finalfracneg = '-'
                  elif '-' in str(add_num_not_equal_denom) and '-' in str(add_denom_not_equal_denom):
                      if frac1neg == 'y' and frac2neg == 'y':
                          finalfracneg = '+'
                      elif frac1neg == 'n' and frac2neg == 'y':
                          finalfracneg = '-'
                      elif frac1neg == 'y' and frac2neg == 'n':
                          finalfracneg = '-'
                      elif frac1neg == 'n' and frac2neg == 'n':
                          finalfracneg = '+'
                  if '-' in str(add_num_not_equal_denom):
                        add_num_not_equal_denom = str(add_num_not_equal_denom).replace('-', '')
                  if '-' in str(add_denom_not_equal_denom):
                        add_denom_not_equal_denom = str(add_denom_not_equal_denom).replace('-', '')
                  print('''Your result is:
		    
		           ''' + str(add_num_not_equal_denom) + '''
	                ''' + finalfracneg + ''' -----
		           ''' + str(add_denom_not_equal_denom) + ''' ''')
        elif operation == '-':
            if denominator1 == denominator2:
                sub_num_simple = numerator1 - numerator2
                sub_denom_simple = denominator1
            if '-' not in str(sub_num_simple) and '-' in str(sub_denom_simple):
                if frac1neg == 'y' and frac2neg == 'y':
                    finalfracneg = '-'
                elif frac1neg == 'n' and frac2neg == 'y':
                    finalfracneg = '+'
                elif frac1neg == 'y' and frac2neg == 'n':
                    finalfracneg = '+'
                elif frac1neg == 'n' and frac2neg == 'n':
                    finalfracneg = '-'
            if '-'  in str(sub_num_simple) and '-' not in str(sub_denom_simple):
                if frac1neg == 'y' and frac2neg == 'y':
                    finalfracneg = '-'
                elif frac1neg == 'n' and frac2neg == 'y':
                    finalfracneg = '+'
                elif frac1neg == 'y' and frac2neg == 'n':
                    finalfracneg = '+'
                elif frac1neg == 'n' and frac2neg == 'n':
                    finalfracneg = '-'
            elif '-' in str(sub_num_simple) and '-' in str(sub_denom_simple):
                if frac1neg == 'y' and frac2neg == 'y':
                    finalfracneg = '+'
                elif frac1neg == 'n' and frac2neg == 'y':
                    finalfracneg = '-'
                elif frac1neg == 'y' and frac2neg == 'n':
                    finalfracneg = '-'
                elif frac1neg == 'n' and frac2neg == 'n':
                    finalfracneg = '+'
            if '-' in str(sub_num_simple):
                sub_num_simple = str(sub_num_simple).replace('-', '')
            if '-' in str(sub_denom_simple):
                sub_denom_simple = str(sub_denom_simple).replace('-', '')
                print('''Your result is:
                        
                   ''' + str(sub_num_simple) + '''
                    ''' + finalfracneg + ''' -----
                   ''' + str(sub_denom_simple) + ''' ''')
            else:
                 sub_num1_not_equal_denom = numerator1 * denominator2
                 sub_denom_not_equal_denom = denominator1 * denominator2
                 sub_num2_not_equal_denom = numerator2 * denominator1
                 sub_num_not_equal_denom = sub_num1_not_equal_denom - sub_num2_not_equal_denom
            if '-' not in str(sub_num_not_equal_denom) and '-' in str(sub_denom_not_equal_denom):
                if frac1neg == 'y' and frac2neg == 'y':
                    finalfracneg = '-'
                elif frac1neg == 'n' and frac2neg == 'y':
                    finalfracneg = '+'
                elif frac1neg == 'y' and frac2neg == 'n':
                    finalfracneg = '+'
                elif frac1neg == 'n' and frac2neg == 'n':
                    finalfracneg = '-'
            if '-'  in str(sub_num_not_equal_denom) and '-' not in str(sub_denom_not_equal_denom):
                if frac1neg == 'y' and frac2neg == 'y':
                    finalfracneg = '-'
                elif frac1neg == 'n' and frac2neg == 'y':
                    finalfracneg = '+'
                elif frac1neg == 'y' and frac2neg == 'n':
                    finalfracneg = '+'
                elif frac1neg == 'n' and frac2neg == 'n':
                    finalfracneg = '-'
            elif '-' in str(sub_num_not_equal_denom) and '-' in str(sub_denom_not_equal_denom):
                if frac1neg == 'y' and frac2neg == 'y':
                    finalfracneg = '+'
                elif frac1neg == 'n' and frac2neg == 'y':
                    finalfracneg = '-'
                elif frac1neg == 'y' and frac2neg == 'n':
                    finalfracneg = '-'
                elif frac1neg == 'n' and frac2neg == 'n':
                    finalfracneg = '+'
            if '-' in str(sub_num_not_equal_denom):
                sub_num_not_equal_denom = str(sub_num_not_equal_denom).replace('-', '')
            if '-' in str(sub_denom_not_equal_denom):
                sub_denom_not_equal_denom = str(sub_denom_not_equal_denom).replace('-', '')
            print('''Your result is:
                        
                   ''' + str(sub_num_not_equal_denom) + '''
                 ''' + finalfracneg + ''' -----
                    ''' + str(sub_denom_not_equal_denom) + ''' ''')

        elif operation == '/':
            div_num_final = denominator2 * numerator1
            div_denom_final = numerator2 * denominator1
            if '-' not in str(div_num_final) and '-' in str(div_denom_final):
                if frac1neg == 'y' and frac2neg == 'y':
                    finalfracneg = '-'
                elif frac1neg == 'n' and frac2neg == 'y':
                    finalfracneg = '+'
                elif frac1neg == 'y' and frac2neg == 'n':
                    finalfracneg = '+'
                elif frac1neg == 'n' and frac2neg == 'n':
                    finalfracneg = '-'
            if '-'  in str(div_num_final) and '-' not in str(div_denom_final):
                if frac1neg == 'y' and frac2neg == 'y':
                    finalfracneg = '-'
                elif frac1neg == 'n' and frac2neg == 'y':
                    finalfracneg = '+'
                elif frac1neg == 'y' and frac2neg == 'n':
                    finalfracneg = '+'
                elif frac1neg == 'n' and frac2neg == 'n':
                    finalfracneg = '-'
            elif '-' in str(div_num_final) and '-' in str(div_denom_final):
                if frac1neg == 'y' and frac2neg == 'y':
                    finalfracneg = '+'
                elif frac1neg == 'n' and frac2neg == 'y':
                    finalfracneg = '-'
                elif frac1neg == 'y' and frac2neg == 'n':
                    finalfracneg = '-'
                elif frac1neg == 'n' and frac2neg == 'n':
                    finalfracneg = '+'
            if '-' in str(div_num_final):
                div_num_final = str(div_num_final).replace('-', '')
            if '-' in str(div_denom_final):
                div_denom_final = str(div_denom_final).replace('-', '')
            print('''Your result is:
                        
                   ''' + str(div_num_final) + '''
              ''' + finalfracneg + '''   -----
                   ''' + str(div_denom_final) + ''' ''')
        elif operation == '*':
            multi_num1_X_num2 = numerator1 * numerator2
            multi_denom1_X_denom2 = denominator1 * denominator2
            if '-' not in str(multi_num1_X_num2) and '-' in str(multi_denom1_X_denom2):
                if frac1neg == 'y' and frac2neg == 'y':
                    finalfracneg = '-'
                elif frac1neg == 'n' and frac2neg == 'y':
                    finalfracneg = '+'
                elif frac1neg == 'y' and frac2neg == 'n':
                    finalfracneg = '+'
                elif frac1neg == 'n' and frac2neg == 'n':
                    finalfracneg = '-'
            if '-'  in str(multi_num1_X_num2) and '-' not in str(multi_denom1_X_num2):
                if frac1neg == 'y' and frac2neg == 'y':
                    finalfracneg = '-'
                elif frac1neg == 'n' and frac2neg == 'y':
                    finalfracneg = '+'
                elif frac1neg == 'y' and frac2neg == 'n':
                    finalfracneg = '+'
                elif frac1neg == 'n' and frac2neg == 'n':
                    finalfracneg = '-'
            elif '-' in str(multi_num1_X_num2) and '-' in str(multi_denom1_X_num2):
                if frac1neg == 'y' and frac2neg == 'y':
                    finalfracneg = '+'
                elif frac1neg == 'n' and frac2neg == 'y':
                    finalfracneg = '-'
                elif frac1neg == 'y' and frac2neg == 'n':
                    finalfracneg = '-'
                elif frac1neg == 'n' and frac2neg == 'n':
                    finalfracneg = '+'
            if '-' in str(multi_num1_X_num2):
                str(multi_num1_X_num2).replace('-','')
            if '-' in str(multi_denom1_X_denom2):
                str(multi_denom1_X_denom2).replace('-','')
            print('''Your result is:
                        
                   ''' + str(multi_num1_X_num2) + '''
              ''' + finalfracneg + '''   -----
                   ''' + str(multi_denom1_X_denom2) + ''' ''')

    #17 easter eggs
    elif operation == "dat krown boi":
        print('hey ya found da easter egg great job')
        timesleep(2)
        clicknclear()
        start()

    elif operation == "fbi open up":
        print('E.T. M.W.')
        timesleep(2)
        clicknclear()
        start()

    else:
        oops()
    
    #18 TL;DR: calculates gcd and prints it out at the end
    #19 basically is the num and denom see comment 7
    num = add_num_simple + sub_num_simple + div_num_final + multi_num1_X_num2 + add_num_not_equal_denom + sub_num_not_equal_denom
    denom = add_denom_simple + add_denom_not_equal_denom + sub_denom_simple + sub_denom_not_equal_denom + div_denom_final + multi_denom1_X_denom2
    #20 calculates gcd
    gcd = mathgcd(num,denom)
    #21 results
    num_ans_final = int(num / gcd)
    denom_ans_final = int(denom / gcd)
    print('''------------------------------------------------------------------------------------------
    ''')
    #22 prints out gcd
    print('Greatest common divisor:', gcd)
    print('''
------------------------------------------------------------------------------------------''')
    #23 result of calculation
    print('''Your result is:
                        
                   ''' + str(num_ans_final) + '''
                ''' + finalfracneg + ''' -----
                   ''' + str(denom_ans_final) + ''' ''')

    #24 what the text says
    input("\n\nPress Enter to Exit.")
#25 'start' starts all the code as defined in comment #4
start()