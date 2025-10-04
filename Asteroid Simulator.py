import streamlit as st
import folium
from streamlit_folium import st_folium


st.set_page_config(page_title="Asteroid Impact Visualizer", layout="wide", page_icon="☄️")
st.title(" Asteroid Impact Visualizer")
st.write("Simulate and visualize asteroid impacts on Earth using adjustable parameters.")

#  left  controls, right map
col1,col2 = st.columns([1, 1])
with col1:
    st.subheader("Select Impact Location")
    m = folium.Map(location=[20,0],zoom_start=2)
    st_data = st_folium(m, width=450, height=350)

    location=None
    if st_data and st_data.get['last_clicked']:
        location = st_data['last_clicked']
        st.write("Selected Location:",location)

# sliders
with col2:
    st.header("⚙️ Asteroid Parameters")
    asteroid_type = st.selectbox(
        "Asteroid Type",
        ["D-type (Carbon-rich)", "V-type (Vestoids)", "S-type (Stony)", "M-type (Metallic)", 
         "C-type (Carbon)", "Custom"])
    densities = {
        "D-type (Carbon-rich)":1300,
        "V-type(Vestoids)":3500,
        "S-type (Stony)":2700,
        "M-type (Metallic)":7800,
        "C-type (Carbon)":1700}

    if asteroid_type == "Custom":
        density = st.number_input("Enter Custom Density (kg/m³)", min_value=1000, max_value=15000, value=7500)
    else:    
        density = densities[asteroid_type]
     
    diameter = st.slider("Asteroid Diameter (meters)", 10, 20000, 5000)
    velocity = st.slider("Speed (km/s)", 1, 72, 25)
    impact_angle = st.slider("Impact Angle (Degree)", 0, 90, 45)
     #defense
    st.subheader("Defend Earth")
    defend=st.radio("Do you want to defend earth",["Yes","No"])
    if defend=="Yes":
        strategy=st.selectbox("Choose your mitigation strategy",["Kinetic Impactor","Gravity Tractor"])
        
    calculate = st.button("🚀 Calculate Impact")
    
if calculate:
    #front end result impavt result
    st.markdown(---)
    st.header("💥 Impact Results")

    st.write("Calculating results...")

    # 
    st.write(f"Asteroid Type:{asteroid_type}")
    st.write(f"Density:{density}kg/m3")
    st.metric("Kinetic Energy", f"{KE:.2e} J")
    st.metric("Asteroid Mass", f"{mass:.2e}kg")
    st.metric("Crater Diameter", f"{crater_diameter:.2f}km")
    st.metric("TNT Equivalent", f"{TNT:.2e}tons")
    st.metric("Estimated Casualties", casualties)
    st.metric("Crater Depth", "")
    st.metric("Blast Radius", "—")
    st.metric("Tsunami Height", tsunami)
    #evacuation
    st.subheader("EVACUATION AND SAFETY PLAN")
    if casualties=="Millions":
        st.warning('Evacuate all coastal and populated areas within 500km of impact')
        st.write("Move inland or to higher ground")
        st.write("There is going to be after shock waves and atmospheric effects")
    elif casualties=="Thousands":
        st.warning("Evacuate nearest cities within 200km raadius")
        st.write("Move to higher ground")
    else:
        st.success("No major evacuation needed.Minor local impact")
        

    st.success("✅ Simulation complete! You can adjust parameters to explore more impacts.")

    # Restart button
    if st.button("🔁 Simulate Again"):
        st.experimental_rerun()
