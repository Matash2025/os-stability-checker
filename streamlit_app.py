import streamlit as st

def check_stability(data):
    result = []

    if data['BOD_out'] < 15:
        result.append("✅ БПК₅ на выходе в норме.")
    else:
        result.append("⚠️ БПК₅ на выходе повышен — возможно, перегрузка или сбой биопроцесса.")

    if data['NH4_out'] < 2:
        result.append("✅ Аммоний удаляется хорошо.")
    else:
        result.append("⚠️ Высокий аммоний — нитрификация работает плохо.")

    if data['NO3_out'] < 10:
        result.append("✅ Денитрификация в норме.")
    else:
        result.append("⚠️ Высокие нитраты — возможен сбой денитрификации.")

    if data['PO4_out'] < 1.5:
        result.append("✅ Фосфор удаляется эффективно.")
    else:
        result.append("⚠️ Фосфор на выходе высокий — сбой в биологическом удалении фосфора.")

    if data['SVI'] < 150:
        result.append("✅ Ил хорошо осаждается.")
    else:
        result.append("⚠️ Высокий SVI — возможен рост нитчатого ила.")

    if 8 <= data['SRT'] <= 15:
        result.append("✅ Иловый возраст оптимальный.")
    else:
        result.append("⚠️ Иловый возраст вне нормы — скорректируйте отвод избыточного ила.")

    if 2500 <= data['MLSS'] <= 6000:
        result.append("✅ Концентрация активного ила в норме.")
    elif data['MLSS'] > 9000:
        result.append("⚠️ Очень высокая концентрация ила — риск всплытия.")
    else:
        result.append("⚠️ Низкий MLSS — возможно, биомассы недостаточно.")

    return result

st.title("Проверка стабильности очистных сооружений")

bod_out = st.number_input("БПК₅ на выходе (мг/л):", min_value=0.0, value=18.0)
nh4_out = st.number_input("Аммоний (NH₄⁺) на выходе (мг/л):", min_value=0.0, value=5.0)
no3_out = st.number_input("Нитраты (NO₃⁻) на выходе (мг/л):", min_value=0.0, value=12.0)
po4_out = st.number_input("Фосфаты (PO₄³⁻) на выходе (мг/л):", min_value=0.0, value=2.3)
svi = st.number_input("SVI (мл/г):", min_value=0.0, value=180.0)
srt = st.number_input("Возраст ила (сутки):", min_value=0.0, value=12.0)
mlss = st.number_input("MLSS (мг/л):", min_value=0.0, value=9200.0)

if st.button("Проверить систему"):
    input_data = {
        'BOD_out': bod_out,
        'NH4_out': nh4_out,
        'NO3_out': no3_out,
        'PO4_out': po4_out,
        'SVI': svi,
        'SRT': srt,
        'MLSS': mlss,
    }
    results = check_stability(input_data)
    st.subheader("Результаты:")
    for line in results:
        st.write(line)
