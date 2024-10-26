# MacOS saverScrape

is a command-line tool for downloading and managing wallpapers and media files directly from specified URLs on macOS. It includes functionality for downloading files with progress tracking and managing downloaded files. The project is modular, with organized Python files for a cleaner structure.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/unawarexi/.git
   cd wallget
   ```
2 **Install Requirements:**

- Ensure you have Python 3 installed.
- Install any additional dependencies if necessary.
- Run with Administrator Privileges:

Some functions require administrator privileges to access and manage system files. Run using sudo:
3. **Starting WallGet:**

Run the main script to begin:
```bash
Copy code
sudo python3 macOS.py
```
4. **Selecting a Category:**

You will be prompted to select a category from available wallpaper or media categories.
5. **Download or Delete:**

After selecting a category, choose to (d)ownload or (x)delete files in that category. You can select specific files or download all items in the chosen category.
The download process shows real-time progress with a percentage indicator.
6. **Updating Download Status in Settings:**
You may choose to kill the idleassetsd process to refresh download statuses within macOS settings.

### Project Structure
This project is organized into separate files for modularity:

```bash
saverScrap/
├── macOS.py                  # Main file for running the application
├── utils/
│   ├── file_management.py    # Functions for file download and delete operations
│     
├── data/
│   └── network.py            # Networking functions for handling HTTP requests
├── routes/
│   └── paths.py            # System path specifications and functions
└── README.md                 # Project documentation
```
- #### macOS.py: Contains the primary script and main program flow, prompting the user for input and directing actions to appropriate modules.
- #### utils/file_management.py: Manages file downloading and deletion, including functions for showing download progress.
- #### routes/paths.py: Houses system paths and specifications functions such as formatting bytes and converting user inputs.
- #### data/network.py: Contains network-related functions for establishing secure connections and obtaining file size metadata.

## Features
**Category Selection:** Choose from available wallpaper or media categories.
**Download with Progress Tracking:** Shows real-time progress percentage for each file.
**Delete Files:** Clean up previously downloaded files from the system.
**Disk Space Check:** Verifies available space before downloading files.
**Process Management:** Option to kill the idleassetsd process to update download statuses in macOS settings.

Contributing
Contributions are welcome! Feel free to submit pull requests or report issues.

```bash
Fork the Project
Create a Feature Branch (git checkout -b feature/NewFeature)
Commit Changes (git commit -m 'Add NewFeature')
Push to Branch (git push origin feature/NewFeature)
Open a Pull Request
```
## License
Distributed under the MIT License. See LICENSE for more information.

## Disclaimer
Please run this tool with caution as it may interact with system-level files, requiring elevated permissions.