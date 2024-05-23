def format(x,y):
    new_x,new_y = [],[]
    for i in range(len(y)):
        if y[i]:
            new_y.append(float(y[i]))
            new_x.append(float(x[i]))
    return new_x,new_y
