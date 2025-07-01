def func_one(X):
    try:
        return 1 / X
    except ZeroDivisionError:
        return "Cannot divide by zero"
    except TypeError:
        return "Invalid type"
    finally:
        print("Execution completed")
print('for x=2 :',func_one(2))  # Should print 0.5 and "Execution completed"
print('for x=0:',func_one(0))  # Should print "Cannot divide by zero" and "Execution completed"