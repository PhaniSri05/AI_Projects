from fpdf import FPDF
import csv

# Read data from CSV
data = []
with open('data.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # Convert sales from string like "$1,200.00" to float 1200.0
        sales = float(row['Sales'].replace('$', '').replace(',', ''))
        data.append({'Name': row['Name'], 'Sales': sales})

# Calculate summary stats
total_sales = sum(item['Sales'] for item in data)
average_sales = total_sales / len(data)
highest_sale = max(item['Sales'] for item in data)
top_seller = max(data, key=lambda x: x['Sales'])['Name']

# Create PDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", 'B', 16)

pdf.cell(0, 10, 'Sales Report', ln=True, align='C')
pdf.ln(10)

# Table Header
pdf.set_font("Arial", 'B', 12)
pdf.cell(90, 10, 'Name', border=1)
pdf.cell(90, 10, 'Sales', border=1, ln=True)

# Table rows
pdf.set_font("Arial", '', 12)
for item in data:
    pdf.cell(90, 10, item['Name'], border=1)
    pdf.cell(90, 10, f"${item['Sales']:,.2f}", border=1, ln=True)

pdf.ln(10)

# Summary Section
pdf.set_font("Arial", 'B', 14)
pdf.cell(0, 10, 'Summary', ln=True)

pdf.set_font("Arial", '', 12)
pdf.cell(0, 10, f"Total Sales: ${total_sales:,.2f}", ln=True)
pdf.cell(0, 10, f"Average Sales: ${average_sales:,.2f}", ln=True)
pdf.cell(0, 10, f"Highest Sale: ${highest_sale:,.2f}", ln=True)
pdf.cell(0, 10, f"Top Seller: {top_seller}", ln=True)

# Save PDF
pdf.output("report.pdf")
print("✅ Report generated as 'report.pdf'")
