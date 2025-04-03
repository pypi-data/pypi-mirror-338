# Project Setup and Usage Guide

## Environment Setup
This project uses the following environment:
- Micromamba as package manager
- Python 3.13
- PyTorch 2.6.0
- PyTorch Lightning

You can use `setup.ps1` to install all required dependencies.

## Mode Configuration
The project supports different running modes:
- Default mode: test
- Available modes: test, dev, prod

To change the mode, use the following command:
```powershell
.\set_mode.ps1 -Mode [mode_name]
```
Example:
```powershell
.\set_mode.ps1 -Mode prod
.\set_mode.ps1 -Mode dev
.\set_mode.ps1 -Mode test
```

## Running and Debugging
The project is configured for both running and debugging in VS Code:
1. Use the right-click context menu in the editor
2. Select "Run Python File" to execute the current file
3. Debug configurations are available in `.vscode` settings

## Environment Information
The project includes an environment information script (`src/env.py`) that displays:
- Python version
- PyTorch version
- CUDA version and device information (if available)
- Python executable path

To run the environment check:
```powershell
D:/dev/mamba/envs/pytorch/python.exe src/env.py
```

## Temporary Files
When creating temporary files:
- All temporary files must be created in the `temp` directory
- The `temp` directory is ignored by git (configured in `.gitignore`)
- This rule applies to all AI-assisted code generation and temporary file creation

## Unit Testing
The project includes a sample test file (`tests/add_test.py`) that demonstrates basic unittest setup and structure. Here's how to work with unit tests:

### Running Tests
You can run tests in several ways:
1. In Cursor IDE:
   - Open the Testing view in the sidebar
   - All test files will be automatically discovered
   - You can run individual tests or all tests from the Testing view
   - When editing a test file (e.g., `add_test.py`), right-click in the editor and select "Run Python File" to run the test

2. In Editor:
   - Open the test file (e.g., `add_test.py`) in the editor
   - Right-click in the editor
   - Select "Run Python File"
   - The test will run in the terminal

### Test Configuration
1. Configure test settings using `Ctrl+Shift+P`
2. Select "Python: Configure Tests"
3. Choose "unittest" (not pytest) as the test framework
4. Select the `tests` folder
5. Test files should follow the `*_test.py` naming convention

### Example Test Structure
The `add_test.py` demonstrates:
- Basic unittest setup with `unittest.TestCase`
- Test case structure with `setUp` and `tearDown` methods
- Simple assertion testing (1+2=3)