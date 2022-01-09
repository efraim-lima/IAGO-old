from TikTokApi import TikTokApi
from IPython.display import display
import pandas as pd

def color_negative_red(val):
    """
    Takes a scalar and returns a string with
    the css property `'color: red'` for negative
    strings, black otherwise.
    """
    color = 'blue' if val > 90 else 'black'
    return 'color: % s' % color


api = TikTokApi.get_instance()
results = 10

# Since TikTok changed their API you need to use the custom_verifyFp option. 
# In your web browser you will need to go to TikTok, Log in and get the s_v_web_id value.
trending = api.by_trending(count=results, custom_verifyFp="")

for tiktok in trending:
    # Prints the id of the tiktok
    print(tiktok['id'])

dataset = pd.DataFrame(trending)
corr = dataset.corr()
dataset.to_csv('./tiktok_data.csv')
pata = dataset.style
patati = dataset.style.applymap(color_negative_red)
patata = dataset.style.background_gradient(cmap ='viridis')\
        .set_properties(**{'font-size': '20px'})
patatita = corr.style.background_gradient(cmap ='coolwarm')

display(dataset)
print(len(trending))
print(pata)
print(patati)
print(patata)
print(patatita)
