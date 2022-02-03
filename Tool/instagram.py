from igramscraper.instagram import Instagram 

proxies = {
    'http': 'http://123.45.67.8:1087',
    'https': 'http://123.45.67.8:1087',
}
instagram = Instagram()

instagram.with_credentials('iago.develop', 'pasteldefrango')
instagram.login()

# instagram.set_proxies(proxies)
account = instagram.get_account('jadepicon')
full_name = account.full_name
bio = account.biography
posts = account.media_count
followers = account.followed_by_count

print(f'''
      Name:
      {full_name}
      
      Bio:
      {bio}
      
      Posts:
      {posts}
      
      Followers:
      {followers}
      
      
      
      ''')