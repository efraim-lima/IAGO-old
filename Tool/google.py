from googlesearch import search
import pandas as pd


searching = search("foo")
df = pd.DataFrame(searching)
print(df)

print(searching)