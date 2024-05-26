# runs the linear regression model on the dataset and draws a graph

import numpy as np
import random
import matplotlib.pyplot as plt

from queries import initSql, closeSql # remove this when done testing, only crescent-1.py should run sql queries
cursor = None

def predict_Y(_bias, _weight, _X):
        return _bias + _weight * _X # if X with multiple features, this would be np.dot(_weight, _X)
    
# cost function
def cost_function(_Y, _Y_hat):
    N = len(_Y)
    Y_resd = _Y - _Y_hat
    Y_resd_sq = Y_resd ** 2
    Y_summation = np.sum(Y_resd_sq)
    cost = Y_summation / N # this could also have been Y_summation / (2*N), but chatgpt says that doesn't change because gradient descent is
    # scaled using the learning rate
    return cost

# this function updates the bias and weight
def update_bias_and_weight(_X,_Y,_Y_hat,_bias,_weight,_learning_rate): # alpha is the learning rate
    N = len(_Y) # number of observations
    Y_resd = _Y_hat - _Y
    d_bias = (np.sum(Y_resd) * 2) / N # d_bias means derivative of bias
    d_weight = (np.dot(Y_resd, _X)*2) / N # d_weight means derivative of weight
    new_bias = _bias - _learning_rate * d_bias
    new_weight = _weight - _learning_rate * d_weight
    return new_bias, new_weight

def run_gradient_descent(_X, _Y, _learning_rate, num_of_iter):
    # data capture variables to study later
    iteration_number = 0
    iter_num_arr = []
    cost_arr = []
    # END data capture variables

    bias = random.random() # initialize the bias
    weight = random.random() # initialize the weight, also called slope, or coefficient of X
    print("Initial bias: " + str(bias) + " Initial weight: " + str(weight))

    # loop start
    for _ in range(num_of_iter): # _ when a counter isn't necessary
        Y_hat = predict_Y(bias, weight, _X)
        cost = cost_function(_Y, Y_hat)
        prev_bias = bias
        prev_weight = weight
        bias, weight = update_bias_and_weight(_X,_Y,Y_hat,prev_bias,prev_weight,_learning_rate)
        if (iteration_number % 10 == 0): # print the cost every 10 iterations for tracking later in graph
            iter_num_arr.append(iteration_number)
            cost_arr.append(cost)
        iteration_number += 1
    gd_iteration = [iter_num_arr, cost_arr] # make it cleaner

    for i in range(len(iter_num_arr)):
        print("Iteration: " + str(iter_num_arr[i]) + " Cost: " + str(cost_arr[i]))
    
    print("Final bias: " + str(bias) + " Final weight: " + str(weight))
    print("Final cost: " + str(cost_arr[-1])) # [-1] means the last element in the list
    
    return gd_iteration, bias, weight

def LR():
    # ML code start (Linear Regression)

    sales = [] # list of sales per year from 2014 to 2024
    CostOfManufacturing = [] # list of construction costs per year from 2014 to 2024


    for year in range(2000, 2010):
        cursor.execute(f"SELECT * FROM Sales WHERE YEAR(sale_date) = {year}")
        rows = cursor.fetchall()
        yearlyCostOfManufacturing = 0 # initialize a variable
        for row in rows:
            # `rows` is a list of rows, iterating we get single row per loop, `row` is a list of columns, so accessing second column is row[1]
            currentHouse_id = row[1]
            # find all material and supplier relationships for current house_id in HouseMaterials table
            cursor.execute(f"SELECT material_id, supplier_id, how_many FROM HouseMaterials WHERE house_id = {currentHouse_id}")
            house_materials = cursor.fetchall()

            house_construction_cost = 0
            for material in house_materials:
                material_id = material[0]
                supplier_id = material[1]
                how_many = material[2]

                cursor.execute(f"SELECT unit_price FROM SupplierMaterials WHERE supplier_id = {supplier_id} AND material_id = {material_id}")
                unit_price = cursor.fetchone()[0]

                house_construction_cost += unit_price * how_many
                
            yearlyCostOfManufacturing += house_construction_cost
        CostOfManufacturing.append(yearlyCostOfManufacturing)
        cursor.execute(f"select SUM(sale_price) from Sales where year(sale_date) = {year}")
        sales.append(cursor.fetchone()[0]) # append the total sales for that year

    # we now have a list years worth of sales and cost data ready
    for i in range(len(sales)):
        print(f"Year: {i+2000} Cost: {CostOfManufacturing[i]} Sales: {sales[i]}")

    # gradient descent algorithm
    # X is the predictor variable data set, and Y is the response variable data set
    # each data point in the dataset represents the cost of manufacturing and the sales for a particular year
    # for this dataset the datapoints span from 2000 to 2009
    # the cost of manufacturing is not the ideal predictor variable for this project, but we are using it here for testing purposes
    # we will research a better features (predictor variables) later

    # the X and Y values need to be standardized first, to make sure they are on the same scale (this is different from normalization)
    X = np.array(CostOfManufacturing, dtype=float) # convert the list to a numpy array
    Y = np.array(sales, dtype=float) # convert the list to a numpy array
    # datatype converted into float because numpy only works with floats
    Y = np.array((Y-Y.mean())/Y.std()) # standardize the Y values
    X = np.array((X-X.mean())/X.std()) # standardize the X values
    # here X contains only one feature, so it can use the same formula as Y, otherwise you would perform this on each
    # individual column of data (dot product)
    
    gd_iteration, bias, weight = run_gradient_descent(X,Y,0.01,100)

    # plot the graph with subplots for cost function and costOfManufacturing vs sales
    fig, axs = plt.subplots(2)
    fig.suptitle('Linear Regression Model')
    axs[0].plot(gd_iteration[0], gd_iteration[1])
    axs[0].set(ylabel='Cost Function')
    axs[0].set(xlabel='Number of Iterations')
    axs[1].scatter(X,Y)
    axs[1].plot(X, bias + weight*X, color='red')
    axs[1].set(xlabel='Cost of Manufacturing', ylabel='Sales')
    plt.show()

    # ask user for a cost of construction and predict the sales
    in_cost = float(input("Enter the cost of construction: "))
    pred_sales = predict_Y(bias, weight, in_cost)
    print("Predicted sales: " + str(pred_sales))




if __name__ == "__main__": # just for testing purposes, makes it easy to run the ML function directly
    cursor = initSql()
    LR()
    closeSql()