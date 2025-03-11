import pandas as pd
import streamlit as st

dataset = pd.read_csv(r'C:\Users\\RAJA\\Downloads\\transaction_data.csv')
st.title("Transaction Data Viewer")
st.dataframe(dataset)


top_customers =dataset["customer_id"].unique()
highest_spenders = dataset[dataset["customer_id"].isin(top_customers)]\
.groupby("customer_id")["amount"].sum().reset_index().sort_values(by="amount", ascending=False)
st.subheader("Highest Spenders per Category")
st.dataframe(highest_spenders)

st.subheader("unique customer id")
st.dataframe(top_customers)

Zero_spender=dataset[dataset["amount"].isna() | (dataset["amount"] == 0)]["customer_id"].unique()
st.subheader("not spend any money")
st.write(Zero_spender)
