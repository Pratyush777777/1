import streamlit as st
import webbrowser
import time

hide_st_style = """
            <style>
            .css-1jc7ptx, .e1ewe7hr3, .viewerBadge_container__1QSob, .styles_viewerBadge__1yB5_, .viewerBadge_link__1S137, .viewerBadge_text__1JaDK, .css-1oe5cao { display: none; } 
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            footer:after {content:''; display:none;}
            header { visibility: hidden; }
            ._profileContainer_1yi6l_53 { display: none; }
            ._profilePreview_1yi6l_63 { display: none; } 
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# Dictionary of artist names with their respective fame scores based on biography length
artist_fame_scores = {
    "Amit Bhar": 2, "Anuradha Thakur": 3, "Basuki Das Gupta": 4, "Bharti Prajapati": 3, "Buwa Shete": 2,
    "F.N. Souza": 4, "Jagannath Paul": 2, "Jamini Roy": 4, "Je Shen": 1, "Kalamkari": 1, "Kandi Narsimlu": 3,
    "Laxma Goud": 3, "Madhuri Bhaduri": 3, "Maqbool Fida Husain": 5, "Mithila Art": 2, "Nishant Dange": 2,
    "Om Swami": 1, "Ramesh Gorjala": 3, "Sandeep Jigdung": 1, "Sayed Haider Raza": 5, "Senaka Senanayake": 3,
    "Seema Kohli": 4, "Siddharth Shingade": 3, "S. Sivabalan": 2, "Sudip Roy": 3, "Sujata Achrekar": 3,
    "Sumanto Chowdhury": 2, "Swati Pasari": 3, "Thota Vaikuntam": 4, "Vinita Karim": 3, "Vivek Kumavat": 2
}

# Function to open the artist URL
def open_artist_page(artist_name):
    base_url = "https://laasyaart.com/"
    artist_url = base_url + artist_name.lower().replace(" ", "-") + "/"
    st.markdown(f"[Click Here to Open Artist Page]({artist_url})")

# Streamlit UI
time.sleep(2.5)
st.title("ArtInnovate Beta")
uploaded_image = st.file_uploader("Upload Your Painting")

# Columns for artist name and creation year
col1, col2 = st.columns(2)
with col1:
    artist_name = st.text_input("Enter Artist Name")
with col2:
    creation_year = st.text_input("Enter Creation Year")



# Prompt for art characteristics
st.markdown("###### If Your Painting Has These Characteristics, Please Enter 1 or 0")
art_styles = ['Modern Art', 'Abstract Art', 'Expressionism', 'Feminist Art', 'Conceptual Art', 'Geometric Art', 'Cubism', 'Environmental Art']
style_values = {style: st.selectbox(style, options=[0, 1]) for style in art_styles}

# Function to calculate the painting price
def calculate_painting_price(fame_score, creation_year, art_styles):
    base_price = 30000.8163  # Ensure base price is a float
    
    # Fame score impact
    fame_impact = fame_score * 10000.2354
    price = base_price + fame_impact
    
    # Creation year impact
    try:
        year = int(creation_year)
        if year < 1800:
            price += 50000.6382  # Fixed increase for older paintings
        else:
            years_since_1800 = year - 1800
            price -= (years_since_1800 // 50) * 5000.9373  # Decrease per 50 years after 1800
    except ValueError:
        st.error("Invalid year entered.")
    
    # Art style impact
    decrease_styles = ['Modern Art', 'Feminist Art', 'Environmental Art']
    increase_styles = ['Abstract Art', 'Expressionism', 'Conceptual Art', 'Geometric Art', 'Cubism']

    # Decrease for specific styles
    for style in decrease_styles:
        if art_styles[style] == 1:
            price -= 5000.9153
    
    # Increase for other styles
    for style in increase_styles:
        if art_styles[style] == 1:
            price += 5000.1637
    
    return price

# Button to trigger the action
if st.button("Calculate Price"):
    if not uploaded_image:
        st.error("Please upload your painting.")
    elif not artist_name:
        st.error("Please enter the artist name.")
    elif not creation_year:
        st.error("Please enter the creation year.")
    else:
        with st.spinner("Calculating... Please wait."):
            time.sleep(10)
        open_artist_page(artist_name)
        
        # Check and assign fame value from the dictionary
        fame = artist_fame_scores.get(artist_name, 0)
        
        # Calculate the final price
        final_price = calculate_painting_price(fame, creation_year, style_values)
        
        # Display final results
        st.write(f"Estimated Price of Painting: ₹{final_price:.2f}")  # Display in INR with decimals
