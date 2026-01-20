# Creating CSV files
import csv

# Creating a file
data = [
    ["Date", "Product", "Amount", "Units Sold"],
    ["2024-01-01", "Laptop", "1200", "5"],
    ["2024-01-02", "Mouse", "25", "50"],
    ["2024-01-03", "Keyboard", "45", "30"],
    ["2024-01-04", "Monitor", "300", "15"],
    ["2024-01-05", "Headphones", "60", "20"]
]

# Writing to the file
with open('sales_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("sales_data.csv has been created successfully!")

# Import necessary libraries
import csv  # Used to read the text file
from fpdf import FPDF  # Used to create the PDF report

def generate_report():
    print("Starting the task...")

    # --- PART 1: READ AND ANALYZE THE DATA ---
    filename = 'sales_data.csv'
    sales_data = []
    total_sales_amount = 0
    total_units_sold = 0
    
    try:
        # Open the file
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            
            # Read the header row (so we don't try to do math on the word "Amount")
            header = next(reader) 
            
            # Loop through the rest of the rows
            for row in reader:
                sales_data.append(row) # Save the row to use in the PDF table later
                
                # Analysis: Calculate totals
                # row[2] is the Amount column, row[3] is Units column
                amount = float(row[2]) 
                units = int(row[3])
                
                total_sales_amount += amount
                total_units_sold += units

    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
        return

    # Simple Calculation
    number_of_transactions = len(sales_data)
    average_sale = total_sales_amount / number_of_transactions

    print(f"Data analyzed. Total Sales: ${total_sales_amount}")

    # --- PART 2: GENERATE THE PDF REPORT ---
    
    # Initialize the PDF
    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Arial", 'B', 16)
    
    # Add a Title
    pdf.cell(200, 10, "Monthly Sales Report", ln=True, align='C')
    
    # Add a line break
    pdf.ln(10)

    # Add the Analysis Summary
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, f"Total Revenue Generated: ${total_sales_amount}", ln=True)
    pdf.cell(200, 10, f"Total Units Sold: {total_units_sold}", ln=True)
    pdf.cell(200, 10, f"Average Transaction Value: ${average_sale:.2f}", ln=True)
    
    pdf.ln(10) # Add some space before the table

    # --- PART 3: CREATE A DATA TABLE IN PDF ---
    
    # Table Header
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(40, 10, "Date", 1)
    pdf.cell(40, 10, "Product", 1)
    pdf.cell(40, 10, "Amount ($)", 1)
    pdf.cell(40, 10, "Units", 1)
    pdf.ln() # Go to next line

    # Table Rows (Looping through our data again)
    pdf.set_font("Arial", size=12)
    for row in sales_data:
        date = row[0]
        product = row[1]
        amount = row[2]
        units = row[3]
        
        pdf.cell(40, 10, date, 1)
        pdf.cell(40, 10, product, 1)
        pdf.cell(40, 10, amount, 1)
        pdf.cell(40, 10, units, 1)
        pdf.ln()

    # --- PART 4: SAVE THE FILE ---
    output_filename = "Final_Sales_Report.pdf"
    pdf.output(output_filename)
    
    print(f"Success! Report saved as {output_filename}")

# Run the function
if __name__ == "__main__":
    generate_report()