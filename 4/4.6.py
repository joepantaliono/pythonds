from stack import Stack

def matching_par(str):
    """check matching parentheses using stack"""
    s = Stack()
    for c in str:
        # iterate and push opening pars onto stack
        if c == "(":
            s.push(c)
        else:
            # if the stack is empty, we have too many closing tags. pars are not balanced
            if s.is_empty() == True:
                return False
            else:
                # if closing, pop off its opening par from stack
                s.pop()
    # empty stack *after loop is complete* means it matched
    return s.is_empty()
       


matching_par("((()))")  # true
matching_par("(()())") # true
matching_par("((())))")  # false