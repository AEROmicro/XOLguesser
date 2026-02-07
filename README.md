## Vision



XOLguesser is designed to be:



- Lightweight

- Fully open-source

- Expandable

- Cross-platform

- Long-term maintainable



Built for learning, competition, and global geography mastery.XOLguesser

**XOLguesser** is a lightweight, cross-platform geography quiz engine written entirely in pure Python.

It runs in the terminal with zero external dependencies and is licensed under the GNU General Public License v3.0 (GPLv3).

Designed for performance, portability, and long-term extensibility.

---

## Features

- Countries & Territories mode
- Guess the Capital
- Reverse Capitals (Capital → Country)
- U.S. States
- U.S. State Capitals
- Canadian Provinces
- Optional Timer Mode (cross-platform, pure Python)
- Timed “Name as Many Countries as Possible” mode
- Fuzzy spell-check (minor typos allowed)
- Live stats tracking
- Tag-based filtering system for scalable game modes
- No external dependencies

---

## 🛠 Requirements

- Python 3.8 or higher
- No additional libraries required

Works on:
- Linux
- Windows
- macOS

---

## Installation

Clone the repository:

```bash
git clone https://github.com/AEROmicro/XOLguesser.git
cd XOLguesser
```

Run the game:

```bash
python XOLguesser.py
```

That’s it.

---

## Game Modes

### Main Menu Options

1. Countries / Territories  
2. Countries Only  
3. Territories Only  
4. U.S. States  
5. Canadian Provinces  
6. Guess the Capital  
7. State Capitals  
8. Guess the Country from the Capital  
9. Guess the State from the Capital  
10. Timed Modes  

---

## Timer Mode

Optional timed answering system:

- 30-second standard mode
-60-second extended mode
- Automatic timeout handling
- Fully cross-platform implementation

---

## Speed Mode

Timed challenge:

- Name as many countries as possible before time runs out
- Duplicate answers prevented
- Real-time validation
- Final results summary

---

##  Engine Design

XOLguesser uses a tag-based architecture for flexible filtering and future expansion.
Most of the game follows this structure, with territories and states follow a bit of a diffrent format

Example data structure:

```python

    {"name":"Iceland",
    "short":"Iceland",
    "continent":"Europe",
    "capital":"Reykjavík",
    "region":"Northern Europe",
    "population":0.36,"aliases":[],
    "territory":False, 
    "un_member":True},

```

This allows:

- Easy filtering by type
- Reverse question generation
- Continent-based modes
- Clean scalability without rewriting logic
-Easy to add extra catigorys if wanted

---

## Project Structure

```
XOLguesser.py
README.md
LICENSE
```

Script layout:

1. Imports  
2. Utility functions (timer, fuzzy matching, universal answer handler)  
3. Game mode functions  
4. Main menu loop  

---

## License

This project is licensed under the **GNU General Public License v3.0 (GPLv3)**.

You may:

- Use
- Modify
- Distribute

Under the condition that:

- Modified versions must also be licensed under GPLv3
- Original copyright notices must remain intact

See the `LICENSE` file for full legal details.

---

## Author

Developed by **AEROforge**  
Supervised and Founded by **AEROxol**  
Programming and Debugging by **AEROxol**

Copyright (C) 2026 AEROforge

---

##  Contributing

Contributions are welcome.

To contribute:

1. Fork the repository
2. Create a new branch
3. Commit your changes
4. Submit a pull request

All contributions must comply with GPLv3.

---

## Disclaimer
This software is provided “as is”, without warranty of any kind.

See the GNU GPLv3 license for full terms.

This software is provided “as is”, without warranty of any kind.
See the GNU GPLv3 license for full terms.
