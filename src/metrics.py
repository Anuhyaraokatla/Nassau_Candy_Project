def calculate_metrics(df):

    # Gross Margin %
    df['Gross Margin %'] = (
        df['Gross Profit'] / df['Sales']
    ) * 100

    # Profit Per Unit
    df['Profit Per Unit'] = (
        df['Gross Profit'] / df['Units']
    )

    # Revenue Contribution
    df['Revenue Contribution %'] = (
        df['Sales'] / df['Sales'].sum()
    ) * 100

    # Profit Contribution
    df['Profit Contribution %'] = (
        df['Gross Profit'] / df['Gross Profit'].sum()
    ) * 100

    return df