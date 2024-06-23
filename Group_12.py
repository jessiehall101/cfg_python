import csv
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Function to read data from sales.csv file
def read_data():
    # Initialise an empty list to store data
    data = []
    # Open the CSV file and read data row by row
    with open('sales.csv', 'r') as sales_csv:
        # Use DictReader to parse the CSV file
        spreadsheet = csv.DictReader(sales_csv)
        # Iterate over each row and append it to the data list
        for row in spreadsheet:
            data.append(row)
    return data


# Function to write total sales summary to a CSV file
def write_summary(total_sales):
    # Open a new CSV file for writing the summary
    with open('sales_summary.csv', 'w', newline='') as summary_csv:
        # Define the fieldnames for the CSV writer
        fieldnames = ['Total Sales']
        # Create a CSV writer object
        writer = csv.DictWriter(summary_csv, fieldnames=fieldnames)
        # Write the header row
        writer.writeheader()
        # Write the total sales data
        writer.writerow({'Total Sales': total_sales})


# Main function to run the analysis
def run():
    # Read data from the CSV file
    data = read_data()

    # Initialise lists to store sales and month data
    sales = []
    months = []

    # Iterate over each row in the data and extract sales and month information
    for row in data:
        sale = int(row['sales'])  # Extract sales information and convert it to integer
        month = row['month']  # Extract month information
        sales.append(sale)  # Append sales to the sales list
        months.append(month)  # Append month to the months list

    # Calculate total sales and average sales
    total = sum(sales)  # Calculate total sales by using sum
    average = total / len(sales)  # Calculate average sales by diving total by number of sales
    print('Total sales:', total)  # Print total sales
    print('Average sales:', round(average, 2))  # Print average sales and round to 2 decimal places

    # Write the total sales summary to a CSV file
    write_summary(total)


    # Sort the data based on sales values to find lowest and highest sales
    sorted_rows = sorted(data, key=lambda row: int(row['sales']))  # Sort data by sales in ascending order
    lowest_entry = sorted_rows[0]  # Get the lowest sales entry
    lowest_month = lowest_entry['month']  # Extract month with lowest sales
    lowest_sales = lowest_entry['sales']  # Extract lowest sales
    print('Lowest month sales in {}: {}'.format(lowest_month, lowest_sales))  # Print lowest sales month and value

    sorted_rows = sorted(data, key=lambda row: int(row['sales']),
                         reverse=True)  # Sort data by sales in descending order
    highest_entry = sorted_rows[0]  # Get the highest sales entry
    highest_month = highest_entry['month']  # Extract month with highest sales
    highest_sales = highest_entry['sales']  # Extract highest sales
    print('highest month sales in {}: {}'.format(highest_month, highest_sales))  # Print highest sales month and value

    # Identify the month with the highest and lowest sales
    # max_value = max(sales)  # Working out the highest sales number
    # print('The highest sales number is', max_value)
    # print([sales.index(max(sales))]) # Working out the index of the highest sales number
    # print(months[6]) # Printing the index so we can see what it is
    max_sales_month = months[6]  # Matching the index to the month with that index and inputting into a variable
    print("Month with the highest sales:",
          max_sales_month)  # Printing the variable - printing the month with the highest number of sales

    # min_value = min(sales) # Doing the sale all again but with the min value
    # print('The lowest sales number is', min_value)
    # print([sales.index(min(sales))])
    # print(months[1])
    min_sales_month = months[1]
    print("Month with the lowest sales:", min_sales_month)

    # Print monthly changes in sales as percentage
    print("Monthly changes in sales as percentage:")  # Print heading for section
    for i in range(1, len(months)):  # Iterate over each month
        prev_month_sales = sales[i - 1]  # Get sales of previous month
        current_month_sales = sales[i]  # Get sales of current month
        percentage_change = ((current_month_sales - prev_month_sales) / prev_month_sales) * 100  # Calculate percentage change
        print("Change from", months[i - 1], "to", months[i], ":", round(percentage_change, 2),
              "%")  # Print percentage change for each month and round to 2 decimal places

    # Write monthly percentage changes to a CSV file
    header = ['monthly change', 'percentage']  # Define header for CSV file
    data = [['from jan to feb', -75.57], ['from feb to mar', 21.10],
            ['from mar to apr', 11.35], ['from apr to may', -15.75],
            ['from may to jun', 23.73], ['from jun to jul', 249.81],
            ['from jul to aug', -40.71], ['from aug to sep', -18.47],
            ['from sep to oct', 51.37], ['from oct to nov', 32.02],
            ['from nov to dec', -74.92]]  # Define data for CSV file
    data = pd.DataFrame(data, columns=header)  # Create a DataFrame
    data.to_csv('monthly percentage changes.csv', index=False)  # Write DataFrame to CSV file

    # Use Pandas to calculate maximum, minimum, average, and total sales
    df = pd.read_csv('sales.csv')
    max_sales = df['sales'].max()  # Calculate maximum sales
    min_sales = df['sales'].min()  # Calculate minimum sales
    average_sales = df['sales'].mean()  # Calculate average sales
    total_sales = df['sales'].sum()  # Calculate total sales
    print("lowest sales:", min_sales)  # Print minimum sales
    print("highest sales:", max_sales)  # Print maximum sales
    print("average sales:", round(average_sales, 2))  # Print average sales and round to 2 decimal places
    print("total sales:", total_sales)  # Print total sales

    # Visualise data using seaborn

    # Bar plot of total sales by month
    sns.barplot(pd.read_csv('sales.csv'), x="month", y="sales", color='purple')  # Create a bar plot
    plt.title("Bar Plot of Total Sales by Month")  # Set title for the plot
    plt.xlabel("Month")  # Set label for x-axis
    plt.ylabel("Total Sales ($)")  # Set label for y-axis
    plt.show()  # Display the plot

    # Bar plot of total expenditure by month
    sns.barplot(pd.read_csv('sales.csv'), x="month", y="expenditure", color='pink')  # Create a bar plot
    plt.title("Bar Plot of Total Expenditure by Month")  # Set title for the plot
    plt.xlabel("Month")  # Set label for x-axis
    plt.ylabel("Total Expenditure ($)")  # Set label for y-axis
    plt.show()  # Display the plot

    # PairGrid plot of sales and expenditure by month
    g = sns.PairGrid(pd.read_csv('sales.csv'), y_vars=['month'],
                     x_vars=["sales", "expenditure"])  # Create PairGrid plot
    g.map(sns.barplot)  # Map seaborn barplot to the PairGrid
    plt.show()  # Display the plot



    # Scatter plot of monthly percentage changes
    sns.scatterplot(pd.read_csv('monthly percentage changes.csv'), x="monthly change", y="percentage",
                    color='pink')  # Create a scatter plot
    plt.title("Monthly Percentage Changes")  # Set title for the plot
    plt.xlabel("Monthly Change")  # Set label for x-axis
    plt.ylabel("Percentage Changes in Sales")  # Set label for y-axis
    plt.show()  # Display the plot

    # Line plot of monthly percentage changes in sales
    sns.lineplot(pd.read_csv('monthly percentage changes.csv'), x="monthly change", y="percentage", color='green')
    plt.title("Line Plot of Monthly Percentage Changes in Sales")
    plt.xlabel("Monthly change")
    plt.ylabel("Percentage changes in sales (%)")
    plt.xticks(rotation=20)
    plt.show()


run()  # Call the main function to run the analysis