import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import joblib


st.set_page_config(
    page_title="Car",
    page_icon="🏎"
)

tab1, tab2, tab3, tab4, tab5= st.tabs(["ALL MODELS", "SUPER CAR", "SPORT CAR", "Calculate","Sci-kit" ])
st.sidebar.title('Preview SUPER CAR & SPORT CAR')
Car = st.sidebar.button('ChevroletCorvetteZ06')

if Car:
    with st.sidebar:
        st.video("https://youtu.be/ztgWQmPH5r0")

Car2 = st.sidebar.button('Audi R8 Coupe V10 GT RWD')

if Car2:
    with st.sidebar:
        st.video("https://youtu.be/njTAITHZRxA")

Car3 = st.sidebar.button('Porsche 911 Carrera S 2022')

if Car3:
    with st.sidebar:
        st.video("https://youtu.be/O5c93RDGLn8")

Car4 = st.sidebar.button('BMW 8 Series 2023')

if Car4:
    with st.sidebar:
        st.video("https://youtu.be/vXIa5E0Ev8M")

Car5 = st.sidebar.button('2022 Lexus LC')

if Car5:
    with st.sidebar:
        st.video("https://youtu.be/RjC5O47DP3I")

Car6 = st.sidebar.button('Ferrari 296 GTB')

if Car6:
    with st.sidebar:
        st.video("https://youtu.be/7ezD7jJOVWw")

Car7 = st.sidebar.button('Porsche 911 GT3 RS')

if Car7:
    with st.sidebar:
        st.video("https://youtu.be/478Ay_lNpT4")

Car8 = st.sidebar.button('Lamborghini Huracan Tecnica')

if Car8:
    with st.sidebar:
        st.video("https://youtu.be/bStQfHFODKs")

Car9 = st.sidebar.button('McLaren Artura')

if Car9:
    with st.sidebar:
        st.video("https://youtu.be/gZGOz6sir40")

Car10 = st.sidebar.button('Maserati MC20')

if Car10:
    with st.sidebar:
        st.video("https://youtu.be/RjC5O47DP3I")
st.markdown(
    f"""
       <style>
       .stApp {{
           background-image: url("https://img.freepik.com/free-vector/abstract-black-texture-background-hexagon_206725-413.jpg");
           background-attachment: fixed;
           background-size: cover;
           /* opacity: 0.3; */
       }}
       </style>
       """,
    unsafe_allow_html=True
)

with tab1:
   st.header("SUPER CAR & SPORT CAR ภาษีนำเข้ากี่บาท?")
   st.subheader("Chevrolet Corvette Z06")
   st.image("https://www.cars.com/i/large/in/v2/stock_photos/5fc28f44-ec02-4496-9995-4d613dad127e/dc2b6933-41f7-44e3-b159-98542892c9f1.png", width=300)
   if st.button('ดูข้อมูลเพิ่มเติม'):
       st.write('***-เครื่องยนต์ V8 ขนาด 5.5 ลิตร แบบไร้ระบบอัดอากาศ***')
       st.write('***-ล้อหน้าขนาด 20x10 นิ้ว ที่รัดด้วยยางขนาด 275/30ZR20 เเละล้อหลังขนาด 21x13 นิ้ว ที่รัดด้วยยางขนาด 345/25ZR21 ซึ่งยางตามมาตรฐานนั้นจะใช้ยางจาก Michelin Pilot Sport***')
       st.write('***-ด้านระบบเบรกจะมาพร้อมจานเบรกที่ด้านหน้าขนาด 370 มม. พร้อมคาลิปเปอร์ 6 พอทและด้านหลังจะใช้จานเบรกขนาด 380 มม. พร้อมคาลิปเปอร์ 4 พอท***')
       st.write('***-ราคา THB 2,800,000***')

