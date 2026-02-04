import pandas as pd

def preprocess_ecommerce_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean and preprocess ecommerce behavior data
    """

    # Convert event_time to datetime
    df['event_time'] = pd.to_datetime(df['event_time'])

    # Handle missing categorical values
    df['brand'] = df['brand'].fillna('Unknown')
    df['category_code'] = df['category_code'].fillna('Unknown')

    # Drop rows with missing user_session (very few)
    df = df.dropna(subset=['user_session'])

    return df
