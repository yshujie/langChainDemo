from feast import FeatureStore


def case1():
    feast_repo_path = "/Users/ysj/Applications/feast/my_feature_repo/feature_repo/"
    store = FeatureStore(repo_path=feast_repo_path)    