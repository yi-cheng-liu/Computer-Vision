import math
import numpy as np


"""
Defines forward and backward passes through different computational graphs.

Students should complete the implementation of all functions in this file.
"""

# Optional
def f1(x1, w1, x2, w2, b, y):
    """
    Computes the forward and backward pass through the computational graph f1
    from the homework PDF.

    A few clarifications about the graph:
    - The subtraction node in the graph computes d = y_hat - y
    - The ^2 node squares its input

    Inputs:
    - x1, w1, x2, w2, b, y: Python floats

    Returns a tuple of:
    - L: Python scalar giving the output of the graph
    - grads: A tuple (grad_x1, grad_w1, grad_x2, grad_w2, grad_b, grad_y)
    giving the derivative of the output L with respect to each input.
    """
    # Forward pass: compute loss
    a1 = x1 * w1
    a2 = x2 * w2
    y_hat = a1 + a2 + b
    d = y_hat - y
    L = d**2
    ###########################################################################
    # TODO: Implement the forward pass for the computational graph f1 shown   #
    # in the homework description. Store the loss in the variable L.          #
    ###########################################################################
    ###########################################################################
    #                              END OF YOUR CODE                           #
    ###########################################################################

    # Backward pass: compute gradients
    grad_L = 1.0
    grad_d = 2 * d * grad_L
    grad_y = -grad_d
    grad_y_hat = grad_d
    grad_b = grad_y_hat
    grad_a1 = grad_d
    grad_a2 = grad_d
    grad_x1 = w1 * grad_a1
    grad_w1 = x1 * grad_a1
    grad_x2 = w2 * grad_a2
    grad_w2 = x2 * grad_a2
    
    ###########################################################################
    # TODO: Implement the backward pass for the computational graph f1 shown  #
    # in the homework description. Store the gradients for each input         #
    # variable in the corresponding grad variagbles defined above.            #
    ###########################################################################
    ###########################################################################
    #                              END OF YOUR CODE                           #
    ###########################################################################

    grads = (grad_x1, grad_w1, grad_x2, grad_w2, grad_b, grad_y)
    return L, grads

# Optional
def f2(x):
    """
    Computes the forward and backward pass through the computational graph f2
    from the homework PDF.

    A few clarifications about this graph:
    - The "x2" node multiplies its input by the constant 2
    - The "+1" and "-1" nodes add or subtract the constant 1
    - The division node computes y = t / b

    Inputs:
    - x: Python float

    Returns a tuple of:
    - y: Python float
    - grads: A tuple (grad_x,) giving the derivative of the output y with
      respect to the input x
    """
    # Forward pass: Compute output
    d = 2 * x
    e = np.exp(d)
    t = e - 1
    b = e + 1
    y = t/b
    
    ###########################################################################
    # TODO: Implement the forward pass for the computational graph f2 shown   #
    # in the homework description. Store the output in the variable y.        #
    ###########################################################################
    ###########################################################################
    #                              END OF YOUR CODE                           #
    ###########################################################################

    # Backward pass: Compute gradients
    grad_y = 1.0
    grad_b = grad_y * -(b**-2) * t
    grad_t = grad_y * (b**-1)
    grad_e = grad_t + grad_b
    grad_d = grad_e * np.exp(d)
    grad_x = 2 * grad_d
    ###########################################################################
    # TODO: Implement the backward pass for the computational graph f2 shown  #
    # in the homework description. Store the gradients for each input         #
    # variable in the corresponding grad variagbles defined above.            #
    ###########################################################################
    ###########################################################################
    #                              END OF YOUR CODE                           #
    ###########################################################################

    return y, (grad_x,)

# Required
def f3(s1, s2, y):
    """
    Computes the forward and backward pass through the computational graph f3
    from the homework PDF.

    A few clarifications about the graph:
    - The input y is an integer with y == 1 or y == 2; you do not need to
      compute a gradient for this input.
    - The division nodes compute p1 = e1 / d and p2 = e2 / d
    - The choose(p1, p2, y) node returns p1 if y is 1, or p2 if y is 2.

    Inputs:
    - s1, s2: Python floats
    - y: Python integer, either equal to 1 or 2

    Returns a tuple of:
    - L: Python scalar giving the output of the graph
    - grads: A tuple (grad_s1, grad_s2) giving the derivative of the output L
    with respect to the inputs s1 and s2.
    """
    assert y == 1 or y == 2
    # Forward pass: Compute loss
    e1 = np.exp(s1)
    e2 = np.exp(s2)
    d = e1 + e2
    p1 = e1/d
    p2 = e2/d
    if y == 1:
        p = p1
    elif y == 2:
        p = p2
    L = -np.log(p)
    ###########################################################################
    # TODO: Implement the forward pass for the computational graph f3 shown   #
    # in the homework description. Store the loss in the variable L.          #
    ###########################################################################
    ###########################################################################
    #                              END OF YOUR CODE                           #
    ###########################################################################

    # Backward pass: Compute gradients
    grad_L = 1.0
    grad_p = grad_L * -(1/p)
    if y == 1:
        grad_p1 = grad_p
        grad_p2 = 0
    elif y == 2:
        grad_p2 = grad_p
        grad_p1 = 0
    grad_d1 = grad_p1 * -(d**-2) * e1
    grad_d2 = grad_p2 * -(d**-2) * e2
    grad_d = grad_d1 + grad_d2
    
    grad_e1 = grad_p1 * (d**-1) + grad_d
    grad_s1 = grad_e1 * np.exp(s1)
    
    grad_e2 = grad_p2 * (d**-1) + grad_d
    grad_s2 = grad_e2 * np.exp(s2)
    
    ###########################################################################
    # TODO: Implement the backward pass for the computational graph f3 shown  #
    # in the homework description. Store the gradients for each input         #
    # variable in the corresponding grad variagbles defined above. You do not #
    # need to compute a gradient for the input y since it is an integer.      #
    #                                                                         #
    # HINT: You may need an if statement to backprop through the choose node  #
    ###########################################################################
    ###########################################################################
    #                              END OF YOUR CODE                           #
    ###########################################################################

    grads = (grad_s1, grad_s2)
    return L, grads


def f3_y1(s1, s2):
    """
    Helper function to compute f3 in the case where y = 1

    Inputs:
    - s1, s2: Same as f3

    Outputs: Same as f3
    """
    return f3(s1, s2, y=1)


def f3_y2(s1, s2):
    """
    Helper function to compute f3 in the case where y = 2

    Inputs:
    - s1, s2: Same as f3

    Outputs: Same as f3
    """
    return f3(s1, s2, y=2)

# Optional
def f4():
    loss, grads = None, None
    ###########################################################################
    # TODO: Implement a forward and backward pass through a computational     #
    # graph of your own construction. It should have at least five operators. #
    # Include a drawing of your computational graph in your report.           #
    # You can modify this function to take any number of arguments.           #
    ###########################################################################

    ###########################################################################
    #                         /     END OF YOUR CODE                           #
    ###########################################################################
    return loss, grads
