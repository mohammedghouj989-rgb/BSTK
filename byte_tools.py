import os
import sys

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def main_menu():
    while True:
        clear_screen()
        print("=" * 40)
        print("      [ Byte Security Toolkit ]")
        print("=" * 40)
        print("[1] Port Scanner")
        print("[2] Ping Sweep - Coming Soon")
        print("[0] Exit")
        print("=" * 40)
        
        choice = input("Select an option: ")
        
        if choice == '1':
            target_ip = input("\nEnter Target IP (or press Enter for 127.0.0.1): ")
            
            if not target_ip.strip():
                target_ip = "127.0.0.1"
                
            print(f"\nStarting Port Scanner on {target_ip}...")
            os.system(f'python scanner.py {target_ip}')
            input("\nPress Enter to return to menu...")
            
        elif choice == '2':
            print("\n[!] This tool is under development.")
            input("\nPress Enter to return to menu...")
            
        elif choice == '0':
            print("\nGoodbye, Byte! Use your tools for good.")
            sys.exit()
            
        else:
            print("\n[!] Invalid option. Try again.")
            input("\nPress Enter to try again...")

if __name__ == "__main__":
    main_menu()
