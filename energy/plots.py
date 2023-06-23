'''
import pandas as pd
import plotly.express as px

df = pd.read_csv('output.csv')
df.info()
fig = px.line(df, x='TIME+', y="%CPU", title='CPU vs time')
fig.show()
'''

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

# read the data from a CSV file
df = pd.read_csv('output.csv')

df.info()


df['%CPU'] = df['%CPU'].str.replace(',', '.')

df['%CPU'] = pd.to_numeric(df['%CPU'])

# create a list of unique processes
processes = df['COMMAND'].unique()

# calculate the average %CPU for each category
means = df.groupby('COMMAND')['%CPU'].mean()

# create a PDF file
pdf_pages = PdfPages('category_plots.pdf')
'''
for process in processes:


    # select the rows for the current process
    subset = df[df['COMMAND'] == process]
    
    # convert the columns to numpy arrays
    x = subset['TIME+'].to_numpy()
    
    y = subset['%CPU'].to_numpy()
  
    
    # create a line plot
    plt.figure()
    plt.plot(y)
    plt.title('CPU usage for process {}'.format(process))
    plt.xlabel('Time')
    plt.ylabel('% CPU')

    pdf_pages.savefig()
 '''   

means.plot(kind='bar')
plt.title('Average %CPU by rosnode')
plt.xlabel('Node')
plt.ylabel('Average %CPU')

pdf_pages.savefig()

# close the PDF file
pdf_pages.close()



# show the plot
plt.show()



