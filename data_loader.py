import pandas as pd

def load_data(filepath, target_column=None):
    
    # Charger le fichier
    if filepath.endswith('.csv'):
        df = pd.read_csv(filepath)
    elif filepath.endswith('.xlsx') or filepath.endswith('.xls'):
        df = pd.read_excel(filepath)
    else:
        raise ValueError("Format non supporté. Utilisez CSV ou Excel.")
    
    print(f"Dataset chargé : {df.shape[0]} lignes, {df.shape[1]} colonnes")
    print(f"Colonnes : {list(df.columns)}\n")
    
    # Demander la colonne target que l'on souhaite (le y)
    if target_column is None:
        target_column = input("Quel est le nom de la colonne target ? ")
    
    # Vérifier que la colonne existe dans le dataset
    if target_column not in df.columns:
        raise ValueError(f"Colonne '{target_column}' non trouvée dans le dataset")
    
    # Séparer x et y
    X = df.drop(target_column, axis=1)
    y = df[target_column]
    
    print(f"Features : {X.shape[1]} colonnes")
    print(f"Target : {y.name} (classes : {sorted(y.unique())})\n")
    
    return X, y

if __name__ == "__main__":
    X, y = load_data('bienetre.csv', target_column='target')
    print("X shape:", X.shape)
    print("y shape:", y.shape)