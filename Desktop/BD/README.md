# E-commerce Data Pipeline Project

## Description
This project involves building a complete data pipeline, from data extraction to visualization. The aim is to extract data from diverse sources, transform it, store it in a database, and visualize it to extract meaningful insights.

## Features
- Data extraction from Kaggle
- Data transformation using PySpark
- Data storage in PostgreSQL and DuckDB
- Data visualization using Microsoft Power BI

## Requirements
- Python 3.x
- See `requirements.txt` for dependencies

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Download the large files from the following links:
   - [Clean Data CSV](https://drive.google.com/file/d/1wWYZhAbVm2iOu6-CJO9XCQeEBwqGs3nP/view?usp=sharing)
   - [ShopSpectra Transaction Dataset CSV](https://drive.google.com/file/d/1T1HopzGwvk93GrMw6u6MCqX5mTb2njAl/view?usp=sharing)
   - [Power BI Report PBIX](https://drive.google.com/file/d/1iMrKRIetGCpnjISTEsIJ9Uv5umcuFGiI/view?usp=sharing)
2. Extract the files and place them in the appropriate directories:
   - `data/processed/`
   - `data/raw/`
3. Run the data pipeline:
   ```bash
   python scripts/data_pipeline.py
   ```
4. Load data into PostgreSQL
5. Visualize data in Power BI (connect to SQL database)

## Data Pipeline Steps
### Data Extraction
- Obtained the dataset from Kaggle and extracted it using PySpark.

### Data Transformation
- Performed data cleaning and feature engineering using PySpark.

### Data Loading
- Processed the cleaned data using DuckDB.
- Loaded the data into PostgreSQL using SQLAlchemy.

### Data Visualization
- Connected Power BI with the SQL database.
- Created visualizations to represent key metrics and insights.

## Visualizations on the Dashboard
1. **Top-Selling Products:**
   - Horizontal bar chart showing the count of product IDs for different merchant categories, with categories like Entertainment, Groceries, and Clothing leading the list.
2. **Sales by Product Category:**
   - Vertical bar chart showing the sum of total amounts for different merchant categories, reflecting the revenue contribution from each category.
3. **Sales Trends Over Time:**
   - Line chart tracking the sum of total amounts over the years 2023 to 2024, indicating overall sales performance and fluctuations.
4. **Customer Distribution by Location:**
   - Pie chart showing customer percentage distribution by location, highlighting top cities like New York, Los Angeles, and Chicago.
5. **Slice Based on Location:**
   - Slicer panel listing different cities for filtering data based on location.

## Patterns and Trends
1. **Sales Trends Over Time**
   - **Overall Sales Performance:**
     - Sales in 2023 reached approximately 4.2 billion, while 2024 sales are projected at 4.16 billion, indicating a slight decline of 10.32%.
     - This decline suggests a potential challenge in maintaining growth momentum, which could be due to market saturation, increased competition, or changing customer preferences.

   - **Quarterly/Monthly Trends:**
     - Specific figures like 806.39 million and 910.22 million likely represent sales for specific periods (e.g., quarters or months).
     - The 11.65% and 11.71% changes indicate fluctuations in sales performance over time.
     - These fluctuations could reflect seasonal trends, promotional impacts, or external economic factors.

2. **Customer Segmentation by Age**
   - The dashboard includes customer age groups, but exact ranges are unclear. However, age-based segmentation is a critical factor in understanding purchasing behavior.
     - **Potential Trend:** Younger age groups (e.g., millennials, Gen Z) may dominate online shopping, while older demographics might show slower adoption.

3. **Sales by Product Category**
   - The total sales amount is 2.0 billion, distributed across various merchant categories.
     - **Pattern:** Certain product categories likely drive the majority of sales, while others underperform.

4. **Customer Distribution by Location**
   - **Geographical Trends:**
     - Chicago stands out as the top city, contributing 32,000 customers (34.1%), followed by Houston (30,000, 7.8%), Phoenix (29,000, 7.58%), and San Antonio (25,000, 6.55%).
     - Other cities like Detroit, San Diego, and Philadelphia also show significant customer bases but with smaller shares.
     - **Pattern:** Urban areas with higher population densities tend to have larger customer bases, while smaller cities contribute less to overall sales.

## Potential Business Insights
1. **Declining Sales Growth**
   - The 10.32% decline in sales from 2023 to 2024 highlights a potential issue that needs further investigation. This could be due to factors such as customer churn, reduced marketing effectiveness, or external economic conditions.

2. **High-Performing Regions**
   - Cities like Chicago, Houston, and Phoenix are key markets with large customer bases. These regions likely have strong brand awareness or effective local marketing strategies.

3. **Underperforming Regions**
   - Smaller cities like Oklahoma City and El Paso have relatively low customer contributions. This could indicate untapped potential or barriers to customer acquisition in these areas.

4. **Product Category Optimization**
   - The uneven distribution of sales across product categories suggests that some categories are more popular than others. Identifying these categories can provide insights into customer preferences and market demand.

5. **Customer Age Segmentation**
   - Age-based segmentation reveals differences in purchasing behavior across demographics. Younger customers may prefer trendy or tech-savvy products, while older customers might prioritize reliability and convenience.

6. **Seasonal or Periodic Fluctuations**
   - The 11.65% and 11.71% changes in sales suggest periodic fluctuations. These could be tied to seasonal trends, such as holiday shopping spikes or summer slumps.
