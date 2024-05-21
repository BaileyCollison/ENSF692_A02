# input_processing.py
# BAILEY COLLISON, ENSF 692 P24
# A terminal-based program for processing computer vision changes detected by a car.

class Sensor:

    # Initialize default values for traffic parameters
    def __init__(self):
        self.Light = "green"
        self.Pedestrian = "no"
        self.Vehicle = "no"

    # Update the current status of each traffic parameter
    # Light will only take "green", "yellow", or "red"
    # Pedestrian will only take "yes" or "no"
    # Vehicle will also only take "yes" or "no"
    def update_status(self, Light, Pedestrian, Vehicle):
        if Light in ("green", "yellow", "red"):
            self.Light = Light
        else:
            print("Invalid vision change.")

        if Pedestrian in ("yes", "no"):
            self.Pedestrian = Pedestrian
        else:
            print("Invalid vision change.")
        
        if Vehicle in ("yes", "no"):
            self.Vehicle = Vehicle
        else:
            print("Invalid vision change.")
        
        return True

# The sensor object is passed to this function to update and print the action message and current status for each traffic parameter
def print_message(sensor):
    if sensor.Light == "green" and sensor.Pedestrian == "no" and sensor.Vehicle == "no":
        print("\nProceed\n")
    elif sensor.Light == "yellow" and sensor.Pedestrian == "no" and sensor.Vehicle == "no":
        print("\nCaustion\n")
    elif sensor.Light == "red" or sensor.Pedestrian == "yes" or sensor.Vehicle == "yes":
        print("\nSTOP\n")
    
    print("Light = " + sensor.Light + " , Pedestrian = " + sensor.Pedestrian + " , Vehicle = " + sensor.Vehicle)

# The main function handles the user input values and sends parameters to the sensor class and print_message function
# to determine the output. It also loops to allow for the program to be reset without running again.
def main():
    print("\n***ENSF 692 Car Vision Detector Processing Program***\n")
    sensor = Sensor()

    while True:
        # These will print for each loop
        print("\nAre there changes detected in the vision input?")
        selection = input("Select 1 for light, 2 for pedestrian, 3 for vehicle, or 0 to end the program: ")

        # If statement based on the input of the user from each loop
        if selection == "0":
            break
        elif selection == "1":
            user_input = input("What change has been identified?: ")
            # I struggled with this part for quite a while and spent a lot of time looking through the lecture notes
            # to determine how to deal with updating my variables through other functions/classes
            if sensor.update_status(user_input, sensor.Pedestrian, sensor.Vehicle):
                print_message(sensor)
        elif selection == "2":
            user_input = input("What change has been identified?: ")
            if sensor.update_status(sensor.Light, user_input, sensor.Vehicle):
                print_message(sensor)
        elif selection == "3":
            user_input = input("What change has been identified?: ")
            if sensor.update_status(sensor.Light, sensor.Pedestrian, user_input):
                print_message(sensor)
        # Dealing with ValueError
        else:
            print("You must select either 1, 2, 3, or 0.")


if __name__ == '__main__':
    main()

