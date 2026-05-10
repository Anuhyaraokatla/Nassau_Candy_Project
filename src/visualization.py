import plotly.express as px


def profit_chart(top_df):

    fig = px.bar(
        top_df,
        x=top_df.index,
        y='Gross Profit',
        title='Top Profitable Products'
    )

    return fig


def division_chart(division_df):

    fig = px.pie(
        division_df,
        names=division_df.index,
        values='Gross Profit',
        title='Division Profit Distribution'
    )

    return fig