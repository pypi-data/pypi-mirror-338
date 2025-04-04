# #Feature extraction
# feature_store = {}
# for month in tqdm(cv.months[1:], desc="Processing months"):
#     hist_df = cv.get_hist_df(month)
#     if not hist_df.empty:
#         features = fe.extract(hist_df)
#         index, target = cv.get_target_df(month, fe.target_col, fe.drop_cols)
#         for dt in [index, features]:
#             for col in dt.select_dtypes(include=['object']).columns:
#                 dt[col] = dt[col].astype('category')
#         feature_store[month] = (index, features, target)

# for month, (index, features, target) in tqdm(feature_store.items(), desc="Staging data"):
#     month_str = month.strftime("%Y-%m-%d")
#     index.to_parquet(f"{FEATURE_STORE_DIR}/index_{month_str}.parquet")
#     features.to_parquet(f"{FEATURE_STORE_DIR}/features_{month_str}.parquet")
#     with open(f"{FEATURE_STORE_DIR}/target_{month_str}.pkl", "wb") as f:
#         pickle.dump(target, f)