with tab1:
   st.subheader("Audi R8 Coupe V10 GT RWD")
   st.image("https://mediaservice.audi.com/media/fast/H4sIAAAAAAAAAFvzloG1tIiBOTrayfuvpGh6-m1zJgaGigIGBgZGoDhTtNOaz-I_2DhCHkCFGe8ysJSnJhUwAlW4MXFl5iamp-qDBPgZuYssdFMrSnTzUnPz2YHSfDxx82OvGmYdv7P9odeX-UEuL9jvPBNn4JG80c5idmnvwdZ5rgwT-Nb8-CLL6sPA80Ljz3ynLG9X55KNxmkmK6rP_I85ysDDa3x7zo9_LDP1Pj_UUr3v_Yxjg5s2A8-MJyEt65yrn0119Z3L518bciD7fCcDTxCz1fvu0JJWKYF9l_j8Dz1mmz9zIgNPBuPMFeeOTFT5uu3h5VpjA8cN328C3eBSWnq15cu9uD38u77f-HyweolJyCYGnrYY8XKRUnPBmOJb6e_al5lxiDFnMPDsrVD8zRJnIXDzyYnLnX9PyqZftxAE-mLb95P758kv3-XpdrKVa2rDfnGW7Qw8r6fW-q0pU3kZI7RXxsLVqtQuOnM3Aw_DA72seu0VTJP1jL5sV1p2aXfI8ucMPJ1X3V-mBMfM5JHmyfJ4N3leDNPScwyswIBl2g0kWOKABM8TIMFhwwAmQUG-AUgwLgTxWeuZGRi4HRgY2EIYQIBPuLQopyCxKDFXryi1uCA_rzizLFVQw4BIIMzq4xjpGgQAa47rIxACAAA?mimetype=image/png", width=300)
   if st.button('ดูข้อมูลเพิ่มเติม  '):
       st.write('***-เครื่องยนต์ V10 ขนาด 5.2 ลิตร ที่ให้กำลัง 620 แรงม้าและแรงบิด 565 นิวตันเมตร ส่งกำลังผ่านเกียร์อัตโนมัติคลัทซ์คู่ 7 จังหวะ***')
       st.write('***-ล้ออัลลอยแบบ Forged น้ำหนักเบาขนาด 20 นิ้วจึงทำให้น้ำหนักลงอีก 20 กก. ทำให้มีน้ำหนักรวมที่ 1,570 กก.***')
       st.write('***-ระบบเบรกด้านหน้า Discs ระบบเบรกด้านหลัง Discs***')
       st.write('***-ราคา THB 19,000,000***')

with tab1:
   st.subheader("Porsche 911 Carrera S 2022")
   st.image("https://carsguide-res.cloudinary.com/image/upload/f_auto,fl_lossy,q_auto,t_cg_hero_low/v1/editorial/vhs/porsche-911-2021.png", width=300)
   if st.button('ดูข้อมูลเพิ่มเติม   '):
       st.write('***-เครื่องยนต์เบนซิน 6 สูบนอน Boxer ขนาด 3.0 ลิตร 2,981 ซีซี Twin Turbo กระบอกสูบ x ระยะช่วงชัก : 91.0 x 76.4 มิลลิเมตร พละกำลังสูงสุด 450 แรงม้า ที่ 6,500 รอบ/นาที แรงบิดสูงสุด 530 นิวตันเมตร***')
       st.write('***-ล้ออัลลอย คู่หน้า ขนาด 20 นิ้ว พร้อมยาง 245/35 ZR20 ล้ออัลลอย คู่หลัง ขนาด 21 นิ้ว พร้อมยาง 305/30 ZR21***')
       st.write('***-ระบบเบรก ให้ความมั่นใจ หยุด 450 แรงม้าได้นิ่ง และนุ่มนวล Porsche 911 Carrera S มีการเปลี่ยนระบบเสริมแรงเบรกจากหม้อลม***')
       st.write('***-ราคา THB 12,810,000***')

