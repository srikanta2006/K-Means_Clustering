# 🎯 K-Means Clustering - Wholesale Customer Segmentation

An interactive Streamlit web application for K-Means clustering analysis on wholesale customer data.

## 📋 Features

### 🔍 Clustering Analysis Page
- Upload and analyze wholesale customer data
- Visualize customer segments in 3 clusters
- View cluster distribution
- Analyze cluster characteristics
- Download cluster data as CSV

### 📈 Elbow Method Page
- Interactive visualization of the Elbow Method
- Shows WCSS (Within-Cluster Sum of Squares) for k=1 to 10
- Identifies optimal number of clusters
- Detailed WCSS values table

### ℹ️ About Page
- Comprehensive K-Means explanation
- Algorithm steps and workflow
- Use cases and applications
- Advantages and limitations
- Dataset information

## 🚀 Quick Start (Local)

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the App
```bash
streamlit run streamlit_app.py
```

App opens at: `http://localhost:8501`

## 🌐 Deploy to Cloud

### Option 1: Streamlit Cloud (Recommended - FREE)
1. Push code to GitHub
2. Visit https://streamlit.io/cloud
3. Click "New app" → Select your repo
4. Done! Get public URL

### Option 2: Docker
```bash
docker build -t kmeans-clustering .
docker run -p 8501:8501 kmeans-clustering
```

### Option 3: Heroku
```bash
heroku create your-app-name
git push heroku main
```

## 📊 Dataset

**Wholesale Customer Dataset**
- 440 customer records
- 6 product categories:
  - Fresh
  - Milk
  - Grocery
  - Frozen
  - Detergents_Paper
  - Delicassen

## 🎯 K-Means Configuration

- **Number of Clusters:** 3 (optimal based on Elbow Method)
- **Initialization:** k-means++ (smart initialization)
- **Max Iterations:** 300
- **Number of Initializations:** 10
- **Random State:** 42 (reproducibility)

## 📁 Files

| File | Purpose |
|------|---------|
| `streamlit_app.py` | Main Streamlit application |
| `app.py` | Original K-Means script |
| `Whole_Sale.csv` | Dataset |
| `requirements.txt` | Python dependencies |
| `.streamlit/config.toml` | Streamlit configuration |
| `README.md` | This file |

## 🔧 Technologies

- **Python 3.8+**
- **Streamlit** - Web framework
- **scikit-learn** - Machine learning
- **pandas** - Data processing
- **matplotlib** - Visualization
- **seaborn** - Statistical plots

## 📈 Algorithm Overview

K-Means clustering works by:

1. **Initialization:** Randomly select k initial centroids
2. **Assignment:** Assign each point to nearest centroid
3. **Update:** Recalculate centroids
4. **Convergence:** Repeat until centroids stabilize

## 💡 Insights from Clustering

The 3 clusters represent different customer segments:

- **Cluster 0:** One customer group profile
- **Cluster 1:** Another distinct segment
- **Cluster 2:** Third unique segment

Each cluster has different average spending patterns across product categories.

## 📊 Elbow Method

The Elbow Method identifies the optimal k by plotting WCSS against cluster count.
The "elbow" point (where the curve bends) indicates the optimal number of clusters.

In this analysis, **k=3 is optimal** because:
- Significant WCSS decrease from k=1 to k=3
- Rate of decrease slows after k=3
- Good balance between model complexity and performance

## 🎓 Learning Resources

- [Streamlit Docs](https://docs.streamlit.io)
- [scikit-learn K-Means](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html)
- [K-Means Tutorial](https://en.wikipedia.org/wiki/K-means_clustering)

## 📝 Usage

1. **Explore Clustering:** View how customers are segmented
2. **Understand Method:** Read about Elbow Method selection
3. **Download Data:** Export cluster assignments for analysis
4. **Make Decisions:** Use insights for business strategies

## 🎉 Features

✅ Interactive web interface
✅ Real-time cluster visualization
✅ Elbow method analysis
✅ Downloadable cluster data
✅ Responsive design
✅ Production-ready

## 🚀 Deployment Status

**READY FOR PRODUCTION**
- All dependencies specified
- Configuration optimized
- Error handling implemented
- Documentation complete

## 📞 Support

For issues or questions:
1. Check Streamlit documentation
2. Review scikit-learn docs
3. Check the About page in the app

## 📄 License

MIT License - Free to use for educational purposes

---

**Built with ❤️ using Streamlit and scikit-learn**
