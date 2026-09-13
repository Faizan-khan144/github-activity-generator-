<div align="center">

# GitHub Activity Generator

### A Python utility for generating controlled Git commit activity

Create, test, and experiment with Git commit history using customizable contribution patterns.

<br>

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge\&logo=python\&logoColor=white)](https://www.python.org/)
[![Git](https://img.shields.io/badge/Git-Version_Control-F05032?style=for-the-badge\&logo=git\&logoColor=white)](https://git-scm.com/)
[![GitHub](https://img.shields.io/badge/GitHub-Repository-181717?style=for-the-badge\&logo=github\&logoColor=white)](https://github.com/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

</div>

---

## Overview

**GitHub Activity Generator** is a lightweight Python utility for creating controlled Git commit activity.

It was built primarily for experimenting with Git history, contribution graphs, automated workflows, and GitHub behavior in a dedicated repository.

Instead of manually creating individual commits, the tool can automate the process based on the configuration and workflow defined by the project.

---

## Features

* Generate Git commits automatically
* Work with custom contribution dates
* Experiment with Git commit history
* Test GitHub contribution behavior
* Automate repetitive Git operations
* Python-based and lightweight
* Includes contribution testing utilities
* Includes example activity repositories
* Suitable for Git and GitHub learning

---

## How It Works

```text
Configuration
     │
     ▼
Generate Changes
     │
     ▼
Create Git Commits
     │
     ▼
Assign Commit Dates
     │
     ▼
Push to GitHub
     │
     ▼
GitHub Contribution Activity
```

The generator creates Git commits according to the selected configuration. GitHub then processes those commits according to its contribution rules.

---

## Project Structure

```text
github-activity-generator/
│
├── .github/
│   ├── FUNDING.yml
│   ├── README.md
│   ├── before.png
│   ├── after.png
│   └── workflows/
│       └── build.yml
│
├── contribution-test/
├── github-activity/
├── github-activity-backup/
├── github-activity-demo-2026-09-13-00-42-37/
├── github-activity-demo-2026-09-13-00-44-36/
│
├── contribute.py
├── test_contribute.py
└── LICENSE
```

---

## Requirements

* Python 3.x
* Git
* GitHub account
* A repository you own or have permission to modify

Check your installation:

```bash
python --version
git --version
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Faizan-khan144/github-activity-generator-.git
```

Enter the project directory:

```bash
cd github-activity-generator-
```

---

## Usage

Run the generator:

```bash
python contribute.py
```

Follow the instructions provided by the script.

After generating the activity, inspect the Git history:

```bash
git log --oneline
```

Check the repository state:

```bash
git status
```

Push the generated commits:

```bash
git push
```

---

## Testing

The project includes a test script:

```bash
python test_contribute.py
```

Use it to test the contribution functionality before working with another repository.

---

## Screenshots

### Before

<img src=".github/before.png" alt="GitHub contribution graph before activity generation" width="800">

### After

<img src=".github/after.png" alt="GitHub contribution graph after activity generation" width="800">

---

## GitHub Contribution Rules

GitHub does not necessarily count every commit toward a user's contribution graph.

Contribution visibility can depend on factors such as:

* Commit email attribution
* Repository visibility
* Repository ownership
* Default branch
* GitHub contribution rules

For experimentation, using a dedicated test repository is recommended.

---

## Responsible Use

This project is intended for:

* Learning Git
* Testing automation
* GitHub experimentation
* Demonstrations
* Contribution-graph research
* Development workflow testing

Do not use generated activity to falsely represent professional experience, employment, project work, or development history.

---

## Contributing

Contributions are welcome.

Fork the repository, create a feature branch, make your changes, and open a pull request.

```bash
git checkout -b feature/my-feature
git add .
git commit -m "Add my feature"
git push origin feature/my-feature
```

---

## License

This project is licensed under the **MIT License**.

See [LICENSE](LICENSE) for the full license text.

---

<div align="center">

## Built with Python & Git

**Muhammad Faizan Khan**

[GitHub](https://github.com/Faizan-khan144) · [LinkedIn](https://www.linkedin.com/in/muhammad-faizan-khan-76513041/)

</div>