with tab1:
   st.subheader("BMW 8 Series 2023")
   st.image("https://img.sm360.ca/ir/w640h390c/images/newcar/ca/2023/bmw/serie-8-gran-coupe/m850i-xdrive/coupe/exteriorColors/13971_cc0640_032_a96.png", width=300)
   if st.button('ดูข้อมูลเพิ่มเติม     '):
       st.write('***-เครื่องยนต์ V8 ขนาด 4.4 ลิตร เทอร์โบคู่ ให้กำลัง 617 แรงม้า และแรงบิด 749 นิวตันเมตร ส่งกำลังด้วยเกียร์อัตโนมัติ 8 สปีดและระบบขับเคลื่อน 4 ล้อ***')
       st.write('***-ขนาดยางหน้า Front:245/35 R20 Rear: 275/30 R20 ประเภทยางรถยนต์ Radial***')
       st.write('***-ระบบเบรกด้านหน้า-หลัง Discs***')
       st.write('***-ราคา THB 2,800,000***')

with tab1:
   st.subheader("2022 Lexus LC")
   st.image("https://images.dealer.com/ddc/vehicles/2022/Lexus/LC%20500/Coupe/perspective/front-left/2022_24.png", width=300)
   if st.button('ดูข้อมูลเพิ่มเติม      '):
       st.write('***-เครื่องยนต์ V8 ขนาด 4.4 ลิตร เทอร์โบคู่ ให้กำลัง 617 แรงม้า และแรงบิด 749 นิวตันเมตร ส่งกำลังด้วยเกียร์อัตโนมัติ 8 สปีดและระบบขับเคลื่อน 4 ล้อ***')
       st.write('***-ขนาดยางหน้า Front:245/35 R20 Rear: 275/30 R20 ประเภทยางรถยนต์ Radial***')
       st.write('***-ระบบเบรกด้านหน้า-หลัง Discs***')
       st.write('***-ราคา THB 2,800,000***')

with tab1:
   st.subheader("Ferrari 296 GTB ")
   st.image("https://media-server1.modenamotorsgmbh.com/40970-large_default/ferrari-296-gtb.jpg", width=300)
   if st.button('ดูข้อมูลเพิ่มเติม       '):
       st.write('***-เครื่องยนต์ V6 ทำมุม 120 องศา ขนาด 663 แรงม้า(เครื่องอย่างเดียว) มอเตอร์ไฟฟ้า กำลัง 122 กิโลวัตต์ (167 แรงม้า)***')
       st.write('***-ล้ออัลลอยดีไซน์ใหม่ขนาด 20 นิ้ว มีตัวเลือกล้อฟอร์จ และล้อคาร์บอนไฟเบอร์เบอร์ที่เบาลงไปอีก 8 กก.***')
       st.write('***-ระบบเบรกใช้จานคาร์บอน-เซรามิค ดึงมาจาก SF90 ด้านหน้า 398 มม. หลัง 360 มม.***')
       st.write('***-ราคา THB 21,900,000***')

with tab1:
   st.subheader("Porsche 911 GT3 RS")
   st.image("https://www.pngplay.com/wp-content/uploads/13/Porsche-911-GT3-RS-Free-PNG.png", width=300)
   if st.button('ดูข้อมูลเพิ่มเติม        '):
       st.write('***-เครื่องยนต์เบนซินแบบ 6 สูบ Boxer ขนาด 4.0 ลิตร ไร้ระบบอัดอากาศ ให้กำลังสูงสุด 525 แรงม้า (PS) จับคู่กับเกียร์อัตโนมัติ PDK 7 จังหวะ***')
       st.write('***-ล้ออัลลอย Forged น้ำหนักเบา คู่หน้าขนาด 20 นิ้ว คู่หลังขนาด 21 นิ้ว พร้อมดุมล้อแบบชิ้นเดียวเหมือนรถแข่ง***')
       st.write('***-ระบบเบรกด้านหน้าใช้แบบ 6 ลูกสูบ ด้านหลังแบบ 4 ลูกสูบ พร้อมจานเบรกทำจากวัสดุเซรามิคคอมโพสิท เพื่อลดน้ำหนักของระบบเบรกโดยรวมเป็นออปชั่นเสริม***')
       st.write('***-ราคา THB 7,942,662***')

