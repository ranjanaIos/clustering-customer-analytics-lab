# 🧠 Customer Segmentation using E-commerce Behavioral Data

## 📌 Project Overview
This project focuses on **customer segmentation** using real-world **e-commerce clickstream data**.  
By applying **unsupervised machine learning (KMeans clustering)** on customer behavioral features, we identify distinct customer groups and translate them into **actionable business insights**.

The goal is to help businesses improve:
- Personalization
- Marketing targeting
- Customer retention
- Revenue optimization

---

## 🗂 Dataset Description
The dataset contains **e-commerce user interaction events**, including:
- Product views
- Cart actions
- Purchases

Each record represents a user action with attributes such as:
- Event timestamp
- Product and category
- Brand
- Price
- User and session identifiers

📊 Total records: ~1,000,000  
👤 Unit of clustering: **Customer (`user_id`)**

---

## 🧪 Problem Type
- **Unsupervised Learning**
- **Customer Analytics**
- **Clustering**

---

## ⚙️ Tech Stack
- Python
- Pandas, NumPy
- Scikit-learn
- Matplotlib
- SQLite
- VS Code
- GitHub

---

## 🔄 Project Workflow

### 1️⃣ Data Loading
- Connected to SQLite database
- Loaded `ecommerce_behavior` table

### 2️⃣ Data Cleaning
- Converted timestamps to datetime
- Handled missing categorical values
- Removed negligible invalid records

### 3️⃣ Feature Engineering
Created **customer-level features**, including:
- Recency
- Frequency
- Monetary value
- Event behavior ratios
- Product, category, and brand diversity

### 4️⃣ Feature Scaling
- Log transformation for skewed features
- Standard scaling for clustering readiness

### 5️⃣ Clustering
- Applied **KMeans**
- Determined optimal K using:
  - Elbow Method
  - Silhouette Score

### 6️⃣ Cluster Interpretation
- PCA visualization for 2D cluster view
- Behavioral analysis per cluster
- Business recommendations per segment

---

## 📊 Customer Segments (Example)

| Cluster | Segment Name | Key Characteristics |
|------|-------------|--------------------|
| 0 | High-Value Loyal Customers | High spend, frequent purchases |
| 1 | Frequent Browsers | High views, low conversion |
| 2 | Occasional Buyers | Moderate engagement |
| 3 | Inactive Users | Low activity, high recency |

📌 Detailed insights available in  
`reports/business_insights.md`

---

## 💡 Business Impact
This segmentation can help businesses:
- Personalize offers for high-value users
- Retarget hesitant browsers
- Re-engage dormant customers
- Optimize marketing spend

---

## 🚀 Future Improvements
- Try Hierarchical / DBSCAN clustering
- Add time-based cohort analysis
- Integrate the recommendation system
- Add dashboard (Streamlit / Power BI)
- Use LLMs to auto-generate customer insights

---

## 👩‍💻 Author
**Ranjana Patidar**  
AI & ML Enthusiast  

📫 GitHub: https://github.com/ranjanaIos

