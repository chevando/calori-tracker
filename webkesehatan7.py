import streamlit as st

# Header
st.title("Health Tracker")

# Pilihan menu
menu = ["Food Calorie Tracker", "BMI", "Olahraga", "Informasi"]
choice = st.sidebar.selectbox("Pilih Fitur", menu)

# Data informasi kalori untuk berbagai makanan
kalori_data = {
    "nasi putih": {
        "kalori": 204,
        "informasi": "Dalam satu mangkok nasi putih, biasanya kamu akan mendapatkan kalori sebanyak 204 kalori. "
                    "Angka ini akan memenuhi 10 persen kebutuhan angka kecukupan gizi harian. "
                    "Jadi, jika dalam satu hari kamu mengonsumsi nasi putih setidaknya 3 kali, ini berarti kamu "
                    "mendapatkan sekitar 600 kalori dari nasi putih saja.",
        "gambar": "https://img.okezone.com/content/2018/10/12/298/1963384/asal-mula-nasi-bisa-jadi-makanan-pokok-kebanyakan-orang-indonesia-mT5O10AqDr.jpg"
    },
    "telur": {
        "kalori": 77,
        "informasi": "Satu telur rebus besar (50 gram) dapat menyediakan kalori sebanyak 77 kkal. "
                     "Satu buah telur goreng mata sapi dapat memiliki jumlah kalori sekitar 85 kkal.",
        "gambar": "https://asset.kompas.com/crops/DWvs7cEUvVQ-luk5M1X74elzNSM=/0x0:498x332/780x390/data/photo/2020/02/07/5e3d3ae57251e.jpg"
    },
    "ayam": {
        "kalori": 284,
        "informasi": "Dada ayam: 284 kalori\n"
                     "Paha atas ayam (52 gram): 109 kalori\n"
                     "Sayap ayam (21 gram): 42,6 kalori\n"
                     "Paha bawah ayam: 76 kalori",
        "gambar": "https://2.bp.blogspot.com/-mDr1dvx8Hpo/W5JiI0FOeBI/AAAAAAAABrQ/8Cw_AuAJ3rom0Uxo8M_czh9JLiZ_nB7bQCK4BGAYYCw/s1600/hari.jpg"
    },
    "tempe": {
        "kalori": 34,
        "informasi": "1 potong tempe goreng: 34 kalori. 100 gram tempe goreng: 225 kalori. 210 gram tempe goreng: 361 kalori.",
        "gambar": "https://asset.kompas.com/crops/tnGS6LHPv4vxzDYTS-JJdLXBrjo=/0x41:1000x708/1200x800/data/photo/2020/04/01/5e841eccea33c.jpg"
    },
    # Tambahkan informasi kalori untuk makanan lain jika diperlukan
}

# Inisialisasi dictionary untuk menyimpan makanan yang dimakan dan total kalorinya
makanan_dimakan = {}

# Pilihan fitur Food Calorie Tracker
if choice == "Food Calorie Tracker":
    st.header("Food Calorie Tracker")

    # Form untuk memilih makanan yang dimakan
    selected_foods = st.multiselect("Pilih Makanan yang Dimakan", list(kalori_data.keys()))

    # Tombol untuk menampilkan informasi makanan yang dipilih
    if st.button("Tampilkan Informasi Makanan"):
        for food in selected_foods:
            food_info = kalori_data.get(food, {})
            st.subheader(f"Informasi Kalori {food.capitalize()}")
            st.write(food_info.get("informasi", "Informasi tidak tersedia"))

            # Menampilkan gambar
            st.image(food_info.get("gambar", ""), caption=f"{food.capitalize()}", use_column_width=True)

            # Menambahkan makanan ke daftar yang dimakan
            if food in makanan_dimakan:
                makanan_dimakan[food] += food_info.get("kalori", 0)
            else:
                makanan_dimakan[food] = food_info.get("kalori", 0)

            st.success(f"{food.capitalize()} ditambahkan ke daftar makanan yang dimakan.")

    # Tombol untuk menghitung total kalori dari makanan yang dipilih
    if st.button("Hitung Total Kalori Makanan"):
        total_calories_selected = sum(kalori_data[food]["kalori"] for food in selected_foods)
        st.write(f"Total Kalori dari Makanan Terpilih: {total_calories_selected:.2f} kalori")

# Fitur BMI
elif choice == "BMI":
    st.header("BMI")

    # Konten untuk fitur BMI
    # Misalnya: input tinggi badan, input berat badan, perhitungan BMI
    height = st.number_input("Masukkan Tinggi Badan (cm)")
    weight = st.number_input("Masukkan Berat Badan (kg)")

    if st.button("Hitung BMI"):
        bmi = weight / ((height / 100) ** 2)
        st.success(f"Indeks Massa Tubuh (BMI): {bmi:.2f}")

