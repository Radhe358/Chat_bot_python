
import random

def main():
    # Predefined cab rates per kilometre
    cab_rates = {
        1: ("Auto", 12),
        2: ("Sedan", 18),
        3: ("SUV", 25)
    }

    # Predefined routes: source, destination, distance
    routes = {
        1: ("Pune Station", "Shivajinagar", 5),
        2: ("Swargate", "Kothrud", 8),
        3: ("Hinjawadi", "Wakad", 10)
    }

    # Main menu loop
    while True:
        print("\n===== CAB BOOKING CHATBOT =====")
        print("1. Book Ride")
        print("2. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input! Please enter 1 or 2.")
            continue

        # Exit option
        if choice == 2:
            print("Thank you for using Cab Booking Chatbot!")
            print("Goodbye!")
            break

        # Book ride option
        elif choice == 1:
            print("\n----- Choose Cab Type -----")
            print("1. Auto - Rs. 12/km")
            print("2. Sedan - Rs. 18/km")
            print("3. SUV - Rs. 25/km")

            try:
                cab_choice = int(input("Select cab type: "))
            except ValueError:
                print("Invalid cab choice! Returning to main menu.")
                continue

            if cab_choice not in cab_rates:
                print("Invalid cab choice! Returning to main menu.")
                continue

            cab_name, rate = cab_rates[cab_choice]

            # Display predefined routes
            print("\n----- Available Routes -----")
            for number, route in routes.items():
                source, destination, distance = route
                print(
                    f"{number}. {source} to {destination} "
                    f"({distance} km)"
                )

            try:
                route_choice = int(input("Select route number: "))
            except ValueError:
                print("Invalid route choice! Returning to main menu.")
                continue

            if route_choice not in routes:
                print("Invalid route choice! Returning to main menu.")
                continue

            source, destination, distance = routes[route_choice]

            # Calculate fare
            fare = rate * distance

            # Display booking details
            print("\n===== RIDE DETAILS =====")
            print("Cab Type       :", cab_name)
            print("Source         :", source)
            print("Destination    :", destination)
            print("Distance       :", distance, "km")
            print("Rate per km    : Rs.", rate)
            print("Total Fare     : Rs.", fare)

            # Confirm or cancel before sharing OTP
            print("\n1. Confirm & Share OTP")
            print("2. Cancel Ride")

            try:
                confirm_choice = int(
                    input("Enter your choice: ")
                )
            except ValueError:
                print("Invalid confirmation choice!")
                print("Ride not confirmed. Returning to main menu.")
                continue

            if confirm_choice == 2:
                print("Ride cancelled successfully.")
                print("No OTP has been shared.")

            elif confirm_choice == 1:
                # Generate a four-digit OTP
                otp = random.randint(1000, 9999)

                print("\n===== BOOKING CONFIRMED =====")
                print("Your OTP is:", otp)
                print("Please share this OTP with your driver.")
                print("IMPORTANT: Once OTP is shared,")
                print("the ride cannot be cancelled.")

            else:
                print("Invalid confirmation choice!")
                print("Ride not confirmed. No OTP shared.")

        else:
            print("Invalid menu choice! Please select 1 or 2.")


if __name__ == "__main__":
    main()
