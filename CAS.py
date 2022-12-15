import pandas as pd
import streamlit as st
import numpy as np
import time

st.title('指揮官能力値')

a = [['弓', 'サーセイ', 1489, 3164, 1983, 987, 2649, 5640, 'ジェイミー[武勇:36]、ウーマ[信仰:36]、シオン[幸運:36]、デナ[知恵:36]、夜王[知恵:36]'], ['弓', 'シオン', 1324, 3168, 2642, 1487, 1647, 5979, 'サーセイ[幸運:36]、ソーレン[武勇:30]、サブリナ[幸運:30]'], ['弓', 'ソーレン', 919, 2646, 2313, 766, 1080, 4331, 'シオン[武勇:24]、メリサンドル[知恵:20]、シエラ[計略:16]、ロナール[知恵:16]、マットス[幸運:20]'], ['弓', 'メリサンドル', 1702, 2174, 766, 1389, 1234, 5265, 'ソーレン[知恵:20]、シエラ[計略:16]'], ['弓', 'マットス', 1236, 1855, 924, 1077, 2622, 4168, 'ウーマ[幸運:20]、ソーレン[武勇:20]、クラフリス[幸運:16]'], ['弓', 'ウーマ', 1080, 2790, 922, 607, 2327, 4477, 'サーセイ[信仰:36]、マットス[武勇:20]'], ['槍', 'ジェイミー', 2491, 3505, 1151, 1149, 1987, 7145, 'サーセイ[信仰:36]、オデロ[武勇:36]、ティリオン[信仰:36]、デナ[知恵:36]、夜王[知恵:36]、レイア[武勇:36]'], ['槍', 'ティリオン', 1987, 3334, 1485, 1655, 1808, 6976, 'ジェイミー[信仰:36]、マージェリー[武勇:30]'], ['槍', 'ヴァリス', 783, 2371, 783, 1556, 2346, 4710, 'マージェリー[幸運:20]、アルスラーン[信仰:16]'], ['槍', 'マージェリー', 924, 1543, 2328, 1241, 1233, 3708, 'リアナ[武勇:24]、バレット[幸運:20]、ヴァリス[幸運:20]、ジュリアン[計略:16]、ティリオン[知恵:24]'], ['槍', 'リアナ', 1637, 3126, 1476, 1149, 2461, 5912, 'オデロ[武勇:24]、メランダ[武勇:30]、マージェリー[幸運:30]'], ['槍', 'バレット', 927, 2335, 919, 1382, 2154, 4644, 'サガー[武勇:20]、マージェリー[幸運:20]、アルスラーン[計略:16]'], ['槍', 'アン', 2016, 1387, 1229, 2013, 1075, 5416, 'シモン[信仰:16]'], ['槍', 'レイア', 1328, 2179, 3270, 1772, 1752, 5279, 'パトロ[信仰:36]、オデロ[武勇:36]、ジェイミー[幸運:36]、デナ[幸運:36]'], ['槍', 'オデロ', 926, 2802, 1075, 764, 2159, 4492, 'ジェイミー[信仰:36]、リアナ[武勇:30]、レイア[信仰:36]'], ['槍', 'パトロ', 1720, 2951, 2029, 1244, 2430, 5915, 'ジェイミー[武勇:24]、ティリオン[武勇:30]、オデロ[幸運:30]、レイア[武勇:36]'], ['騎', 'サンサ', 1158, 3164, 2482, 1821, 1321, 6143, 'アリア[武勇:36]、ピーター[計略:36]、ロブ[武勇:30]、カール[知恵:30]'], ['騎', 'ピーター', 2153, 3162, 1981, 1649, 1321, 6964, 'アリア[信仰:36]、サンサ[武勇:36]、サブリナ[知恵:24]'], ['騎', 'アリア', 2319, 3317, 2144, 1481, 1806, 7117, 'ピーター[武勇:36]、サンサ[信仰:36]、ジョン[信仰:36]、デナ[幸運:36]、夜王[幸運:36]'], ['騎', 'カール', 1077, 2646, 1543, 1385, 1073, 5108, 'サンサ[武勇:24]、サブリナ[知恵:20]、ケビン[計略:16]、サルマ[知恵:24]'], ['騎', 'サブリナ', 1233, 2485, 1857, 1229, 920, 4947, 'ピーター[信仰:24]、シオン[武勇:24]、カール[知恵:20]、シナーラ[計略:16]'], ['騎', 'サルマ', 1321, 3159, 2149, 1815, 1817, 6295, 'カール[知恵:30]'], ['騎', 'サラレイ', 2323, 3325, 2151, 1470, 1804, 7118, 'ピーター[武勇:36]、カール[信仰36]、サンサ[武勇:36]、デナ[幸運:36]、夜王[幸運:36]'], ['歩', 'ジョン', 2832, 2828, 1317, 1978, 1317, 7638, 'アリア[武勇:36]、サンダー[信仰:36]、デナ[信仰:36]、夜王[信仰:36]'], ['歩', 'ロブ', 2172, 1857, 766, 1229, 1694, 5258, 'サンダー[信仰:24]、ラッセル[計略:20]、サンサ[信仰:24]、ヘイリー[幸運:16]、サガー[武勇:20]'], ['歩', 'サンダー', 1821, 2675, 1155, 2148, 2149, 6644, 'ジョン[信仰:36]、ロブ[信仰:30]'], ['歩', 'サガー', 1231, 1711, 1233, 1229, 1867, 4171, 'ロブ[信仰:20]、グリア[武勇:16]、バレット[計略:20]'], ['歩', 'ラッセル', 1699, 2020, 922, 1538, 1543, 5257, 'ロブ[計略:20]、ウィック[信仰:20]、オスムンド[武勇:16]、エイロン[幸運:16]'], ['歩', 'ウィック', 2361, 1721, 775, 1401, 771, 5483, 'ラッセル[信仰:20]'], ['歩', 'ボリアン', 2341, 3157, 1317, 1821, 1640, 7319, 'サンダー[武勇:36]、ラッセル[武勇:36]'], ['全', 'デナ', 2814, 3655, 1814, 1314, 1978, 7783, 'ジョン[信仰:36]、アリア[武勇:36]、ジェイミー[幸運:36]、サーセイ[武勇:36]、レイア[武勇36]'], ['全', '夜王', 2781, 3533, 1876, 1708, 2067, 8022, 'ジョン[信仰:36]、アリア[武勇:36]、ジェイミー[幸運:36]、サーセイ[武勇:36]'], ['弓', 'アリサン', 1124, 1838, 841, 984, 1549, 3946, 'ロナール[幸運:8]'], ['弓', 'ラエナ', 1267, 1408, 842, 702, 2119, 3377, 'クラフリス[知恵:8]'], ['弓', 'シエラ', 697, 1981, 1549, 837, 1411, 3515, 'メリサンドル[知恵:10]、ソーレン[武勇:10]、ロナール[幸運:8]、エグ[計略:8]'], ['弓', 'クラフリス', 1126, 1693, 1554, 841, 1121, 3660, 'マットス[武勇:10]、ロナール[幸運:8]、ラエナ[知恵:8]'], ['弓', 'シモン', 1551, 1269, 700, 1551, 1269, 4371, 'アン[信仰:10]'], ['弓', 'エグ', 1121, 1549, 1699, 987, 979, 3657, 'シエラ[武勇:8]'], ['弓', 'ロナール', 981, 1845, 1408, 1121, 984, 3947, 'ソーレン[武勇:10]、シエラ[幸運:8]、アリサン[幸運:8]、クラフリス[計略:8]'], ['槍', 'ファース', 1119, 1838, 1272, 1272, 839, 4229, 'レイモンド[幸運:8]、ジュリアン[武勇:8]、アルスラーン[幸運:8]'], ['槍', 'アルスラーン', 841, 1989, 981, 839, 1696, 3669, 'ヴァリス[幸運:10]、バレット[武勇:10]、ジュリアン[幸運:8]、ファース[計略:8]'], ['槍', 'メランダ', 1554, 1408, 844, 981, 1549, 3943, 'ジュリアン[幸運:16]、リアナ[武勇:24]'], ['槍', 'ジュリアン', 842, 1696, 1554, 1122, 1119, 3660, 'メランダ[武勇:10]、マージェリー[幸運:10]、アルスラーン[計略:8]、ファース[知恵:8]'], ['騎', 'シナーラ', 841, 1986, 1269, 1411, 837, 4238, 'サブリナ[武勇:10]、ケビン[知恵:8]'], ['騎', 'タイボルト', 1699, 1557, 1406, 839, 839, 4095, 'ケビン[武勇:8]、アンドレア[知恵:8]'], ['騎', 'ケビン', 985, 1984, 699, 1261, 1546, 4230, 'カール[武勇:10]、シナーラ[知恵:8]、ジェニィ[知恵:8]、タイボルト[計略:8]'], ['騎', 'アンドレア', 1124, 1841, 981, 981, 1411, 3946, 'ケビン[知恵:8]'], ['騎', 'ジェニィ', 1122, 1267, 1696, 1412, 839, 3801, 'ケビン[知恵:8]'], ['歩', 'オスムンド※', 1366, 1178, 421, 823, 776, 3367, 'ラッセル[信仰:10]、ヘイリー[計略:8]、エイロン[幸運:8]'], ['歩', 'ヘイリー', 1557, 1415, 557, 1686, 1121, 4658, 'ロブ[信仰:10]、オスムンド[計略:8]、グリア[武勇:8]'], ['歩', 'レイモンド', 1409, 1841, 697, 1554, 841, 4804, 'ファース[幸運:8]'], ['歩', 'グリア', 1699, 1699, 839, 981, 1121, 4379, 'ヘイリー[計略:8]、サガー[信仰:10]'], ['歩', 'エイロン', 844, 1404, 985, 1121, 1981, 3369, 'ラッセル[幸運:10]、オスムンド[武勇:8]']]
b = ['兵種', '指揮官', '信仰\nHPバフ', '武勇\n攻撃バフ', '知恵\nクリダメ', '計略\n防御バフ', '幸運\nクリ率',
       '攻防体関係値合計', '絆 指揮官[上昇能力：上昇%]']
df = pd.DataFrame(a)
df = df.set_axis(b, axis='columns')

with st.form("my_form", clear_on_submit=False):
    heisyu = st.selectbox(label='兵種を選択してください', options=['全兵種','歩兵','騎兵','槍兵','弓兵'])
    ST = st.selectbox(label='ソート能力値選択', options=['信仰\nHPバフ','武勇\n攻撃バフ','知恵\nクリダメ','計略\n防御バフ','幸運\nクリ率'])
    submitted = st.form_submit_button("表示")

if submitted:
    with st.spinner("処理中です..."):
        time.sleep(1)
    if heisyu == '歩兵':
        df1 = df.query('兵種 == "歩"')
    elif heisyu == '騎兵':
        df1 = df.query('兵種 == "騎"') 
    elif heisyu == '槍兵':
        df1 = df.query('兵種 == "槍"')
    elif heisyu == '弓兵':
        df1 = df.query('兵種 == "弓"')
    else:
        df1 = df
    df2 = df1.sort_values(ST, ascending=False)
    st.dataframe(df2)
