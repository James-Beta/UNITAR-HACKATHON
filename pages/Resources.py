import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt
st.set_option('deprecation.showPyplotGlobalUse', False)

st.title('Resources')
st.subheader('How can I upskill?')
st.text('We have worked on a collection of resources aimed to create the future tech talent in Africa')
st.text('Here we have compiled a small list of resources to get you started in the three categories of Cybersecurity, Data & AI and Software')

st.subheader('Which field are you interested in?')
tab1, tab2, tab3 = st.tabs([ "Cybersecurity", "Data & AI", "Software"])

with tab1:
   st.header("Cybersecurity")
   st.image("cyber.jpg")
   st.write("Cybersecurity is the practice of protecting internet-connected systems and data from unauthorized access, use, disclosure, disruption, modification, or destruction. In simple terms, it's all about keeping your digital life safe and secure.")
   st.subheader('Why consider a career in cybersecurity today?')
   st.write('The demand for cybersecurity professionals is booming, with a global cybersecurity workforce shortage estimated to reach 3.5 million by 2025.')
   st.write('Cybersecurity professionals are highly sought-after and often command competitive salaries. The median annual wage for information security analysts in the U.S., for instance, is over $103,000.')
   st.write('Cybersecurity professionals play a critical role in protecting individuals, businesses, and governments from cybercrime. By securing critical infrastructure and data, you can directly contribute to building a safer and more secure digital world.')
   st.header("Essential Skills and Knowledge")
   # Text with formatting
   st.write("Maintaining the security of your digital life is crucial in today's world. Let's explore some key skills needed to become a cybersecurity expert:")
   text = "network security, intrusion detection, cryptography, malware analysis, forensics, risk management, incident response, vulnerability assessment"
   # Create the wordcloud object
   wordcloud = WordCloud(width=480, height=480, margin=0).generate(text)
   # Display the generated image:
   plt.imshow(wordcloud, interpolation='bilinear')
   plt.axis("off")
   plt.margins(x=0, y=0)
   st.pyplot(plt.show())
   st.header('Resources')
   st.subheader('Tech4dev')
   st.write('Technology for Social Change and Development Initiative (Tech4Dev) is a non-profit social enterprise established in 2016 that creates access to decent work and opportunities for Africans through digital skills empowerment and advocacy.')
   st.link_button("Go to Tech4dev", "https://tech4dev.com/")

with tab2:
   st.header("Data & AI")
   st.image("AI.jpg")
   st.write("Data and AI: The Powerhouse Drivers of the Modern World Data. Think of it as the digital age's raw material. Every click, purchase, sensor reading, and social media post generates data, creating a vast ocean of information waiting to be explored. But just like oil, raw data isn't directly useful. That's where AI comes in, acting as the refinery, transforming data into actionable insights and powerful tools.")
   st.subheader('Why wouldn't you consider a career in Data & AI?')
   st.write("Data and AI aren't just buzzwords; they're reshaping every aspect of our lives. From tailoring your Netflix recommendations to predicting pandemics, from revolutionizing healthcare to powering self-driving cars, the impact of data and AI is immense and ever-growing.")
   st.write("The need for skilled data and AI professionals is skyrocketing across various industries. From tech giants to startups, everyone's scrambling for talent, leading to exciting job opportunities and excellent career prospects.")
   st.write(" It's a dynamic field constantly evolving with new discoveries and challenges. You'll need problem-solving skills, analytical thinking, and even a touch of creativity to make sense of the data and build impactful AI solutions.")
   st.header("Essential Skills and Knowledge")
   # Text with formatting
   st.write("Let's explore some key skills needed to get into the field of Data & AI")
   text = "Ethics and bias in AI, Computer vision, Statistical modeling, Hypothesis testing, Business intelligence,  Machine learning algorithms, Statistics, Deep learning, Cloud computing, Big data technologies"
   # Create the wordcloud object
   wordcloud = WordCloud(width=480, height=480, margin=0).generate(text)
   # Display the generated image:
   plt.imshow(wordcloud, interpolation='bilinear')
   plt.axis("off")
   plt.margins(x=0, y=0)
   st.pyplot(plt.show())
   st.header('Resources')
   st.subheader('ALX')
   st.write("On our mission to address the global shortage of tech talent, ALX Africa takes centre stage. It serves as the technology training apparatus that provides the techno-fluent leaders of tomorrow with access to the skills and tools they need to succeed in today’s digital world.")
   st.link_button("Go to ALX", "https://www.alxafrica.com/programme/data-science/")

with tab3:
   st.header("Software")
   st.image("software.jpg")
   st.write("Software, the code that runs computers and devices, is the unseen force behind almost everything we do in the digital age. From streaming your favorite show to booking a flight, managing finances to sending messages, software plays a crucial role in our personal and professional lives.")
   st.subheader('Why consider a career in Software today?')
   st.write("The need for skilled software developers is soaring across industries, with estimates suggesting millions of unfilled developer positions globally. This translates to excellent career prospects and job security for those with the right skills.")
   st.write("Software development offers a vast array of specializations, from building mobile apps to creating complex enterprise systems, from developing video games to designing virtual reality experiences. This caters to diverse interests and allows for creative problem-solving and innovation.")
   st.write("Software developers are amongst the highest-paid professionals globally, with median salaries exceeding $100,000 in many countries. Many companies also offer attractive benefits packages and opportunities for professional growth.")
   st.header("Essential Skills and Knowledge")
   # Text with formatting
   st.write("Let's explore some key skills needed to get into the field of Software")
   text = "Programming Languages, Data Structures and Algorithms, Databases, Critical Thinking, Design Patterns, version control systems, Operating Systems "
   # Create the wordcloud object
   wordcloud = WordCloud(width=480, height=480, margin=0).generate(text)
   # Display the generated image:
   plt.imshow(wordcloud, interpolation='bilinear')
   plt.axis("off")
   plt.margins(x=0, y=0)
   st.pyplot(plt.show())
   st.header('Resources')
   st.subheader('ALX Programming & Development')
   st.write("On our mission to address the global shortage of tech talent, ALX Africa takes centre stage. It serves as the technology training apparatus that provides the techno-fluent leaders of tomorrow with access to the skills and tools they need to succeed in today’s digital world.")
   st.link_button("Go to ALX Programming & Development", "https://www.alxafrica.com/programme/front-end-web-development/")
   st.subheader('AltSchool Africa')
   st.write("AltSchool Africa is a digital based learning platform. It was founded in 2021 by Adewale Yusuf, Akintunde Sultan and Opeyemi Awoyemi. Like the name suggests, AltSchool Africa offers a more effective “alternative” to traditional academic institutions, in that it explores and offers practical & functional learning with the aid of modern technology.")
   st.link_button("Go to AltSchool Africa", "https://www.altschoolafrica.com/")
