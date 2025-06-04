from RecentPosts.RecentPostsManager import RecentPostsManager


recentPost = RecentPostsManager()

recentPost.add_post(" [Insert = 1] John's sunset photo at Cox's Bazar 🌅")
recentPost.add_post(" [Insert = 2] Sarah checked in at Saint Martin's Island")
recentPost.add_post(
    " [Insert = 3]  Alex just posted a food review at Burger King")
recentPost.add_post(
    " [Insert = 4] Nafis shared a photo from his study desk #BCSPrep")
recentPost.add_post(" [Insert = 5] Arif completed a 20km ride today #fitness")
recentPost.add_post(
    " [Insert = 6] New baby picture uploaded by Mahi and Sara!")
recentPost.add_post(" [Insert = 7] Eid Mubarak from the Rahman family 🌙")
recentPost.add_post(
    " [Insert = 8] Tanvir watched 'The Dark Knight' again! #classic")
recentPost.add_post(" [Insert = 9]  Farzana just landed in Dubai 🇦🇪")
recentPost.add_post(" [Insert = 10] Umran got promoted at Google .")
recentPost.add_post(
    " [Insert = 11] Software Developer Imran2 got promoted  Meta.")


print(recentPost.get_recent_post())
feeds = recentPost.get_recent_post()

for key, value in feeds.items():
    print(f"{key}: {value}")
    # print(f"serial:{i}  Post\n {feed}\n")
