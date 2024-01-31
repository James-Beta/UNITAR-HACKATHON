# -- Set page config
apptitle = 'Bether Youth'


st.set_page_config(page_title=apptitle, layout="wide", initial_sidebar_state="expanded")

# Title the app
st.title('🏡 BetHER YOUth')
st.subheader('Power in Your Hands')

st.write("BetHER YOUth aims to help transform Women and Youth in Africa by aiding them to discover opportunities in technology and personal development.") 
st.write('')
col1, col2 = st.columns(2)
col1.metric("Population of women (% of total population)", "50.2%", "-1.16%")
col2.metric("Population of youth (% of total population)", "60%")
st.write('')
st.subheader('Why betHER YOUth')
st.write('Connects you to world-class training programs that will equip you with technical skills and transformative knowledge.')
st.write('Helps you connect with individuals with passion for growth.')
st.write("Does in depth research into the programs and trainings so you don't have to.")



