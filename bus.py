


AVAILABEL_SEATS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
AMOUNT = 100

selected_seats = []
booking_details = []

def show_facilities():
    print("1.Booking")
    print("2.Available Seats")
    print("3.Selected Seats")
    print("4.Cancel a seat")
    print("5.Exit")
    select=int(input("Select any one::"))
    return select


def available_Seats():
    print(AVAILABEL_SEATS)

def selectes_Seats():
    print(selected_seats)

def cancel_ticket():
    seat_no=int(input('Enter your seat number ::'))
    if seat_no in selected_seats:
        selected_seats.remove(seat_no)
        AVAILABEL_SEATS.append(seat_no)
        AVAILABEL_SEATS.sort()
    else:
        print("Enter valid seat number")

def booking():
    select_seat=[]
    num_of_seat=int(input("Enter how many seats do you want ::"))
    print("AVAILABLE SEATS ARE :: ", AVAILABEL_SEATS)

    for x in range(0,num_of_seat):
        seat_number = int(input("Enter %d seat numbers "  %x))
        select_seat.append(seat_number)

    count_number_of_seats=0
    for to_take_one_seat in select_seat:
        if to_take_one_seat in AVAILABEL_SEATS:
            count_number_of_seats=count_number_of_seats+1

    if count_number_of_seats==num_of_seat:
        passenger_name = input("Enter your Name ::")
        passenger_age = int(input("Enter your Age ::"))
        passenger_gender = input("Enter your Gender ::")
        source = input("Source ::")
        destination = input("Enter your Destination ::")
        amount= len(select_seat) * AMOUNT
        print("Amount ::",amount)
        detais = [passenger_name, passenger_age, passenger_gender, source, destination, amount, select_seat]
        booking_details.append(detais)
        for remove_seats in select_seat:
            selected_seats.append(remove_seats)
            AVAILABEL_SEATS.remove(remove_seats)
        print("Thanks")
    else:
        print("please select valid seat number")






y='y'
while y=='y':
    select=show_facilities()
    if select==1:
        booking()
    if select==3:
        selectes_Seats()
    if select==2:
        available_Seats()
    if select==4:
        cancel_ticket()
    if select==5:
        y='z'
    y=input("press 'y' to continue ")







print(AVAILABEL_SEATS)