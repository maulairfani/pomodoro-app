import streamlit as st
import time

st.title('Pomodoro App ⏳')


#-------------------#
side = st.sidebar
side.subheader('Sesuaikan pomodoro senyamanmu')
form = side.form('data_pomodoro')
tugas = form.text_input('Tugas')
t1 = form.number_input('Waktu Fokus (menit)', min_value=0, max_value=120)
# pengulangan = form.slider('Pengulangan', min_value=1, max_value=5)
t2 = form.number_input('Waktu Istirahat (menit)', min_value=0, max_value=25)
# istirahat_panjang = form.number_input('Waktu Istirahat Pendek (menit)', min_value=10, max_value=60)
pilihan_musik = ['Lo-fi Jazz', 'Lo-fi Cool']
musik = form.radio('Musik', options=pilihan_musik)

mulai = form.form_submit_button('Mulai !')

#-------------------#

t1 *= 60
t2 *= 60

def timer(t1, t2):
    with st.empty():
        while t1:
            mins, secs = divmod(t1, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            st.subheader(f"⏳ Waktu tersisa *{timer}* ")
            time.sleep(1)
            t1 -= 1
            st.success("🔔 Waktu fokus selesai! Anda dapat istirahat sejenak")

    with st.empty():
        while t2:
            # Start the break
            mins2, secs2 = divmod(t2, 60)
            timer2 = '{:02d}:{:02d}'.format(mins2, secs2)
            st.subheader(f"⏳ Waktu tersisa {timer2}")
            time.sleep(1)
            t2 -= 1
            st.error("⏰ 5 minute break is over!")
            
    
if mulai:
    if musik == 'Lo-fi Jazz':
        st.audio('pomodoro-app/app/jazz.wav')
    elif musik == 'Lo-fi Cool':
        st.audio('pomodoro-app/app/cool.wav')  
    st.subheader(tugas)
    st.write('''*Tetaplah fokus hingga timer selesai!*''')
    timer(t1, t2)



st.markdown('''
## Apa itu *pomodoro* ?
Teknik Pomodoro adalah teknik pengaturan waktu yang telah diperkenalkan pada akhir tahun 1980 oleh Fransisco Cirillo. 
Pomodoro sendiri dalam Bahasa Spanyol artinya tomat, Cirillo saat masih menjadi mahasiswa menggunakan kitchen timer berbentuk tomat
sebagai pengatur waktu saat belajar.
''')
st.markdown('''
## Cara Menerapkan Teknik Pomodoro
1. Jauhi distraksi dan siapkan materi yang harus dipelajari
2. Tentukan waktu dan mulai fokus untuk beraktivitas
3. Lakukan kegiatan yang menyenangkan saat istirahat
4. Ulangi teknik di atas hingga empat kali
''')
