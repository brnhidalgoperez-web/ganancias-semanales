# Ganancias semanales (Streamlit)

App web para registrar Efectivo y SINPE por día y ver totales.

## Archivos
- `app.py` — código de la app
- `requirements.txt` — dependencias (solo `streamlit`)

## Cómo correr localmente
```bash
pip install -r requirements.txt
streamlit run app.py
```
Luego abre el enlace que aparece en la terminal (http://localhost:8501).

## Cómo publicarla (gratis) en Streamlit Community Cloud
1. Crea un repo en GitHub y sube `app.py` y `requirements.txt`.
2. Ve a https://share.streamlit.io → “New app” → selecciona tu repo y `app.py`.
3. Listo: tendrás una URL pública (abre en iPhone/Android/PC).

> Nota: El archivo `ganancias.json` se guarda en el servidor de la app. 
En Community Cloud puede reiniciarse si la app se duerme o hay redeploy. 
Para persistencia total, conecta una base de datos (Supabase/Firebase) o Google Sheets.
