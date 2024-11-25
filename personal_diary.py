"""_summary_

    Creating a Personal Diary

"""


def main():
    
    # ask user for the current date and time
    current_date_time = input(
        "Enter the current date and time (e.g., YYYY-MM-DD HH:MM): ")

    # ask user for their diary entry
    diary_entry = input("Enter your diary entry: ")

    # Open the file 'diary.txt' in append mode
    with open("diary.txt", "a") as file:
        # Write the date and time
        file.write(f"Date and Time: {current_date_time}\n")

        # Write the diary entry
        file.write(f"Entry: {diary_entry}\n")

        file.write("\n")

    # letting the user know it has been saved
    print("Your diary entry has been saved!")



main()
