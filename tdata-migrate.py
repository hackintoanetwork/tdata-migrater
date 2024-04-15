import os
import shutil
import sys

def migrate_telegram_tdata_mac(new_tdata_path):
    home = os.getenv('HOME')
    old_tdata_path = os.path.join(home, "Library/Application Support/Telegram Desktop/tdata")
    
    if os.path.exists(old_tdata_path):
        try:
            shutil.rmtree(old_tdata_path)
            print(f"The directory {old_tdata_path} has been deleted.")
        except Exception as e:
            print(f"[-] An error occurred: {e}")
            return

    try:
        shutil.copytree(new_tdata_path, old_tdata_path)
        print(f"The directory {new_tdata_path} has been copied to {old_tdata_path}.")
    except Exception as e:
        print(f"[-] An error occurred during copying: {e}")

def migrate_telegram_tdata_win(new_tdata_path):
    home = os.getenv('USERPROFILE')
    if home is None:
        print("[-] Error: USERPROFILE environment variable not found.")
        return

    old_tdata_path = os.path.join(home, "AppData\\Roaming\\Telegram Desktop\\tdata")
    print(old_tdata_path)
    if os.path.exists(old_tdata_path):
        try:
            shutil.rmtree(old_tdata_path)
            print(f"The directory {old_tdata_path} has been deleted.")
        except Exception as e:
            print(f"[-] An error occurred: {e}")
            return
    try:
        shutil.copytree(new_tdata_path, old_tdata_path)
        print(f"The directory {new_tdata_path} has been copied to {old_tdata_path}.")
    except Exception as e:
        print(f"[-] An error occurred during copying: {e}")

def main():
    if len(sys.argv) < 3:
        print("Usage: python3 tdata-migrate.py --mac <path_to_new_tdata> or python3 tdata.py --win <path_to_new_tdata>")
        return

    platform_flag = sys.argv[1]
    new_tdata_path = sys.argv[2]

    if platform_flag == "--mac":
        migrate_telegram_tdata_mac(new_tdata_path)
    elif platform_flag == "--win":
        migrate_telegram_tdata_win(new_tdata_path)
    else:
        print("Invalid flag. Use --mac for macOS or --win for Windows.")

if __name__ == "__main__":
    main()