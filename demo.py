import streamlit as st


name=st.text_input('enter you name:')
fname=st.text_input('father name:')
Aadr=st.text_area('enter you tetxt---')
classdata=st.selectbox('enter you class:',(1,2,3,4,5))

button=st.button('done')
if button :
    st.markdown(f'''
    Name:{name}
    FtherName:{fname}
    addrs:{Aadr}
    CLASS:{classdata}
''')
