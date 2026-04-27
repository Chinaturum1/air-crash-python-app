import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# ── PAGE CONFIG
st.set_page_config(
    page_title="Aircrash Analysis (1908–2024)",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ── LOAD & CLEAN DATA
@st.cache_data
def load_data():
    df = pd.read_csv("aircrahesFullDataUpdated_2024.csv")

    # Fill missing values in object columns
    df["Country/Region"] = df["Country/Region"].fillna("Unknown")
    df["Operator"] = df["Operator"].fillna("Unknown")

    # Strip whitespace
    for col in ["Country/Region", "Aircraft Manufacturer", "Aircraft", "Location", "Operator"]:
        df[col] = df[col].str.strip()

    # Title case
    for col in ["Country/Region", "Aircraft Manufacturer", "Aircraft", "Location", "Operator"]:
        df[col] = df[col].str.title()

    # Replace "'-" with Unknown
    df = df.replace("'-", "Unknown")

    # Derived column
    df["Survivors"] = df["Aboard"] - df["Fatalities (air)"]

    return df

df = load_data()

# ── SIDEBAR 
st.sidebar.title("🛩️ Air Crash Analysis")
st.sidebar.markdown("""
This dashboard explores **aircraft crash data from 1908 to 2024**, 
covering crash frequency, fatalities, operators, aircraft types, 
and survivor proportions.

**Dataset:** 5,035 records | 12 columns  
**Source:** aircrahesFullDataUpdated_2024.csv
""")

st.sidebar.markdown("---")
st.sidebar.markdown("### Dataset Summary")
st.sidebar.write(f"**Total Records:** {len(df):,}")
st.sidebar.write(f"**Years Covered:** {int(df['Year'].min())} – {int(df['Year'].max())}")
st.sidebar.write(f"**Unique Countries:** {df['Country/Region'].nunique()}")
st.sidebar.write(f"**Unique Operators:** {df['Operator'].nunique()}")

# ── PAGE TITLE
st.title("✈️ Aircraft Crash Analysis (1908–2024)")
st.markdown("""
An exploratory data analysis of global aircraft crashes spanning over a century.
Each chart below answers one of seven research questions drawn from the dataset.
""")

# A horizontal line to separate the intro from the charts
st.markdown("---")


# RQ 1 — HOW HAVE AIRCRAFT CRASHES TRENDED OVER THE YEARS?

st.subheader("RQ 1 — How Have Aircraft Crashes Trended Over the Years?")

year_counts = df["Year"].value_counts().sort_index()


fig1, ax1 = plt.subplots(figsize=(12, 5))
ax1.plot(year_counts.index, year_counts.values, color="red", linewidth=2)
ax1.set_xlabel("Year")
ax1.set_ylabel("Number of Crashes")
ax1.set_title("Crash Frequency Across The Years (1908–2024)")
plt.tight_layout()


st.pyplot(fig1)


st.markdown("""
**Insight:** Crash frequency rose sharply through the mid-20th century as commercial 
aviation expanded globally. A peak is visible around the 1950s–1990s, after which 
improved safety regulations, better aircraft engineering, and pilot training standards 
contributed to a steady long-term decline into the 2000s and 2020s.
""")

st.markdown("---")



# RQ 2 — WHICH COUNTRIES RECORDED THE MOST AIRCRAFT CRASHES?

st.subheader("RQ 2 — Which Countries Recorded the Most Aircraft Crashes?")

country_counts = df["Country/Region"].value_counts()
country_counts = country_counts[country_counts.index != "Unknown"].head(10)

fig2, ax2 = plt.subplots(figsize=(10, 5))
ax2.barh(country_counts.index, country_counts.values, color="steelblue")
ax2.set_xlabel("Number of Crashes")
ax2.set_ylabel("Country")
ax2.set_title("Top 10 Countries by Crashes")
ax2.invert_yaxis()
plt.tight_layout()
st.pyplot(fig2)

st.markdown("""
**Insight:** The USA leads significantly in total recorded crashes, 
reflecting its long aviation history and the sheer volume of flights operated 
since the early 1900s. Russia and other countries with large military aviation 
programmes also feature prominently in the top 10.
""")

st.markdown("---")



# RQ 3 — WHICH OPERATORS WERE INVOLVED IN THE MOST CRASHES?

st.subheader("RQ 3 — Which Operators or Airlines Were Involved in the Most Crashes?")

opt_counts = df["Operator"].value_counts()
opt_counts = opt_counts[opt_counts.index != "Unknown"].head(10)

fig3, ax3 = plt.subplots(figsize=(10, 5))
ax3.barh(opt_counts.index, opt_counts.values, color="steelblue")
ax3.set_xlabel("Number of Crashes")
ax3.set_ylabel("Operator")
ax3.set_title("Top 10 Operators by Aircraft Crash Frequency")
ax3.invert_yaxis()
plt.tight_layout()
st.pyplot(fig3)

st.markdown("""
**Insight:** Military operators dominate this list, which is expected given that 
military aviation involves more risk, more flights in adverse conditions, and 
spans the entire history of aviation. Among commercial carriers, the operators 
with the most crashes are generally those that have operated the longest or 
across the most routes.
""")

st.markdown("---")



# RQ 4 — WHICH AIRCRAFT TYPES APPEARED MOST IN CRASH RECORDS?

st.subheader("RQ 4 — Which Aircraft Types Appeared Most in Crash Records?")

aft_counts = df["Aircraft"].value_counts()
aft_counts = aft_counts[aft_counts.index != "Unknown"].head(10)

fig4, ax4 = plt.subplots(figsize=(10, 5))
ax4.barh(aft_counts.index, aft_counts.values, color="steelblue")
ax4.set_xlabel("Number of Crashes")
ax4.set_ylabel("Aircraft")
ax4.set_title("Top 10 Aircrafts by Aircrash Frequency")
ax4.invert_yaxis()
plt.tight_layout()
st.pyplot(fig4)

st.markdown("""
**Insight:** Older aircraft models from the mid-20th century dominate crash records, 
largely because they were produced in high volumes and operated during a period when 
safety standards were still maturing. Higher crash counts for a specific model do not 
necessarily mean the aircraft is unsafe — flight volume and era of operation matter greatly.
""")

st.markdown("---")



# RQ 5 — WHICH MONTHS HISTORICALLY RECORD THE MOST CRASHES?

st.subheader("RQ 5 — Which Months Historically Record the Most Crashes?")

month_counts = df["Month"].value_counts()

fig5, ax5 = plt.subplots(figsize=(10, 5))
ax5.bar(month_counts.index, month_counts.values, color="steelblue")
ax5.set_ylabel("Number of Crashes")
ax5.set_xlabel("Month")
ax5.set_title("Months by Aircraft Crash Frequency")
ax5.invert_xaxis()
plt.tight_layout()
st.pyplot(fig5)

st.markdown("""
**Insight:** Crash frequency varies across months, with certain months showing 
consistently higher numbers. This can be linked to seasonal weather patterns such as 
winter fog, icing conditions, and reduced visibility which increase the likelihood 
of incidents, particularly in the Northern Hemisphere.
""")

st.markdown("---")



# RQ 6 — FATALITIES IN THE AIR VS GROUND VS ABOARD

st.subheader("RQ 6 — What Is the Difference Between Fatalities in the Air, Casualties on the Ground, and Those Aboard?")

fatality_totals = df[["Fatalities (air)", "Ground", "Aboard"]].sum()

fig6, ax6 = plt.subplots(figsize=(8, 5))
ax6.bar(fatality_totals.index, fatality_totals.values, color=["steelblue", "red", "green"])
ax6.set_title("Total Fatalities: Air, Ground and Aboard (1908–2024)")
ax6.set_xlabel("Category")
ax6.set_ylabel("Total Count")
plt.tight_layout()
st.pyplot(fig6)

st.markdown("""
**Insight:** The total aboard figure is expectedly the highest as it represents 
everyone on board regardless of outcome. Fatalities in the air make up the majority 
of deaths, while ground casualties — though smaller — represent innocent lives lost 
on the surface due to crashes into populated areas, a sobering reminder of aviation's 
wider impact on communities.
""")

st.markdown("---")



# RQ 7 — WHAT PROPORTION OF CRASHES HAD ZERO SURVIVORS?

st.subheader("RQ 7 — What Proportion of Crashes Had Zero Survivors?")

survivor_counts = (df["Survivors"] == 0).value_counts()

fig7, ax7 = plt.subplots(figsize=(5, 5))
ax7.pie(
    survivor_counts.values,
    labels=["No Survivors", "Survivors"],
    autopct="%1.1f%%",
    colors=["red", "steelblue"],
    startangle=90
)
ax7.set_title("Proportion of Crashes With and Without Survivors")
plt.tight_layout()
st.pyplot(fig7)

st.markdown("""
**Insight:** A significant proportion of recorded crashes resulted in no survivors at all, 
underlining the historically fatal nature of aviation incidents. However, the share of 
crashes with at least one survivor shows that improved emergency response, aircraft 
design, and safety procedures have given passengers a better chance of survival 
in non-fatal incidents over time.
""")

st.markdown("---")


# CCONCLUSION AND RECOMMENDATION
st.subheader("Conclusion and Recommendation")

st.markdown("""
Looking at the data, it's clear that aviation safety has come a long way over the years. 
The decline in crash fatalities from 1908 to 2024 suggests that better aviation technology, 
stricter regulations, and improved operational standards have made air travel much safer than 
it used to be. That said, there is still work to be done.
""")

st.markdown("""
A few things could help push safety even further. Aircraft should be maintained and inspected 
regularly to catch mechanical issues before they become problems. More investment in aviation 
technology and safety systems would also go a long way. Weather is another factor worth paying 
attention to — it wasn't captured in this dataset, but it's very likely that it played a role 
in a number of these crashes. Operators should also be held to consistent safety standards through 
regular checks and accountability measures.
""")

st.markdown("""
Overall, the progress in aviation safety over the past century is impressive. 
Keeping that momentum going through continued investment in technology, regulation, 
and training is what will make flying even safer in the years ahead.
""")


st.markdown("---")



# ── FOOTER 
st.markdown("""
<div style='text-align: center; color: grey; font-size: 13px;'>
    Aircrash Analysis Dashboard · Built with Streamlit · Okonkwo Uchechukwu Faith
</div>
""", unsafe_allow_html=True)