with tab1:
   st.subheader("Lamborghini Huracan Tecnica")
   st.image("https://www.lamborghini.com/sites/it-en/files/DAM/lamborghini/facelift_2019/connectivity/huracan/model_chooser/huracan_Tecnica_m.png", width=300)
   if st.button('ดูข้อมูลเพิ่มเติม         '):
       st.write('***-เครื่องยนต์ 5,204 cc., 640 แรงม้า(HP)***')
       st.write('***-ล้ออัลลอยลาย Damiso แบบ Diamond cut กว้าง 8.5 นิ้ว รัดด้วยยาง Bridgestone Potenza Sport ขนาด 245/30 R20 ที่ล้อคู่หน้า และขนาด 305/30 R20 ที่ล้อคู่หลัง***')
       st.write('***-ระบบเบรกเป็นดิสก์เบรกทั้ง 4 ล้อ จานเบรกคู่หน้าเป็นแบบมีครีบและรูระบายความร้อนทำจากคาร์บอนเซเรมิค ขนาด 380 มิลลิเมตร จับคู่กับคาลิปเปอร์ 6 พอต***')
       st.write('***-ราคา THB 22,980,000***')

with tab1:
   st.subheader("McLaren Artura")
   st.image("https://static.tcimg.net/vehicles/primary/e34ad3b5a048d413/2023-McLaren-Artura-white-full_color-driver_side_front_quarter.png", width=300)
   if st.button('ดูข้อมูลเพิ่มเติม          '):
       st.write('***-ครื่องยนต์เบนซินวางกลางลำ รหัส M630 แบบ V6 ขนาด 2,993 ซีซี. เทอร์โบคู่ กำลังสูงสุด 585 แรงม้า ที่ 7,500 รอบ/นาที แรงบิดสูงสุด 585 นิวตันเมตร ที่ 2,250 – 7,000 รอบ/นาที จับคู่กับเกียร์อัตโนมัติ SSG 8 จังหวะ***')
       st.write('***-ล้ออัลลอยลาย 7 ก้าน ขอบหน้า 19 นิ้ว หลัง 20 นิ้ว มาเป็นมาตรฐาน สวมกับยาง Pirelli P Zero ที่มีระบบ Pirelli Cyber Tyre ฝังเซนเซอร์ไว้ที่ยาง***')
       st.write('***-เบรกด้านหลังมีขนาด 380 มิลลิเมตร มาพร้อมกับคาลิปเปอร์ขนาด 4 สูบ***')
       st.write('***-ราคา THB 20,500,000***')

with tab1:
   st.subheader("Maserati MC20")
   st.image("https://maserati.scene7.com/is/image/maserati/maserati/international/Models/my23/mc20-cielo/picker/MC20-cielo-picker.png?$1400x2000$&fmt=png-alpha&fit=constrain", width=300)
   if st.button('ดูข้อมูลเพิ่มเติม                                          '):
       st.write('***-เครื่องยนต์เบนซิน เทอร์โบ วี 6 สูบ ขนาด 3.0 ลิตร กำลังสูงสุด 630 แรงม้า มาพร้อมระบบเครื่องยนต์เทคโนโลยีแบบเดียวกับรถแข่งสูตร 1 หรือ F1 ถูกนำมาใช้กับรถสปอร์ทระดับซูเพอร์คาร์ครั้งแรก***')
       st.write('***-ล้อแมกขนาด 20 นิ้ว***')
       st.write('***-ระบบเบรกด้านหน้า-หลัง Ventilated Disc***')
       st.write('***-ราคา THB 21,500,000***')

