import streamlit as st

def check_stability(data):
    result = []

    # Проверки на выходе
    if data['BOD_out'] < 15:
        result.append("✅ БПК₅ на выходе в норме.")
    else:
        result.append("⚠️ БПК₅ на выходе повышен — возможно, перегрузка или сбой биопроцесса.")

    if data['NH4_out'] < 2:
        result.append("✅ Аммоний на выходе в норме.")
    else:
        result.append("⚠️ Повышенный аммоний — нитрификация работает плохо.")

    if data['NO3_out'] < 10:
        result.append("✅ Нитраты на выходе в норме.")
    else:
        result.append("⚠️ Повышенные нитраты — возможен сбой денитрификации.")

    if data['PO4_out'] < 1.5:
        result.append("✅ Фосфор на выходе в норме.")
    else:
        result.append("⚠️ Высокий фосфор — возможен сбой БПР.")

    if data['SVI'] < 150:
        result.append("✅ SVI в норме, ил осаждается хорошо.")
    else:
        result.append("⚠️ Высокий SVI — возможен рост нитчатого ила.")

    if 8 <= data['SRT'] <= 15:
        result.append("✅ Возраст ила в норме.")
    else:
        result.append("⚠️ Возраст ила вне оптимального диапазона.")

    if 2500 <= data['MLSS'] <= 6000:
        result.append("✅ MLSS в норме.")
    elif data['MLSS'] > 9000:
        result.append("⚠️ Очень высокий MLSS — риск всплытия.")
    else:
        result.append("⚠️ Низкий MLSS — недостаточно биомассы.")

    # Новые параметры
    if 6.5 <= data['pH'] <= 8.0:
        result.append("✅ pH в аэротенке в норме.")
    else:
        result.append("⚠️ pH вне нормы — биопроцессы могут нарушаться.")

    if data['TSS_in'] > 400:
        result.append("⚠️ Высокие TSS на входе — возможно, перегрузка.")
    else:
        result.append("✅ Взвешенные на входе в пределах нормы.")

    if data['TSS_out'] < 30:
        result.append("✅ TSS на выходе в норме.")
    else:
        result.append("⚠️ Высокие TSS на выходе — плохое осветление стока.")

    if data['COD_in'] <= 1000:
        result.append("✅ ХПК на входе в пределах нормы.")
    else:
        result.append("⚠️ Очень высокий COD — возможна перегрузка.")

    if data['NH4_in'] < 60:
        result.append("✅ Аммоний на входе в пределах типичной нагрузки.")
    else:
        result.append("⚠️ Повышенный аммоний на входе — может потребоваться больше кислорода.")

    if data['P_in'] < 10:
        result.append("✅ Фосфор на входе в пределах нормы.")
    else:
        result.append("⚠️ Повышенная фосфорная нагрузка.")

    return result

st.title("Проверка стабильности очистных сооружений")

bod_out = st.number_input("БПК₅ на выходе (мг/л):", min_value=0.0, value=18.0)
nh4_out = st.number_input("Аммоний (NH₄⁺) на выходе (мг/л):", min_value=0.0, value=5.0)
no3_out = st.number_input("Нитраты (NO₃⁻) на выходе (мг/л):", min_value=0.0, value=12.0)
po4_out = st.number_input("Фосфаты (PO₄³⁻) на выходе (мг/л):", min_value=0.0, value=2.3)
svi = st.number_input("SVI (мл/г):", min_value=0.0, value=180.0)
srt = st.number_input("Возраст ила (сутки):", min_value=0.0, value=12.0)
mlss = st.number_input("MLSS (мг/л):", min_value=0.0, value=9200.0)

# Новые параметры
pH = st.number_input("pH в аэротенке:", min_value=0.0, max_value=14.0, value=7.2)
TSS_in = st.number_input("TSS на входе (мг/л):", min_value=0.0, value=350.0)
TSS_out = st.number_input("TSS на выходе (мг/л):", min_value=0.0, value=25.0)
COD_in = st.number_input("COD (ХПК) на входе (мг/л):", min_value=0.0, value=600.0)
NH4_in = st.number_input("Аммоний (NH₄⁺) на входе (мг/л):", min_value=0.0, value=50.0)
P_in = st.number_input("Фосфор общий на входе (мг/л):", min_value=0.0, value=8.5)

if st.button("Проверить систему"):
    input_data = {
        'BOD_out': bod_out,
        'NH4_out': nh4_out,
        'NO3_out': no3_out,
        'PO4_out': po4_out,
        'SVI': svi,
        'SRT': srt,
        'MLSS': mlss,
        'pH': pH,
        'TSS_in': TSS_in,
        'TSS_out': TSS_out,
        'COD_in': COD_in,
        'NH4_in': NH4_in,
        'P_in': P_in,
    }
    results = check_stability(input_data)
    st.subheader("Результаты:")
    for line in results:
        st.write(line)
