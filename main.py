def shutdown(n):
    if n=='yes':
        print("Shutting down")
    elif n=='no':
        print("Abort shutdown")
    else:
        print("Sorry")

value=input("Would you like to shutdown the system?: ")

shutdown(value)
