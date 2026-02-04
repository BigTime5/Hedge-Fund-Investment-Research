"""
Master Script for Financial Analysis Project
=============================================

This script runs the complete analysis pipeline:
1. Executes financial_analysis.py to generate all data files
2. Verifies all required files were created
3. Provides instructions for running the Jupyter notebook

Usage:
    python run_analysis.py
"""

import os
import sys
import subprocess
from pathlib import Path

def print_header(text):
    """Print a formatted header"""
    print("\n" + "="*80)
    print(f"  {text}")
    print("="*80 + "\n")

def check_data_files():
    """Check if required data files exist"""
    print_header("📁 STEP 1: Checking Data Files")
    
    required_files = [
        'data/Balance_Sheet.xlsx',
        'data/Income_Statement.xlsx'
    ]
    
    missing_files = []
    for file in required_files:
        if os.path.exists(file):
            print(f"✓ Found: {file}")
        else:
            print(f"✗ Missing: {file}")
            missing_files.append(file)
    
    if missing_files:
        print("\n⚠️  ERROR: Missing required data files!")
        print("\nPlease ensure the following files are in the 'data/' directory:")
        for file in missing_files:
            print(f"  - {file}")
        print("\nCreate the 'data/' directory and add your Excel files, then run this script again.")
        return False
    
    print("\n✓ All data files found!")
    return True

def check_python_script():
    """Check if financial_analysis.py exists"""
    print_header("📄 STEP 2: Checking Analysis Script")
    
    if os.path.exists('financial_analysis.py'):
        print("✓ Found: financial_analysis.py")
        
        # Check for the bug in the script
        with open('financial_analysis.py', 'r') as f:
            content = f.read()
            if "income_df = pd.read_excel('data/Balance_Sheet.xlsx')" in content:
                print("\n⚠️  WARNING: Detected potential bug in financial_analysis.py")
                print("   Line 8 loads Balance_Sheet.xlsx for both datasets.")
                print("   It should load Income_Statement.xlsx for income_df.")
                print("\n   Current (line 8):")
                print("   income_df = pd.read_excel('data/Balance_Sheet.xlsx')")
                print("\n   Should be:")
                print("   income_df = pd.read_excel('data/Income_Statement.xlsx')")
                print("\n   Please fix this before proceeding!")
                
                response = input("\n   Continue anyway? (y/n): ").lower()
                if response != 'y':
                    return False
        return True
    else:
        print("✗ Missing: financial_analysis.py")
        print("\nPlease ensure financial_analysis.py is in the current directory.")
        return False

def run_analysis():
    """Run the financial analysis script"""
    print_header("🚀 STEP 3: Running Financial Analysis")
    
    print("Executing financial_analysis.py...\n")
    
    try:
        result = subprocess.run(
            [sys.executable, 'financial_analysis.py'],
            capture_output=True,
            text=True,
            timeout=60
        )
        
        # Print output
        if result.stdout:
            print(result.stdout)
        
        if result.returncode == 0:
            print("\n✓ Analysis completed successfully!")
            return True
        else:
            print("\n✗ Analysis failed with errors:")
            if result.stderr:
                print(result.stderr)
            return False
            
    except subprocess.TimeoutExpired:
        print("\n✗ Analysis timed out (exceeded 60 seconds)")
        return False
    except Exception as e:
        print(f"\n✗ Error running analysis: {str(e)}")
        return False

def verify_output_files():
    """Verify all expected output files were created"""
    print_header("✅ STEP 4: Verifying Output Files")
    
    expected_files = [
        'processed_financial_data.csv',
        'industry_summary.csv',
        'real_est_company_summary.csv',
        'real_est_trend.csv',
        'industry_trend.csv',
        'chart_data.json',
        'summary_stats.json'
    ]
    
    all_present = True
    for file in expected_files:
        if os.path.exists(file):
            size = os.path.getsize(file)
            print(f"✓ {file} ({size:,} bytes)")
        else:
            print(f"✗ {file} - NOT FOUND")
            all_present = False
    
    if all_present:
        print("\n✓ All output files generated successfully!")
        return True
    else:
        print("\n⚠️  Some output files are missing. Check the analysis script for errors.")
        return False

def check_notebook():
    """Check if the Jupyter notebook exists"""
    print_header("📓 STEP 5: Checking Notebook")
    
    if os.path.exists('financial_analysis_notebook.ipynb'):
        print("✓ Found: financial_analysis_notebook.ipynb")
        return True
    else:
        print("✗ Missing: financial_analysis_notebook.ipynb")
        print("\nPlease ensure the notebook file is in the current directory.")
        return False

def print_next_steps():
    """Print instructions for next steps"""
    print_header("🎓 NEXT STEPS")
    
    print("Your analysis is ready! Here's what to do next:\n")
    
    print("1. OPEN THE NOTEBOOK:")
    print("   jupyter notebook financial_analysis_notebook.ipynb")
    print("   OR")
    print("   jupyter lab financial_analysis_notebook.ipynb\n")
    
    print("2. RUN ALL CELLS:")
    print("   In Jupyter: Cell → Run All\n")
    
    print("3. EXPLORE THE INSIGHTS:")
    print("   • Cross-industry comparisons")
    print("   • Real estate deep dive")
    print("   • Statistical correlation analysis")
    print("   • Risk-adjusted returns")
    print("   • Investment recommendations\n")
    
    print("4. EXPORT KEY FINDINGS:")
    print("   • Use Plotly's interactive charts")
    print("   • Save visualizations for presentations")
    print("   • Share insights with your hedge fund manager\n")
    
    print("="*80)
    print("  📊 Happy Analyzing!")
    print("="*80 + "\n")

def create_requirements():
    """Create a requirements.txt file"""
    requirements = """pandas>=1.3.0
numpy>=1.21.0
plotly>=5.0.0
openpyxl>=3.0.0
scipy>=1.7.0
jupyter>=1.0.0
jupyterlab>=3.0.0
"""
    
    with open('requirements.txt', 'w') as f:
        f.write(requirements)
    
    print("✓ Created requirements.txt")

def main():
    """Main execution function"""
    print("\n" + "="*80)
    print("  🎯 FINANCIAL ANALYSIS PROJECT - MASTER EXECUTION SCRIPT")
    print("="*80)
    
    # Create requirements.txt
    create_requirements()
    
    # Step 1: Check data files
    if not check_data_files():
        sys.exit(1)
    
    # Step 2: Check Python script
    if not check_python_script():
        sys.exit(1)
    
    # Step 3: Run analysis
    if not run_analysis():
        print("\n❌ Analysis failed. Please check the errors above and try again.")
        sys.exit(1)
    
    # Step 4: Verify output
    if not verify_output_files():
        print("\n❌ Output verification failed. Some files may be missing.")
        sys.exit(1)
    
    # Step 5: Check notebook
    if not check_notebook():
        print("\n⚠️  Notebook file not found, but analysis data is ready.")
    
    # Print next steps
    print_next_steps()
    
    print("✓ Setup complete! All files are ready.\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Script interrupted by user.")
        sys.exit(1)
    except Exception as e:
        print(f"\n\n❌ Unexpected error: {str(e)}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
