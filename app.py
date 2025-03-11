# # Step 2: Import Libraries and Initialize Pint Unit Registry                  1

# import streamlit as st
# from pint import UnitRegistry

# # Initialize the Pint unit registry
# ureg = UnitRegistry()


# # Step 3: Define Unit Conversion Function

# def convert_units(value, from_unit, to_unit):
#     # Convert the value to the desired unit
#     result = (value * ureg[from_unit]).to(to_unit)
    
#     return result.magnitude


# # Step 4: Create Streamlit App

# # Create a Streamlit app
# st.title("Google Unit Converter")

# # Add input fields for value, from unit, and to unit
# value = st.number_input("Enter value")
# from_unit = st.selectbox("From unit", ["meters", "kilometers", "miles"])
# to_unit = st.selectbox("To unit", ["meters", "kilometers", "miles"])

# # Add a button to trigger the unit conversion
# if st.button("Convert"):
#     # Call the unit conversion function
#     result = convert_units(value, from_unit, to_unit)
    
#     # Display the result
#     st.write(f"{value} {from_unit} is equal to {result} {to_unit}")
# # Step 2: Import Libraries and Initialize Pint Unit Registry                 2

# import streamlit as st
# from pint import UnitRegistry

# # Initialize the Pint unit registry
# ureg = UnitRegistry()


# # Step 3: Define Unit Conversion Function

# def convert_units(value, from_unit, to_unit):
#     # Convert the value to the desired unit
#     result = (value * ureg[from_unit]).to(to_unit)
    
#     return result.magnitude


# # Step 4: Create Streamlit App

# # Create a Streamlit app
# st.title("Google Unit Converter")

# # Add input fields for value, from unit, and to unit
# value = st.number_input("Enter value")
# from_unit = st.selectbox("From unit", ["metre", "kilometre", "mile", "centimetre", "millimetre", "micrometre", "nanometre", "yard", "foot", "inch", "nautical mile"])
# to_unit = st.selectbox("To unit", ["metre", "kilometre", "mile", "centimetre", "millimetre", "micrometre", "nanometre", "yard", "foot", "inch", "nautical mile"])

# # Add a button to trigger the unit conversion
# if st.button("Convert"):
#     # Call the unit conversion function
#     result = convert_units(value, from_unit, to_unit)
    
#     # Display the result
#     st.write(f"{value} {from_unit} is equal to {result} {to_unit}")
# # Import Libraries and Initialize Pint Unit Registry                                    3
# import streamlit as st
# from pint import UnitRegistry

# # Initialize the Pint unit registry
# ureg = UnitRegistry()

# # Define Unit Conversion Function
# def convert_units(value, from_unit, to_unit):
#     # Convert the value to the desired unit
#     result = (value * ureg[from_unit]).to(to_unit)
#     return result.magnitude

# # Create Streamlit App
# # Create a Streamlit app
# st.title("Google Unit Converter")

# # Add a selectbox for unit type
# unit_type = st.selectbox("Select unit type", ["Length", "Mass", "Time"])

# # Define units for each type
# units = {
#     "Length": ["meters", "kilometers", "miles", "centimeters", "millimeters"],
#     "Mass": ["kilograms", "grams", "pounds", "ounces"],
#     "Time": ["seconds", "minutes", "hours", "days"]
# }

# # Add a selectbox for from unit
# from_unit = st.selectbox("From unit", units[unit_type])

# # Add a selectbox for to unit
# to_unit = st.selectbox("To unit", units[unit_type])

# # Add input field for value
# value = st.number_input("Enter value")

# # Add a button to trigger the unit conversion
# if st.button("Convert"):
#     # Call the unit conversion function
#     result = convert_units(value, from_unit, to_unit)
#     # Display the result
#     st.write(f"{value} {from_unit} is equal to {result} {to_unit}")
# import streamlit as st                                  4
# from pint import UnitRegistry

# # Initialize the Pint unit registry
# ureg = UnitRegistry()

# # Define Unit Conversion Function
# def convert_units(value, from_unit, to_unit):
#     # Convert the value to the desired unit
#     result = (value * ureg[from_unit]).to(to_unit)
#     return result.magnitude

# # Create Streamlit App
# # Create a Streamlit app
# st.title("Google Unit Converter")

# # Define units for each type
# units = {
#     "Length": ["metres", "kilometres", "miles", "centimetres", "millimetres"],
#     "Area": ["square kilometre", "square metre", "square mile", "square yard", "square foot", "square inch", "hectare", "acre"],
#     "Data transfer rate": ["bit per second", "kilobit per second", "kilobyte per second", "kibibit per second", "megabit per second", "megabyte per second", "mebibit per second", "gigabit per second", "gigabyte per second", "gibibit per second", "terabit per second", "terabyte per second", "tebibit per second"],
#     "Mass": ["kilograms", "grams", "pounds", "ounces"],
#     "Time": ["seconds", "minutes", "hours", "days"]
# }

# # Add a selectbox for unit type
# unit_type = st.selectbox("Select unit type", list(units.keys()))

# # Add input field for value
# value = st.number_input("Enter value")

# # Add a selectbox for from unit
# from_unit = st.selectbox("From unit", units[unit_type])

# # Add a selectbox for to unit
# to_unit = st.selectbox("To unit", units[unit_type])

