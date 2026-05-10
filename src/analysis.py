def top_products(df):

    top_df = df.groupby(
        'Product Name'
    )[['Sales', 'Gross Profit']].sum()

    top_df = top_df.sort_values(
        by='Gross Profit',
        ascending=False
    ).head(10)

    return top_df


def division_analysis(df):

    division_df = df.groupby(
        'Division'
    )[['Sales', 'Gross Profit']].sum()

    return division_df