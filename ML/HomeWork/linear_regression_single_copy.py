# from constant import *
X = (0,1,2,3)
y = (1,3,5,7)
m = len(X)
n=1
def Hypothesis(theta__0, theta__1, x_):
    return theta__0 + theta__1*x_

def product_sum(theta0, theta1, k=0):
    sum = 0
    for i in range(m):
        x_ = X[i]
        y_ = y[i]
        m_ = 1 if k == 0 else x_
        sum = sum + ( Hypothesis(theta0,theta1,x_) - y_ )*m_
    return sum


def Cost_(theta0, theta1):
    cost = 0
    for i in range(m):
        x_ = X[i]
        y_ = y[i]
        cost = cost + ( Hypothesis(theta0, theta1, x_) - y_ )**2
    return cost

def linear_regression():
    theta_0 = 0
    theta_1 = 0
    alpha = 0.1
    cost = 1000
    count = 0
    stop = 1500
    while count < stop:
        k0 = theta_0
        k1 = theta_1
        theta_0 = k0 - alpha*(1/m)*product_sum(k0, k1, 0)
        # theta_1 = k1 - alpha*(1/m)*product_sum(k0, k1, 1)
        for key in range(1,n+1):
            k = 0 if key == 0 else 1
            theta_1 = k0 - alpha*(1/m)*product_sum(k0, k1, k)

        cost = Cost_(theta_0, theta_1)
        count = count + 1
    return {'theta_0' : theta_0, 'theta_1': theta_1,
            'cost':cost, 'count':count}

print('test')
for k,v in linear_regression().items():
    print(k,':', v)
