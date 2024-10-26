import os
from data.network import download_file_with_progress
from routes.paths import IDLEASSETSD_PATH, STRINGS_PATH, ENTRIES_PATH, VIDEO_PATH
from utils.file_management import validate_environment, read_localizable_strings, read_asset_entries, as_int

def main():
    # Check if running as admin
    if os.geteuid() != 0:
        print(f'Please run as admin: sudo python3 "{__file__}"')
        exit()

    print("WallGet Live Wallpaper Download/Delete Script")
    print("---------------------------------------------\n")

    # Validate environment
    validate_environment()

    # Read localizable strings
    strings = read_localizable_strings()

    # Read asset entries
    asset_entries = read_asset_entries()

    # Show categories
    item = 0
    categories = asset_entries.get("categories", [])
    for category in categories:
        name = strings.get(category.get("localizedNameKey", ""), "")
        item += 1
        print(f"{item}. {name}")
    print(f"{item + 1}. All")

    # Select category
    category_index = as_int(input("\nCategory number? "))
    if category_index < 1 or category_index > item + 1:
        print("\nNo category selected.")
        exit()
    category_id = (
        categories[int(category_index) - 1]["id"] if category_index <= item else None
    )

    # Download or delete?
    action = input("\n(d)Download or (x)delete? (d/x) ").strip().lower()
    if action != "d" and action != "x":
        print("\nNo action selected.")
        exit()

    # Select single file or download all
    select_and_download_single_or_all(category_id, asset_entries, strings, action)

    # Optionally kill idleassetsd to update wallpaper status
    should_kill = (
        input("\nKill idleassetsd to update download status in Settings? (y/n) ")
        .strip()
        .lower()
    )
    if should_kill == "y":
        os.system("killall idleassetsd")
        print("Killed idleassetsd.")

    print("\nDone.")

def select_and_download_single_or_all(category_id, asset_entries, strings, action):
    """
    Displays a list of items in the selected category and prompts user to download a single item or all items.
    """
    items = [
        (strings.get(asset.get("localizedNameKey", ""), ""), asset.get("url-4K-SDR-240FPS", ""), f"{VIDEO_PATH}/{asset.get('id')}.mp4")
        for asset in asset_entries.get("assets", [])
        if not category_id or category_id in asset.get("categories", [])
    ]
    
    if not items:
        print("No items found in this category.")
        return

    # Display items in the selected category
    print("\nItems in selected category:")
    for index, (label, url, file_path) in enumerate(items, start=1):
        print(f"{index}. {label}")

    # Ask user for selection
    item_index = as_int(input("\nSelect item number to download or '0' to download all: "))
    if item_index == 0:
        download_items(items, action)
    elif 1 <= item_index <= len(items):
        download_items([items[item_index - 1]], action)
    else:
        print("Invalid selection.")

def download_items(items, action):
    """
    Downloads or deletes items based on the action ('d' for download, 'x' for delete).
    """
    if action == "d":
        print("\nStarting download...")
        for item in items:
            label, url, file_path = item
            download_file_with_progress((label, url, file_path))
            print(f"\n  Downloaded '{label}'")
        print(f"\nDownloaded {len(items)} file(s).")
    elif action == "x":
        print("\nDeleting files...")
        for item in items:
            label, _, file_path = item
            if os.path.exists(file_path):
                os.remove(file_path)
                print(f"  Deleted '{label}'")
        print(f"\nDeleted {len(items)} file(s).")

if __name__ == "__main__":
    main()
