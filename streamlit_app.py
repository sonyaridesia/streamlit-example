import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def main():
    st.title("Data Processing Group Project")
    st.write("Nama Anggota:")
    st.write("- Isky Dwi Aprilianto-064002200006")
    st.write("- Sonya Ridesia Hastari-064002200007")
    st.write("- Chaesa Namida Arumdapta-064002200008")
    st.write("- Tarum Widyasti Pertiwi-064002200027")
    st.write("- Vania Rahma Dewi-064002200030")

    # Upload CSV file through Streamlit
    uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])

    # Tombol "Process" untuk menampilkan data setelah file diunggah
    if uploaded_file is not None:
        if st.button("Process CSV"):
            # Read CSV file into DataFrame
            df = pd.read_csv(uploaded_file)

            # Display basic information
            st.write("## Basic Information:")
            st.write(f"Number of Rows: {df.shape[0]}")
            st.write(f"Number of Columns: {df.shape[1]}")

            # Display data types and missing values
            st.write("## Data Types and Missing Values:")
            st.write(df.dtypes)
            st.write(df.isnull().sum())

            # Display descriptive statistics
            st.write("## Descriptive Statistics:")
            st.write(df.describe())

            # Display visualizations and other features as before...
            st.write("## Data Preview:")
            st.write(df)

            # Menambahkan fitur menghitung rata-rata
            st.write("## Rata-rata:")
            for column in df.select_dtypes(include='number').columns:
                mean_value = df[column].mean()
                st.write(f"Mean of {column}: {mean_value}")

            # Menambahkan fitur menampilkan histogram
            st.write("## Histogram:")
            for column in df.columns:
                st.subheader(f"Histogram for {column}")
                st.bar_chart(df[column])

            # Menambahkan fitur menampilkan boxplot
            st.write("## Boxplot:")
            for column in df.columns:
                st.subheader(f"Boxplot for {column}")
                st.pyplot(plot_boxplot(df, column))

def plot_boxplot(df, column):
    plt.figure(figsize=(8, 6))
    
    # Periksa apakah kolom berisi data numerik
    if pd.api.types.is_numeric_dtype(df[column]):
        sns.boxplot(x=df[column])
        plt.title(f'Boxplot for {column}')
    else:
        plt.title(f'Cannot create boxplot for non-numeric column: {column}')
    
    return plt

if __name__ == "__main__":
    main()
