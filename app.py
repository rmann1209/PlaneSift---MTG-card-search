import pandas as pd
import streamlit as st
from main import get_creature_types, read_in_cards

ALL_CARDS, ALL_CREATURES = read_in_cards()

st.header("Magic Card Sorter")
st.subheader("")

keywords_tag = st.text_input("Please insert a comma separated list of keywords to search for", placeholder = r'Destroy, Flying,...')
keywords_tag = [x.lower() for x in keywords_tag.replace(",", "").split(" ")] # Produces a lowercased list of keywords
st.write(keywords_tag)
name_tag = st.text_input("Card Name", placeholder =r'"Pacifism"')
converted_mana_cost_tag  = st.slider('Select a Range for converted mana costs',   0, 16, (0, 5), 1)
supertype_tag = st.multiselect("Choose Card Supertype", ["Basic", "Legendary", "Snow", "World"], ["World"])
rarity_tag = st.multiselect("Choose Card Rarity", ["Common", "Uncommon", "Rare", "Mythic"], ["Rare"])

card_type = st.select_slider("Card Types:", ["Creature", "Noncreature"])
if card_type == "Creature":
    subtypes_tag = st.multiselect("Choose Creature Types", get_creature_types(ALL_CREATURES), ["Human"])
    power_tag  = st.slider('Select a Range for Power',   0, 16, (0, 5), 1)
    toughness_tag  = st.slider('Select a Range for Toughness',   0, 16, (0, 5), 1)
else:
    print('etst')