with tab3:
   st.subheader("Chevrolet Corvette Z06")
   st.image("https://www.cars.com/i/large/in/v2/stock_photos/5fc28f44-ec02-4496-9995-4d613dad127e/dc2b6933-41f7-44e3-b159-98542892c9f1.png", width=300)
   if st.button('ดูข้อมูลเพิ่มเติม            '):
       st.write('***-เครื่องยนต์ V8 ขนาด 5.5 ลิตร แบบไร้ระบบอัดอากาศ***')
       st.write('***-ล้อหน้าขนาด 20x10 นิ้ว ที่รัดด้วยยางขนาด 275/30ZR20 เเละล้อหลังขนาด 21x13 นิ้ว ที่รัดด้วยยางขนาด 345/25ZR21 ซึ่งยางตามมาตรฐานนั้นจะใช้ยางจาก Michelin Pilot Sport***')
       st.write('***-ด้านระบบเบรกจะมาพร้อมจานเบรกที่ด้านหน้าขนาด 370 มม. พร้อมคาลิปเปอร์ 6 พอทและด้านหลังจะใช้จานเบรกขนาด 380 มม. พร้อมคาลิปเปอร์ 4 พอท***')
       st.write('***-ราคา THB 2,800,000***')

with tab3:
   st.subheader("Audi R8 Coupe V10 GT RWD")
   st.image("https://mediaservice.audi.com/media/fast/H4sIAAAAAAAAAFvzloG1tIiBOTrayfuvpGh6-m1zJgaGigIGBgZGoDhTtNOaz-I_2DhCHkCFGe8ysJSnJhUwAlW4MXFl5iamp-qDBPgZuYssdFMrSnTzUnPz2YHSfDxx82OvGmYdv7P9odeX-UEuL9jvPBNn4JG80c5idmnvwdZ5rgwT-Nb8-CLL6sPA80Ljz3ynLG9X55KNxmkmK6rP_I85ysDDa3x7zo9_LDP1Pj_UUr3v_Yxjg5s2A8-MJyEt65yrn0119Z3L518bciD7fCcDTxCz1fvu0JJWKYF9l_j8Dz1mmz9zIgNPBuPMFeeOTFT5uu3h5VpjA8cN328C3eBSWnq15cu9uD38u77f-HyweolJyCYGnrYY8XKRUnPBmOJb6e_al5lxiDFnMPDsrVD8zRJnIXDzyYnLnX9PyqZftxAE-mLb95P758kv3-XpdrKVa2rDfnGW7Qw8r6fW-q0pU3kZI7RXxsLVqtQuOnM3Aw_DA72seu0VTJP1jL5sV1p2aXfI8ucMPJ1X3V-mBMfM5JHmyfJ4N3leDNPScwyswIBl2g0kWOKABM8TIMFhwwAmQUG-AUgwLgTxWeuZGRi4HRgY2EIYQIBPuLQopyCxKDFXryi1uCA_rzizLFVQw4BIIMzq4xjpGgQAa47rIxACAAA?mimetype=image/png", width=300)
   if st.button('ดูข้อมูลเพิ่มเติม             '):
       st.write('***-เครื่องยนต์ V10 ขนาด 5.2 ลิตร ที่ให้กำลัง 620 แรงม้าและแรงบิด 565 นิวตันเมตร ส่งกำลังผ่านเกียร์อัตโนมัติคลัทซ์คู่ 7 จังหวะ***')
       st.write('***-ล้ออัลลอยแบบ Forged น้ำหนักเบาขนาด 20 นิ้วจึงทำให้น้ำหนักลงอีก 20 กก. ทำให้มีน้ำหนักรวมที่ 1,570 กก.***')
       st.write('***-ระบบเบรกด้านหน้า Discs ระบบเบรกด้านหลัง Discs***')
       st.write('***-ราคา THB 19,000,000***')

