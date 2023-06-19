# This a roadside assistance program.
import datetime
import random


x = datetime.datetime.now()
print(x.strftime("\n%A %B %d %Y, %H:%M:%S"))

company = ["state farm", "liberty mutual", "connect", "usaa",
           "mazda", "american family", "progressive", "kia", "subaru"]
print("\nWelcome to RoadSide Assistance!")
# safety
safety = input(
    "\nAre you and your vehicle in a safe location? (yes, no): ").lower()
if safety == "yes":
    # company's name
    name = input("\nWe are glad that you are SAFE! Please provide your insurance company's name: (state farm, liberty mutual, connect, usaa, mazda, american family, progressive, kia, subaru): ").lower()
    if name in company:
        print(f"\nYour insurance commpay is: {name}")
# policy Number
        policy = input(
            "\nEnter your policy number. Policy should have 16 characters: ")
        if len(policy) == 16:
            print(f"\nYour policy number is: {policy}")
# VIN Number
            vin = input(
                "\nEnter your VIN number. VIN should have 17 characters: ")
            if len(vin) == 17:
                print(f"\nYour VIN number is: {vin}")
# Year
                year = int(input("\nWhat is the Year of the vehicle? "))
                print(f"\nThe Year of the vehicle is: {year}")
# Make
                make = input("\nWhat is the Make of the vehicle? ")
                print(f"\nThe Make of the vehicle is: {make}")
# Model.
                model = input("\nWhat is the Model of the vehicle? ")
                print(f"\nThe Model of the vehicle is: {model}")
# color.
                color = input("\nWhat is the Color of the vehicle? ")
                print(f"\nThe Color of the vehicle is: {color}")
# Mileage.
                mileage = int(input("\nWhat is the Mileage of the vehicle? "))
                print(f"\nThe Mileage of the vehicle is: {mileage}")
# phone Number
                phone_number = input(
                    "\nEnter your phone number, Phone Number should have 10 characters: ")
                if len(phone_number) == 10:
                    print(f"\nYour phone number is: {phone_number}")
# First and Last Name
                    fname = input("\nEnter your first name: ").capitalize()
                    lname = input("\nEnter yor last name: ").capitalize()
                    print(f"\nName: {fname} {lname}")
# Services and Type of Service.
                    services = ["tow", "jump start", "tire change",
                                "fuel delivery", "locked out", "winch"]
                    type_of_service = input(
                        "\nWhat type of service do you need today? (tow, jump start, tire change, fuel delivery, locked out, winch) ").lower()
                    if type_of_service in services:
                        print(
                            f"\nWe are sorry that you have trouble with your vehicle. We are going to set up a {type_of_service} for you.")
# Tow Service
                        if type_of_service == "tow":
                            keys = input(
                                "\nAre the keys present? (yes, no) ")
                            present = input(
                                "\nWill you be with the vehicle at the time of service? (yes, no) ")
                            if present == "yes":
                                neutral = input(
                                    "\nCan the vehicle be put in neutral? (yes, no) ")
                                types = input(
                                    "\nIs the vehicle a Four-wheel drive? (yes, no) ")
                                height = input(
                                    "\nAre you in a low clearance? (yes, no) ")
                                if height == "yes":
                                    input("\nWhat is the height? ")
                                    ride = input(
                                        "\nDo you need a ride? (yes, no) ")
                                    if ride == "yes":
                                        print(
                                            "\nWe will set up a lyft for you at the end of the request.")
                                        trailer = input(
                                            "\nIs the vehicle has a trailer attach to it? (yes, no) ")
                                        if trailer == "yes":
                                            input(
                                                "\nPlease enter the weight of the trailer: ")
# Location Type
                                            pick_up = input(
                                                "\nPlease enter your correct location. (Ex: 4721 Florida Ave S, Lakeland, FL 33813) ")
                                            print(
                                                f"\nPick up location is: {pick_up}")
                                            drop_off = input(
                                                "\nPlease enter the drop off location: (Ex: 4721 Florida Ave S, Lakeland, FL 33813)")
                                            print(
                                                f"\nPick up location is: {drop_off}")
# Notes
                                            note = input(
                                                "\nPlease add any additional information about the vehicle and your location: ")
