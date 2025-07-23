import pandas as pd
import plotly.graph_objects as go
import matplotlib.pyplot as plt

def iqr(series:pd.Series) -> pd.Series:
    q1 = series.quantile(0.25)
    q3 = series.quantile(0.75) 
    iqr = q3 - q1
    lower_lim = q1 - 1.5 * iqr
    upper_lim =  q3 + 1.5 * iqr
    return series.apply(lambda value: (value > lower_lim) and (value < upper_lim))

def rinde_por_columna(df:pd.DataFrame, columna:str, cultivo:str):
    df_grouped = df.groupby('Crop_Year')[['Yield', columna]].sum().reset_index()

    # Crear figura y ejes
    fig, ax1 = plt.subplots(figsize=(10, 6))

    # Gráfico de barras (Pesticide)
    ax1.bar(df_grouped['Crop_Year'], df_grouped[columna], color='lightgreen', label=columna)
    ax1.set_ylabel(columna)
    ax1.set_xlabel('Crop Year')

    # Eje secundario para Yield
    ax2 = ax1.twinx()
    ax2.plot(df_grouped['Crop_Year'], df_grouped['Yield'], color='blue', marker='o', label='Yield')
    ax2.set_ylabel('Yield')

    # Títulos y leyendas
    plt.title(f'Evolución de Yield y {columna} por Crop_Year para {cultivo}')
    ax1.legend(loc='upper left')
    ax2.legend(loc='upper right')

    plt.tight_layout()
    plt.show()

def rinde_por_columna_interactivo(df:pd.DataFrame, columna:str, cultivo:str):
    df_grouped = df.groupby('Crop_Year')[['Yield', columna]].sum().reset_index()

    fig = go.Figure()

    # Agregar barras
    fig.add_trace(go.Bar(x=df_grouped['Crop_Year'], y=df_grouped[columna], name=columna, marker_color='lightgreen'))

    # Agregar línea
    fig.add_trace(go.Scatter(x=df_grouped['Crop_Year'], y=df_grouped['Yield'], name='Yield', mode='lines+markers', marker_color='blue', yaxis="y2"))

    # Configurar ejes
    fig.update_layout(
        title=f"Evolución de Yield y {columna} por Crop Year para {cultivo}",
        xaxis_title="Crop Year",
        yaxis=dict(title=columna),
        yaxis2=dict(title="Yield", overlaying='y', side='right'),
        legend=dict(x=0.01, y=0.99),
        bargap=0.2
    )

    fig.show()
