import streamlit as st
import pandas as pd
import json
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as ticker


def main():
    st.title("Trabalho de Python para Análise de Dados")

    st.write("Nome: Gabriel Biancardi Wood")
    st.write("A ideia do presente projeto é observar a relação de preço e área (m²) dos imóveis disponíveis no bairro de Pinheiros da cidade de São Paulo e traçar uma linha de tendência com essas informações")
    st.write("Fonte dos Dados: ZAP Imovéis")


    # Upload JSON file
    uploaded_file = st.file_uploader("Upload JSON File", type=["json"])

    if uploaded_file is not None:
        data = json.load(uploaded_file)
        df = pd.DataFrame(data)

        df["preco"] = df["preco"].astype(int)
        df["area"] = df["area"].astype(int)

        st.subheader("Preview of JSON Data:")
        st.dataframe(df)

        st.subheader("Select Columns for the Graph:")
        x_axis = st.selectbox("X-axis", df.columns, index=2)
        y_axis = st.selectbox("Y-axis", df.columns, index=1)

        st.subheader("Choose the Type of Graph:")
        graph_type = st.selectbox("Graph Type", ["scatter", "line", "bar"])

        plt.figure(figsize=(12, 8)) 

        sns.set(style="darkgrid")  

        ax = plt.gca()

        # ax.get_xaxis().get_major_formatter().set_scientific(False)
        # ax.get_yaxis().get_major_formatter().set_scientific(False)

        if graph_type == "line":
            graph = sns.lineplot(x=x_axis, y=y_axis, data=df)
        elif graph_type == "bar":
            graph = sns.barplot(x=x_axis, y=y_axis, data=df)
        else:
            graph = sns.scatterplot(x=x_axis, y=y_axis, data=df)
            sns.regplot(x=x_axis, y=y_axis, data=df)

        plt.ticklabel_format(style="plain", axis="both")

        st.pyplot(plt.gcf())


if __name__ == "__main__":
    main()
    
