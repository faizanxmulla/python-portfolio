import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    return patients[patients['conditions'].str.contains(r'\bDIAB1', na=False)]



# alternate solutions: 

#  1. return patients[patients.conditions.apply(lambda x: any(c[:5] == 'DIAB1' for c in x.split(' ')))]
#  2. return patients.loc[patients.conditions.str.contains(r'\bDIAB1')]

# NOTE: The \b in the pattern is a word boundary assertion that ensures 'DIAB1' is a separate word and not part of another word.