with tab3:
   st.subheader("Porsche 911 Carrera S 2022")
   st.image("https://carsguide-res.cloudinary.com/image/upload/f_auto,fl_lossy,q_auto,t_cg_hero_low/v1/editorial/vhs/porsche-911-2021.png", width=300)
   if st.button('ดูข้อมูลเพิ่มเติม                                                            '):
       st.write('***-เครื่องยนต์เบนซิน 6 สูบนอน Boxer ขนาด 3.0 ลิตร 2,981 ซีซี Twin Turbo กระบอกสูบ x ระยะช่วงชัก : 91.0 x 76.4 มิลลิเมตร พละกำลังสูงสุด 450 แรงม้า ที่ 6,500 รอบ/นาที แรงบิดสูงสุด 530 นิวตันเมตร***')
       st.write('***-ล้ออัลลอย คู่หน้า ขนาด 20 นิ้ว พร้อมยาง 245/35 ZR20 ล้ออัลลอย คู่หลัง ขนาด 21 นิ้ว พร้อมยาง 305/30 ZR21***')
       st.write('***-ระบบเบรก ให้ความมั่นใจ หยุด 450 แรงม้าได้นิ่ง และนุ่มนวล Porsche 911 Carrera S มีการเปลี่ยนระบบเสริมแรงเบรกจากหม้อลม***')
       st.write('***-ราคา THB 12,810,000***')

with tab3:
   st.subheader("BMW 8 Series 2023")
   st.image("https://img.sm360.ca/ir/w640h390c/images/newcar/ca/2023/bmw/serie-8-gran-coupe/m850i-xdrive/coupe/exteriorColors/13971_cc0640_032_a96.png", width=300)
   if st.button('ดูข้อมูลเพิ่มเติม                                                                        '):
       st.write('***-เครื่องยนต์ V8 ขนาด 4.4 ลิตร เทอร์โบคู่ ให้กำลัง 617 แรงม้า และแรงบิด 749 นิวตันเมตร ส่งกำลังด้วยเกียร์อัตโนมัติ 8 สปีดและระบบขับเคลื่อน 4 ล้อ***')
       st.write('***-ขนาดยางหน้า Front:245/35 R20 Rear: 275/30 R20 ประเภทยางรถยนต์ Radial***')
       st.write('***-ระบบเบรกด้านหน้า-หลัง Discs***')
       st.write('***-ราคา THB 2,800,000***')

with tab3:
   st.subheader("2022 Lexus LC")
   st.image("https://images.dealer.com/ddc/vehicles/2022/Lexus/LC%20500/Coupe/perspective/front-left/2022_24.png", width=300)
   if st.button('ดูข้อมูลเพิ่มเติม               '):
       st.write('***-เครื่องยนต์ V8 ขนาด 4.4 ลิตร เทอร์โบคู่ ให้กำลัง 617 แรงม้า และแรงบิด 749 นิวตันเมตร ส่งกำลังด้วยเกียร์อัตโนมัติ 8 สปีดและระบบขับเคลื่อน 4 ล้อ***')
       st.write('***-ขนาดยางหน้า Front:245/35 R20 Rear: 275/30 R20 ประเภทยางรถยนต์ Radial***')
       st.write('***-ระบบเบรกด้านหน้า-หลัง Discs***')
       st.write('***-ราคา THB 2,800,000***')

