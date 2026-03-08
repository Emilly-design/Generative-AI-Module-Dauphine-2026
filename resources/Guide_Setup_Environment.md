# Python Flask Development Environment Setup Guide

## Introduction
This guide will help you set up a professional Python development environment for working with Flask applications. This setup is specifically designed for the Generative AI module and will ensure you have all the necessary tools to complete your coursework and projects.

## Prerequisites
- A computer running Windows, macOS, or Linux
- Administrator/root access to install software
- At least 4GB of RAM (8GB recommended)
- At least 10GB of free disk space

## 1. Install Git
Git is essential for version control and collaboration.

### Windows/macOS:
- **Download**: Go to the [Git website](https://git-scm.com/) and download the installer for your operating system.
- **Install**: Run the installer and follow the on-screen instructions.
  - **Important**: Check the option "Add Git to PATH" during installation.
  - **macOS users**: You can also install Git using Homebrew: `brew install git`

### Verification:
Open a terminal/command prompt and run:
```bash
git --version
```
You should see the installed Git version.

## 2. Install a Code Editor

You can use any code editor you prefer. Here are some recommended options:

### Option A: VS Code (Recommended)
- **Download**: Go to the [VS Code website](https://code.visualstudio.com/) and download the installer.
- Install the **Python** and **Jupyter** extensions from the Extensions sidebar.

### Option B: Any editor of your choice
- PyCharm, Sublime Text, or any editor you're comfortable with.

## 3. Install Claude Code

Claude Code is an AI-powered coding assistant that runs in your terminal. It can understand your codebase, write code, run commands, and help you build projects faster.

### Installation:

Claude Code requires Node.js. Install it first if you don't have it:
- **Download Node.js**: Go to the [Node.js website](https://nodejs.org/) and download the LTS version.

Then install Claude Code globally:
```bash
npm install -g @anthropic-ai/claude-code
```

### Usage:
Navigate to your project directory and launch Claude Code:
```bash
cd your-project-folder
claude
```

Claude Code will be your AI pair-programmer throughout this course. Use it to:
- Generate code from natural language descriptions
- Debug and fix issues in your code
- Understand unfamiliar code
- Run and test your application
- Help with Git operations

### Authentication:
When you first run Claude Code, you will need to authenticate. You can log in with your Anthropic account or use an API key directly:
```bash
# Set your API key (the instructor will provide one during the course)
export ANTHROPIC_API_KEY=your_api_key_here
```

For more information, see the [Claude Code documentation](https://docs.anthropic.com/en/docs/claude-code).

## 4. Install Python
We'll use Python 3.12 for this course.

### Windows/macOS:
- **Download**: Visit the [Python website](https://www.python.org/downloads/) and download Python 3.12.
- **Install**: Run the installer with these important steps:
  - Check "Add Python 3.12 to PATH"
  - Choose "Customize installation"
  - Select all optional features
  - Choose "Install for all users" (recommended)

### Verification:
Open a terminal/command prompt and run:
```bash
python --version
```
You should see "Python 3.12.x"

## 5. Set Up Your Development Environment

You have two options for managing your Python environment:

### Option 1: Using Python's built-in venv (Recommended for beginners)
```bash
# Create a new virtual environment
python -m venv genai_env

# Activate the environment
# On Windows:
genai_env\Scripts\activate
# On macOS/Linux:
source genai_env/bin/activate
```

### Option 2: Using Anaconda (Optional)
Anaconda provides a more comprehensive environment management system with additional scientific computing packages.

#### Installation:
- **Download**: Go to the [Anaconda website](https://www.anaconda.com/products/individual) and download Anaconda for Python 3.12.
- **Install**: Run the installer and follow the on-screen instructions.
  - Choose "Install for all users" (recommended)
  - Add Anaconda to PATH (recommended)

#### Create and Activate Environment:
```bash
# Create a new environment
conda create -n genai_env python=3.12

# Activate the environment
conda activate genai_env
```

### Verification (for both options):
```bash
# Verify Python version
python --version

# Verify environment is active (should show genai_env)
which python  # On macOS/Linux
where python  # On Windows
```

### Install Required Packages
In your activated environment (using either venv or conda), run:
```bash
pip install -r requirements.txt
```

Or install manually:
```bash
pip install pandas numpy flask anthropic chromadb jupyter ipykernel
```

### Verify Package Installation:
```bash
# Test Flask installation
python -c "import flask; print(flask.__version__)"
# Test Anthropic SDK
python -c "import anthropic; print('Anthropic SDK installed successfully')"
# Test other packages
python -c "import pandas as pd; import numpy as np; print('All packages installed successfully')"
```

## 6. Configure Your Editor

### If using VS Code:

#### Install Required Extensions
1. Open VS Code
2. Go to Extensions (sidebar)
3. Install these essential extensions:
   - Python
   - Jupyter

#### Configure Python Interpreter
1. Open Command Palette (Ctrl+Shift+P / Cmd+Shift+P)
2. Type "Python: Select Interpreter"
3. Choose the `genai_env` environment you created

## 7. Best Practices

### Version Control
- Initialize Git in your project directory
- Create a `.gitignore` file
- Make regular commits with meaningful messages

### Virtual Environment
- Always work in your virtual environment
- Keep `requirements.txt` up to date
- Document all dependencies

### Code Organization
- Follow PEP 8 style guide
- Use meaningful variable and function names
- Add comments and docstrings
- Write tests for your code

### Using Claude Code effectively
- Be specific in your prompts: describe what you want clearly
- Use it to scaffold boilerplate code, then refine
- Ask it to explain code you don't understand
- Use it to debug: paste error messages and ask for help

## Need Help?
If you encounter any issues during setup:
1. Ask Claude Code in your terminal
2. Search for similar issues online
3. Contact your instructor
