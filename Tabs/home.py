"""This modules contains data about home page"""

# Import necessary modules
import streamlit as st

def app():
    """This function create the home page"""
    
    # Add title to the home page
    st.title("Milk Yield Estimation System")

    # Add image to the home page
    st.image("https://media.istockphoto.com/id/1297005217/photo/farmer-pouring-raw-milk-into-container.jpg?s=612x612&w=0&k=20&c=toiruwu04HHkwnLZhpKEjNPqOHI7Kmut5NMGTFSGm4M=")

    # Add brief describtion of your web app
    st.markdown(
    """<p style="font-size:20px;">
            A dairy yield prediction system represents a revolutionary tool in modern agriculture, leveraging advanced technologies to forecast and optimize milk production in dairy farms. This innovative system combines data analytics, artificial intelligence, and sensor technologies to monitor various factors influencing milk production, such as the health and nutrition of dairy cows, environmental conditions, and feeding practices. By analyzing historical data and real-time information, the system can accurately predict future milk yields, allowing farmers to make informed decisions about herd management, resource allocation, and feeding schedules. This not only maximizes milk production efficiency but also improves animal welfare by ensuring that cows receive the proper care and nutrition they need. In an era of sustainability and precision farming, the dairy yield prediction system plays a crucial role in enhancing both the productivity and sustainability of dairy operations.
        </p>
    """, unsafe_allow_html=True)
