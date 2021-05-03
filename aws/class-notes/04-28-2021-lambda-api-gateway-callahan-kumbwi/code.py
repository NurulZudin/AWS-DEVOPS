from random import randint

print('Loading function')

def lambda_handler(event, context):
    myNumber = randint(0,1000)
    print(f"Random No. [{myNumber}]")
    return myNumber

event=""
context=""
lambda_handler(event, context)