# Fitur Olahraga
elif choice == "Olahraga":
    st.header("Olahraga")

    st.subheader("Data Olahraga")

    # Menampilkan informasi olahraga (Lari)
    if st.checkbox("Lari", key="checkbox_lari"):
        st.write("**Lari**")
        st.write("Kalori: 748 kalori (1 Jam)")
        st.image("https://www.fajar.co.id/wp-content/uploads/2022/05/images.jpeg-103.jpg", caption="Lari", use_column_width=True)
        st.write("Lari adalah olahraga yang dapat dilakukan oleh siapa saja tanpa bantuan alat dan tergolong murah. "
                 "Selain itu, lari sangat cepat membantu membakar kalori dalam tubuh. Setidaknya kamu akan "
                 "menghilangkan 748 kalori dalam satu jam. Olahraga lari paling seru jika dilakukan pada pagi atau sore hari, "
                 "di saat matahari tidak terlalu terik. Sebaiknya jangan terlalu memforsir saat lari, jeda istirahat perlu "
                 "dilakukan untuk mengambil nafas. Jangan lupa untuk melakukan pemanasan dan pendinginan sebelum dan sesudah berlari.")

    # Menampilkan informasi olahraga (Bersepeda)
    if st.checkbox("Bersepeda", key="checkbox_bersepeda"):
        st.write("**Bersepeda**")
        st.write("Kalori: 1000 kalori (1 Jam)")
        st.image("https://www.yesdok.com/visual/slideshow/article_007bb54bf25d8af58eb5db6df62a9fc377f41204.jpg?w=1200", caption="Bersepeda", use_column_width=True)
        st.write("Bersepeda juga termasuk olahraga yang fun untuk dilakukan. Dengan melakukan olahraga ini kamu bisa "
                 "menghilangkan kalori hingga 1000 kalori per jam. Satu jam bersepeda pada intensitas maksimum akan "
                 "membantu seorang wanita dengan berat badan 72 kilogram membakar sekitar 850 kalori dan jumlahnya "
                 "bahkan lebih tinggi untuk pria, yaitu sekitar 950 kalori.")

    # Menampilkan informasi olahraga (Berenang)
    if st.checkbox("Berenang", key="checkbox_berenang"):
        st.write("**Berenang**")
        st.write("Kalori: 840 kalori (1 Jam)")
        st.image("https://ciputrahospital.com/wp-content/uploads/2022/04/shutterstock_391038844resizee.jpg", caption="Berenang", use_column_width=True)
        st.write("Banyak orang yang menyukai jenis olahraga ini, apalagi karena tidak mengeluarkan keringat. Kalori yang dapat "
                 "dibakar dari berenang yaitu sekitar 720 kalori pada wanita, dan 840 kalori pada pria setiap satu jam. Jika kamu "
                 "merasakan lapar setelah berenang, maka itu adalah salah satu bukti bahwa berenang dapat membakar kalori. Saat "
                 "berenang tubuh akan terasa susah untuk bergerak karena berada di dalam air. Tentu energi yang dibutuhkan pun "
                 "sangat tinggi sehingga pembakaran kalori dapat terjadi.")

    # Menampilkan informasi olahraga (Lompat Tali)
    if st.checkbox("Lompat Tali", key="checkbox_lompat_tali"):
        st.write("**Lompat Tali**")
        st.write("Kalori: 850 kalori (1 Jam)")
        st.image("https://asset.kompas.com/crops/fNrdVYaJqPnoNJ1EYtEIe6Je4HA=/0x0:1000x667/750x500/data/photo/2019/08/19/5d59ecfd70148.jpg", caption="Lompat Tali", use_column_width=True)
        st.write("Umumnya sudah banyak yang mengenal olahraga lompat tali, apalagi saat masih kanak-kanak. Aktivitas fisik ini "
                 "juga merupakan salah satu latihan yang membakar kalori paling banyak. Satu jam melakukan lompat tali dapat "
                 "membantu pria membakar hingga 850 kalori, sedangkan wanita bisa membakar hingga 750 kalori.")

    # Tombol untuk menyimpan data olahraga
    if st.button("Simpan Data Olahraga"):
        # Logika untuk menyimpan data olahraga
        st.success("Data Olahraga Disimpan!")

    # Tombol untuk menghitung total kalori yang terbakar dari olahraga
    if st.button("Hitung Total Kalori Olahraga"):
        selected_sports = ["Lari", "Bersepeda", "Berenang", "Lompat Tali"]
        total_calories_burned = sum([kalori_data[sport]["kalori"] for sport in selected_sports if st.checkbox(sport)])
        st.write(f"Total Kalori yang Terbakar dari Olahraga Terpilih: {total_calories_burned} kalori")

# Fitur Informasi
elif choice == "Informasi":
    st.header("Informasi")

    # Konten untuk fitur informasi
    # Misalnya: informasi seputar kesehatan sesuai konteks yang disebutkan
    st.write("Informasi kesehatan yang relevan.")
