def Runge_Kutta4 (Func, initialT, initialCondition, numOfIterations, h):
    solution = [initialCondition]
    t = initialT
    
    for i in range(numOfIterations):
        k1 = Func(t, solution[-1])
        k2 = Func(t + h / 2, solution[-1] + h / 2 * k1)
        k3 = Func(t + h / 2, solution[-1] + h / 2 * k2)
        k4 = Func(t + h, solution[-1] + h * k3)
        t += h
        solution.append(solution[-1] + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4))
        
    return solution

def Runge_Kutta2 (Func, initialT, initialCondition, numOfIterations, h):
    solution = [initialCondition]
    t = initialT
    
    for i in range(numOfIterations):
        k1 = Func(t, solution[-1])
        k2 = Func(t + h , solution[-1] + h * k1)
        t += h
        solution.append(solution[-1] + h / 2 * (k1 + k2))
        
    return solution

def Addams4 (Func, initialT, initialСondition, numOfIterations, h):
    solution = initialСondition
    t = initialT
    
    for i in range(numOfIterations):
        solution.append(solution[-1] + h * (55/24*Func(t + 3*h, solution[-1]) - \
                        59/24*Func(t + 2*h, solution[-2]) + 37/24*Func(t + h, solution[-3]) - \
                        3/8*Func(t, solution[-4])))

        t += h
            
    return solution