"""Ticket sales and Seat takens away"""

# the number of tickets for the event
tickets = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12",
           "13", "14", "15", "16", "17", "18", "19", "20"]

# if all tickets are sold
finished_sales = "0"

while finished_sales != "No more tickets":
    for number in tickets:
        print(number)
        # to what ticket the customer wanted
    finished_sales = input("\nPlease pick the ticket you would like:  ")
    if finished_sales in tickets:
        tickets.remove(finished_sales) # removal of the ticket that got sold
    if len(tickets) == 0: # if all tickets are sold
        print("All tickets have been sold. We are sold out now.")