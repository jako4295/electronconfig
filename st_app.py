import numpy as np
import electronconfig as ec
import streamlit as st
import re


st.title("Electron Configurations")
ec_obj = ec.ElectronConfig()

col1, col2 = st.columns(2)
with col1:
    element_input = st.selectbox("Select Element", np.arange(1, 119), index=81)
with col2:
    default = 54 if 54 in np.arange(1, int(element_input)) else 0
    remove_input = st.selectbox(
        "Remove Electrons", np.arange(0, int(element_input)), index=default
    )

latex_convert = "".join(
    [
        str(e1) + e2 + "^{" + str(e3) + "}"
        for e1, e2, e3 in ec_obj._split_ec_in_row(int(element_input))
    ]
)
st.markdown("The electron configuration of " + str(element_input) + " is,")
latex_str = "".join(
    [
        str(e1) + e2 + "^{" + str(e3) + "}"
        for e1, e2, e3 in ec_obj._split_ec_in_row(int(element_input))
    ]
)
st.latex(latex_str + ".")

remove_str = ec_obj.remove_electrons(int(element_input), int(remove_input))
rem_to_latex = np.array(  # regex to split string into numbers and letters
    re.findall("\d+|\D+", remove_str) + [" "],
    dtype="object",
).reshape(-1, 4)[:, :3]

remove_latex_str = "".join(
    [str(e1) + e2 + "^{" + str(e3) + "}" for e1, e2, e3 in rem_to_latex]
)
st.markdown(f"After removing {remove_input} electrons, the electron configuration is,")
st.latex(remove_latex_str + ".")

st.markdown("The principle quantum number of outermost projectile electron is then,")
st.latex(f"n_0={ec_obj.n0(int(element_input), int(remove_input))}.")