# Notification
                                            notification = input(
                                                "\nDo you want to receive phone call or text message? (yes, no) ").lower()
                                            if notification == "yes":
                                                print(f"\n{fname} I can see that you are covered for the service, we recommand that you call the dealership and let them know your vehicle is coming in for service. When I have secured service I will send you the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. we have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
                                            else:
                                                print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. You will receive a phone and that phone call will let you know about the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. we have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
# Job ID
                                            chars = "1234567890"
                                            number = 10
                                            length = 8

                                            for _ in range(number):
                                                passwords = ""
                                                for c in range(length):
                                                    passwords += random.choice(
                                                        chars)

                                            print(
                                                f"\nYour job ID is: {passwords}")

# else trailer
                                        else:
                                            pick_up = input(
                                                "\nPlease enter your correct location. (Ex: 4721 Florida Ave S, Lakeland, FL 33813) ")
                                            print(
                                                f"\nPick up location is: {pick_up}")
                                            drop_off = input(
                                                "\nPlease enter the drop off location: (Ex: 4721 Florida Ave S, Lakeland, FL 33813)")
                                            print(
                                                f"\nPick up location is: {drop_off}")
# Notes
                                            note = input(
                                                "\nPlease add any other information about the vehicle and your location: ")
# Notification
                                            notification = input(
                                                "\nDo you want to receive phone call or text message? (yes, no) ").lower()
                                            if notification == "yes":
                                                print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. When I have secured service I will send you the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
                                            else:
                                                print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. You will receive a phone and that phone call will let you know about the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
# Job ID
                                            chars = "1234567890"
                                            number = 10
                                            length = 8

                                            for _ in range(number):
                                                passwords = ""
                                                for c in range(length):
                                                    passwords += random.choice(
                                                        chars)
                                            print(
                                                f"\nYour job ID is: {passwords}")

# else ride
                                    else:
                                        trailer = input(
                                            "\nIs the vehicle has a trailer attach to it? (yes, no) ")
                                        if trailer == "yes":
                                            input(
                                                "\nPlease enter the weight of the trailer: ")
# Location Type
                                            pick_up = input(
                                                "\nPlease enter your correct location. (Ex: 4721 Florida Ave S, Lakeland, FL 33813) ")
                                            print(
                                                f"\nPick up location is: {pick_up}")
                                            drop_off = input(
                                                "\nPlease enter the drop off location: (Ex: 4721 Florida Ave S, Lakeland, FL 33813)")
                                            print(
                                                f"\nPick up location is: {drop_off}")
# Notes
                                            note = input(
                                                "\nPlease add any other information about the vehicle and your location: ")
# Notification
                                            notification = input(
                                                "\nDo you want to receive phone call or text message? (yes, no) ").lower()
                                            if notification == "yes":
                                                print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. When I have secured service I will send you the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
                                            else:
                                                print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. You will receive a phone and that phone call will let you know about the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
# Job ID
                                                chars = "1234567890"
                                                number = 10
                                                length = 8

                                                for _ in range(number):
                                                    passwords = ""
                                                    for c in range(length):
                                                        passwords += random.choice(
                                                            chars)

                                                print(
                                                    f"\nYour job ID is: {passwords}")

# else trailer
                                        else:
                                            pick_up = input(
                                                "\nPlease enter your correct location. (Ex: 4721 Florida Ave S, Lakeland, FL 33813) ")
                                            print(
                                                f"\nPick up location is: {pick_up}")
                                            drop_off = input(
                                                "\nPlease enter the drop off location: (Ex: 4721 Florida Ave S, Lakeland, FL 33813)")
                                            print(
                                                f"\nPick up location is: {drop_off}")
# Notes
                                            note = input(
                                                "\nPlease add any other information about the vehicle and your location: ")
# Notification
                                            notification = input(
                                                "\nDo you want to receive phone call or text message? (yes, no) ").lower()
                                            if notification == "yes":
                                                print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. When I have secured service I will send you the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
                                            else:
                                                print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. You will receive a phone and that phone call will let you know about the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
# Job ID
                                            chars = "1234567890"
                                            number = 10
                                            length = 8

                                            for _ in range(number):
                                                passwords = ""
                                                for c in range(length):
                                                    passwords += random.choice(
                                                        chars)
                                            print(
                                                f"\nYour job ID is: {passwords}")

# else height
                                else:
                                    ride = input(
                                        "\nDo you need a ride? (yes, no) ")
                                    if ride == "yes":
                                        print(
                                            "\nWe will set up a lyft for you at the end of the request.")
                                        trailer = input(
                                            "\nIs the vehicle has a trailer attach to it? (yes, no) ")
                                        if trailer == "yes":
                                            input(
                                                "\nPlease enter the weight of the trailer: ")
# Location Type
                                            pick_up = input(
                                                "\nPlease enter your correct location. (Ex: 4721 Florida Ave S, Lakeland, FL 33813) ")
                                            print(
                                                f"\nPick up location is: {pick_up}")
                                            drop_off = input(
                                                "\nPlease enter the drop off location: (Ex: 4721 Florida Ave S, Lakeland, FL 33813)")
                                            print(
                                                f"\nPick up location is: {drop_off}")
# Notes
                                            note = input(
                                                "\nPlease add any other information about the vehicle and your location: ")
# Notification
                                            notification = input(
                                                "\nDo you want to receive phone call or text message? (yes, no) ").lower()
                                            if notification == "yes":
                                                print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. When I have secured service I will send you the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
                                            else:
                                                print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. You will receive a phone and that phone call will let you know about the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
# Job ID
                                            chars = "1234567890"
                                            number = 10
                                            length = 8

                                            for _ in range(number):
                                                passwords = ""
                                                for c in range(length):
                                                    passwords += random.choice(
                                                        chars)

                                            print(
                                                f"\nYour job ID is: {passwords}")

# else trailer
                                        else:
                                            pick_up = input(
                                                "\nPlease enter your correct location. (Ex: 4721 Florida Ave S, Lakeland, FL 33813) ")
                                            print(
                                                f"\nPick up location is: {pick_up}")
                                            drop_off = input(
                                                "\nPlease enter the drop off location: (Ex: 4721 Florida Ave S, Lakeland, FL 33813)")
                                            print(
                                                f"\nPick up location is: {drop_off}")
# Notes
                                            note = input(
                                                "\nPlease add any other information about the vehicle and your location: ")
# Notification
                                            notification = input(
                                                "\nDo you want to receive phone call or text message? (yes, no) ").lower()
                                            if notification == "yes":
                                                print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. When I have secured service I will send you the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
                                            else:
                                                print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. You will receive a phone and that phone call will let you know about the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
# Job ID
                                            chars = "1234567890"
                                            number = 10
                                            length = 8

                                            for _ in range(number):
                                                passwords = ""
                                                for c in range(length):
                                                    passwords += random.choice(
                                                        chars)
                                            print(
                                                f"\nYour job ID is: {passwords}")

# else ride
                                    else:
                                        trailer = input(
                                            "\nIs the vehicle has a trailer attach to it? (yes, no) ")
                                        if trailer == "yes":
                                            input(
                                                "\nPlease enter the weight of the trailer: ")
# Location Type
                                            pick_up = input(
                                                "\nPlease enter your correct location. (Ex: 4721 Florida Ave S, Lakeland, FL 33813) ")
                                            print(
                                                f"\nPick up location is: {pick_up}")
                                            drop_off = input(
                                                "\nPlease enter the drop off location: (Ex: 4721 Florida Ave S, Lakeland, FL 33813)")
                                            print(
                                                f"\nPick up location is: {drop_off}")
# Notes
                                            note = input(
                                                "\nPlease add any other information about the vehicle and your location: ")
# Notification
                                            notification = input(
                                                "\nDo you want to receive phone call or text message? (yes, no) ").lower()
                                            if notification == "yes":
                                                print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. When I have secured service I will send you the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
                                            else:
                                                print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. You will receive a phone and that phone call will let you know about the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
# Job ID
                                                chars = "1234567890"
                                                number = 10
                                                length = 8

                                                for _ in range(number):
                                                    passwords = ""
                                                    for c in range(length):
                                                        passwords += random.choice(
                                                            chars)

                                                print(
                                                    f"\nYour job ID is: {passwords}")

# else trailer
                                        else:
                                            pick_up = input(
                                                "\nPlease enter your correct location. (Ex: 4721 Florida Ave S, Lakeland, FL 33813) ")
                                            print(
                                                f"\nPick up location is: {pick_up}")
                                            drop_off = input(
                                                "\nPlease enter the drop off location: (Ex: 4721 Florida Ave S, Lakeland, FL 33813)")
                                            print(
                                                f"\nPick up location is: {drop_off}")
# Notes
                                            note = input(
                                                "\nPlease add any other information about the vehicle and your location: ")
# Notification
                                            notification = input(
                                                "\nDo you want to receive phone call or text message? (yes, no) ").lower()
                                            if notification == "yes":
                                                print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. When I have secured service I will send you the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
                                            else:
                                                print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. You will receive a phone and that phone call will let you know about the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
# Job ID
                                            chars = "1234567890"
                                            number = 10
                                            length = 8

                                            for _ in range(number):
                                                passwords = ""
                                                for c in range(length):
                                                    passwords += random.choice(
                                                        chars)
                                            print(
                                                f"\nYour job ID is: {passwords}")

# if not present
                            else:
                                input("\nPlease add the location of the keys. ")
                                neutral = input(
                                    "\nCan the vehicle be put in neutral? (yes, no) ")
                                types = input(
                                    "\nIs the the vehicle a Four-wheel drive? (yes, no) ")
                                height = input(
                                    "\nAre you in a low clearance? (yes, no) ")
                                if height == "yes":
                                    input("\nWhat is the height? ")
                                    ride = input(
                                        "\nDo you need a ride? (yes, no) ")
                                    if ride == "yes":
                                        print(
                                            "\nWe will set up a lyft for you at the end of the request.")
                                        trailer = input(
                                            "\nIs the vehicle has a trailer attach to it? (yes, no) ")
                                        if trailer == "yes":
                                            input(
                                                "\nPlease enter the weight of the trailer: ")
# Location Type
                                            pick_up = input(
                                                "\nPlease enter your correct location. (Ex: 4721 Florida Ave S, Lakeland, FL 33813) ")
                                            print(
                                                f"\nPick up location is: {pick_up}")
                                            drop_off = input(
                                                "\nPlease enter the drop off location: (Ex: 4721 Florida Ave S, Lakeland, FL 33813)")
                                            print(
                                                f"\nPick up location is: {drop_off}")
# Notes
                                            note = input(
                                                "\nPlease add any other information about the vehicle and your location: ")
# Notification
                                            notification = input(
                                                "\nDo you want to receive phone call or text message? (yes, no) ").lower()
                                            if notification == "yes":
                                                print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. When I have secured service I will send you the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
                                            else:
                                                print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. You will receive a phone and that phone call will let you know about the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
# Job ID
                                            chars = "1234567890"
                                            number = 10
                                            length = 8

                                            for _ in range(number):
                                                passwords = ""
                                                for c in range(length):
                                                    passwords += random.choice(
                                                        chars)

                                            print(
                                                f"\nYour job ID is: {passwords}")

# else trailer
                                        else:
                                            pick_up = input(
                                                "\nPlease enter your correct location. (Ex: 4721 Florida Ave S, Lakeland, FL 33813) ")
                                            print(
                                                f"\nPick up location is: {pick_up}")
                                            drop_off = input(
                                                "\nPlease enter the drop off location: (Ex: 4721 Florida Ave S, Lakeland, FL 33813)")
                                            print(
                                                f"\nPick up location is: {drop_off}")
# Notes
                                            note = input(
                                                "\nPlease add any other information about the vehicle and your location: ")
# Notification
                                            notification = input(
                                                "\nDo you want to receive phone call or text message? (yes, no) ").lower()
                                            if notification == "yes":
                                                print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. When I have secured service I will send you the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
                                            else:
                                                print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. You will receive a phone and that phone call will let you know about the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
# Job ID
                                            chars = "1234567890"
                                            number = 10
                                            length = 8

                                            for _ in range(number):
                                                passwords = ""
                                                for c in range(length):
                                                    passwords += random.choice(
                                                        chars)
                                            print(
                                                f"\nYour job ID is: {passwords}")

# else ride
                                    else:
                                        trailer = input(
                                            "\nIs the vehicle has a trailer attach to it? (yes, no) ")
                                        if trailer == "yes":
                                            input(
                                                "\nPlease enter the weight of the trailer: ")
# Location Type
                                            pick_up = input(
                                                "\nPlease enter your correct location. (Ex: 4721 Florida Ave S, Lakeland, FL 33813) ")
                                            print(
                                                f"\nPick up location is: {pick_up}")
                                            drop_off = input(
                                                "\nPlease enter the drop off location: (Ex: 4721 Florida Ave S, Lakeland, FL 33813)")
                                            print(
                                                f"\nPick up location is: {drop_off}")
# Notes
                                            note = input(
                                                "\nPlease add any other information about the vehicle and your location: ")
# Notification
                                            notification = input(
                                                "\nDo you want to receive phone call or text message? (yes, no) ").lower()
                                            if notification == "yes":
                                                print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. When I have secured service I will send you the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
                                            else:
                                                print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. You will receive a phone and that phone call will let you know about the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
# Job ID
                                                chars = "1234567890"
                                                number = 10
                                                length = 8

                                                for _ in range(number):
                                                    passwords = ""
                                                    for c in range(length):
                                                        passwords += random.choice(
                                                            chars)

                                                print(
                                                    f"\nYour job ID is: {passwords}")

# else trailer
                                        else:
                                            pick_up = input(
                                                "\nPlease enter your correct location. (Ex: 4721 Florida Ave S, Lakeland, FL 33813) ")
                                            print(
                                                f"\nPick up location is: {pick_up}")
                                            drop_off = input(
                                                "\nPlease enter the drop off location: (Ex: 4721 Florida Ave S, Lakeland, FL 33813)")
                                            print(
                                                f"\nPick up location is: {drop_off}")
# Notes
                                            note = input(
                                                "\nPlease add any other information about the vehicle and your location: ")
# Notification
                                            notification = input(
                                                "\nDo you want to receive phone call or text message? (yes, no) ").lower()
                                            if notification == "yes":
                                                print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. When I have secured service I will send you the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
                                            else:
                                                print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. You will receive a phone and that phone call will let you know about the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
# Job ID
                                            chars = "1234567890"
                                            number = 10
                                            length = 8

                                            for _ in range(number):
                                                passwords = ""
                                                for c in range(length):
                                                    passwords += random.choice(
                                                        chars)
                                            print(
                                                f"\nYour job ID is: {passwords}")

# else height
                                else:
                                    ride = input(
                                        "\nDo you need a ride? (yes, no) ")
                                    if ride == "yes":
                                        print(
                                            "\nWe will set up a lyft for you at the end of the request.")
                                        trailer = input(
                                            "\nIs the vehicle has a trailer attach to it? (yes, no) ")
                                        if trailer == "yes":
                                            input(
                                                "\nPlease enter the weight of the trailer: ")
# Location Type
                                            pick_up = input(
                                                "\nPlease enter your correct location. (Ex: 4721 Florida Ave S, Lakeland, FL 33813) ")
                                            print(
                                                f"\nPick up location is: {pick_up}")
                                            drop_off = input(
                                                "\nPlease enter the drop off location: (Ex: 4721 Florida Ave S, Lakeland, FL 33813)")
                                            print(
                                                f"\nPick up location is: {drop_off}")
# Notes
                                            note = input(
                                                "\nPlease add any other information about the vehicle and your location: ")
# Notification
                                            notification = input(
                                                "\nDo you want to receive phone call or text message? (yes, no) ").lower()
                                            if notification == "yes":
                                                print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. When I have secured service I will send you the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
                                            else:
                                                print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. You will receive a phone and that phone call will let you know about the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
# Job ID
                                            chars = "1234567890"
                                            number = 10
                                            length = 8

                                            for _ in range(number):
                                                passwords = ""
                                                for c in range(length):
                                                    passwords += random.choice(
                                                        chars)

                                            print(
                                                f"\nYour job ID is: {passwords}")

# else trailer
                                        else:
                                            pick_up = input(
                                                "\nPlease enter your correct location. (Ex: 4721 Florida Ave S, Lakeland, FL 33813) ")
                                            print(
                                                f"\nPick up location is: {pick_up}")
                                            drop_off = input(
                                                "\nPlease enter the drop off location: (Ex: 4721 Florida Ave S, Lakeland, FL 33813)")
                                            print(
                                                f"\nPick up location is: {drop_off}")
# Notes
                                            note = input(
                                                "\nPlease add any other information about the vehicle and your location: ")
# Notification
                                            notification = input(
                                                "\nDo you want to receive phone call or text message? (yes, no) ").lower()
                                            if notification == "yes":
                                                print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. When I have secured service I will send you the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
                                            else:
                                                print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. You will receive a phone and that phone call will let you know about the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
# Job ID
                                            chars = "1234567890"
                                            number = 10
                                            length = 8

                                            for _ in range(number):
                                                passwords = ""
                                                for c in range(length):
                                                    passwords += random.choice(
                                                        chars)

                                            print(
                                                f"\nYour job ID is: {passwords}")

# else ride
                                    else:
                                        trailer = input(
                                            "\nIs the vehicle has a trailer attach to it? (yes, no) ")
                                        if trailer == "yes":
                                            input(
                                                "\nPlease enter the weight of the trailer: ")
# Location Type
                                            pick_up = input(
                                                "\nPlease enter your correct location. (Ex: 4721 Florida Ave S, Lakeland, FL 33813) ")
                                            print(
                                                f"\nPick up location is: {pick_up}")
                                            drop_off = input(
                                                "\nPlease enter the drop off location: (Ex: 4721 Florida Ave S, Lakeland, FL 33813)")
                                            print(
                                                f"\nPick up location is: {drop_off}")
# Notes
                                            note = input(
                                                "\nPlease add any other information about the vehicle and your location: ")
# Notification
                                            notification = input(
                                                "\nDo you want to receive phone call or text message? (yes, no) ").lower()
                                            if notification == "yes":
                                                print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. When I have secured service I will send you the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
                                            else:
                                                print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. You will receive a phone and that phone call will let you know about the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
# Job ID
                                                chars = "1234567890"
                                                number = 10
                                                length = 8

                                                for _ in range(number):
                                                    passwords = ""
                                                    for c in range(length):
                                                        passwords += random.choice(
                                                            chars)

                                                print(
                                                    f"\nYour job ID is: {passwords}")

# else trailer
                                        else:
                                            pick_up = input(
                                                "\nPlease enter your correct location. (Ex: 4721 Florida Ave S, Lakeland, FL 33813) ")
                                            print(
                                                f"\nPick up location is: {pick_up}")
                                            drop_off = input(
                                                "\nPlease enter the drop off location: (Ex: 4721 Florida Ave S, Lakeland, FL 33813)")
                                            print(
                                                f"\nPick up location is: {drop_off}")
# Notes
                                            note = input(
                                                "\nPlease add any other information about the vehicle and your location: ")
# Notification
                                            notification = input(
                                                "\nDo you want to receive phone call or text message? (yes, no) ").lower()
                                            if notification == "yes":
                                                print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. When I have secured service I will send you the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
                                            else:
                                                print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. You will receive a phone and that phone call will let you know about the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
# Job ID
                                            chars = "1234567890"
                                            number = 10
                                            length = 8

                                            for _ in range(number):
                                                passwords = ""
                                                for c in range(length):
                                                    passwords += random.choice(
                                                        chars)

                                            print(
                                                f"\nYour job ID is: {passwords}")


# Jump Start
                        elif type_of_service == "jump start":
                            keys = input(
                                "\nAre the keys present? (yes, no) ")
                            present = input(
                                "\nWill you be with the vehicle at the time of service? (yes, no) ")
                            if present == "yes":
                                stall = input(
                                    "\nDid the vehicle stop when running? (yes, no) ")
                                if stall == "yes":
                                    print(
                                        "\nSince that happened you will need a TOW SERICE.")
                                    neutral = input(
                                        "\nCan the vehicle be put in neutral? (yes, no) ")
                                    types = input(
                                        "\nIs the the vehicle a Four-wheel drive? (yes, no) ")
                                    height = input(
                                        "\nAre you in a low clearance? (yes, no) ")
                                    if height == "yes":
                                        input("\nWhat is the height? ")
                                        ride = input(
                                            "\nDo you need a ride? (yes, no) ")
                                        if ride == "yes":
                                            print(
                                                "\nWe will set up a lyft for you at the end of the request.")
                                            trailer = input(
                                                "\nIs the vehicle has a trailer attach to it? (yes, no) ")
                                            if trailer == "yes":
                                                input(
                                                    "\nPlease enter the weight of the trailer: ")
# Location Type
                                                pick_up = input(
                                                    "\nPlease enter your correct location. (Ex: 4721 Florida Ave S, Lakeland, FL 33813) ")
                                                print(
                                                    f"\nPick up location is: {pick_up}")
                                                drop_off = input(
                                                    "\nPlease enter the drop off location: (Ex: 4721 Florida Ave S, Lakeland, FL 33813)")
                                                print(
                                                    f"\nPick up location is: {drop_off}")
    # Notes
                                                note = input(
                                                    "\nPlease add any other information about the vehicle and your location: ")
    # Notification
                                                notification = input(
                                                    "\nDo you want to receive phone call or text message? (yes, no) ").lower()
                                                if notification == "yes":
                                                    print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. When I have secured service I will send you the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
                                                else:
                                                    print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. You will receive a phone and that phone call will let you know about the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
    # Job ID
                                                chars = "1234567890"
                                                number = 10
                                                length = 8

                                                for _ in range(number):
                                                    passwords = ""
                                                    for c in range(length):
                                                        passwords += random.choice(
                                                            chars)

                                                print(
                                                    f"\nYour job ID is: {passwords}")
    # else trailer
                                            else:
                                                pick_up = input(
                                                    "\nPlease enter your correct location. (Ex: 4721 Florida Ave S, Lakeland, FL 33813) ")
                                                print(
                                                    f"\nPick up location is: {pick_up}")
                                                drop_off = input(
                                                    "\nPlease enter the drop off location: (Ex: 4721 Florida Ave S, Lakeland, FL 33813)")
                                                print(
                                                    f"\nPick up location is: {drop_off}")
    # Notes
                                                note = input(
                                                    "\nPlease add any other information about the vehicle and your location: ")
    # Notification
                                                notification = input(
                                                    "\nDo you want to receive phone call or text message? (yes, no) ").lower()
                                                if notification == "yes":
                                                    print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. When I have secured service I will send you the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
                                                else:
                                                    print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. You will receive a phone and that phone call will let you know about the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
    # Job ID
                                                chars = "1234567890"
                                                number = 10
                                                length = 8

                                                for _ in range(number):
                                                    passwords = ""
                                                    for c in range(length):
                                                        passwords += random.choice(
                                                            chars)
                                                print(
                                                    f"\nYour job ID is: {passwords}")
    # else ride
                                        else:
                                            trailer = input(
                                                "\nIs the vehicle has a trailer attach to it? (yes, no) ")
                                            if trailer == "yes":
                                                input(
                                                    "\nPlease enter the weight of the trailer: ")
    # Location Type
                                                pick_up = input(
                                                    "\nPlease enter your correct location. (Ex: 4721 Florida Ave S, Lakeland, FL 33813) ")
                                                print(
                                                    f"\nPick up location is: {pick_up}")
                                                drop_off = input(
                                                    "\nPlease enter the drop off location: (Ex: 4721 Florida Ave S, Lakeland, FL 33813)")
                                                print(
                                                    f"\nPick up location is: {drop_off}")
    # Notes
                                                note = input(
                                                    "\nPlease add any other information about the vehicle and your location: ")
    # Notification
                                                notification = input(
                                                    "\nDo you want to receive phone call or text message? (yes, no) ").lower()
                                                if notification == "yes":
                                                    print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. When I have secured service I will send you the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
                                                else:
                                                    print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. You will receive a phone and that phone call will let you know about the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
    # Job ID
                                                    chars = "1234567890"
                                                    number = 10
                                                    length = 8

                                                    for _ in range(number):
                                                        passwords = ""
                                                        for c in range(length):
                                                            passwords += random.choice(
                                                                chars)

                                                    print(
                                                        f"\nYour job ID is: {passwords}")
    # else trailer
                                            else:
                                                pick_up = input(
                                                    "\nPlease enter your correct location. (Ex: 4721 Florida Ave S, Lakeland, FL 33813) ")
                                                print(
                                                    f"\nPick up location is: {pick_up}")
                                                drop_off = input(
                                                    "\nPlease enter the drop off location: (Ex: 4721 Florida Ave S, Lakeland, FL 33813)")
                                                print(
                                                    f"\nPick up location is: {drop_off}")
    # Notes
                                                note = input(
                                                    "\nPlease add any other information about the vehicle and your location: ")
    # Notification
                                                notification = input(
                                                    "\nDo you want to receive phone call or text message? (yes, no) ").lower()
                                                if notification == "yes":
                                                    print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. When I have secured service I will send you the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
                                                else:
                                                    print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. You will receive a phone and that phone call will let you know about the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
    # Job ID
                                                chars = "1234567890"
                                                number = 10
                                                length = 8

                                                for _ in range(number):
                                                    passwords = ""
                                                    for c in range(length):
                                                        passwords += random.choice(
                                                            chars)
                                                print(
                                                    f"\nYour job ID is: {passwords}")
    # else height
                                    else:
                                        ride = input(
                                            "\nDo you need a ride? (yes, no) ")
                                        if ride == "yes":
                                            print(
                                                "\nWe will set up a lyft for you at the end of the request.")
                                            trailer = input(
                                                "\nIs the vehicle has a trailer attach to it? (yes, no) ")
                                            if trailer == "yes":
                                                input(
                                                    "\nPlease enter the weight of the trailer: ")
    # Location Type
                                                pick_up = input(
                                                    "\nPlease enter your correct location. (Ex: 4721 Florida Ave S, Lakeland, FL 33813) ")
                                                print(
                                                    f"\nPick up location is: {pick_up}")
                                                drop_off = input(
                                                    "\nPlease enter the drop off location: (Ex: 4721 Florida Ave S, Lakeland, FL 33813)")
                                                print(
                                                    f"\nPick up location is: {drop_off}")
    # Notes
                                                note = input(
                                                    "\nPlease add any other information about the vehicle and your location: ")
    # Notification
                                                notification = input(
                                                    "\nDo you want to receive phone call or text message? (yes, no) ").lower()
                                                if notification == "yes":
                                                    print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. When I have secured service I will send you the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
                                                else:
                                                    print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. You will receive a phone and that phone call will let you know about the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
    # Job ID
                                                chars = "1234567890"
                                                number = 10
                                                length = 8

                                                for _ in range(number):
                                                    passwords = ""
                                                    for c in range(length):
                                                        passwords += random.choice(
                                                            chars)

                                                print(
                                                    f"\nYour job ID is: {passwords}")
    # else trailer
                                            else:
                                                pick_up = input(
                                                    "\nPlease enter your correct location. (Ex: 4721 Florida Ave S, Lakeland, FL 33813) ")
                                                print(
                                                    f"\nPick up location is: {pick_up}")
                                                drop_off = input(
                                                    "\nPlease enter the drop off location: (Ex: 4721 Florida Ave S, Lakeland, FL 33813)")
                                                print(
                                                    f"\nPick up location is: {drop_off}")
    # Notes
                                                note = input(
                                                    "\nPlease add any other information about the vehicle and your location: ")
    # Notification
                                                notification = input(
                                                    "\nDo you want to receive phone call or text message? (yes, no) ").lower()
                                                if notification == "yes":
                                                    print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. When I have secured service I will send you the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
                                                else:
                                                    print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. You will receive a phone and that phone call will let you know about the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
    # Job ID
                                                chars = "1234567890"
                                                number = 10
                                                length = 8

                                                for _ in range(number):
                                                    passwords = ""
                                                    for c in range(length):
                                                        passwords += random.choice(
                                                            chars)
                                                print(
                                                    f"\nYour job ID is: {passwords}")
    # else ride
                                        else:
                                            trailer = input(
                                                "\nIs the vehicle has a trailer attach to it? (yes, no) ")
                                            if trailer == "yes":
                                                input(
                                                    "\nPlease enter the weight of the trailer: ")
    # Location Type
                                                pick_up = input(
                                                    "\nPlease enter your correct location. (Ex: 4721 Florida Ave S, Lakeland, FL 33813) ")
                                                print(
                                                    f"\nPick up location is: {pick_up}")
                                                drop_off = input(
                                                    "\nPlease enter the drop off location: (Ex: 4721 Florida Ave S, Lakeland, FL 33813)")
                                                print(
                                                    f"\nPick up location is: {drop_off}")
    # Notes
                                                note = input(
                                                    "\nPlease add any other information about the vehicle and your location: ")
    # Notification
                                                notification = input(
                                                    "\nDo you want to receive phone call or text message? (yes, no) ").lower()
                                                if notification == "yes":
                                                    print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. When I have secured service I will send you the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
                                                else:
                                                    print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. You will receive a phone and that phone call will let you know about the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
    # Job ID
                                                    chars = "1234567890"
                                                    number = 10
                                                    length = 8

                                                    for _ in range(number):
                                                        passwords = ""
                                                        for c in range(length):
                                                            passwords += random.choice(
                                                                chars)

                                                    print(
                                                        f"\nYour job ID is: {passwords}")
    # else trailer
                                            else:
                                                pick_up = input(
                                                    "\nPlease enter your correct location. (Ex: 4721 Florida Ave S, Lakeland, FL 33813) ")
                                                print(
                                                    f"\nPick up location is: {pick_up}")
                                                drop_off = input(
                                                    "\nPlease enter the drop off location: (Ex: 4721 Florida Ave S, Lakeland, FL 33813)")
                                                print(
                                                    f"\nPick up location is: {drop_off}")
    # Notes
                                                note = input(
                                                    "\nPlease add any other information about the vehicle and your location: ")
    # Notification
                                                notification = input(
                                                    "\nDo you want to receive phone call or text message? (yes, no) ").lower()
                                                if notification == "yes":
                                                    print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. When I have secured service I will send you the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
                                                else:
                                                    print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. You will receive a phone and that phone call will let you know about the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
    # Job ID
                                                chars = "1234567890"
                                                number = 10
                                                length = 8

                                                for _ in range(number):
                                                    passwords = ""
                                                    for c in range(length):
                                                        passwords += random.choice(
                                                            chars)
                                                print(
                                                    f"\nYour job ID is: {passwords}")

# attempt
                                else:
                                    attempt = input(
                                        "Have you attempted a jump start yet? (yes, no) ")
                                    if attempt == "yes":
                                        print(
                                            "\nSince that happened you will need a TOW SERICE.")
                                        neutral = input(
                                            "\nCan the vehicle be put in neutral? (yes, no) ")
                                        types = input(
                                            "\nIs the the vehicle a Four-wheel drive? (yes, no) ")
                                        height = input(
                                            "\nAre you in a low clearance? (yes, no) ")
                                        if height == "yes":
                                            input("\nWhat is the height? ")
                                            ride = input(
                                                "\nDo you need a ride? (yes, no) ")
                                            if ride == "yes":
                                                print(
                                                    "\nWe will set up a lyft for you at the end of the request.")
                                                trailer = input(
                                                    "\nIs the vehicle has a trailer attach to it? (yes, no) ")
                                                if trailer == "yes":
                                                    input(
                                                        "\nPlease enter the weight of the trailer: ")
    # Location Type
                                                    pick_up = input(
                                                        "\nPlease enter your correct location. (Ex: 4721 Florida Ave S, Lakeland, FL 33813) ")
                                                    print(
                                                        f"\nPick up location is: {pick_up}")
                                                    drop_off = input(
                                                        "\nPlease enter the drop off location: (Ex: 4721 Florida Ave S, Lakeland, FL 33813)")
                                                    print(
                                                        f"\nPick up location is: {drop_off}")
        # Notes
                                                    note = input(
                                                        "\nPlease add any other information about the vehicle and your location: ")
        # Notification
                                                    notification = input(
                                                        "\nDo you want to receive phone call or text message? (yes, no) ").lower()
                                                    if notification == "yes":
                                                        print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. When I have secured service I will send you the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
                                                    else:
                                                        print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. You will receive a phone and that phone call will let you know about the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
        # Job ID
                                                    chars = "1234567890"
                                                    number = 10
                                                    length = 8

                                                    for _ in range(number):
                                                        passwords = ""
                                                        for c in range(length):
                                                            passwords += random.choice(
                                                                chars)

                                                    print(
                                                        f"\nYour job ID is: {passwords}")
        # else trailer
                                                else:
                                                    pick_up = input(
                                                        "\nPlease enter your correct location. (Ex: 4721 Florida Ave S, Lakeland, FL 33813) ")
                                                    print(
                                                        f"\nPick up location is: {pick_up}")
                                                    drop_off = input(
                                                        "\nPlease enter the drop off location: (Ex: 4721 Florida Ave S, Lakeland, FL 33813)")
                                                    print(
                                                        f"\nPick up location is: {drop_off}")
        # Notes
                                                    note = input(
                                                        "\nPlease add any other information about the vehicle and your location: ")
        # Notification
                                                    notification = input(
                                                        "\nDo you want to receive phone call or text message? (yes, no) ").lower()
                                                    if notification == "yes":
                                                        print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. When I have secured service I will send you the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
                                                    else:
                                                        print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. You will receive a phone and that phone call will let you know about the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
        # Job ID
                                                    chars = "1234567890"
                                                    number = 10
                                                    length = 8

                                                    for _ in range(number):
                                                        passwords = ""
                                                        for c in range(length):
                                                            passwords += random.choice(
                                                                chars)
                                                    print(
                                                        f"\nYour job ID is: {passwords}")
        # else ride
                                            else:
                                                trailer = input(
                                                    "\nIs the vehicle has a trailer attach to it? (yes, no) ")
                                                if trailer == "yes":
                                                    input(
                                                        "\nPlease enter the weight of the trailer: ")
        # Location Type
                                                    pick_up = input(
                                                        "\nPlease enter your correct location. (Ex: 4721 Florida Ave S, Lakeland, FL 33813) ")
                                                    print(
                                                        f"\nPick up location is: {pick_up}")
                                                    drop_off = input(
                                                        "\nPlease enter the drop off location: (Ex: 4721 Florida Ave S, Lakeland, FL 33813)")
                                                    print(
                                                        f"\nPick up location is: {drop_off}")
        # Notes
                                                    note = input(
                                                        "\nPlease add any other information about the vehicle and your location: ")
        # Notification
                                                    notification = input(
                                                        "\nDo you want to receive phone call or text message? (yes, no) ").lower()
                                                    if notification == "yes":
                                                        print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. When I have secured service I will send you the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
                                                    else:
                                                        print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. You will receive a phone and that phone call will let you know about the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
        # Job ID
                                                        chars = "1234567890"
                                                        number = 10
                                                        length = 8

                                                        for _ in range(number):
                                                            passwords = ""
                                                            for c in range(length):
                                                                passwords += random.choice(
                                                                    chars)

                                                        print(
                                                            f"\nYour job ID is: {passwords}")
        # else trailer
                                                else:
                                                    pick_up = input(
                                                        "\nPlease enter your correct location. (Ex: 4721 Florida Ave S, Lakeland, FL 33813) ")
                                                    print(
                                                        f"\nPick up location is: {pick_up}")
                                                    drop_off = input(
                                                        "\nPlease enter the drop off location: (Ex: 4721 Florida Ave S, Lakeland, FL 33813)")
                                                    print(
                                                        f"\nPick up location is: {drop_off}")
        # Notes
                                                    note = input(
                                                        "\nPlease add any other information about the vehicle and your location: ")
        # Notification
                                                    notification = input(
                                                        "\nDo you want to receive phone call or text message? (yes, no) ").lower()
                                                    if notification == "yes":
                                                        print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. When I have secured service I will send you the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
                                                    else:
                                                        print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. You will receive a phone and that phone call will let you know about the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
        # Job ID
                                                    chars = "1234567890"
                                                    number = 10
                                                    length = 8

                                                    for _ in range(number):
                                                        passwords = ""
                                                        for c in range(length):
                                                            passwords += random.choice(
                                                                chars)
                                                    print(
                                                        f"\nYour job ID is: {passwords}")
        # else height
                                        else:
                                            ride = input(
                                                "\nDo you need a ride? (yes, no) ")
                                            if ride == "yes":
                                                print(
                                                    "\nWe will set up a lyft for you at the end of the request.")
                                                trailer = input(
                                                    "\nIs the vehicle has a trailer attach to it? (yes, no) ")
                                                if trailer == "yes":
                                                    input(
                                                        "\nPlease enter the weight of the trailer: ")
        # Location Type
                                                    pick_up = input(
                                                        "\nPlease enter your correct location. (Ex: 4721 Florida Ave S, Lakeland, FL 33813) ")
                                                    print(
                                                        f"\nPick up location is: {pick_up}")
                                                    drop_off = input(
                                                        "\nPlease enter the drop off location: (Ex: 4721 Florida Ave S, Lakeland, FL 33813)")
                                                    print(
                                                        f"\nPick up location is: {drop_off}")
        # Notes
                                                    note = input(
                                                        "\nPlease add any other information about the vehicle and your location: ")
        # Notification
                                                    notification = input(
                                                        "\nDo you want to receive phone call or text message? (yes, no) ").lower()
                                                    if notification == "yes":
                                                        print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. When I have secured service I will send you the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
                                                    else:
                                                        print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. You will receive a phone and that phone call will let you know about the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
        # Job ID
                                                    chars = "1234567890"
                                                    number = 10
                                                    length = 8

                                                    for _ in range(number):
                                                        passwords = ""
                                                        for c in range(length):
                                                            passwords += random.choice(
                                                                chars)

                                                    print(
                                                        f"\nYour job ID is: {passwords}")
        # else trailer
                                                else:
                                                    pick_up = input(
                                                        "\nPlease enter your correct location. (Ex: 4721 Florida Ave S, Lakeland, FL 33813) ")
                                                    print(
                                                        f"\nPick up location is: {pick_up}")
                                                    drop_off = input(
                                                        "\nPlease enter the drop off location: (Ex: 4721 Florida Ave S, Lakeland, FL 33813)")
                                                    print(
                                                        f"\nPick up location is: {drop_off}")
        # Notes
                                                    note = input(
                                                        "\nPlease add any other information about the vehicle and your location: ")
        # Notification
                                                    notification = input(
                                                        "\nDo you want to receive phone call or text message? (yes, no) ").lower()
                                                    if notification == "yes":
                                                        print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. When I have secured service I will send you the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
                                                    else:
                                                        print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. You will receive a phone and that phone call will let you know about the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
        # Job ID
                                                    chars = "1234567890"
                                                    number = 10
                                                    length = 8

                                                    for _ in range(number):
                                                        passwords = ""
                                                        for c in range(length):
                                                            passwords += random.choice(
                                                                chars)
                                                    print(
                                                        f"\nYour job ID is: {passwords}")
        # else ride
                                            else:
                                                trailer = input(
                                                    "\nIs the vehicle has a trailer attach to it? (yes, no) ")
                                                if trailer == "yes":
                                                    input(
                                                        "\nPlease enter the weight of the trailer: ")
        # Location Type
                                                    pick_up = input(
                                                        "\nPlease enter your correct location. (Ex: 4721 Florida Ave S, Lakeland, FL 33813) ")
                                                    print(
                                                        f"\nPick up location is: {pick_up}")
                                                    drop_off = input(
                                                        "\nPlease enter the drop off location: (Ex: 4721 Florida Ave S, Lakeland, FL 33813)")
                                                    print(
                                                        f"\nPick up location is: {drop_off}")
        # Notes
                                                    note = input(
                                                        "\nPlease add any other information about the vehicle and your location: ")
        # Notification
                                                    notification = input(
                                                        "\nDo you want to receive phone call or text message? (yes, no) ").lower()
                                                    if notification == "yes":
                                                        print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. When I have secured service I will send you the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
                                                    else:
                                                        print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. You will receive a phone and that phone call will let you know about the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
        # Job ID
                                                        chars = "1234567890"
                                                        number = 10
                                                        length = 8

                                                        for _ in range(number):
                                                            passwords = ""
                                                            for c in range(length):
                                                                passwords += random.choice(
                                                                    chars)

                                                        print(
                                                            f"\nYour job ID is: {passwords}")
        # else trailer
                                                else:
                                                    pick_up = input(
                                                        "\nPlease enter your correct location. (Ex: 4721 Florida Ave S, Lakeland, FL 33813) ")
                                                    print(
                                                        f"\nPick up location is: {pick_up}")
                                                    drop_off = input(
                                                        "\nPlease enter the drop off location: (Ex: 4721 Florida Ave S, Lakeland, FL 33813)")
                                                    print(
                                                        f"\nPick up location is: {drop_off}")
        # Notes
                                                    note = input(
                                                        "\nPlease add any other information about the vehicle and your location: ")
        # Notification
                                                    notification = input(
                                                        "\nDo you want to receive phone call or text message? (yes, no) ").lower()
                                                    if notification == "yes":
                                                        print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. When I have secured service I will send you the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
                                                    else:
                                                        print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. You will receive a phone and that phone call will let you know about the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
        # Job ID
                                                    chars = "1234567890"
                                                    number = 10
                                                    length = 8

                                                    for _ in range(number):
                                                        passwords = ""
                                                        for c in range(length):
                                                            passwords += random.choice(
                                                                chars)
                                                    print(
                                                        f"\nYour job ID is: {passwords}")
    # if not attempted = height
                                    else:
                                        height = input(
                                            "\nAre you in a low clearance? (yes, no) ")
                                        if height == "yes":
                                            input("\nWhat is the height? ")
        # Location Type
                                            pick_up = input(
                                                "\nPlease enter your correct location. (Ex: 4721 Florida Ave S, Lakeland, FL 33813) ")
                                            print(
                                                f"\nPick up location is: {pick_up}")
        # Notes
                                            note = input(
                                                "\nPlease add any other information about the vehicle and your location: ")
        # Notification
                                            notification = input(
                                                "\nDo you want to receive phone call or text message? (yes, no) ").lower()
                                            if notification == "yes":
                                                print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. When I have secured service I will send you the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
                                            else:
                                                print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. You will receive a phone and that phone call will let you know about the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")

        # Job ID
                                            chars = "1234567890"
                                            number = 10
                                            length = 8

                                            for _ in range(number):
                                                passwords = ""
                                                for c in range(length):
                                                    passwords += random.choice(
                                                        chars)

                                            print(
                                                f"\nYour job ID is: {passwords}")
        # if no height
                                        else:
                                            # Location Type
                                            pick_up = input(
                                                "\nPlease enter your correct location. (Ex: 4721 Florida Ave S, Lakeland, FL 33813) ")
                                            print(
                                                f"\nPick up location is: {pick_up}")
        # Notes
                                            note = input(
                                                "\nPlease add any other information about the vehicle and your location: ")
        # Notification
                                            notification = input(
                                                "\nDo you want to receive phone call or text message? (yes, no) ").lower()
                                            if notification == "yes":
                                                print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. When I have secured service I will send you the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
                                            else:
                                                print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. You will receive a phone and that phone call will let you know about the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")

        # Job ID
                                            chars = "1234567890"
                                            number = 10
                                            length = 8

                                            for _ in range(number):
                                                passwords = ""
                                                for c in range(length):
                                                    passwords += random.choice(
                                                        chars)

                                            print(
                                                f"\nYour job ID is: {passwords}")


# If not present
                            else:
                                print(
                                    "Someone must be there in order to get service.")
                                stall = input(
                                    "\nDid the vehicle stop when running? (yes, no) ")
                                if stall == "yes":
                                    print(
                                        "\nSince that happened you will need a TOW SERICE.")
                                    neutral = input(
                                        "\nCan the vehicle be put in neutral? (yes, no) ")
                                    types = input(
                                        "\nIs the the vehicle a Four-wheel drive? (yes, no) ")
                                    height = input(
                                        "\nAre you in a low clearance? (yes, no) ")
                                    if height == "yes":
                                        input("\nWhat is the height? ")
                                        ride = input(
                                            "\nDo you need a ride? (yes, no) ")
                                        if ride == "yes":
                                            print(
                                                "\nWe will set up a lyft for you at the end of the request.")
                                            trailer = input(
                                                "\nIs the vehicle has a trailer attach to it? (yes, no) ")
                                            if trailer == "yes":
                                                input(
                                                    "\nPlease enter the weight of the trailer: ")
# Location Type
                                                pick_up = input(
                                                    "\nPlease enter your correct location. (Ex: 4721 Florida Ave S, Lakeland, FL 33813) ")
                                                print(
                                                    f"\nPick up location is: {pick_up}")
                                                drop_off = input(
                                                    "\nPlease enter the drop off location: (Ex: 4721 Florida Ave S, Lakeland, FL 33813)")
                                                print(
                                                    f"\nPick up location is: {drop_off}")
    # Notes
                                                note = input(
                                                    "\nPlease add any other information about the vehicle and your location: ")
    # Notification
                                                notification = input(
                                                    "\nDo you want to receive phone call or text message? (yes, no) ").lower()
                                                if notification == "yes":
                                                    print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. When I have secured service I will send you the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
                                                else:
                                                    print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. You will receive a phone and that phone call will let you know about the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
    # Job ID
                                                chars = "1234567890"
                                                number = 10
                                                length = 8

                                                for _ in range(number):
                                                    passwords = ""
                                                    for c in range(length):
                                                        passwords += random.choice(
                                                            chars)

                                                print(
                                                    f"\nYour job ID is: {passwords}")
    # else trailer
                                            else:
                                                pick_up = input(
                                                    "\nPlease enter your correct location. (Ex: 4721 Florida Ave S, Lakeland, FL 33813) ")
                                                print(
                                                    f"\nPick up location is: {pick_up}")
                                                drop_off = input(
                                                    "\nPlease enter the drop off location: (Ex: 4721 Florida Ave S, Lakeland, FL 33813)")
                                                print(
                                                    f"\nPick up location is: {drop_off}")
    # Notes
                                                note = input(
                                                    "\nPlease add any other information about the vehicle and your location: ")
    # Notification
                                                notification = input(
                                                    "\nDo you want to receive phone call or text message? (yes, no) ").lower()
                                                if notification == "yes":
                                                    print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. When I have secured service I will send you the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
                                                else:
                                                    print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. You will receive a phone and that phone call will let you know about the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
    # Job ID
                                                chars = "1234567890"
                                                number = 10
                                                length = 8

                                                for _ in range(number):
                                                    passwords = ""
                                                    for c in range(length):
                                                        passwords += random.choice(
                                                            chars)
                                                print(
                                                    f"\nYour job ID is: {passwords}")
    # else ride
                                        else:
                                            trailer = input(
                                                "\nIs the vehicle has a trailer attach to it? (yes, no) ")
                                            if trailer == "yes":
                                                input(
                                                    "\nPlease enter the weight of the trailer: ")
    # Location Type
                                                pick_up = input(
                                                    "\nPlease enter your correct location. (Ex: 4721 Florida Ave S, Lakeland, FL 33813) ")
                                                print(
                                                    f"\nPick up location is: {pick_up}")
                                                drop_off = input(
                                                    "\nPlease enter the drop off location: (Ex: 4721 Florida Ave S, Lakeland, FL 33813)")
                                                print(
                                                    f"\nPick up location is: {drop_off}")
    # Notes
                                                note = input(
                                                    "\nPlease add any other information about the vehicle and your location: ")
    # Notification
                                                notification = input(
                                                    "\nDo you want to receive phone call or text message? (yes, no) ").lower()
                                                if notification == "yes":
                                                    print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. When I have secured service I will send you the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
                                                else:
                                                    print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. You will receive a phone and that phone call will let you know about the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
    # Job ID
                                                    chars = "1234567890"
                                                    number = 10
                                                    length = 8

                                                    for _ in range(number):
                                                        passwords = ""
                                                        for c in range(length):
                                                            passwords += random.choice(
                                                                chars)

                                                    print(
                                                        f"\nYour job ID is: {passwords}")
    # else trailer
                                            else:
                                                pick_up = input(
                                                    "\nPlease enter your correct location. (Ex: 4721 Florida Ave S, Lakeland, FL 33813) ")
                                                print(
                                                    f"\nPick up location is: {pick_up}")
                                                drop_off = input(
                                                    "\nPlease enter the drop off location: (Ex: 4721 Florida Ave S, Lakeland, FL 33813)")
                                                print(
                                                    f"\nPick up location is: {drop_off}")
    # Notes
                                                note = input(
                                                    "\nPlease add any other information about the vehicle and your location: ")
    # Notification
                                                notification = input(
                                                    "\nDo you want to receive phone call or text message? (yes, no) ").lower()
                                                if notification == "yes":
                                                    print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. When I have secured service I will send you the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
                                                else:
                                                    print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. You will receive a phone and that phone call will let you know about the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
    # Job ID
                                                chars = "1234567890"
                                                number = 10
                                                length = 8

                                                for _ in range(number):
                                                    passwords = ""
                                                    for c in range(length):
                                                        passwords += random.choice(
                                                            chars)
                                                print(
                                                    f"\nYour job ID is: {passwords}")
    # else height
                                    else:
                                        ride = input(
                                            "\nDo you need a ride? (yes, no) ")
                                        if ride == "yes":
                                            print(
                                                "\nWe will set up a lyft for you at the end of the request.")
                                            trailer = input(
                                                "\nIs the vehicle has a trailer attach to it? (yes, no) ")
                                            if trailer == "yes":
                                                input(
                                                    "\nPlease enter the weight of the trailer: ")
    # Location Type
                                                pick_up = input(
                                                    "\nPlease enter your correct location. (Ex: 4721 Florida Ave S, Lakeland, FL 33813) ")
                                                print(
                                                    f"\nPick up location is: {pick_up}")
                                                drop_off = input(
                                                    "\nPlease enter the drop off location: (Ex: 4721 Florida Ave S, Lakeland, FL 33813)")
                                                print(
                                                    f"\nPick up location is: {drop_off}")
    # Notes
                                                note = input(
                                                    "\nPlease add any other information about the vehicle and your location: ")
    # Notification
                                                notification = input(
                                                    "\nDo you want to receive phone call or text message? (yes, no) ").lower()
                                                if notification == "yes":
                                                    print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. When I have secured service I will send you the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
                                                else:
                                                    print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. You will receive a phone and that phone call will let you know about the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
    # Job ID
                                                chars = "1234567890"
                                                number = 10
                                                length = 8

                                                for _ in range(number):
                                                    passwords = ""
                                                    for c in range(length):
                                                        passwords += random.choice(
                                                            chars)

                                                print(
                                                    f"\nYour job ID is: {passwords}")
    # else trailer
                                            else:
                                                pick_up = input(
                                                    "\nPlease enter your correct location. (Ex: 4721 Florida Ave S, Lakeland, FL 33813) ")
                                                print(
                                                    f"\nPick up location is: {pick_up}")
                                                drop_off = input(
                                                    "\nPlease enter the drop off location: (Ex: 4721 Florida Ave S, Lakeland, FL 33813)")
                                                print(
                                                    f"\nPick up location is: {drop_off}")
    # Notes
                                                note = input(
                                                    "\nPlease add any other information about the vehicle and your location: ")
    # Notification
                                                notification = input(
                                                    "\nDo you want to receive phone call or text message? (yes, no) ").lower()
                                                if notification == "yes":
                                                    print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. When I have secured service I will send you the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
                                                else:
                                                    print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. You will receive a phone and that phone call will let you know about the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
    # Job ID
                                                chars = "1234567890"
                                                number = 10
                                                length = 8

                                                for _ in range(number):
                                                    passwords = ""
                                                    for c in range(length):
                                                        passwords += random.choice(
                                                            chars)
                                                print(
                                                    f"\nYour job ID is: {passwords}")
    # else ride
                                        else:
                                            trailer = input(
                                                "\nIs the vehicle has a trailer attach to it? (yes, no) ")
                                            if trailer == "yes":
                                                input(
                                                    "\nPlease enter the weight of the trailer: ")
    # Location Type
                                                pick_up = input(
                                                    "\nPlease enter your correct location. (Ex: 4721 Florida Ave S, Lakeland, FL 33813) ")
                                                print(
                                                    f"\nPick up location is: {pick_up}")
                                                drop_off = input(
                                                    "\nPlease enter the drop off location: (Ex: 4721 Florida Ave S, Lakeland, FL 33813)")
                                                print(
                                                    f"\nPick up location is: {drop_off}")
    # Notes
                                                note = input(
                                                    "\nPlease add any other information about the vehicle and your location: ")
    # Notification
                                                notification = input(
                                                    "\nDo you want to receive phone call or text message? (yes, no) ").lower()
                                                if notification == "yes":
                                                    print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. When I have secured service I will send you the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
                                                else:
                                                    print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. You will receive a phone and that phone call will let you know about the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
    # Job ID
                                                    chars = "1234567890"
                                                    number = 10
                                                    length = 8

                                                    for _ in range(number):
                                                        passwords = ""
                                                        for c in range(length):
                                                            passwords += random.choice(
                                                                chars)

                                                    print(
                                                        f"\nYour job ID is: {passwords}")
    # else trailer
                                            else:
                                                pick_up = input(
                                                    "\nPlease enter your correct location. (Ex: 4721 Florida Ave S, Lakeland, FL 33813) ")
                                                print(
                                                    f"\nPick up location is: {pick_up}")
                                                drop_off = input(
                                                    "\nPlease enter the drop off location: (Ex: 4721 Florida Ave S, Lakeland, FL 33813)")
                                                print(
                                                    f"\nPick up location is: {drop_off}")
    # Notes
                                                note = input(
                                                    "\nPlease add any other information about the vehicle and your location: ")
    # Notification
                                                notification = input(
                                                    "\nDo you want to receive phone call or text message? (yes, no) ").lower()
                                                if notification == "yes":
                                                    print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. When I have secured service I will send you the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
                                                else:
                                                    print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. You will receive a phone and that phone call will let you know about the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
    # Job ID
                                                chars = "1234567890"
                                                number = 10
                                                length = 8

                                                for _ in range(number):
                                                    passwords = ""
                                                    for c in range(length):
                                                        passwords += random.choice(
                                                            chars)
                                                print(
                                                    f"\nYour job ID is: {passwords}")

# attempt
                                else:
                                    attempt = input(
                                        "Have you attempted a jump start yet? (yes, no) ")
                                    if attempt == "yes":
                                        print(
                                            "\nSince that happened you will need a TOW SERICE.")
                                        neutral = input(
                                            "\nCan the vehicle be put in neutral? (yes, no) ")
                                        types = input(
                                            "\nIs the the vehicle a Four-wheel drive? (yes, no) ")
                                        height = input(
                                            "\nAre you in a low clearance? (yes, no) ")
                                        if height == "yes":
                                            input("\nWhat is the height? ")
                                            ride = input(
                                                "\nDo you need a ride? (yes, no) ")
                                            if ride == "yes":
                                                print(
                                                    "\nWe will set up a lyft for you at the end of the request.")
                                                trailer = input(
                                                    "\nIs the vehicle has a trailer attach to it? (yes, no) ")
                                                if trailer == "yes":
                                                    input(
                                                        "\nPlease enter the weight of the trailer: ")
    # Location Type
                                                    pick_up = input(
                                                        "\nPlease enter your correct location. (Ex: 4721 Florida Ave S, Lakeland, FL 33813) ")
                                                    print(
                                                        f"\nPick up location is: {pick_up}")
                                                    drop_off = input(
                                                        "\nPlease enter the drop off location: (Ex: 4721 Florida Ave S, Lakeland, FL 33813)")
                                                    print(
                                                        f"\nPick up location is: {drop_off}")
        # Notes
                                                    note = input(
                                                        "\nPlease add any other information about the vehicle and your location: ")
        # Notification
                                                    notification = input(
                                                        "\nDo you want to receive phone call or text message? (yes, no) ").lower()
                                                    if notification == "yes":
                                                        print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. When I have secured service I will send you the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
                                                    else:
                                                        print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. You will receive a phone and that phone call will let you know about the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
        # Job ID
                                                    chars = "1234567890"
                                                    number = 10
                                                    length = 8

                                                    for _ in range(number):
                                                        passwords = ""
                                                        for c in range(length):
                                                            passwords += random.choice(
                                                                chars)

                                                    print(
                                                        f"\nYour job ID is: {passwords}")
        # else trailer
                                                else:
                                                    pick_up = input(
                                                        "\nPlease enter your correct location. (Ex: 4721 Florida Ave S, Lakeland, FL 33813) ")
                                                    print(
                                                        f"\nPick up location is: {pick_up}")
                                                    drop_off = input(
                                                        "\nPlease enter the drop off location: (Ex: 4721 Florida Ave S, Lakeland, FL 33813)")
                                                    print(
                                                        f"\nPick up location is: {drop_off}")
        # Notes
                                                    note = input(
                                                        "\nPlease add any other information about the vehicle and your location: ")
        # Notification
                                                    notification = input(
                                                        "\nDo you want to receive phone call or text message? (yes, no) ").lower()
                                                    if notification == "yes":
                                                        print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. When I have secured service I will send you the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
                                                    else:
                                                        print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. You will receive a phone and that phone call will let you know about the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
        # Job ID
                                                    chars = "1234567890"
                                                    number = 10
                                                    length = 8

                                                    for _ in range(number):
                                                        passwords = ""
                                                        for c in range(length):
                                                            passwords += random.choice(
                                                                chars)
                                                    print(
                                                        f"\nYour job ID is: {passwords}")
        # else ride
                                            else:
                                                trailer = input(
                                                    "\nIs the vehicle has a trailer attach to it? (yes, no) ")
                                                if trailer == "yes":
                                                    input(
                                                        "\nPlease enter the weight of the trailer: ")
        # Location Type
                                                    pick_up = input(
                                                        "\nPlease enter your correct location. (Ex: 4721 Florida Ave S, Lakeland, FL 33813) ")
                                                    print(
                                                        f"\nPick up location is: {pick_up}")
                                                    drop_off = input(
                                                        "\nPlease enter the drop off location: (Ex: 4721 Florida Ave S, Lakeland, FL 33813)")
                                                    print(
                                                        f"\nPick up location is: {drop_off}")
        # Notes
                                                    note = input(
                                                        "\nPlease add any other information about the vehicle and your location: ")
        # Notification
                                                    notification = input(
                                                        "\nDo you want to receive phone call or text message? (yes, no) ").lower()
                                                    if notification == "yes":
                                                        print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. When I have secured service I will send you the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
                                                    else:
                                                        print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. You will receive a phone and that phone call will let you know about the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
        # Job ID
                                                        chars = "1234567890"
                                                        number = 10
                                                        length = 8

                                                        for _ in range(number):
                                                            passwords = ""
                                                            for c in range(length):
                                                                passwords += random.choice(
                                                                    chars)

                                                        print(
                                                            f"\nYour job ID is: {passwords}")
        # else trailer
                                                else:
                                                    pick_up = input(
                                                        "\nPlease enter your correct location. (Ex: 4721 Florida Ave S, Lakeland, FL 33813) ")
                                                    print(
                                                        f"\nPick up location is: {pick_up}")
                                                    drop_off = input(
                                                        "\nPlease enter the drop off location: (Ex: 4721 Florida Ave S, Lakeland, FL 33813)")
                                                    print(
                                                        f"\nPick up location is: {drop_off}")
        # Notes
                                                    note = input(
                                                        "\nPlease add any other information about the vehicle and your location: ")
        # Notification
                                                    notification = input(
                                                        "\nDo you want to receive phone call or text message? (yes, no) ").lower()
                                                    if notification == "yes":
                                                        print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. When I have secured service I will send you the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
                                                    else:
                                                        print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. You will receive a phone and that phone call will let you know about the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
        # Job ID
                                                    chars = "1234567890"
                                                    number = 10
                                                    length = 8

                                                    for _ in range(number):
                                                        passwords = ""
                                                        for c in range(length):
                                                            passwords += random.choice(
                                                                chars)
                                                    print(
                                                        f"\nYour job ID is: {passwords}")
        # else height
                                        else:
                                            ride = input(
                                                "\nDo you need a ride? (yes, no) ")
                                            if ride == "yes":
                                                print(
                                                    "\nWe will set up a lyft for you at the end of the request.")
                                                trailer = input(
                                                    "\nIs the vehicle has a trailer attach to it? (yes, no) ")
                                                if trailer == "yes":
                                                    input(
                                                        "\nPlease enter the weight of the trailer: ")
        # Location Type
                                                    pick_up = input(
                                                        "\nPlease enter your correct location. (Ex: 4721 Florida Ave S, Lakeland, FL 33813) ")
                                                    print(
                                                        f"\nPick up location is: {pick_up}")
                                                    drop_off = input(
                                                        "\nPlease enter the drop off location: (Ex: 4721 Florida Ave S, Lakeland, FL 33813)")
                                                    print(
                                                        f"\nPick up location is: {drop_off}")
        # Notes
                                                    note = input(
                                                        "\nPlease add any other information about the vehicle and your location: ")
        # Notification
                                                    notification = input(
                                                        "\nDo you want to receive phone call or text message? (yes, no) ").lower()
                                                    if notification == "yes":
                                                        print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. When I have secured service I will send you the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
                                                    else:
                                                        print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. You will receive a phone and that phone call will let you know about the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
        # Job ID
                                                    chars = "1234567890"
                                                    number = 10
                                                    length = 8

                                                    for _ in range(number):
                                                        passwords = ""
                                                        for c in range(length):
                                                            passwords += random.choice(
                                                                chars)

                                                    print(
                                                        f"\nYour job ID is: {passwords}")
        # else trailer
                                                else:
                                                    pick_up = input(
                                                        "\nPlease enter your correct location. (Ex: 4721 Florida Ave S, Lakeland, FL 33813) ")
                                                    print(
                                                        f"\nPick up location is: {pick_up}")
                                                    drop_off = input(
                                                        "\nPlease enter the drop off location: (Ex: 4721 Florida Ave S, Lakeland, FL 33813)")
                                                    print(
                                                        f"\nPick up location is: {drop_off}")
        # Notes
                                                    note = input(
                                                        "\nPlease add any other information about the vehicle and your location: ")
        # Notification
                                                    notification = input(
                                                        "\nDo you want to receive phone call or text message? (yes, no) ").lower()
                                                    if notification == "yes":
                                                        print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. When I have secured service I will send you the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
                                                    else:
                                                        print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. You will receive a phone and that phone call will let you know about the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
        # Job ID
                                                    chars = "1234567890"
                                                    number = 10
                                                    length = 8

                                                    for _ in range(number):
                                                        passwords = ""
                                                        for c in range(length):
                                                            passwords += random.choice(
                                                                chars)
                                                    print(
                                                        f"\nYour job ID is: {passwords}")
        # else ride
                                            else:
                                                trailer = input(
                                                    "\nIs the vehicle has a trailer attach to it? (yes, no) ")
                                                if trailer == "yes":
                                                    input(
                                                        "\nPlease enter the weight of the trailer: ")
        # Location Type
                                                    pick_up = input(
                                                        "\nPlease enter your correct location. (Ex: 4721 Florida Ave S, Lakeland, FL 33813) ")
                                                    print(
                                                        f"\nPick up location is: {pick_up}")
                                                    drop_off = input(
                                                        "\nPlease enter the drop off location: (Ex: 4721 Florida Ave S, Lakeland, FL 33813)")
                                                    print(
                                                        f"\nPick up location is: {drop_off}")
        # Notes
                                                    note = input(
                                                        "\nPlease add any other information about the vehicle and your location: ")
        # Notification
                                                    notification = input(
                                                        "\nDo you want to receive phone call or text message? (yes, no) ").lower()
                                                    if notification == "yes":
                                                        print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. When I have secured service I will send you the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
                                                    else:
                                                        print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. You will receive a phone and that phone call will let you know about the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
        # Job ID
                                                        chars = "1234567890"
                                                        number = 10
                                                        length = 8

                                                        for _ in range(number):
                                                            passwords = ""
                                                            for c in range(length):
                                                                passwords += random.choice(
                                                                    chars)

                                                        print(
                                                            f"\nYour job ID is: {passwords}")
        # else trailer
                                                else:
                                                    pick_up = input(
                                                        "\nPlease enter your correct location. (Ex: 4721 Florida Ave S, Lakeland, FL 33813) ")
                                                    print(
                                                        f"\nPick up location is: {pick_up}")
                                                    drop_off = input(
                                                        "\nPlease enter the drop off location: (Ex: 4721 Florida Ave S, Lakeland, FL 33813)")
                                                    print(
                                                        f"\nPick up location is: {drop_off}")
        # Notes
                                                    note = input(
                                                        "\nPlease add any other information about the vehicle and your location: ")
        # Notification
                                                    notification = input(
                                                        "\nDo you want to receive phone call or text message? (yes, no) ").lower()
                                                    if notification == "yes":
                                                        print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. When I have secured service I will send you the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
                                                    else:
                                                        print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. You will receive a phone and that phone call will let you know about the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
        # Job ID
                                                    chars = "1234567890"
                                                    number = 10
                                                    length = 8

                                                    for _ in range(number):
                                                        passwords = ""
                                                        for c in range(length):
                                                            passwords += random.choice(
                                                                chars)
                                                    print(
                                                        f"\nYour job ID is: {passwords}")
    # if not attempted = height
                                    else:
                                        height = input(
                                            "\nAre you in a low clearance? (yes, no) ")
                                        if height == "yes":
                                            input("\nWhat is the height? ")
        # Location Type
                                            pick_up = input(
                                                "\nPlease enter your correct location. (Ex: 4721 Florida Ave S, Lakeland, FL 33813) ")
                                            print(
                                                f"\nPick up location is: {pick_up}")
        # Notes
                                            note = input(
                                                "\nPlease add any other information about the vehicle and your location: ")
        # Notification
                                            notification = input(
                                                "\nDo you want to receive phone call or text message? (yes, no) ").lower()
                                            if notification == "yes":
                                                print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. When I have secured service I will send you the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
                                            else:
                                                print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. You will receive a phone and that phone call will let you know about the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")

        # Job ID
                                            chars = "1234567890"
                                            number = 10
                                            length = 8

                                            for _ in range(number):
                                                passwords = ""
                                                for c in range(length):
                                                    passwords += random.choice(
                                                        chars)

                                            print(
                                                f"\nYour job ID is: {passwords}")
        # if no height
                                        else:
                                            # Location Type
                                            pick_up = input(
                                                "\nPlease enter your correct location. (Ex: 4721 Florida Ave S, Lakeland, FL 33813) ")
                                            print(
                                                f"\nPick up location is: {pick_up}")
        # Notes
                                            note = input(
                                                "\nPlease add any other information about the vehicle and your location: ")
        # Notification
                                            notification = input(
                                                "\nDo you want to receive phone call or text message? (yes, no) ").lower()
                                            if notification == "yes":
                                                print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. When I have secured service I will send you the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
                                            else:
                                                print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. You will receive a phone and that phone call will let you know about the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")

        # Job ID
                                            chars = "1234567890"
                                            number = 10
                                            length = 8

                                            for _ in range(number):
                                                passwords = ""
                                                for c in range(length):
                                                    passwords += random.choice(
                                                        chars)

                                            print(
                                                f"\nYour job ID is: {passwords}")


# Tire change
                        elif type_of_service == "tire change":
                            keys = input(
                                "\nAre the keys present? (yes, no) ")
                            present = input(
                                "\nWill you be with the vehicle at the time of service? (yes, no) ")
                            if present == "yes":
                                tire = input(
                                    "\nWhich tire is damaged? (Driver Front, Passenger Front, Driver Rear, Passenger Rear, Multiple ) ")
                                spare = input(
                                    "\nDo you have a good spare tire? (yes, no) ")
                                if spare == "yes":
                                    height = input(
                                        "\nAre you in a low clearance? (yes, no) ")
                                    if height == "yes":
                                        input("\nWhat is the height? ")
# Location Type
                                        pick_up = input(
                                            "\nPlease enter your correct location. (Ex: 4721 Florida Ave S, Lakeland, FL 33813) ")
                                        print(
                                            f"\nPick up location is: {pick_up}")
# Notes
                                        note = input(
                                            "\nPlease add any other information about the vehicle and your location: ")
# Notification
                                        notification = input(
                                            "\nDo you want to receive phone call or text message? (yes, no) ").lower()
                                        if notification == "yes":
                                            print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. When I have secured service I will send you the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
                                        else:
                                            print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. You will receive a phone and that phone call will let you know about the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
# Job ID
                                        chars = "1234567890"
                                        number = 10
                                        length = 8

                                        for _ in range(number):
                                            passwords = ""
                                            for c in range(length):
                                                passwords += random.choice(chars)

                                        print(f"\nYour job ID is: {passwords}")
# else height
                                    else:
                                        # Location Type
                                        pick_up = input(
                                            "\nPlease enter your correct location. (Ex: 4721 Florida Ave S, Lakeland, FL 33813) ")
                                        print(
                                            f"\nPick up location is: {pick_up}")
# Notes
                                        note = input(
                                            "\nPlease add any other information about the vehicle and your location: ")
# Notification
                                        notification = input(
                                            "\nDo you want to receive phone call or text message? (yes, no) ").lower()
                                        if notification == "yes":
                                            print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. When I have secured service I will send you the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
                                        else:
                                            print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. You will receive a phone and that phone call will let you know about the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
# Job ID
                                        chars = "1234567890"
                                        number = 10
                                        length = 8

                                        for _ in range(number):
                                            passwords = ""
                                            for c in range(length):
                                                passwords += random.choice(chars)

                                        print(f"\nYour job ID is: {passwords}")

# If no spare
                                else:
                                    print(
                                        "If you don't have a good spare, we will have to tow the vehicle.")
                                    neutral = input(
                                        "\nCan the vehicle be put in neutral? (yes, no) ")
                                    types = input(
                                        "\nIs the the vehicle a Four-wheel drive? (yes, no) ")
                                    height = input(
                                        "\nAre you in a low clearance? (yes, no) ")
                                    if height == "yes":
                                        input("\nWhat is the height? ")
                                        ride = input(
                                            "\nDo you need a ride? (yes, no) ")
                                        if ride == "yes":
                                            print(
                                                "\nWe will set up a lyft for you at the end of the request.")
                                            trailer = input(
                                                "\nIs the vehicle has a trailer attach to it? (yes, no) ")
                                            if trailer == "yes":
                                                input(
                                                    "\nPlease enter the weight of the trailer: ")
    # Location Type
                                                pick_up = input(
                                                    "\nPlease enter your correct location. (Ex: 4721 Florida Ave S, Lakeland, FL 33813) ")
                                                print(
                                                    f"\nPick up location is: {pick_up}")
                                                drop_off = input(
                                                    "\nPlease enter the drop off location: (Ex: 4721 Florida Ave S, Lakeland, FL 33813)")
                                                print(
                                                    f"\nPick up location is: {drop_off}")
    # Notes
                                                note = input(
                                                    "\nPlease add any other information about the vehicle and your location: ")
    # Notification
                                                notification = input(
                                                    "\nDo you want to receive phone call or text message? (yes, no) ").lower()
                                                if notification == "yes":
                                                    print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. When I have secured service I will send you the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
                                                else:
                                                    print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. You will receive a phone and that phone call will let you know about the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
    # Job ID
                                                chars = "1234567890"
                                                number = 10
                                                length = 8

                                                for _ in range(number):
                                                    passwords = ""
                                                    for c in range(length):
                                                        passwords += random.choice(
                                                            chars)

                                                print(
                                                    f"\nYour job ID is: {passwords}")

    # else trailer
                                            else:
                                                pick_up = input(
                                                    "\nPlease enter your correct location. (Ex: 4721 Florida Ave S, Lakeland, FL 33813) ")
                                                print(
                                                    f"\nPick up location is: {pick_up}")
                                                drop_off = input(
                                                    "\nPlease enter the drop off location: (Ex: 4721 Florida Ave S, Lakeland, FL 33813)")
                                                print(
                                                    f"\nPick up location is: {drop_off}")
    # Notes
                                                note = input(
                                                    "\nPlease add any other information about the vehicle and your location: ")
    # Notification
                                                notification = input(
                                                    "\nDo you want to receive phone call or text message? (yes, no) ").lower()
                                                if notification == "yes":
                                                    print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. When I have secured service I will send you the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
                                                else:
                                                    print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. You will receive a phone and that phone call will let you know about the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
    # Job ID
                                                chars = "1234567890"
                                                number = 10
                                                length = 8

                                                for _ in range(number):
                                                    passwords = ""
                                                    for c in range(length):
                                                        passwords += random.choice(
                                                            chars)
                                                print(
                                                    f"\nYour job ID is: {passwords}")

    # else ride
                                        else:
                                            trailer = input(
                                                "\nIs the vehicle has a trailer attach to it? (yes, no) ")
                                            if trailer == "yes":
                                                input(
                                                    "\nPlease enter the weight of the trailer: ")
    # Location Type
                                                pick_up = input(
                                                    "\nPlease enter your correct location. (Ex: 4721 Florida Ave S, Lakeland, FL 33813) ")
                                                print(
                                                    f"\nPick up location is: {pick_up}")
                                                drop_off = input(
                                                    "\nPlease enter the drop off location: (Ex: 4721 Florida Ave S, Lakeland, FL 33813)")
                                                print(
                                                    f"\nPick up location is: {drop_off}")
    # Notes
                                                note = input(
                                                    "\nPlease add any other information about the vehicle and your location: ")
    # Notification
                                                notification = input(
                                                    "\nDo you want to receive phone call or text message? (yes, no) ").lower()
                                                if notification == "yes":
                                                    print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. When I have secured service I will send you the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
                                                else:
                                                    print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. You will receive a phone and that phone call will let you know about the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
    # Job ID
                                                    chars = "1234567890"
                                                    number = 10
                                                    length = 8

                                                    for _ in range(number):
                                                        passwords = ""
                                                        for c in range(length):
                                                            passwords += random.choice(
                                                                chars)

                                                    print(
                                                        f"\nYour job ID is: {passwords}")

    # else trailer
                                            else:
                                                pick_up = input(
                                                    "\nPlease enter your correct location. (Ex: 4721 Florida Ave S, Lakeland, FL 33813) ")
                                                print(
                                                    f"\nPick up location is: {pick_up}")
                                                drop_off = input(
                                                    "\nPlease enter the drop off location: (Ex: 4721 Florida Ave S, Lakeland, FL 33813)")
                                                print(
                                                    f"\nPick up location is: {drop_off}")
    # Notes
                                                note = input(
                                                    "\nPlease add any other information about the vehicle and your location: ")
    # Notification
                                                notification = input(
                                                    "\nDo you want to receive phone call or text message? (yes, no) ").lower()
                                                if notification == "yes":
                                                    print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. When I have secured service I will send you the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
                                                else:
                                                    print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. You will receive a phone and that phone call will let you know about the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
    # Job ID
                                                chars = "1234567890"
                                                number = 10
                                                length = 8

                                                for _ in range(number):
                                                    passwords = ""
                                                    for c in range(length):
                                                        passwords += random.choice(
                                                            chars)
                                                print(
                                                    f"\nYour job ID is: {passwords}")

    # else height
                                    else:
                                        ride = input(
                                            "\nDo you need a ride? (yes, no) ")
                                        if ride == "yes":
                                            print(
                                                "\nWe will set up a lyft for you at the end of the request.")
                                            trailer = input(
                                                "\nIs the vehicle has a trailer attach to it? (yes, no) ")
                                            if trailer == "yes":
                                                input(
                                                    "\nPlease enter the weight of the trailer: ")
    # Location Type
                                                pick_up = input(
                                                    "\nPlease enter your correct location. (Ex: 4721 Florida Ave S, Lakeland, FL 33813) ")
                                                print(
                                                    f"\nPick up location is: {pick_up}")
                                                drop_off = input(
                                                    "\nPlease enter the drop off location: (Ex: 4721 Florida Ave S, Lakeland, FL 33813)")
                                                print(
                                                    f"\nPick up location is: {drop_off}")
    # Notes
                                                note = input(
                                                    "\nPlease add any other information about the vehicle and your location: ")
    # Notification
                                                notification = input(
                                                    "\nDo you want to receive phone call or text message? (yes, no) ").lower()
                                                if notification == "yes":
                                                    print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. When I have secured service I will send you the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
                                                else:
                                                    print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. You will receive a phone and that phone call will let you know about the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
    # Job ID
                                                chars = "1234567890"
                                                number = 10
                                                length = 8

                                                for _ in range(number):
                                                    passwords = ""
                                                    for c in range(length):
                                                        passwords += random.choice(
                                                            chars)

                                                print(
                                                    f"\nYour job ID is: {passwords}")

    # else trailer
                                            else:
                                                pick_up = input(
                                                    "\nPlease enter your correct location. (Ex: 4721 Florida Ave S, Lakeland, FL 33813) ")
                                                print(
                                                    f"\nPick up location is: {pick_up}")
                                                drop_off = input(
                                                    "\nPlease enter the drop off location: (Ex: 4721 Florida Ave S, Lakeland, FL 33813)")
                                                print(
                                                    f"\nPick up location is: {drop_off}")
    # Notes
                                                note = input(
                                                    "\nPlease add any other information about the vehicle and your location: ")
    # Notification
                                                notification = input(
                                                    "\nDo you want to receive phone call or text message? (yes, no) ").lower()
                                                if notification == "yes":
                                                    print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. When I have secured service I will send you the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
                                                else:
                                                    print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. You will receive a phone and that phone call will let you know about the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
    # Job ID
                                                chars = "1234567890"
                                                number = 10
                                                length = 8

                                                for _ in range(number):
                                                    passwords = ""
                                                    for c in range(length):
                                                        passwords += random.choice(
                                                            chars)
                                                print(
                                                    f"\nYour job ID is: {passwords}")

    # else ride
                                        else:
                                            trailer = input(
                                                "\nIs the vehicle has a trailer attach to it? (yes, no) ")
                                            if trailer == "yes":
                                                input(
                                                    "\nPlease enter the weight of the trailer: ")
    # Location Type
                                                pick_up = input(
                                                    "\nPlease enter your correct location. (Ex: 4721 Florida Ave S, Lakeland, FL 33813) ")
                                                print(
                                                    f"\nPick up location is: {pick_up}")
                                                drop_off = input(
                                                    "\nPlease enter the drop off location: (Ex: 4721 Florida Ave S, Lakeland, FL 33813)")
                                                print(
                                                    f"\nPick up location is: {drop_off}")
    # Notes
                                                note = input(
                                                    "\nPlease add any other information about the vehicle and your location: ")
    # Notification
                                                notification = input(
                                                    "\nDo you want to receive phone call or text message? (yes, no) ").lower()
                                                if notification == "yes":
                                                    print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. When I have secured service I will send you the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
                                                else:
                                                    print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. You will receive a phone and that phone call will let you know about the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
    # Job ID
                                                    chars = "1234567890"
                                                    number = 10
                                                    length = 8

                                                    for _ in range(number):
                                                        passwords = ""
                                                        for c in range(length):
                                                            passwords += random.choice(
                                                                chars)

                                                    print(
                                                        f"\nYour job ID is: {passwords}")

    # else trailer
                                            else:
                                                pick_up = input(
                                                    "\nPlease enter your correct location. (Ex: 4721 Florida Ave S, Lakeland, FL 33813) ")
                                                print(
                                                    f"\nPick up location is: {pick_up}")
                                                drop_off = input(
                                                    "\nPlease enter the drop off location: (Ex: 4721 Florida Ave S, Lakeland, FL 33813)")
                                                print(
                                                    f"\nPick up location is: {drop_off}")
    # Notes
                                                note = input(
                                                    "\nPlease add any other information about the vehicle and your location: ")
    # Notification
                                                notification = input(
                                                    "\nDo you want to receive phone call or text message? (yes, no) ").lower()
                                                if notification == "yes":
                                                    print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. When I have secured service I will send you the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
                                                else:
                                                    print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. You will receive a phone and that phone call will let you know about the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
    # Job ID
                                                chars = "1234567890"
                                                number = 10
                                                length = 8

                                                for _ in range(number):
                                                    passwords = ""
                                                    for c in range(length):
                                                        passwords += random.choice(
                                                            chars)
                                                print(
                                                    f"\nYour job ID is: {passwords}")

        # If not present
                            else:
                                print(
                                    "You need to be there in order to get service.")
                                tire = input(
                                    "\nWhich tire is damaged? (Driver Front, Passenger Front, Driver Rear, Passenger Rear, Multiple ) ")
                                spare = input(
                                    "\nDo you have a good spare tire? (yes, no) ")
                                if spare == "yes":
                                    height = input(
                                        "\nAre you in a low clearance? (yes, no) ")
                                    if height == "yes":
                                        input("\nWhat is the height? ")
# Location Type
                                        pick_up = input(
                                            "\nPlease enter your correct location. (Ex: 4721 Florida Ave S, Lakeland, FL 33813) ")
                                        print(
                                            f"\nPick up location is: {pick_up}")
# Notes
                                        note = input(
                                            "\nPlease add any other information about the vehicle and your location: ")
# Notification
                                        notification = input(
                                            "\nDo you want to receive phone call or text message? (yes, no) ").lower()
                                        if notification == "yes":
                                            print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. When I have secured service I will send you the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
                                        else:
                                            print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. You will receive a phone and that phone call will let you know about the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
# Job ID
                                        chars = "1234567890"
                                        number = 10
                                        length = 8

                                        for _ in range(number):
                                            passwords = ""
                                            for c in range(length):
                                                passwords += random.choice(chars)

                                        print(f"\nYour job ID is: {passwords}")
# else height
                                    else:
                                        # Location Type
                                        pick_up = input(
                                            "\nPlease enter your correct location. (Ex: 4721 Florida Ave S, Lakeland, FL 33813) ")
                                        print(
                                            f"\nPick up location is: {pick_up}")
# Notes
                                        note = input(
                                            "\nPlease add any other information about the vehicle and your location: ")
# Notification
                                        notification = input(
                                            "\nDo you want to receive phone call or text message? (yes, no) ").lower()
                                        if notification == "yes":
                                            print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. When I have secured service I will send you the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
                                        else:
                                            print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. You will receive a phone and that phone call will let you know about the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
# Job ID
                                        chars = "1234567890"
                                        number = 10
                                        length = 8

                                        for _ in range(number):
                                            passwords = ""
                                            for c in range(length):
                                                passwords += random.choice(chars)

                                        print(f"\nYour job ID is: {passwords}")

# If no spare
                                else:
                                    print(
                                        "If you don't have a good spare, we will have to tow the vehicle.")
                                    neutral = input(
                                        "\nCan the vehicle be put in neutral? (yes, no) ")
                                    types = input(
                                        "\nIs the the vehicle a Four-wheel drive? (yes, no) ")
                                    height = input(
                                        "\nAre you in a low clearance? (yes, no) ")
                                    if height == "yes":
                                        input("\nWhat is the height? ")
                                        ride = input(
                                            "\nDo you need a ride? (yes, no) ")
                                        if ride == "yes":
                                            print(
                                                "\nWe will set up a lyft for you at the end of the request.")
                                            trailer = input(
                                                "\nIs the vehicle has a trailer attach to it? (yes, no) ")
                                            if trailer == "yes":
                                                input(
                                                    "\nPlease enter the weight of the trailer: ")
    # Location Type
                                                pick_up = input(
                                                    "\nPlease enter your correct location. (Ex: 4721 Florida Ave S, Lakeland, FL 33813) ")
                                                print(
                                                    f"\nPick up location is: {pick_up}")
                                                drop_off = input(
                                                    "\nPlease enter the drop off location: (Ex: 4721 Florida Ave S, Lakeland, FL 33813)")
                                                print(
                                                    f"\nPick up location is: {drop_off}")
    # Notes
                                                note = input(
                                                    "\nPlease add any other information about the vehicle and your location: ")
    # Notification
                                                notification = input(
                                                    "\nDo you want to receive phone call or text message? (yes, no) ").lower()
                                                if notification == "yes":
                                                    print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. When I have secured service I will send you the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
                                                else:
                                                    print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. You will receive a phone and that phone call will let you know about the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
    # Job ID
                                                chars = "1234567890"
                                                number = 10
                                                length = 8

                                                for _ in range(number):
                                                    passwords = ""
                                                    for c in range(length):
                                                        passwords += random.choice(
                                                            chars)

                                                print(
                                                    f"\nYour job ID is: {passwords}")

    # else trailer
                                            else:
                                                pick_up = input(
                                                    "\nPlease enter your correct location. (Ex: 4721 Florida Ave S, Lakeland, FL 33813) ")
                                                print(
                                                    f"\nPick up location is: {pick_up}")
                                                drop_off = input(
                                                    "\nPlease enter the drop off location: (Ex: 4721 Florida Ave S, Lakeland, FL 33813)")
                                                print(
                                                    f"\nPick up location is: {drop_off}")
    # Notes
                                                note = input(
                                                    "\nPlease add any other information about the vehicle and your location: ")
    # Notification
                                                notification = input(
                                                    "\nDo you want to receive phone call or text message? (yes, no) ").lower()
                                                if notification == "yes":
                                                    print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. When I have secured service I will send you the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
                                                else:
                                                    print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. You will receive a phone and that phone call will let you know about the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
    # Job ID
                                                chars = "1234567890"
                                                number = 10
                                                length = 8

                                                for _ in range(number):
                                                    passwords = ""
                                                    for c in range(length):
                                                        passwords += random.choice(
                                                            chars)
                                                print(
                                                    f"\nYour job ID is: {passwords}")

    # else ride
                                        else:
                                            trailer = input(
                                                "\nIs the vehicle has a trailer attach to it? (yes, no) ")
                                            if trailer == "yes":
                                                input(
                                                    "\nPlease enter the weight of the trailer: ")
    # Location Type
                                                pick_up = input(
                                                    "\nPlease enter your correct location. (Ex: 4721 Florida Ave S, Lakeland, FL 33813) ")
                                                print(
                                                    f"\nPick up location is: {pick_up}")
                                                drop_off = input(
                                                    "\nPlease enter the drop off location: (Ex: 4721 Florida Ave S, Lakeland, FL 33813)")
                                                print(
                                                    f"\nPick up location is: {drop_off}")
    # Notes
                                                note = input(
                                                    "\nPlease add any other information about the vehicle and your location: ")
    # Notification
                                                notification = input(
                                                    "\nDo you want to receive phone call or text message? (yes, no) ").lower()
                                                if notification == "yes":
                                                    print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. When I have secured service I will send you the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
                                                else:
                                                    print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. You will receive a phone and that phone call will let you know about the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
    # Job ID
                                                    chars = "1234567890"
                                                    number = 10
                                                    length = 8

                                                    for _ in range(number):
                                                        passwords = ""
                                                        for c in range(length):
                                                            passwords += random.choice(
                                                                chars)

                                                    print(
                                                        f"\nYour job ID is: {passwords}")

    # else trailer
                                            else:
                                                pick_up = input(
                                                    "\nPlease enter your correct location. (Ex: 4721 Florida Ave S, Lakeland, FL 33813) ")
                                                print(
                                                    f"\nPick up location is: {pick_up}")
                                                drop_off = input(
                                                    "\nPlease enter the drop off location: (Ex: 4721 Florida Ave S, Lakeland, FL 33813)")
                                                print(
                                                    f"\nPick up location is: {drop_off}")
    # Notes
                                                note = input(
                                                    "\nPlease add any other information about the vehicle and your location: ")
    # Notification
                                                notification = input(
                                                    "\nDo you want to receive phone call or text message? (yes, no) ").lower()
                                                if notification == "yes":
                                                    print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. When I have secured service I will send you the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
                                                else:
                                                    print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. You will receive a phone and that phone call will let you know about the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
    # Job ID
                                                chars = "1234567890"
                                                number = 10
                                                length = 8

                                                for _ in range(number):
                                                    passwords = ""
                                                    for c in range(length):
                                                        passwords += random.choice(
                                                            chars)
                                                print(
                                                    f"\nYour job ID is: {passwords}")

    # else height
                                    else:
                                        ride = input(
                                            "\nDo you need a ride? (yes, no) ")
                                        if ride == "yes":
                                            print(
                                                "\nWe will set up a lyft for you at the end of the request.")
                                            trailer = input(
                                                "\nIs the vehicle has a trailer attach to it? (yes, no) ")
                                            if trailer == "yes":
                                                input(
                                                    "\nPlease enter the weight of the trailer: ")
    # Location Type
                                                pick_up = input(
                                                    "\nPlease enter your correct location. (Ex: 4721 Florida Ave S, Lakeland, FL 33813) ")
                                                print(
                                                    f"\nPick up location is: {pick_up}")
                                                drop_off = input(
                                                    "\nPlease enter the drop off location: (Ex: 4721 Florida Ave S, Lakeland, FL 33813)")
                                                print(
                                                    f"\nPick up location is: {drop_off}")
    # Notes
                                                note = input(
                                                    "\nPlease add any other information about the vehicle and your location: ")
    # Notification
                                                notification = input(
                                                    "\nDo you want to receive phone call or text message? (yes, no) ").lower()
                                                if notification == "yes":
                                                    print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. When I have secured service I will send you the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
                                                else:
                                                    print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. You will receive a phone and that phone call will let you know about the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
    # Job ID
                                                chars = "1234567890"
                                                number = 10
                                                length = 8

                                                for _ in range(number):
                                                    passwords = ""
                                                    for c in range(length):
                                                        passwords += random.choice(
                                                            chars)

                                                print(
                                                    f"\nYour job ID is: {passwords}")

    # else trailer
                                            else:
                                                pick_up = input(
                                                    "\nPlease enter your correct location. (Ex: 4721 Florida Ave S, Lakeland, FL 33813) ")
                                                print(
                                                    f"\nPick up location is: {pick_up}")
                                                drop_off = input(
                                                    "\nPlease enter the drop off location: (Ex: 4721 Florida Ave S, Lakeland, FL 33813)")
                                                print(
                                                    f"\nPick up location is: {drop_off}")
    # Notes
                                                note = input(
                                                    "\nPlease add any other information about the vehicle and your location: ")
    # Notification
                                                notification = input(
                                                    "\nDo you want to receive phone call or text message? (yes, no) ").lower()
                                                if notification == "yes":
                                                    print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. When I have secured service I will send you the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
                                                else:
                                                    print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. You will receive a phone and that phone call will let you know about the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
    # Job ID
                                                chars = "1234567890"
                                                number = 10
                                                length = 8

                                                for _ in range(number):
                                                    passwords = ""
                                                    for c in range(length):
                                                        passwords += random.choice(
                                                            chars)
                                                print(
                                                    f"\nYour job ID is: {passwords}")

    # else ride
                                        else:
                                            trailer = input(
                                                "\nIs the vehicle has a trailer attach to it? (yes, no) ")
                                            if trailer == "yes":
                                                input(
                                                    "\nPlease enter the weight of the trailer: ")
    # Location Type
                                                pick_up = input(
                                                    "\nPlease enter your correct location. (Ex: 4721 Florida Ave S, Lakeland, FL 33813) ")
                                                print(
                                                    f"\nPick up location is: {pick_up}")
                                                drop_off = input(
                                                    "\nPlease enter the drop off location: (Ex: 4721 Florida Ave S, Lakeland, FL 33813)")
                                                print(
                                                    f"\nPick up location is: {drop_off}")
    # Notes
                                                note = input(
                                                    "\nPlease add any other information about the vehicle and your location: ")
    # Notification
                                                notification = input(
                                                    "\nDo you want to receive phone call or text message? (yes, no) ").lower()
                                                if notification == "yes":
                                                    print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. When I have secured service I will send you the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
                                                else:
                                                    print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. You will receive a phone and that phone call will let you know about the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
    # Job ID
                                                    chars = "1234567890"
                                                    number = 10
                                                    length = 8

                                                    for _ in range(number):
                                                        passwords = ""
                                                        for c in range(length):
                                                            passwords += random.choice(
                                                                chars)

                                                    print(
                                                        f"\nYour job ID is: {passwords}")

    # else trailer
                                            else:
                                                pick_up = input(
                                                    "\nPlease enter your correct location. (Ex: 4721 Florida Ave S, Lakeland, FL 33813) ")
                                                print(
                                                    f"\nPick up location is: {pick_up}")
                                                drop_off = input(
                                                    "\nPlease enter the drop off location: (Ex: 4721 Florida Ave S, Lakeland, FL 33813)")
                                                print(
                                                    f"\nPick up location is: {drop_off}")
    # Notes
                                                note = input(
                                                    "\nPlease add any other information about the vehicle and your location: ")
    # Notification
                                                notification = input(
                                                    "\nDo you want to receive phone call or text message? (yes, no) ").lower()
                                                if notification == "yes":
                                                    print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. When I have secured service I will send you the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
                                                else:
                                                    print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. You will receive a phone and that phone call will let you know about the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
    # Job ID
                                                chars = "1234567890"
                                                number = 10
                                                length = 8

                                                for _ in range(number):
                                                    passwords = ""
                                                    for c in range(length):
                                                        passwords += random.choice(
                                                            chars)
                                                print(
                                                    f"\nYour job ID is: {passwords}")


# Fuel Delivery
                        elif type_of_service == "fuel delivery":
                            keys = input(
                                "\nAre the keys present? (yes, no) ")
                            present = input(
                                "\nWill you be with the vehicle at the time of service? (yes, no) ")
                            if present == "yes":
                                gas = input(
                                    "\nWhat is the gasoline type? (Regular, Plus, Premium, Diesel)")
                                height = input(
                                    "\nAre you in a low clearance? (yes, no) ")
                                if height == "yes":
                                    input("\nWhat is the height? ")
# Location Type
                                    pick_up = input(
                                        "\nPlease enter your correct location. (Ex: 4721 Florida Ave S, Lakeland, FL 33813) ")
                                    print(f"\nPick up location is: {pick_up}")
# Notes
                                    note = input(
                                        "\nPlease add any other information about the vehicle and your location: ")
# Notification
                                    notification = input(
                                        "\nDo you want to receive phone call or text message? (yes, no) ").lower()
                                    if notification == "yes":
                                        print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. When I have secured service I will send you the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
                                    else:
                                        print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. You will receive a phone and that phone call will let you know about the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")

# Job ID
                                    chars = "1234567890"
                                    number = 10
                                    length = 8

                                    for _ in range(number):
                                        passwords = ""
                                        for c in range(length):
                                            passwords += random.choice(chars)

                                    print(f"\nYour job ID is: {passwords}")
# if no height
                                else:
                                    # Location Type
                                    pick_up = input(
                                        "\nPlease enter your correct location. (Ex: 4721 Florida Ave S, Lakeland, FL 33813) ")
                                    print(f"\nPick up location is: {pick_up}")
# Notes
                                    note = input(
                                        "\nPlease add any other information about the vehicle and your location: ")
# Notification
                                    notification = input(
                                        "\nDo you want to receive phone call or text message? (yes, no) ").lower()
                                    if notification == "yes":
                                        print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. When I have secured service I will send you the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
                                    else:
                                        print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. You will receive a phone and that phone call will let you know about the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")

# Job ID
                                    chars = "1234567890"
                                    number = 10
                                    length = 8

                                    for _ in range(number):
                                        passwords = ""
                                        for c in range(length):
                                            passwords += random.choice(chars)

                                    print(f"\nYour job ID is: {passwords}")
# if not present
                            else:
                                print(
                                    "You need to be there in order to get service.")
                                gas = input(
                                    "\nWhat is the gasoline type? (Regular, Plus, Premium, Diesel)")
                                height = input(
                                    "\nAre you in a low clearance? (yes, no) ")
                                if height == "yes":
                                    input("\nWhat is the height? ")
# Location Type
                                    pick_up = input(
                                        "\nPlease enter your correct location. (Ex: 4721 Florida Ave S, Lakeland, FL 33813) ")
                                    print(f"\nPick up location is: {pick_up}")
# Notes
                                    note = input(
                                        "\nPlease add any other information about the vehicle and your location: ")
# Notification
                                    notification = input(
                                        "\nDo you want to receive phone call or text message? (yes, no) ").lower()
                                    if notification == "yes":
                                        print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. When I have secured service I will send you the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
                                    else:
                                        print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. You will receive a phone and that phone call will let you know about the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")

# Job ID
                                    chars = "1234567890"
                                    number = 10
                                    length = 8

                                    for _ in range(number):
                                        passwords = ""
                                        for c in range(length):
                                            passwords += random.choice(chars)

                                    print(f"\nYour job ID is: {passwords}")
# if no height
                                else:
                                    # Location Type
                                    pick_up = input(
                                        "\nPlease enter your correct location. (Ex: 4721 Florida Ave S, Lakeland, FL 33813) ")
                                    print(f"\nPick up location is: {pick_up}")
# Notes
                                    note = input(
                                        "\nPlease add any other information about the vehicle and your location: ")
# Notification
                                    notification = input(
                                        "\nDo you want to receive phone call or text message? (yes, no) ").lower()
                                    if notification == "yes":
                                        print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. When I have secured service I will send you the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
                                    else:
                                        print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. You will receive a phone and that phone call will let you know about the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")

# Job ID
                                    chars = "1234567890"
                                    number = 10
                                    length = 8

                                    for _ in range(number):
                                        passwords = ""
                                        for c in range(length):
                                            passwords += random.choice(chars)

                                    print(f"\nYour job ID is: {passwords}")


# Locked Out
                        elif type_of_service == "locked out":
                            present = input(
                                "\nWill you be with the vehicle at the time of service? (yes, no) ")
                            if present == "yes":
                                on = input(
                                    "\nIs the vehicle on or running? (yes, no) ")
                                keys = input(
                                    "\nWhere are the keys located? (Trunk: accessible, Trunk: inaccessible, Inside the vehicle, Visor, Under the Floor Mat, Unknown) ")
                                life = input(
                                    "\nAny children or pets locked inside of the vehicle? (yes, no) ")
                                height = input(
                                    "\nAre you in a low clearance? (yes, no) ")
                                if height == "yes":
                                    input("\nWhat is the height? ")
# Location Type
                                    pick_up = input(
                                        "\nPlease enter your correct location. (Ex: 4721 Florida Ave S, Lakeland, FL 33813) ")
                                    print(f"\nPick up location is: {pick_up}")
# Notes
                                    note = input(
                                        "\nPlease add any other information about the vehicle and your location: ")
# Notification
                                    notification = input(
                                        "\nDo you want to receive phone call or text message? (yes, no) ").lower()
                                    if notification == "yes":
                                        print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. When I have secured service I will send you the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
                                    else:
                                        print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. You will receive a phone and that phone call will let you know about the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")

# Job ID
                                    chars = "1234567890"
                                    number = 10
                                    length = 8

                                    for _ in range(number):
                                        passwords = ""
                                        for c in range(length):
                                            passwords += random.choice(chars)

                                    print(f"\nYour job ID is: {passwords}")
# if no height
                                else:
                                    # Location Type
                                    pick_up = input(
                                        "\nPlease enter your correct location. (Ex: 4721 Florida Ave S, Lakeland, FL 33813) ")
                                    print(f"\nPick up location is: {pick_up}")
# Notes
                                    note = input(
                                        "\nPlease add any other information about the vehicle and your location: ")
# Notification
                                    notification = input(
                                        "\nDo you want to receive phone call or text message? (yes, no) ").lower()
                                    if notification == "yes":
                                        print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. When I have secured service I will send you the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
                                    else:
                                        print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. You will receive a phone and that phone call will let you know about the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")

# Job ID
                                    chars = "1234567890"
                                    number = 10
                                    length = 8

                                    for _ in range(number):
                                        passwords = ""
                                        for c in range(length):
                                            passwords += random.choice(chars)

                                    print(f"\nYour job ID is: {passwords}")

# if not present
                            else:
                                print(
                                    "Someone must be there in order to have service.")
                                on = input(
                                    "\nIs the vehicle on or running? (yes, no) ")
                                keys = input(
                                    "\nWhere are the keys located? (Trunk: accessible, Trunk: inaccessible, Inside the vehicle, Visor, Under the Floor Mat, Unknown) ")
                                life = input(
                                    "\nAny children or pets locked inside of the vehicle? (yes, no) ")
                                height = input(
                                    "\nAre you in a low clearance? (yes, no) ")
                                if height == "yes":
                                    input("\nWhat is the height? ")
# Location Type
                                    pick_up = input(
                                        "\nPlease enter your correct location. (Ex: 4721 Florida Ave S, Lakeland, FL 33813) ")
                                    print(f"\nPick up location is: {pick_up}")
# Notes
                                    note = input(
                                        "\nPlease add any other information about the vehicle and your location: ")
# Notification
                                    notification = input(
                                        "\nDo you want to receive phone call or text message? (yes, no) ").lower()
                                    if notification == "yes":
                                        print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. When I have secured service I will send you the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
                                    else:
                                        print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. You will receive a phone and that phone call will let you know about the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")

# Job ID
                                    chars = "1234567890"
                                    number = 10
                                    length = 8

                                    for _ in range(number):
                                        passwords = ""
                                        for c in range(length):
                                            passwords += random.choice(chars)

                                    print(f"\nYour job ID is: {passwords}")
# if no height
                                else:
                                    # Location Type
                                    pick_up = input(
                                        "\nPlease enter your correct location. (Ex: 4721 Florida Ave S, Lakeland, FL 33813) ")
                                    print(f"\nPick up location is: {pick_up}")
# Notes
                                    note = input(
                                        "\nPlease add any other information about the vehicle and your location: ")
# Notification
                                    notification = input(
                                        "\nDo you want to receive phone call or text message? (yes, no) ").lower()
                                    if notification == "yes":
                                        print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. When I have secured service I will send you the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
                                    else:
                                        print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. You will receive a phone and that phone call will let you know about the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")

# Job ID
                                    chars = "1234567890"
                                    number = 10
                                    length = 8

                                    for _ in range(number):
                                        passwords = ""
                                        for c in range(length):
                                            passwords += random.choice(chars)

                                    print(f"\nYour job ID is: {passwords}")

# Winch
                        elif type_of_service == "winch":
                            keys = input(
                                "\nAre the keys present? (yes, no) ")
                            present = input(
                                "\nWill you be with the vehicle at the time of service? (yes, no) ")
                            if present == "yes":
                                neutral = input(
                                    "\nCan the vehicle be put in neutral? (yes, no) ")
                                driveable = input(
                                    "\nIs the the vehicle will be driveable after the winch out? (yes, no) ")
                                feet = input(
                                    "\nIs the vehicle within 10 ft of a paved surface? (yes, no) ")
                                height = input(
                                    "\nAre you in a low clearance? (yes, no) ")
                                if height == "yes":
                                    input("\nWhat is the height? ")
# Location Type
                                    pick_up = input(
                                        "\nPlease enter your correct location. (Ex: 4721 Florida Ave S, Lakeland, FL 33813) ")
                                    print(f"\nPick up location is: {pick_up}")
# Notes
                                    note = input(
                                        "\nPlease add any other information about the vehicle and your location: ")
# Notification
                                    notification = input(
                                        "\nDo you want to receive phone call or text message? (yes, no) ").lower()
                                    if notification == "yes":
                                        print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. When I have secured service I will send you the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
                                    else:
                                        print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. You will receive a phone and that phone call will let you know about the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")

# Job ID
                                    chars = "1234567890"
                                    number = 10
                                    length = 8

                                    for _ in range(number):
                                        passwords = ""
                                        for c in range(length):
                                            passwords += random.choice(chars)

                                    print(f"\nYour job ID is: {passwords}")

# if no height
                                else:
                                    # Location Type
                                    pick_up = input(
                                        "\nPlease enter your correct location. (Ex: 4721 Florida Ave S, Lakeland, FL 33813) ")
                                    print(f"\nPick up location is: {pick_up}")
# Notes
                                    note = input(
                                        "\nPlease add any other information about the vehicle and your location: ")
# Notification
                                    notification = input(
                                        "\nDo you want to receive phone call or text message? (yes, no) ").lower()
                                    if notification == "yes":
                                        print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. When I have secured service I will send you the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
                                    else:
                                        print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. You will receive a phone and that phone call will let you know about the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")

# Job ID
                                    chars = "1234567890"
                                    number = 10
                                    length = 8

                                    for _ in range(number):
                                        passwords = ""
                                        for c in range(length):
                                            passwords += random.choice(chars)

                                    print(f"\nYour job ID is: {passwords}")
# if not present
                            else:
                                print(
                                    "Someone must be there in order to have service.")
                                neutral = input(
                                    "\nCan the vehicle be put in neutral? (yes, no) ")
                                driveable = input(
                                    "\nIs the the vehicle will be driveable after the winch out? (yes, no) ")
                                feet = input(
                                    "\nIs the vehicle within 10 ft of a paved surface? (yes, no) ")
                                height = input(
                                    "\nAre you in a low clearance? (yes, no) ")
                                if height == "yes":
                                    input("\nWhat is the height? ")
# Location Type
                                    pick_up = input(
                                        "\nPlease enter your correct location. (Ex: 4721 Florida Ave S, Lakeland, FL 33813) ")
                                    print(f"\nPick up location is: {pick_up}")
# Notes
                                    note = input(
                                        "\nPlease add any other information about the vehicle and your location: ")
# Notification
                                    notification = input(
                                        "\nDo you want to receive phone call or text message? (yes, no) ").lower()
                                    if notification == "yes":
                                        print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. When I have secured service I will send you the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
                                    else:
                                        print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. You will receive a phone and that phone call will let you know about the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")

# Job ID
                                    chars = "1234567890"
                                    number = 10
                                    length = 8

                                    for _ in range(number):
                                        passwords = ""
                                        for c in range(length):
                                            passwords += random.choice(chars)

                                    print(f"\nYour job ID is: {passwords}")
# if no height
                                else:
                                    # Location Type
                                    pick_up = input(
                                        "\nPlease enter your correct location. (Ex: 4721 Florida Ave S, Lakeland, FL 33813) ")
                                    print(f"\nPick up location is: {pick_up}")
# Notes
                                    note = input(
                                        "\nPlease add any other information about the vehicle and your location: ")
# Notification
                                    notification = input(
                                        "\nDo you want to receive phone call or text message? (yes, no) ").lower()
                                    if notification == "yes":
                                        print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. When I have secured service I will send you the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")
                                    else:
                                        print(f"\n{fname} I can see that you are covered for the service,  we recommand that you call the dealership and let them know your vehicle is coming in for service. You will receive a phone and that phone call will let you know about the name and phone number of the service provider in addition to their estimate time of arrival, that will arrive as a text, standard message and data rates may apply. I have everything needed to get service out to you thank you for calling roadside assistance. Enjoy the rest of your day! Bye-bye!!")

# Job ID
                                    chars = "1234567890"
                                    number = 10
                                    length = 8

                                    for _ in range(number):
                                        passwords = ""
                                        for c in range(length):
                                            passwords += random.choice(chars)

                                    print(f"\nYour job ID is: {passwords}")

                    else:
                        print(f"\nSorry! we don't do {type_of_service}.")
                else:
                    print(
                        "\nPhone should containt 10 characters, Please verify the Number and try again!")
            else:
                print(
                    "\nVIN should have 17 characters. Please verify the VIN Number and try again!")
        else:
            print(
                "\nPolicy should have 16 characters. Please Verify the Policy Number and try again!")
    else:
        print("\nPlease check the list and try again. Thank You!")

else:
    print("\nPlease hang up and call 911.")
    print("\nThank you for calling Roadside Assitance. Enjoy the rest of your day!\n")

# Generate Job ID number
# Add lyft
