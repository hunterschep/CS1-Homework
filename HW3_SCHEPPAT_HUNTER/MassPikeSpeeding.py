# description: Calculate a ticket in Massachusetts state
# author: SCHEPPAT, Hunter
# date: 9.21.22


# ticket class which holds ticket object & computes fines
class Ticket:

    # compute the basic fine
    def basic_fine(self):

        # check driver was going more than 10 over
        if self.driver_Speed - self.speed_Limit > 10:
            # compute charge for 10+ over speedlimit
            self.fine = 50 + ((self.driver_Speed - (self.speed_Limit + 10)) * 10)
        else:
            self.fine = 50

        # make sure fine does not exceed state limits
        if self.fine > 500:
            self.fine = 500

    # determine fine cost if occurred in construction zone
    def construct_zone(self, stop_time, time1, time2):

        # 3x fine if between 10pm and 4am
        if stop_time >= 2200 or stop_time <= 0o400:
            self.fine *= 3

            # make sure fine is not over limit
            if self.fine > 1500:
                self.fine = 1500

        else:

            # make sure stop actually occurred inside zone time
            if time1 <= stop_time <= time2:
                self.fine *= 2

                # make sure fine is not over limit
                if self.fine > 1000:
                    self.fine = 1000
            else:
                return

    # getter method to return fine value
    def get_fine(self):
        return self.fine

    # constructor which takes 3 params: driver speed; speed limit; construction zone
    def __init__(self, driver_Speed, speed_Limit, con_zone):
        self.driver_Speed = driver_Speed
        self.speed_Limit = speed_Limit
        # initialize fine with no value
        self.fine = None
        self.con_zone = con_zone
        self.basic_fine()

        # if it was in a construction zone -> get the times & call the function
        if con_zone in ['y', 'Y']:
            time1 = float(input("Enter zone time begin in 24 hour format: "))
            time2 = float(input("Enter zone time end in 24 hour format: "))
            print("")
            stopTime = float(input("Enter stop time in 24 hour format: "))
            self.construct_zone(stopTime, time1, time2)

        # $50 head injury addition
        self.fine += 50


# explain nature of program
print("This program computes possible fines for motorists stopped on the Massachusetts Turnpike ")
print("")

# get inputs from user
speedMPH = float(input("Enter speed in MPH: "))
print("")
speedLimit = float(input("Enter speed limit in MPH: "))
print("")
conZoneInput = input("Was it in a construction zone? Enter Y or N: ")
print("")

# make sure user was actually speeding
if speedMPH > speedLimit:

    # create ticket object
    myTicket = Ticket(speedMPH, speedLimit, conZoneInput)
    the_fine = myTicket.get_fine()

    # print the final fine
    print("The fine is $ " + str(the_fine) + " Including a $50 donation to the head injury fund")

# dismiss case if not speeding
else:
    print("Case Dismissed")