# # Add a button to trigger the unit conversion
# if st.button("Convert"):
#     # Call the unit conversion function
#     result = convert_units(value, from_unit, to_unit)
#     # Display the result
#     st.write(f"{value} {from_unit} is equal to {result} {to_unit}")

import streamlit as st
from pint import UnitRegistry

# Initialize the Pint unit registry
ureg = UnitRegistry()

# Function to convert units
def convert_units(value, from_unit, to_unit):
    try:
        result = (value * ureg[from_unit]).to(to_unit)
        return result.magnitude
    except Exception as e:
        return f"Error: {e}"

# Streamlit App UI Styling
st.markdown("""
    <style>
    .main {
        background-color: #F4F6F9; /* Light grayish-blue background */
        color: #333333; /* Dark gray text for better readability */
    }
    .unit-box {
        border: 2px solid #D1D5DB; /* Soft gray border */
        padding: 10px;
        border-radius: 8px;
        background-color: #FFFFFF; /* White background for clarity */
        text-align: center;
        font-size: 18px;
        color: #333333;
        box-shadow: 2px 2px 8px rgba(0, 0, 0, 0.1); /* Light shadow effect */
    }
    .result-box {
       border: 2px solid #1E40AF; /* Professional dark blue border */
        padding: 10px;
        border-radius: 8px;
        background-color: #1E3A8A; /* Darker blue for a corporate look */
        color: white;
        font-weight: bold;
        text-align: center;
        font-size: 20px;
        box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.2);
    }
    .equal-sign {
        font-size: 32px;
        font-weight: bold;
        text-align: center;
        color: #1E40AF; /* Subtle dark blue */
    }
    .row-container {
    display: flex;            /* Enables Flexbox for layout control */
    align-items: center;      /* Vertically centers items in the row */
    justify-content: space-between; /* Spaces elements evenly across the row */
    width: 100%;              /* Ensures the row takes full width */
    }

    </style>
""", unsafe_allow_html=True)

st.title("Unit Converter")

# # Define layout structure
# col1, col2, col3 = st.columns([3, 1, 3])

# Define unit categories
units = {
    "Length": ["metre", "kilometre", "mile", "centimetre", "millimetre", "micrometre", "nanometre", "yard", "foot", "inch", "nautical mile"],
    "Area": ["square kilometre", "square metre", "square mile", "square yard", "square foot", "square inch", "hectare","acre"],
    "Data Transfer Rate": ["bit per second", "kilobit per second", "kilobyte per second", "kibibit per second", "megabit per second", "megabyte per second", "mebibit per second", "gigabit per second", "gigabyte per second", "gibibit per second", "terabit per second", "terabyte per second", "tebibit per second"],
    "Digital Storage": ["bit", "kilobit", "kibibit", "megabit", "mebibit", "gigabit", "gibibit", "terabit", "tebibit", "petabit", "pebibit", "byte", "kilobyte", "kibibyte", "megabyte", "mebibyte", "gigabyte", "gibibyte", "terabyte", "tebibyte", "petabyte", "pebibyte", "byte"],
    "Energy": ["joule", "kilojoule", "gram calorie", "kilocalorie", "watt hour", "kilowatt-hour", "electronvolt", "british thermal unit", "us therm", "foot-pound"],
    "Frequency": ["hertz", "kilohertz", "megahertz", "gigahertz"],
    "Fuel Economy": ["kilometre per litre", "mile per us gallon", " mile per gallon", "litre per 100 kilometres"],
    "Plane Angle": ["arcsecond", "degree", "gradian", "milliradian", "minute of arc", "radian"],
    "Pressure": ["bar", "pascal", "pound per square inch", "standard atmosphere", "torr"],
    "Speed": ["metre per second", " mile per hour", "foot per second", "metre per second", "kilometre per hour", "knot"],
    "temperature": ["degree celsius", "fahrenheit", "kelvin"],
    "Mass": ["tonne", "kilogram", "gram", "milligram", "microgram", "imperial ton", "us ton", "stone", "pound", "ounce"],
    "Time": ["nanosecond", "microsecond", "millisecond", "second", "minute", "hour", "day", "week", "month", "calendar year", "decade", "century"],
    "Volume": ["us liquid gallon", "us liquid quart", "us liquid pint", "us legal cup", "us fluid ounce", "us tablespoon", "us teaspoon", "cubic metre", "litre", "millilitre", "imperial gallon", "imperial quart", "imperial pint", "imperial cup", "imperial fluid ounce", "imperial tablespoon", "imperial teaspoon", "cubic foot", "cubic inch"],
  
}

# Select unit type
unit_type = st.selectbox("Select Unit Category", list(units.keys()))
col1, col2, col3 = st.columns([3, 1, 3])

# Input section (Left Column)
with col1:
    value = st.number_input("Enter Value", min_value=0.0, step=0.1)
    from_unit = st.selectbox("From", units[unit_type])

# Middle Column (Equal Sign)
with col2:
    st.write("")  # Space
    st.write("")

    st.markdown('<p class="equal-sign">=</p>', unsafe_allow_html=True)

# Output section (Right Column)
with col3:
    to_unit = st.selectbox("To", units[unit_type])
# Conversion Button
if st.button("Convert"):
    result = convert_units(value, from_unit, to_unit)
    
    # Display the result with styling
    if isinstance(result, str):  # Error Handling
        st.markdown(f'<div class="unit-box">{result}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="result-box">{value} {from_unit} = {result:.4f} {to_unit}</div>', unsafe_allow_html=True)
