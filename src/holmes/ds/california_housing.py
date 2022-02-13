def get_features():
  return {
    'X_features': [
        ('MedInc', 'num', 'median income in block group'),
        ('HouseAge', 'num', 'median house age in block group'),
        ('AveRooms', 'num', 'average number of rooms per household'),
        ('AveBedrms', 'num', 'average number of bedrooms per household'),
        ('Population', 'num', 'block group population'),
        ('AveOccup', 'num', 'average number of household members'),
        ('Latitude', 'num', 'block group latitude'),
        ('Longitude', 'num', 'block group longitude'),
    ],
    'target_feature': ('Value', 'num', 'median house value for California district'),
    'dataset_name': 'California Housing dataset',
    'dataset_desc': 'Predict median house prices in California districts',
  }