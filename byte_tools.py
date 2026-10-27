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
        print("[2] Fast Ping Sweep")
        print("[0] Exit")
        print("=" * 40)
        
        choice = input("Select an option: ")
        
        # الخيار الأول: فحص البورتات
        if choice == '1':
            target_ip = input("\nEnter Target IP (or press Enter for 127.0.0.1): ")
            if not target_ip.strip():
                target_ip = "127.0.0.1"
                
            print(f"\nStarting Port Scanner on {target_ip}...")
            # بنشغل السكانر ونبعتله الـ IP
            os.system(f'python scanner.py {target_ip}')
            input("\nPress Enter to return to menu...")
            
        # الخيار التاني: أداة فحص الشبكة السريعة
        elif choice == '2':
            base_ip = input("\nEnter base IP (e.g., 192.168.0): ")
            if not base_ip.strip():
                print("[!] Base IP is required.")
                input("\nPress Enter to return to menu...")
                continue
                
            print(f"\nStarting Fast Ping Sweep on {base_ip}...")
            # بنشغل أداة البينج سويب ونبعتلها الـ IP
            os.system(f'python fast_ping_sweep.py {base_ip}')
            input("\nPress Enter to return to menu...")
            
        # الخيار صفر: الخروج
        elif choice == '0':
            print("\nGoodbye, Byte! Use your tools for good.")
            break
            
        else:
            print("\n[!] Invalid option. Try again.")
            input("\nPress Enter to try again...")

if __name__ == "__main__":
    main_menu()