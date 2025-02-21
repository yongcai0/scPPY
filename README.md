<div style="background-color: #f5f5f5; padding: 10px; border: 1px solid #ccc; border-radius: 5px;"> <button onclick="copyToClipboard()" style="background-color: #007bff; color: white; border: none; padding: 5px 10px; cursor: pointer; border-radius: 3px;">Copy</button> <pre id="copyText" style="margin-top: 10px; white-space: pre-wrap; overflow-x: auto;"> # scPPY - Free Prepayment Library
Welcome to scPPY, a free open-source library for modeling mortgage prepayment behavior, specifically tailored for U.S. agency mortgage-backed securities (MBS). This project provides a Python-based tool to project prepayment speeds, including the three major components: housing turnover, refinancing, and curtailment. It’s designed for researchers, analysts, and developers interested in mortgage analytics.

Overview
scPPY simulates prepayment behavior for 30-year fixed-rate mortgages, such as those issued by Fannie Mae, Freddie Mac, or Ginnie Mae. The model outputs prepayment speeds in Conditional Prepayment Rate (CPR), which can be visualized over the loan’s life. This library is ideal for studying the dynamics of agency MBS pools, including low-coupon pools like FNCL 3 (3% WAC).

Key Components
The prepayment model includes the following major components:

Housing Turnover: Prepayments due to borrowers selling or moving, influenced by housing market conditions and mobility.
Refinancing: Prepayments resulting from borrowers refinancing to lower interest rates, sensitive to rate incentives.
Curtailment: Partial prepayments where borrowers make extra principal payments, typically increasing with loan age and borrower savings.
Getting Started
Prerequisites
Python 3.7 or later
Required packages: numpy, matplotlib (install with pip install numpy matplotlib)
Installation
Clone this repository to your local machine:

bash
Wrap
Copy
git clone git@github.com:yongcai0/scPPY.git
cd scPPY
Usage
Open the provided Jupyter Notebook (notebook.ipynb) in a Jupyter environment.
Run the notebook to execute the prepayment model and visualize results.
Modify the sample file (script.py in dist/) or create your own to adjust model parameters (e.g., loan term, interest rate, curtailment assumptions).
Sample File
A sample obfuscated Python script (dist/script.py) is included, demonstrating the prepayment model. This file, protected with Pyarmor, generates the prepayment projections. To use it, ensure the dist/ folder and its runtime files (pyarmor_runtime_xxxxxx/) are intact, and import it in your notebook:

python
Wrap
Copy
import sys
sys.path.append('dist')
import script
# Access model outputs or functions as needed
Results
The library projects prepayment speeds (CPR) over the life of a 30-year mortgage, visualized in the following graph:



Blue Line (CPR): Total prepayment speed, reflecting housing turnover, refinancing, and curtailment.
Red Line (PCPR): Principal Conditional Prepayment Rate, focusing on principal prepayments (e.g., curtailment or partial payments).
The graph shows speeds starting at ~6 CPR, rising to 10, 20, and peaking at 30 CPR late-term, consistent with a low-coupon pool (e.g., 3% WAC) in a high-rate environment.
Contributing
Contributions are welcome! To contribute:

Fork this repository.
Create a branch for your changes (git checkout -b feature/new-feature).
Commit changes (git commit -m "Add new feature").
Push to the branch (git push origin feature/new-feature).
Submit a pull request.
License
This project is open-source and available under the MIT License. See the LICENSE file for details.

Contact
For questions or feedback, contact Yong Cai at [your-email@example.com] or open an issue on this repository.
</pre>

<script> function copyToClipboard() { const text = document.getElementById('copyText').textContent; navigator.clipboard.writeText(text).then(() => { alert('Copied to clipboard!'); }).catch(err => { alert('Failed to copy: ' + err); }); } </script> </div>