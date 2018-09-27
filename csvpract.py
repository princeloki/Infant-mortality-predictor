#The optimal values of m and b can be actually calculated with way less effort than doing a linear regression.
#this is just to demonstrate gradient descent

from numpy import *
import time

# y = mx + b
# m is slope, b is y-intercept
def compute_error_for_line_given_points(b, m, points):
    totalError = 0
    for i in range(1, len(points)):
        x = points[i, 1]/1000
        y = points[i, 2]
        totalError += (y - (m * x + b)) ** 2
    return totalError / float(len(points)-1)

def step_gradient(b_current, m_current, points, learningRate):
    b_gradient = 0
    m_gradient = 0
    N = float(len(points)-1)
    for i in range(1, len(points)):
        x = points[i, 1]/1000
        y = points[i, 2]
        b_gradient += (y - ((m_current * x) + b_current))
        m_gradient += x * (y - ((m_current * x) + b_current))
    b_gradient = -(2/N) * b_gradient
    m_gradient = -(2/N) * m_gradient
    new_b = b_current - (learningRate * b_gradient)
    new_m = m_current - (learningRate * m_gradient)
    return [new_b, new_m]

def gradient_descent_runner(points, starting_b, starting_m, learning_rate, num_iterations):
    b = starting_b
    m = starting_m

    for i in range(num_iterations):
        b, m = step_gradient(b, m, array(points), learning_rate)
    return [b, m]

def run():
    points = genfromtxt("infantmortality.csv", delimiter=",")
    points = array(points[97:194])
    learning_rate = 0.1
    initial_b = 65 # initial y-intercept guess
    initial_m = 7 # initial slope guess
    num_iterations = 100000
    print "Starting gradient descent at b = {0}, m = {1}, error = {2}".format(initial_b, initial_m, compute_error_for_line_given_points(initial_b, initial_m, points))
    print "Running..."
    start_time = time.time()
    [b, m] = gradient_descent_runner(points, initial_b, initial_m, learning_rate, num_iterations)
    print "After {0} iterations b = {1}, m = {2}, error = {3}".format(num_iterations, b, m, compute_error_for_line_given_points(b, m, points))
    print 'Time elapsed after Gradient Descent ---- %s seconds---'%(time.time()-start_time)

if __name__ == '__main__':
    run()
