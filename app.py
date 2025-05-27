import streamlit as st
import pandas as pd
import joblib
from geopy.distance import geodesic

# Load trained model & encoder dictionary
model = joblib.load('fraud_detection_model.jb')
encoder = joblib.load('label_encoder.jb')  # encoder adalah dictionary: {'merchant': LabelEncoder, ...}

def haversine(lat1, lon1, lat2, lon2):
    return geodesic((lat1, lon1), (lat2, lon2)).km

# --- Streamlit App Layout ---
st.title("Fraud Detection App")
st.write("Enter the transaction details to predict if it's fraudulent.")

# Input fields untuk memasukkan data transaksi
merchant = st.text_input("Merchant")
category = st.text_input("Category")
amt = st.number_input("Amount", value=0.0)
lat = st.number_input("Latitude", value=0.0)
long = st.number_input("Longitude", value=0.0)
merch_lat = st.number_input("Merchant Latitude", value=0.0)
merch_long = st.number_input("Merchant Longitude", value=0.0)
hour = st.slider("Hour", 0, 23, 12)
day = st.slider("Day", 1, 31, 15)
month = st.slider("Month", 1, 12, 6)
gender = st.selectbox("Gender", ["M", "F"])
cc_num = st.text_input("Credit Card Number")

# Hitung jarak
distance = haversine(lat, long, merch_lat, merch_long)

# Tombol Prediksi
if st.button("Predict"):
    # Pastikan field yang wajib diisi sudah ada nilainya
    if merchant and category and cc_num:
        # Buat DataFrame input
        input_data = pd.DataFrame([[merchant, category, amt, distance, hour, day, month, gender, cc_num]],
                                   columns=['merchant', 'category', 'amt', 'distance', 'hour', 'day', 'month', 'gender', 'cc_num'])
        
        # Kolom kategorikal yang perlu di-encode
        categorical_columns = ['merchant', 'category', 'gender']
        
        # Proses encoding dengan tambahan pembersihan (strip) dan error handling
        for col in categorical_columns:
    val = str(input_data[col].iloc[0]).strip()  # Hapus spasi/tab tersembunyi

    st.write(f"🧪 CLEANED input for '{col}': '{val}'")
    st.write(f"✔️ Known classes: {encoder[col].classes_}")

    if val not in encoder[col].classes_:
        st.warning(f"Value '{val}' in column '{col}' not seen during training. Using fallback value -1.")
        input_data[col] = -1
    else:
        input_data[col] = encoder[col].transform([val])[0]


        # Proses hash untuk Credit Card Number
        input_data['cc_num'] = input_data['cc_num'].apply(lambda x: hash(x) % (10 ** 2))
        
        # Pastikan urutan kolom sesuai dengan data training
        features_order = ['merchant', 'category', 'amt', 'cc_num', 'hour', 'day', 'month', 'gender', 'distance']
        input_data = input_data[features_order]
        
        # Lakukan prediksi
        prediction = model.predict(input_data)[0]
        result = "Fraudulent Transaction" if prediction == 1 else "Legitimate Transaction"
        st.subheader(f"Prediction: {result}")
    else:
        st.warning("Please enter Merchant, Category, and Credit Card Number.")
