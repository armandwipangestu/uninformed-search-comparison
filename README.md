## Installation on Linux

1. Clone the repository:

   ```bash
   git clone https://github.com/armandwipangestu/uninformed-search-comparison
   cd uninformed-search-comparison

   sudo apt install python3-venv
   python -m venv venv
   source venv/bin/activate
   ```

2. Install required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Running the script:

   ```bash
    # Run the experiment
    python src/main.py

    # Show visualize
    python src/plot_result.py
   ```

## Installation on Windows

1. Clone the repository:

   ```bash
   git clone https://github.com/armandwipangestu/uninformed-search-comparison
   cd uninformed-search-comparison

   python -m venv venv
   . .\venv\Scripts\Activate.ps1
   ```

2. Install required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Running the service:

   ```bash
    # Run the experiment
    python src/main.py

    # Show visualize
    python src/plot_result.py
   ```
