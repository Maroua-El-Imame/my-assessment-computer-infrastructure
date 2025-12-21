# Computer Infrastructure

Lecturer: Ian McLoughlin  
Computer Infrastructure S2-2025  
Higher Diploma in Science in Computing in Data Analytics  
Atlantic Technological University - ATU Galway Mayo 2025/2026.  

Author : Maroua EL imame  
Submission deadline : 21/12/2025 

 <br />
 <br />


## Introduction  

This notebook has been prepared to document the development and completion of the tasks assigned in Computer Infrastructure module's assessment.   
It follows the structure outlined in the assignment sheet and addresses each task in the order provided.   


## Purpose & Target Audience  

The purpose of this is to communicate the findings in a structured and comprehensible manner.  
The work is intended for computing professionals (such as a prospective employer) who may not be familiar with the specific tools, libraries, or programming languages employed.  
The notebook code and markdown sections are organized with concise explanations to facilitate understanding of the workflow.  
Results and visualizations are presented with clear descriptions to emphasize the key insights.  


## Assessment Problems

#### 🔹Problem 1: Data from yfinance  
 _Retrieving and preparing data_  
- Created a function `get_data()` to download hourly stock data for the past five days for the FAANG companies and save it as timestamped CSV files in a dedicated `data` folder.



#### 🔹Problem 2: Plotting Data  
 _Visualizing data_  
- Created a function `plot_data()` to read the latest stock data and generate a plot of the closing prices for the five FAANG companies, saving the plot as a timestamped PNG file in a dedicated `plots` folder.


#### 🔹Problem 3: Script
 _Execute a Python script_
- Created a Python script called faang.py in my repository root and added the shebang line (#!/usr/bin/env python3) at the top so the script can run directly from terminal, I also made the script executable with chmod +x faang.py then,lastly, I tested it by running ./faang.py in terminal, and verified that it downloaded the data and created the plot.  

#### 🔹Problem 4: Automation  
 _Script automation_  
- Created the workflow file at .github/workflows/faang.yml and configured it to run automatically every Saturday morning at 6:23 AM  
I added manual trigger option so I could test it anytime, I also set up the workflow steps, each line of the workflow is explained in my notebook problems.ipynb  

## Repository Overview: Audience-Focused Guide  

This repository is organized to clearly separate analysis, automation and outputs, so the workflow can be understood without prior knowledge of python.  

### Repository structure 

*README.md*  
Main repository page, similar to a book cover, where clear instructions are listed. It tells the reader what they're about to read and why is it useful.  

*data folder*     
This folder contains the downloaded hourly stock data for FAANG companies covering the past five days, stored as timestamped CSV files, with new files added on each time the notebook, script or workflow run.  

*plots folder*    
This folder contains plots generated from the analysis.  
Each plot shows the closing prices of the five FAANG companies using the most recent stock csv file and is saved as a timestamped PNG file.  
Multiple plots are stored over time, as a new file is created each time the notebook, script, or automated/manual work flow run.

*requirements.txt*  
Lists the Python packages required to run the notebook and script.

*problems.ipynb*  
An interactive notebook to write code and run it piece by piece.   

*faang.py*  
A Python script that automates data processing and plotting.

*.github/workflows/faang.yml*  
GitHub Actions workflow that automates the execution of the Python script on a schedule or manual trigger.  

### Simplified Explanation of the Workflow    

*Problem 1 — Data Collection (FAANG Stocks)*  

This step automatically fetches the last 5 days of hourly stock data for major tech companies (Meta, Apple, Amazon, Netflix, Google).  
The data is saved as a timestamped CSV file, so every run creates a clear historical dataset.  
This ensures the analysis always uses the most recent, traceable, and reproducible data.  

*Problem 2 — Data Visualization*  

The system automatically finds the most recent dataset and extracts the closing prices.  
All five stocks 'Closing Prices' retrieved from the most recent csv file are plotted on one clear line chart to make comparison easy.  
The chart is saved with a timestamp, creating a visual of market changes over time. Including the timestamp in the filename makes it easy to track and access historical data.  

*Problem 3 — Automation via Script*  

All steps (download + plot) are bundled into one executable script.  
Running a single command triggers the entire workflow end-to-end, with no manual intervention.  
This turns a multi-step analysis into a repeatable process to ensure consistency and prevent mistakes in repeated runs.  

*Problem 4 — Scheduled Automation (GitHub Actions)*  

The workflow runs the script automatically every Saturday morning.  
It installs th e requirements needed, runs the analysis, saves outputs, and sends results back to the repository.  
This ensures timely data acquisition on specific dates, even at night or on weekends, which accelerates the analysis process and delivers insights faster.  

**In conclusion**, this guide presents a simplified version of of a larger workflow capable of handling large datasets and automating both data collection and visualization, which makes it valuable for any industry that relies on analyzing time-sensitive data.  

## Research and documentation  
The following websites were primarily used to explore resources to complete the problems proposed in Computer Infrastructure module's assessment.  
Additional relevant references are cited and included as comments in sections of Code or Markdown where they apply.  

https://ranaroussi.github.io/yfinance/reference/index.html    
https://ranaroussi.github.io/yfinance/  
https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html  
https://docs.python.org/3/library/datetime.html  
https://stackoverflow.com/questions/39327032/how-to-get-the-latest-file-in-a-folder  
https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.html  
https://matplotlib.org/stable/users/explain/quick_start.html  
https://docs.python.org/3/library/os.html  
https://stackoverflow.com/questions/71396488/saving-figure-by-creating-new-folder  
https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax  
&  
*Computer Infrastructure module's course material*   


## Environment Setup  

| Python in Git     |
|----------|

- Navigate to [github](https://github.com/)
- Click Sign up.
- Follow the prompts to create your personal account.  
***  
- Go to github.
- Log in to your account.
- Click the new repository button in the top-right **'+'** symbol
- Follow [steps](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository)
- Click create repository.  
***
- On GitHub, navigate to the main page of the repository.
- Under the repository name, select the code dropdown menu.
- Click Create codespace on main.
<br /> 

- From menu top left click on View > Explorer   
- Under repository title ( in bold) click on New file   
- Lower case file name, then add .ipynb extension   
- Follows steps from coding to committing then lastly syncing changes.   

For more info  
*[Github official page](https://docs.github.com/en)*

| Python on Windows     |
|----------|

[Download cmder](https://cmder.app/)  
[Download notepad++](https://notepad-plus-plus.org/)  
[Download anaconda (python)](https://www.anaconda.com/download)   
[Download vs code](https://code.visualstudio.com/Download)


    
-   Open VS Code and select "File > New File",  
    Save the file as .py format (e.g., my_script.py).   
    Write a Python script in the file.  

-   With Python file open in VS Code, launch the terminal (see vscode menu)   
    Navigate through the terminal until reaching the same directory where Python file is located.  
    Possible to use Cmder for running Python code for '.py' files. Same as in Vs code, navigate to the directory where the Python file is saved using the cd command.  

-   Cmder is mainly for command-line usage, while VS Code is where would most of coding and debugging run.   
    
-   Lastly, steps to [clone repository using command line](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)   
    Clone allows to copy the repository from GitHub to the local machine   
    Changes can be pushed to the remote repository on GitHub and/or pulled from Github into the local machine.   


## Contact

*Maroua El imame*  
Author and sole contributor  
<G00472980@atu.ie>