with tab2:
   st.subheader("Ferrari 296 GTB ")
   st.image("https://media-server1.modenamotorsgmbh.com/40970-large_default/ferrari-296-gtb.jpg", width=300)
   if st.button('ดูข้อมูลเพิ่มเติม                                                                                      '):
       st.write('***-เครื่องยนต์ V6 ทำมุม 120 องศา ขนาด 663 แรงม้า(เครื่องอย่างเดียว) มอเตอร์ไฟฟ้า กำลัง 122 กิโลวัตต์ (167 แรงม้า)***')
       st.write('***-ล้ออัลลอยดีไซน์ใหม่ขนาด 20 นิ้ว มีตัวเลือกล้อฟอร์จ และล้อคาร์บอนไฟเบอร์เบอร์ที่เบาลงไปอีก 8 กก.***')
       st.write('***-ระบบเบรกใช้จานคาร์บอน-เซรามิค ดึงมาจาก SF90 ด้านหน้า 398 มม. หลัง 360 มม.***')
       st.write('***-ราคา THB 21,900,000***')

with tab2:
   st.subheader("Porsche 911 GT3 RS")
   st.image("https://www.pngplay.com/wp-content/uploads/13/Porsche-911-GT3-RS-Free-PNG.png", width=300)
   if st.button('ดูข้อมูลเพิ่มเติม                                                                                                     '):
       st.write('***-เครื่องยนต์เบนซินแบบ 6 สูบ Boxer ขนาด 4.0 ลิตร ไร้ระบบอัดอากาศ ให้กำลังสูงสุด 525 แรงม้า (PS) จับคู่กับเกียร์อัตโนมัติ PDK 7 จังหวะ***')
       st.write('***-ล้ออัลลอย Forged น้ำหนักเบา คู่หน้าขนาด 20 นิ้ว คู่หลังขนาด 21 นิ้ว พร้อมดุมล้อแบบชิ้นเดียวเหมือนรถแข่ง ***')
       st.write('***-ระบบเบรกด้านหน้าใช้แบบ 6 ลูกสูบ ด้านหลังแบบ 4 ลูกสูบ พร้อมจานเบรกทำจากวัสดุเซรามิคคอมโพสิท เพื่อลดน้ำหนักของระบบเบรกโดยรวมเป็นออปชั่นเสริม***')
       st.write('***-ราคา THB 7,942,662 ***')

with tab2:
   st.subheader("Lamborghini Huracan Tecnica")
   st.image("https://www.lamborghini.com/sites/it-en/files/DAM/lamborghini/facelift_2019/connectivity/huracan/model_chooser/huracan_Tecnica_m.png", width=300)
   if st.button('ดูข้อมูลเพิ่มเติม                                                                                                             '):
       st.write('***-เครื่องยนต์ 5,204 cc., 640 แรงม้า(HP)***')
       st.write('***-ล้ออัลลอยลาย Damiso แบบ Diamond cut กว้าง 8.5 นิ้ว รัดด้วยยาง Bridgestone Potenza Sport ขนาด 245/30 R20 ที่ล้อคู่หน้า และขนาด 305/30 R20 ที่ล้อคู่หลัง***')
       st.write('***-ระบบเบรกเป็นดิสก์เบรกทั้ง 4 ล้อ จานเบรกคู่หน้าเป็นแบบมีครีบและรูระบายความร้อนทำจากคาร์บอนเซเรมิค ขนาด 380 มิลลิเมตร จับคู่กับคาลิปเปอร์ 6 พอต***')
       st.write('***-ราคา THB 22,980,000***')

with tab2:
   st.subheader("McLaren Artura")
   st.image("https://static.tcimg.net/vehicles/primary/e34ad3b5a048d413/2023-McLaren-Artura-white-full_color-driver_side_front_quarter.png", width=300)
   if st.button('ดูข้อมูลเพิ่มเติม                                                                                                                '):
       st.write('***-ครื่องยนต์เบนซินวางกลางลำ รหัส M630 แบบ V6 ขนาด 2,993 ซีซี. เทอร์โบคู่ กำลังสูงสุด 585 แรงม้า ที่ 7,500 รอบ/นาที แรงบิดสูงสุด 585 นิวตันเมตร ที่ 2,250 – 7,000 รอบ/นาที จับคู่กับเกียร์อัตโนมัติ SSG 8 จังหวะ***')
       st.write('***-ล้ออัลลอยลาย 7 ก้าน ขอบหน้า 19 นิ้ว หลัง 20 นิ้ว มาเป็นมาตรฐาน สวมกับยาง Pirelli P Zero ที่มีระบบ Pirelli Cyber Tyre ฝังเซนเซอร์ไว้ที่ยาง***')
       st.write('***-เบรกด้านหลังมีขนาด 380 มิลลิเมตร มาพร้อมกับคาลิปเปอร์ขนาด 4 สูบ***')
       st.write('***-ราคา THB 20,500,000***')

