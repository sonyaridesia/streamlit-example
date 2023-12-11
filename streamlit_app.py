import streamlit as st
import pandas as pd
import base64
import io
import plotly.express as px

def main():
    st.title("💗 Data Processing Group Project 💗")
    
    st.markdown(
        """
        <style>
            body {
                background-color: #E0F4FF;
            }
            h1 {
                background-color: #F9F9E0;
                color: #C683D7;
                text-align: center;
                font-size: 48px;
            }
            h4 {
                color: #C683D7;
                text-align: center;
                font-size: 34px;
            }
            ul {
                list-style-type: none;
                padding: 0;
                text-align: center;
            }
            li {
                color: #C683D7;
            }
            .upload-container {
                width: 100%;
                height: 60px;
                line-height: 60px;
                border-width: 1px;
                border-style: dashed;
                border-radius: 5px;
                text-align: center;
                margin: 10px;
                background-color: #F9F9E0;
            }
            .output-container {
                margin-top: 20px;
            }
            .header-section {
                margin-bottom: 20px;
            }
            .preview-section {
                margin-top: 20px;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.write("Nama Anggota:")
    st.write("- Isky Dwi Aprilianto")
    st.write("- Sonya Ridesia Hastari")
    st.write("- Chaesa Namida Arumdapta")
    st.write("- Tarum Widyasti Pertiwi")
    st.write("- Vania Rahma Dewi")

    uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"], key="fileUploader")

    if uploaded_file is not None:
        df = parse_contents(uploaded_file)

        if isinstance(df, pd.DataFrame):
            st.header("🌸 Data Preview 🌸")
            st.write(df)

            st.header("🌼 Deskripsi Dataset 🌼")
            st.code(df.describe().to_json(indent=2))

            st.header("🏵️ Boxplot untuk Deteksi Outlier 🏵️")
            selected_column_boxplot = st.selectbox("Select a column for Boxplot", df.columns)
            st.plotly_chart(update_boxplot(selected_column_boxplot, df))

            st.header("🌻 Histogram 🌻")
            selected_column_histogram = st.selectbox("Select a column for Histogram", df.columns)
            st.plotly_chart(update_histogram(selected_column_histogram, df))

def parse_contents(contents):
    content_type, content_string = contents.type, contents.read()
    decoded = base64.b64decode(content_string)
    
    try:
        if 'csv' in content_type:
            df = pd.read_csv(io.StringIO(decoded.decode('utf-8')))
            return df
    except Exception as e:
        st.error('Error loading CSV file')
        st.write(e)
        return None

def update_boxplot(selected_column, df):
    fig = px.box(df, y=selected_column)
    return fig

def update_histogram(selected_column, df):
    fig = px.histogram(df, x=selected_column)
    return fig

if __name__ == "__main__":
    main()

