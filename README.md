# RL_proj – Reinforcement Learning for Tic-Tac-Toe

A reinforcement learning project that applies machine learning techniques to play the classic game of Tic-Tac-Toe. This project demonstrates the use of Markov Decision Processes (MDP) and value iteration for game strategy development.

---

## Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contribution](#contribution)
- [License](#license)
- [Contact](#contact)
- [Credits](#credits)

---

## Overview

This is a sample project that showcases how reinforcement learning can be used to solve classic board games. The repository is structured for clarity, modularity, and ease of extension.

---

## Project Structure
```
RL_proj/
├── src/
│   ├── components/
│   │   ├── MDP.py
│   │   ├── game_rules.py
│   │   ├── value_iteration.py
│   │   └── __init__.py
│   ├── constants/
│   ├── exception/
│   ├── logging/
│   ├── utils/
│   └── __init__.py
├── main.py
├── projectstructure.py
├── requirements.txt
├── setup.py
├── .gitignore
└── README.md
```

---

## Features

- **Tic-Tac-Toe Environment**: Implementation of the classic game rules.
- **Value Iteration**: Solves the MDP to find optimal strategies.
- **Modular Codebase**: Easily extendable for other board games or RL algorithms.

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Sky313/RL_proj.git
cd RL_proj
```
### 2. Install Dependencies
It is recommended to use a virtual environment:

```
python -m venv venv
source venv/bin/activate  
pip install -r requirements.txt
```
## Usage
### Run the Main Program
To start training or evaluating the RL agent on Tic-Tac-Toe, run:

```
python main.py
```
### Project Structure Utility
To print or inspect the project structure, you can run:

```
python projectstructure.py
```
### Customization

- Game rules and logic are in src/components/game_rules.py.
- MDP and value iteration logic are in src/components/MDP.py and src/components/value_iteration.py.

Feel free to modify these files to experiment with different RL strategies or environments.

## Contribution
Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/your-feature-name`
3. Commit your changes: `git commit -am 'Add new feature'`
4. Push to your branch: `git push origin feature/your-feature-name`
5. Open a Pull Request on GitHub.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contact
For questions, suggestions, or feedback, please open an issue or contact the maintainer.

## Credits
Project Maintainer: Sky313

Thanks to the open-source community for inspiration and resources.
