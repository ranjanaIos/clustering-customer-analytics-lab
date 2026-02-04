import pandas as pd

def create_customer_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create customer-level features from ecommerce event data
    """

    # Reference date for recency calculation
    max_date = df['event_time'].max()

    # Aggregate features at user level
    customer_df = df.groupby('user_id').agg(

        # Recency
        last_event_time=('event_time', 'max'),

        # Frequency
        frequency=('event_type', 'count'),

        # Monetary
        monetary=('price', 'sum'),

        # Event counts
        view_count=('event_type', lambda x: (x == 'view').sum()),
        cart_count=('event_type', lambda x: (x == 'cart').sum()),
        purchase_count=('event_type', lambda x: (x == 'purchase').sum()),

        # Diversity
        unique_products=('product_id', 'nunique'),
        unique_categories=('category_id', 'nunique'),
        unique_brands=('brand', 'nunique')

    ).reset_index()

    # Recency in days
    customer_df['recency_days'] = (
        max_date - customer_df['last_event_time']
    ).dt.days

    # Ratios (avoid division by zero)
    customer_df['purchase_ratio'] = (
        customer_df['purchase_count'] / customer_df['frequency']
    )

    customer_df['cart_to_purchase_ratio'] = customer_df['purchase_count'] / (
        customer_df['cart_count'] + 1
    )

    # Drop raw datetime column
    customer_df = customer_df.drop(columns=['last_event_time'])

    return customer_df
