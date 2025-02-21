# scPPY - Free Prepayment Library

Welcome to **scPPY**, a free library for modeling mortgage prepayment behavior, specifically tailored for U.S. agency mortgage-backed securities (MBS). This project provides a Python-based tool to project prepayment speeds, including the three major components: housing turnover, refinancing, and curtailment. It’s designed for researchers, analysts, and developers interested in mortgage analytics.

## Overview
scPPY simulates prepayment behavior for 30-year fixed-rate mortgages issued by Fannie Mae. The model outputs prepayment speeds in Conditional Prepayment Rate (CPR), which can be visualized over the loan’s life. This library is ideal for studying the dynamics of agency MBS pools or loans.

## Key Components
The prepayment model includes the following major components:
- **Housing Turnover**: Prepayments due to borrowers selling or moving, influenced by housing market conditions and mobility.
- **Refinancing**: Prepayments resulting from borrowers refinancing to lower interest rates, sensitive to rate incentives.
- **Curtailment**: Partial prepayments where borrowers make extra principal payments, typically increasing with loan age and borrower savings.

## Getting Started
### Prerequisites
- Python 3.7 or later
- Required packages: `numpy`, `matplotlib` (install with `pip install numpy matplotlib`)

### Installation
Clone this repository to your local machine:

git clone git@github.com:yongcai0/scPPY.git
cd scPPY

### Usage
Open the provided Jupyter Notebook (SC_PPY_model_Run.ipynb) in a Jupyter environment.
Run the notebook to execute the prepayment model and visualize results.
To use the library properly, ensure the dist/ folder and its runtime files (pyarmor_runtime_xxxxxx/) are intact, and import it in your notebook same way as SC_PPY_model_Run.ipynb does:

import sys
sys.path.append('dist')
import YC_ppy

### Sample File
A sample pool (fnm3467_short.csv) is included. This file has the information fields needed for historical and future prepayment projection. This sample shows how pool information should be formatted as input.

### License
This project is open-source and available under the MIT License. See the LICENSE file for details.

### Contact
For questions or feedback, open an issue on this repository.
# Access model outputs or functions as needed