with tab2:
   st.subheader("Maserati MC20")
   st.image("https://maserati.scene7.com/is/image/maserati/maserati/international/Models/my23/mc20-cielo/picker/MC20-cielo-picker.png?$1400x2000$&fmt=png-alpha&fit=constrain", width=300)
   if st.button('ดูข้อมูลเพิ่มเติม                                                                                                                           '):
       st.write('***-เครื่องยนต์เบนซิน เทอร์โบ วี 6 สูบ ขนาด 3.0 ลิตร กำลังสูงสุด 630 แรงม้า มาพร้อมระบบเครื่องยนต์เทคโนโลยีแบบเดียวกับรถแข่งสูตร 1 หรือ F1 ถูกนำมาใช้กับรถสปอร์ทระดับซูเพอร์คาร์ครั้งแรก***')
       st.write('***-ล้อแมกขนาด 20 นิ้ว***')
       st.write('***-ระบบเบรกด้านหน้า-หลัง Ventilated Disc***')
       st.write('***-ราคา THB 21,500,000***')

with tab4:
    # ฟังก์ชันคำนวณภาษี
    def calculate_tax(price, weight, horsepower):
        tax = (price + weight + horsepower)/1.1 * 3.28 * 0.07 #ราคา + น้ำหนัก + แรงม้า / ภาษีสรรพสามิต * vat 7%
        return tax

    def app():
        st.title('คำนวณภาษีรถนำเข้า')
        st.write('โปรดกรอกข้อมูลด้านล่าง')

        # กำหนดฟิลด์อินพุตสำหรับราคา น้ำหนัก และแรงม้า
        price = st.number_input('ราคารถ (บาท)', min_value=0)
        weight = st.number_input('น้ำหนัก (กิโลกรัม)', min_value=0)
        horsepower = st.number_input('แรงม้า (แรงม้า)', min_value=0)

        # คำนวณภาษี
        if price > 0 and weight > 0 and horsepower > 0:
            tax = calculate_tax(price, weight, horsepower)

            # แสดงผล
            st.write(f'คุณต้องชำระภาษีรถนำเข้าเพิ่มจำนวน {tax:.2f} บาท')
        else:
            st.write('โปรดกรอกข้อมูลให้ถูกต้อง')

    # รันแอพ
    if __name__ == '__main__':
        app()

with tab5:
    st.subheader('scikitlearn')
    left, right = st.columns(2)
    def load_pricecar_data():
        return pd.read_excel('model.xlsx')


    def save_model(model):
        joblib.dump(model, 'model.joblib')


    def load_model():
        return joblib.load('model.joblib')


    generateb = right.button('generate model.xlsx')


    def generate_Y2K_data():
        pass


    if generateb:
        right.write('generating "model.xlsx" ...')
        generate_Y2K_data()
        right.write(' ... done')

    loadb = right.button('load model.xlsx')
    if loadb:
        right.write('loading "model.xlsx ..."')
        df = pd.read_excel('model.xlsx', index_col=0)
        right.write('... done')
        right.dataframe(df)
        fig, ax = plt.subplots()

    trainb = right.button('train pricecar')
    if trainb:
        right.write('training model ...')
        df = pd.read_excel('model.xlsx', index_col=0)
        model = LinearRegression()
        right.write('... done')
        right.dataframe(df)
        save_model(model)