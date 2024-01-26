import streamlit as st 
import pandas as pd




df = pd.read_csv('User_Recommendation.csv')


def main():
    st.write("Welcome to Customer Segmentation Project")
    
    user = st.number_input('Enter user id')
    
    recommend = 'Recommendadtions is not made yet, Click choose user.'
    if st.button('Get Recommended Products.') :
        if user in list(df.User_Id.unique().tolist()) :
            recommend = f'You have 50,000 points to spend , and we have recommended these merchants to spend on : {df[df.User_Id == user]["top_products"].iloc[0]}'
        else:
            recommend = f'We dont have behaviou for entered user , please choose another user'
    st.success(recommend)   
    

if __name__ == '__main__' :
    main()     
            
        
    