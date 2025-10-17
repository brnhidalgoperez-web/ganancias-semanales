import streamlit as st
import json
from pathlib import Path

st.set_page_config(page_title="Ganancias semanales", page_icon="📒", layout="centered")

DATA_FILE = Path("ganancias.json")

def load_data():
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}

def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

data = load_data()

st.title("📒 Ganancias semanales")
st.caption("Registra **Efectivo** y **SINPE** por día, y calcula totales.")

dias = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
col1, col2 = st.columns([2,1])
with col1:
    dia = st.selectbox("📆 Día", dias, index=0)
with col2:
    st.write("")

# Cargar valores existentes del día seleccionado
valores = data.get(dia, {"efectivo": 0, "sinpe": 0})
ef_default = int(valores.get("efectivo", 0) or 0)
sn_default = int(valores.get("sinpe", 0) or 0)

c1, c2 = st.columns(2)
with c1:
    efectivo = st.number_input("💵 Efectivo (₡)", min_value=0, step=100, value=ef_default, key="ef_input")
with c2:
    sinpe = st.number_input("📱 SINPE (₡)", min_value=0, step=100, value=sn_default, key="sn_input")

bcol1, bcol2, bcol3 = st.columns(3)
with bcol1:
    if st.button("💾 Guardar día", use_container_width=True):
        data[dia] = {"efectivo": int(efectivo), "sinpe": int(sinpe)}
        save_data(data)
        st.success(f"Guardado {dia.capitalize()}: Efectivo ₡{efectivo:,} | SINPE ₡{sinpe:,}".replace(",", "."))
with bcol2:
    if st.button("🗑️ Borrar día", use_container_width=True):
        if dia in data:
            data.pop(dia)
            save_data(data)
            st.warning(f"Se borraron los datos de {dia.capitalize()}")
        else:
            st.info("Ese día no tiene datos.")
with bcol3:
    if st.button("❌ Borrar toda la semana", use_container_width=True):
        data.clear()
        save_data(data)
        st.error("Se borraron todos los días.")

st.divider()
st.subheader("📊 Resumen semanal")

def fmt(n): 
    return f"₡{int(n):,}".replace(",", ".")

total_efectivo = sum(int(v.get("efectivo",0) or 0) for v in data.values())
total_sinpe = sum(int(v.get("sinpe",0) or 0) for v in data.values())
total_semana = total_efectivo + total_sinpe

# Tabla
rows = []
orden = ["lunes","martes","miércoles","jueves","viernes","sábado","domingo"]
for d in orden:
    v = data.get(d, {"efectivo":0, "sinpe":0})
    ef = int(v.get("efectivo",0) or 0)
    sn = int(v.get("sinpe",0) or 0)
    rows.append({
        "Día": d.capitalize(),
        "Efectivo (₡)": ef,
        "SINPE (₡)": sn,
        "Total día (₡)": ef + sn
    })

st.table(rows)

m1, m2, m3 = st.columns(3)
with m1:
    st.metric("💵 Total efectivo", fmt(total_efectivo))
with m2:
    st.metric("📱 Total SINPE", fmt(total_sinpe))
with m3:
    st.metric("🧾 Total semana", fmt(total_semana))

st.caption("Nota: En Streamlit Cloud, los archivos pueden reiniciarse cuando la app se duerme o se vuelve a desplegar. Para persistencia 100% garantizada, se puede conectar una base (p. ej., Supabase o Google Sheets).")
