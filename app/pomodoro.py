import streamlit as st
import time

st.title('⏳ Pomodoro App ⏳')
st.caption('*Developed by Kelompok 6*')

# Magic commands implicitly `st.write()`

st.markdown('''
## Apa itu *pomodoro* ?
Teknik Pomodoro adalah teknik pengaturan waktu yang telah diperkenalkan pada akhir tahun 1980 oleh Fransisco Cirillo. 
Pomodoro sendiri dalam Bahasa Spanyol artinya tomat, Cirillo saat masih menjadi mahasiswa menggunakan kitchen timer berbentuk tomat
sebagai pengatur waktu saat belajar.
''')
st.markdown('''
## Cara Menggunakan Pomodoro App
1. Lengkapi data pada samping kiri terkait nama tugas, waktu fokus, waktu istirahat, dan musik pengiring
2. Tekan tombol *Mulai !* untuk memulai timer
3. Kamu dapat melihat timer berjalan dan player musik di sebelah kanan!
4. Ulangi teknik di atas hingga empat kali
''')

#---------------------------------------------#
side = st.sidebar
side.subheader('Sesuaikan pomodoro senyamanmu!')
form = side.form('data_pomodoro')
tugas = form.text_input('Tugas')
t1 = form.number_input('Waktu Fokus (menit)', min_value=0, max_value=120)
t2 = form.number_input('Waktu Istirahat (menit)', min_value=0, max_value=25)
pilihan_musik = ['Lo-fi Jazz', 'Lo-fi Cool']
musik = form.radio('Musik', options=pilihan_musik)

mulai = form.form_submit_button('Mulai !')

#----------------------------------------------#

t1 *= 60
t2 *= 60

col1, col2 = st.columns(2)

def timer(t1, t2):
    with col1.empty():
        while t1:
            mins, secs = divmod(t1, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            st.subheader(f"⏳ Waktu fokus *{timer}* ⏳")
            time.sleep(0.05)
            t1 -= 1
            st.success("🔔 Waktu fokus selesai! Anda dapat istirahat sejenak")

    with col1.empty():
        while t2:
            mins2, secs2 = divmod(t2, 60)
            timer2 = '{:02d}:{:02d}'.format(mins2, secs2)
            st.subheader(f"⏳ Waktu istirahat *{timer2}* ⏳")
            time.sleep(0.05)
            t2 -= 1
            st.error("⏰ Waktu istirahat selesai!")
            
    
if mulai:
    col1.header(tugas)
    col1.write('*Tetaplah fokus hingga timer selesai!*')
    for i in range(5):
        col2.write('')
    col2.write('Putar musikmu disini!')
    if musik == 'Lo-fi Jazz':
        col2.audio('app/jazz.wav')
    elif musik == 'app/Lo-fi Cool':
        col2.audio('cool.wav') 
    timer(t1, t2)
    st.write('Klik tombol *Mulai!* untuk mengulangi')
    st.write('---')
    st.caption('Terima kasih telah menggunakan pomodoro app 😊')
