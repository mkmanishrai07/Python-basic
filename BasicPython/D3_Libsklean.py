import numpy as np  
from sklearn import datasets, linear_model
import matplotlib.pyplot as plt 
from sklearn.metrics import mean_squared_error

# data set
diabates = datasets.load_diabetes()

# find key for particular dataset that you have loaded
# print(diabates.keys())

# find key information of loaded dataset
# print(diabates.DESCR)



diabates_x = diabates.data[:,np.newaxis,2]
# print(diabates_x)

diabates_x_train = diabates_x[:-10]
diabates_x_test = diabates_x[-15:]


# from end last 
diabates_y_train = diabates.target[:-10]

# from start
diabates_y_test = diabates.target[-15:]

# linear_model 
model = linear_model.LinearRegression()
model.fit(diabates_x_train,diabates_x_train)

# predication 
diabates_y_predict = model.predict(diabates_x_test)

# print(diabates_x_test,diabates_y_test)

print("mean sqr erroe is :", mean_squared_error(diabates_y_test,diabates_y_predict))

# print("Weight", model.coef_)
# print("Interceptor", model.intercept_)


plt.scatter(diabates_x_test,diabates_y_test)

# plt.plot(diabates_x_test,diabates_y_test)

# plt.plot(diabates_x_test,diabates_y_predict)
# plt.show()