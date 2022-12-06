import pandas as pd
import streamlit as st
from utils import get_creature_types, read_in_cards,get_noncreature_types, Card, search
import random

# ! USES ENVIRONMENT "mtgreal"
# * streamlit run app.py
ALL_CARDS, ALL_CREATURES, ALL_NONCREATURES = read_in_cards()
RESULT_LIMIT = 200 # * controls the number of cards to show after searching
# ALL_CREATURES = ALL_CREATURES[:10000]
# ALL_CARDS = ALL_CARDS[:10000]
st.header("Magic Card Sorter")

idx = 0 
n_cols = 5
card_pics = [ALL_CARDS[random.randint(0, len(ALL_CARDS))].url for x in range(n_cols)]
for _ in range(len(card_pics)-1): 
    cols = st.columns(n_cols) 
    for i in range(n_cols):
        if idx < len(card_pics): 
            cols[i].image(card_pics[idx],use_column_width =True)
        idx+=1
    
st.subheader("")


def make_grid(cols,rows):
    grid = [0]*cols

    for i in range(cols):
        with st.container():
            grid[i] = st.columns(rows)
    return grid

sort_type_tag = st.select_slider("Sort Type:", ["Quick", "Merge"])
keywords_tag = st.text_input("Keywords: Please insert a comma separated list of keywords to search for", placeholder = r'Flying, Vigilance, etc...')
keywords_tag = [x.lower() for x in keywords_tag.replace(" ", "").split(",")] # Produces a lowercased list of keywords
# st.write(keywords_tag)
name_tag = st.text_input("Card Name", placeholder =r'"Pacifism"')
converted_mana_cost_tag  = st.slider('Select a Range for converted mana costs',   0, 16, (0, 5), 1)
supertype_tag = st.multiselect("Choose Card Supertype", ["Basic", "Legendary", "Snow", "World"])
rarity_tag = st.multiselect("Choose Card Rarity", ["Common", "Uncommon", "Rare", "Mythic"], ["Rare"])
color_tag = st.multiselect("Choose Card Colors", ["Red", "Green", "Blue", "Black","White", "Colorless"], ["Red"])

card_type = st.select_slider("Card Types:", ["Creature", "Noncreature"])
if card_type == "Creature":
    CARDS_TO_SEARCH = ALL_CREATURES
    subtypes_tag = st.multiselect("Choose Creature Types", get_creature_types(ALL_CREATURES), ["Human"])
    power_tag  = st.slider('Select a Range for Power',   0, 16, (0, 5), 1)
    toughness_tag  = st.slider('Select a Range for Toughness',   0, 16, (0, 5), 1)
else:
    CARDS_TO_SEARCH = ALL_NONCREATURES

idx = 0 
# * Collect search parameters and filter cards
search_parameters = {

    "sort_type_tag": sort_type_tag,
    "keywords_tag": keywords_tag,
    "name_tag": name_tag, #! MAYBE CAST TO STR?
    "converted_mana_cost_tag": converted_mana_cost_tag,
    "supertype_tag": supertype_tag,
    "rarity_tag": rarity_tag,
    "color_tag" : color_tag}

if card_type == "Creature":
    search_parameters["subtypes_tag"] = subtypes_tag
    search_parameters["power_tag"] = power_tag
    search_parameters["toughness_tag"] = toughness_tag


if st.button("Search"):
    FILTERED_CARDS = search(CARDS_TO_SEARCH, search_parameters)
    if FILTERED_CARDS is None or len(FILTERED_CARDS)==0:
        st.write("No cards found! Please broaden your search parameters.")
    else:
        if len(FILTERED_CARDS) > RESULT_LIMIT:
            st.write(f"Results exceed {RESULT_LIMIT} cards... ")
            FILTERED_CARDS = FILTERED_CARDS[:RESULT_LIMIT]
        filtered_card_pics = [FILTERED_CARDS[x].url for x in range(len(FILTERED_CARDS))]
        for _ in range(len(filtered_card_pics)-1): 
            cols = st.columns(n_cols) 
            for i in range(n_cols):
                if idx < len(filtered_card_pics): 
                    cols[i].image(filtered_card_pics[idx],use_column_width =True)
                idx+=1
    