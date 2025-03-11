import pandas as pd
import streamlit as st

# Page Configuration
st.set_page_config(page_title="Transaction Data Viewer", layout="wide")

# Load Dataset
dataset = pd.read_csv(r'C:\Users\\RAJA\\Downloads\\transaction_data.csv')

# Sidebar - Filters
st.sidebar.header("Filters")
selected_customer = st.sidebar.selectbox("Select Customer ID", ["All"] + list(dataset["customer_id"].unique()))

# Main Title
st.title("📊 Transaction Data Viewer")

# Show Dataset with Selection
st.subheader("📜 Full Transaction Dataset")
if selected_customer == "All":
    st.dataframe(dataset, use_container_width=True)
else:
    st.dataframe(dataset[dataset["customer_id"] == selected_customer], use_container_width=True)

# Compute Highest Spenders
top_customers = dataset["customer_id"].unique()
highest_spenders = (
    dataset[dataset["customer_id"].isin(top_customers)]
    .groupby("customer_id")["amount"]
    .sum()
    .reset_index()
    .sort_values(by="amount", ascending=False)
)

# Display Highest Spenders
st.subheader("💰 Highest Spenders")
st.dataframe(highest_spenders.style.format({"amount": "₹{:.2f}"}), use_container_width=True)

# Unique Customers
st.subheader("🆔 Unique Customer IDs")
st.write(f"Total Unique Customers: {len(top_customers)}")
st.dataframe(pd.DataFrame(top_customers, columns=["Customer ID"]), use_container_width=True)

# Customers Who Didn't Spend
zero_spender = dataset[dataset["amount"].isna() | (dataset["amount"] == 0)]["customer_id"].unique()
st.subheader("🚫 Customers Who Did Not Spend Money")
st.write(f"Total: {len(zero_spender)} customers")
st.dataframe(pd.DataFrame(zero_spender, columns=["Customer ID"]), use_container_width=True)

# Footer
st.markdown("---")
st.markdown("💡 *uilt with Streamlit - By * **SUBHADIP SADHU** *")