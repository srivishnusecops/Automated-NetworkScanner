import subprocess
import os
from voice import talk

# Function to run masscan (from masscan.py)
def run_masscan():
    # Call masscan.py to run Masscan
    print("Running Masscan...")
    # Assuming masscan.py is in the same directory
    subprocess.run(["python3", "masscan.py"])

# Function to run nmapscanner (from nmapscanner.py)
def run_nmapscanner():
    # Call nmapscanner.py to run Nmap Scanner
    print("Running NmapScanner...")
    # Assuming nmapscanner.py is in the same directory
    subprocess.run(["python3", "nmapscanner.py"])

def main():
    # Display menu
    print("Welcome to the Automated Network Tool")
    print("Choose a tool to use:")
    print("1. Masscan")
    print("2. NmapScanner")
    
    # Voice prompt
    talk("Please select a tool by entering the number")

    # Get user input
    choice = input("Enter your choice (1 or 2): ")
    
    if choice == '1':
        run_masscan()
    elif choice == '2':
        run_nmapscanner()
    else:
        print("Invalid choice! Please select 1 or 2.")
        talk("Invalid choice. Please select 1 or 2.")

if __name__ == "__main__":
    main()
