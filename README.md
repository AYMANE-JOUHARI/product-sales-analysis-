# **Product Sales Analysis Report**

## **1. Data Validation & Cleaning**
Before performing the analysis, I validated and cleaned the dataset to ensure data quality. Below are the **validation and cleaning steps** for each column:

### **✔ Column-Wise Validation & Cleaning**
| **Column**            | **Validation & Cleaning Steps** |
|-----------------------|--------------------------------|
| **week**             | Checked for missing values (Clean). |
| **sales_method**     | Standardized text format to lowercase. Fixed inconsistencies (e.g., 'em +' replaced with 'email +') (Clean). |
| **customer_id**      | Verified uniqueness of IDs (No duplicates, Clean). |
| **nb_sold**         | Checked for missing values (Clean). |
| **revenue**         | - Identified missing values (more than 5%, so not removed). <br> - Used median imputation (since revenue is left-skewed). |
| **years_as_customer** | - Ensured values do not exceed `(2025-1984 = 41 years)`. <br> - Replaced outliers with the median. |
| **nb_site_visits**  | Checked for missing values (Clean). |
| **state**           | Checked categories for inconsistencies (Clean). |

Outcome: The dataset is now clean and ready for analysis.

---

## **2. Exploratory Data Analysis**
This section answers the key business questions with visuals and insights.

### **2.1 Customer Count per Sales Method**
**How many customers were there for each approach?**  
Findings:  
- Email was the most used method (7,466 customers).  
- Call had 4,962 customers.  
- Email + Call had the fewest (2,572 customers).  

**Visualization:**  
![Customer per Method](customer_per_method.png)

---

### **2.2 Revenue Spread per Sales Method**
**What does the revenue distribution look like overall?**  
Findings:  
- Revenue is left-skewed, meaning some customers generate significantly higher revenue.  
- Email + Call produces the highest median revenue, but with greater variance.  
- Call-only customers tend to generate the lowest revenue per customer.  

**Visualization:**  
![Revenue per Method](Revenue_per_method.png)
![Revenue Distribution per Method](Revenue_distribution_per_method.png)

#### **2.2.1 Revenue Distribution**
**Additional Insights:**
- Revenue is **not normally distributed** and shows multiple peaks.
- A **significant portion of revenue** is concentrated below 150.
- The **Kernel Density Estimation (KDE) curve** suggests different revenue groupings.

**Visualization:**  
![Revenue Distribution](revenue_dist.png)

#### **2.2.2 Revenue Spread Analysis**
**Additional Insights:**
- There are **multiple outliers** above 200.
- Most customers have a revenue range between **50 and 125**.
- The **boxplot confirms the left-skewed nature** of revenue.

**Visualization:**  
![Revenue Spread](revenue_spread.png)

---

### **2.3 Revenue Over Time per Sales Method**
**Was there any difference in revenue over time for each method?**  
Findings:  
- All methods show revenue growth over time.  
- Email + Call had the highest growth rate, maintaining a higher revenue trend.  
- Call-only method had the lowest revenue growth.  

**Visualization:**  
![Revenue per Week](Revenue_per_week.png)

---

### **2.4 Revenue Contribution per Method**
**Which method contributed the most revenue?**  
Findings:  
- Email generated the most total revenue (51.3% of total revenue).  
- Email + Call contributed 31.3% of total revenue.  
- Call-only had the lowest contribution (17.4%).  

**Visualization:**  
![Revenue Contribution](Revenue_contribution_pie.png)

---

## **3. Business Metric to Monitor**
### **Metric: Average Revenue per Customer**
**Formula:**  
Avg Revenue per Customer = Total Revenue / Total Customers


**Initial Value from Data:**
Initial Avg Revenue per Customer: 93.62


### **How to Monitor This Metric?**
- Track weekly and monthly in a dashboard.
- Set up alerts if it drops below X% of the average.
- Compare performance by sales method.

---

## **4. Final Summary & Recommendations**
### **Key Takeaways**
- Email had the most customers but moderate revenue per customer.
- Email + Call had fewer customers but the highest revenue per customer.
- Call-only was the least effective method (low total revenue, low per-customer revenue).
- Revenue is increasing over time, but growth is fastest with Email + Call.

### **Business Recommendation**
1. Prioritize "Email + Call" for high-value customers (as it generates the highest revenue per customer).  
2. Use "Email-only" for mass outreach (to minimize team effort while reaching the most customers).  
3. Reduce reliance on "Call-only" (since it requires high effort but produces low revenue).  

Outcome: This strategy will maximize revenue while optimizing team resources.

---

### **Next Steps**
- Build a real-time dashboard to track average revenue per customer.  
- Re-evaluate sales strategy every 6 weeks.  
- Experiment with personalized email strategies to improve engagement.

---
