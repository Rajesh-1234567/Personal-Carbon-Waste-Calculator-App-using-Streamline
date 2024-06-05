import streamlit as st
from PIL import Image

# Define emission factors (example values, replace with accurate data)
EMISSION_FACTORS = {
    "India": {
        "Transportation": 0.14,  # kgCO2/km
        "Electricity": 0.82,  # kgCO2/kWh
        "Diet": 1.25,  # kgCO2/meal
        "Waste": 0.1  # kgCO2/kg
    }
}

# Set wide layout and page name
st.set_page_config(layout="wide", page_title="Personal Carbon Calculator 🌱")

# Streamlit app code
st.title("🌍 Personal Carbon Calculator App ⚠️")

st.markdown("""
Welcome to the Personal Carbon Calculator App! Understanding and reducing your carbon footprint is crucial for combating climate change. 
This tool helps you estimate your carbon emissions based on your daily activities. Make informed choices to reduce your impact on the planet. 🌎
""")

# Load and resize the image
image_path = "/Users/rajeshkumarjena/Desktop/Personal carbon calculator App using Streamlit/Co2.png"
image = Image.open(image_path)
image = image.resize((1400, 400))  # Adjust the width and height as needed
st.image(image)
# User inputs
st.subheader("🏠 Your Country")
country = st.selectbox("Select", ["India"])

col1, col2 = st.columns(2)

with col1:
    st.subheader("🚗 Daily Commute Distance (in km)")
    distance = st.slider("Distance", 0.0, 100.0, key="distance_input")

    st.subheader("💡 Monthly Electricity Consumption (in kWh)")
    electricity = st.slider("Electricity", 0.0, 1000.0, key="electricity_input")

with col2:
    st.subheader("🗑️ Waste Generated Per Week (in kg)")
    waste = st.slider("Waste", 0.0, 100.0, key="waste_input")

    st.subheader("🍽️ Number of Meals Per Day")
    meals = st.number_input("Meals", 0, key="meals_input")

# Normalize inputs
if distance > 0:
    distance = distance * 365  # Convert daily distance to yearly
if electricity > 0:
    electricity = electricity * 12  # Convert monthly electricity to yearly
if meals > 0:
    meals = meals * 365  # Convert daily meals to yearly
if waste > 0:
    waste = waste * 52  # Convert weekly waste to yearly

# Calculate carbon emissions
transportation_emissions = EMISSION_FACTORS[country]["Transportation"] * distance
electricity_emissions = EMISSION_FACTORS[country]["Electricity"] * electricity
diet_emissions = EMISSION_FACTORS[country]["Diet"] * meals
waste_emissions = EMISSION_FACTORS[country]["Waste"] * waste

# Convert emissions to tonnes and round off to 2 decimal points
transportation_emissions = round(transportation_emissions / 1000, 2)
electricity_emissions = round(electricity_emissions / 1000, 2)
diet_emissions = round(diet_emissions / 1000, 2)
waste_emissions = round(waste_emissions / 1000, 2)

# Calculate total emissions
total_emissions = round(
    transportation_emissions + electricity_emissions + diet_emissions + waste_emissions, 2
)

if st.button("🌿 Calculate CO2 Emissions"):

    # Display results
    st.header("📊 Results")

    col3, col4 = st.columns(2)

    with col3:
        st.subheader("🌟 Carbon Emissions by Category")
        st.info(f"🚗 **Transportation**: {transportation_emissions} tonnes CO2 per year")
        st.info(f"💡 **Electricity**: {electricity_emissions} tonnes CO2 per year")
        st.info(f"🍽️ **Diet**: {diet_emissions} tonnes CO2 per year")
        st.info(f"🗑️ **Waste**: {waste_emissions} tonnes CO2 per year")

    with col4:
        st.subheader("🌍 Total Carbon Footprint")
        st.success(f"🌍 **Your total carbon footprint is: {total_emissions} tonnes CO2 per year**")
        st.warning("""
        In 2021, CO2 emissions per capita for India was 1.9 tonnes of CO2 per capita.
        Between 1972 and 2021, CO2 emissions per capita of India grew substantially from 0.39 to 1.9 tonnes of CO2 per capita, rising at an increasing annual rate that reached a maximum of 9.41% in 2021.
        """)

st.markdown("""
## About CO2 Emissions 🌿

Carbon dioxide (CO2) emissions are a significant driver of climate change. Human activities, particularly the burning of fossil fuels for energy and transportation, release large amounts of CO2 into the atmosphere. 

**Key Sources of CO2 Emissions:**
- **Transportation**: Vehicles powered by gasoline and diesel.
- **Electricity**: Power plants burning coal, oil, or natural gas.
- **Diet**: Meat and dairy production have high carbon footprints.
- **Waste**: Decomposing organic waste in landfills releases methane, a potent greenhouse gas.

**Why Reduce CO2 Emissions?**
Reducing CO2 emissions can mitigate climate change, improve air quality, and promote sustainability. By making small changes in our daily lives, such as reducing energy consumption, opting for public transportation, and eating a plant-based diet, we can significantly lower our carbon footprint.

Let's work together to make a positive impact on our planet! 🌍💚
""")
