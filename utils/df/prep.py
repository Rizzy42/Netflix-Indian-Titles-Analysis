def checkForNullEntries(in_df):
	return in_df.isnull().any()

def filterIncompleteEntries(in_df, col):
	entries = in_df[in_df[col].isnull()]
	return entries