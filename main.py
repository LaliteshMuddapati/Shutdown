def shutdown():
    if value=='yes':
        print("Shutting down")
    elif value=='no':
        print("Abort shutdown")
    else:
        print("Sorry")

value=input("Would you like to shutdown the system?: ")

shutdown()
