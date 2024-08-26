import streamlit as st
import requests


API_KEY = st.secrets["api_key"]

def get_gifs(query):
    url = f"https://api.giphy.com/v1/gifs/search?api_key={API_KEY}&q={query}&limit=2"
    response = requests.get(url)
    gifs = response.json()['data']
    return [gif['images']['downsized']['url'] for gif in gifs]

def main():
    st.title('Giphy Search App')

    query = st.text_input('Enter a search term:')
    if query:
        gifs = get_gifs(query)
        for gif in gifs:
            st.image(gif, use_column_width=True)

if __name__ == '__main__':
    main()

# import streamlit as st

# import numpy as np
# import pandas as pd

# st.markdown("""# This is a header
# ## This is a sub header
# This is text""")

# df = pd.DataFrame({
#     'first column': list(range(1, 11)),
#     'second column': np.arange(10, 101, 10)
# })

# # this slider allows the user to select a number of lines
# # to display in the dataframe
# # the selected value is returned by st.slider
# line_count = st.slider('Select a line count', 1, 10, 3)

# # and used to select the displayed lines
# head_df = df.head(line_count)

# head_df

# direction = st.radio('Select a direction', ('top', 'right', 'bottom', 'left'))

# st.write(direction)

# if direction == 'top':
#     st.write('🔼')
# elif direction == 'right':
#     st.write('▶️')
# elif direction == 'bottom':
#     st.write('🔽')
# else:
#     st.write('◀️')

# @st.cache_resource
# def get_line_chart_data():

#     return pd.DataFrame(
#             np.random.randn(20, 3),
#             columns=['a', 'b', 'c']
#         )

# df = get_line_chart_data()

# st.line_chart(df)
