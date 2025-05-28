import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler, LabelEncoder, OneHotEncoder

def load_nsl_kdd(filepath, col_names, drop_last=True):
    """Load NSL-KDD .txt file with optional column header trimming."""
    df = pd.read_csv(filepath, names=col_names)
    if drop_last:
        df = df.iloc[:, :-1]  # drop difficulty level
    return df

def binarize_labels(df, label_column='label'):
    """Convert labels to binary: normal = 0, attack = 1."""
    df[label_column] = df[label_column].apply(lambda x: 0 if x == 'normal' else 1)
    return df

def encode_categorical(df, categorical_cols):
    """One-hot encode categorical features."""
    return pd.get_dummies(df, columns=categorical_cols)

def scale_features(df, label_column='label'):
    """Apply MinMaxScaler to all features except label."""
    scaler = MinMaxScaler()
    features = df.drop(label_column, axis=1)
    labels = df[label_column]
    scaled = scaler.fit_transform(features)
    scaled_df = pd.DataFrame(scaled, columns=features.columns)
    scaled_df[label_column] = labels.values
    return scaled_df

def save_csv(df, output_path):
    """Save DataFrame to CSV."""
    df.to_csv(output_path, index=False)