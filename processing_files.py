"""_summary_

   Processing Files  
    
"""


def main():
   
    filename = "numbers.txt"
    test_data = """13420.22
45229.32
35223.22
29302.20
95893.21
94721.94
84720.32
84793.02
10394.21
30233.33
23432.32"""

    
    with open(filename, "w") as f:
        f.write(test_data)

    
    total = 0
    count = 0

    try:
        with open(filename, "r") as file:
            for line in file:
                try:
                   
                    number = float(line.strip())
                    total += number
                    count += 1
                    
                    print(f"{number:,.2f}")
                except ValueError:
                    print(f"Skipping invalid line: {line.strip()}")

        
        if count > 0:
            average = total / count
            print("\nSummary:")
            print(f"Total: {total:,.2f}")
            print(f"Number of entries: {count}")
            print(f"Average: {average:,.2f}")
        else:
            print("No valid numbers were processed.")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")



main()
