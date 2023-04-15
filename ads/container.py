from ads.dao import AdsDao, CategoriesDao, UserDao, LocationDao

ads_dao = AdsDao()
categories_dao = CategoriesDao()
user_dao = UserDao('username')
location_dao = LocationDao()