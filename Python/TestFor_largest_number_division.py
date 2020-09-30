# Python code to find highest
# K-digit number divisible by X

def answer(X, K):
    """A function to get largest possible number divisible by the number user provided."""

    # Computing MAX
    MAX = pow(10, K) - 1

    # returning ans
    return (MAX - (MAX % X))


running = True
while True:
    print("(Enter 'q' to quit anytime)")
    
    X = input("Enter a Digit You Want To Divide The Largest Number With:")
    
    if X.lower() == 'q':
        break
    else:
        X = int(X)
        
    K = input("Enter a Digit You Want To Get Number of Digits In Your Answer:")
    
    if K.lower() == 'q':
        break
    else:
        K = int(K)

    print(answer(X, K))
