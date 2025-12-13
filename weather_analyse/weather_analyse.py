#1.Kütüphane ve Veri Yükleme:#
import pandas as pd
import numpy as np

df = pd.read_csv("weather_data.csv")

#2.Veriyi Keşfetme:#
print("İlk 5 Satır:")
print(df.head())
print("\nSon 5 Satır:")
print(df.tail())

print("\nİstatistiksel Özet:")
print(df.describe())

#3.Sütun Seçimi:#
print("\nSeçili Sütunlar: Date, City, Temperature")
df_secim = df[["Date", "City", "Temperature"]]
print(df_secim.head())

print("\nSeçili Sütunlar: City, Temperature")
df_secim2 = df[["City", "Temperature"]]
print(df_secim2.head())

#4.Basit Filtreleme:#
print("\nSıcaklık 30°C Üzeri Olan Kayıtlar:")
sicak_30 = df[df["Temperature"] > 30]
print(sicak_30)

print("\nSadece Bursa Olan Kayıtlar:")
bursa_kayit= df[df["City"] == "Bursa"]
print(bursa_kayit.head())

#5.Mantıksal Operatörler ile Filtreleme:#
print("\nİstanbul Ve Nem > 60% Kayıtlar:")
istanbul_nem = df[(df["City"] == "İstanbul") & (df["Humidity"] > 60)]
print(istanbul_nem.head())

print("\nAnkara veya Sıcaklık < 5°C Kayıtlar:")
ankara_sicak = df[(df["City"] == "Ankara") | (df["Temperature"] < 5)]
print(ankara_sicak.head())

print("\nSıcaklık < 10°C veya Nem > 70% Kayıtlar:")
sicak_nem = df[(df["Temperature"] < 10) | (df["Humidity"] > 70)]
print(sicak_nem.head())

#6.Sıralama (Sorting):#
print("\nSıcaklığa Göre Azalan (İlk 10):")
sicaklik_azalan = df.sort_values(by="Temperature", ascending=False)
print(sicaklik_azalan.head(10))

print("\nNeme Göre Azalan (İlk 5):")
nem_azalan = df.sort_values(by="Humidity", ascending=False)
print(nem_azalan.head())

print("\nŞehre Göre Artan (İlk 5):")
sehir_artan = df.sort_values(by="City", ascending=True)
print(sehir_artan.head())

#7.Yeni Sütun Ekleme:#
print("\nFahrenheit Sütunu Eklendi:")
df["Temperature_F"] = (df["Temperature"] * 9/5) + 32
print(df[["Temperature", "Temperature_F" ]].head())

print("\nFeelsLike Sütunu Eklendi:")
df["FeelsLike"] = df["Temperature"] - (df["Humidity"] / 100)
print(df[["Temperature", "Humidity", "FeelsLike"]].head())

#8.Gruplama (Grouping) ve Analiz:#
print("\nŞehir Başına Kayıt Sayısı:")
sehir_say = df.groupby('City')['Date'].count()
# Alternatif: df['City'].value_counts()
print(sehir_say)

print("\nŞehirlere Göre Ortalama Sıcaklık:")
ortalama_sicaklik = df.groupby("City")["Temperature"].mean().round(2)
print(ortalama_sicaklik)

#9.En Yüksek/Düşük Değer Analizi:#
print("\nEn Yüksek Sıcaklığın Olduğu Satır:")
yuksek_sicaklik = df.loc[df["Temperature"].idxmax()]
print(yuksek_sicaklik)

print("\nEn Düşük Nem Oranının Olduğu Satır:")
dusuk_nem = df.loc[df["Humidity"].idxmin()]
print(dusuk_nem)

#10.Dışa Aktarma (Export):#
print("Şehirlere Göre Ortalama Sıcaklık Tablosu:")

#CSV olarak kaydetme
ortalama_sicaklik.to_csv('sehir_sicakliklari.csv', header=True)
print("'sehir_sicakliklari.csv' dosyası oluşturuldu.")

#Excel olarak kaydetme
ortalama_sicaklik.to_excel('sehir_sicakliklari.xlsx', sheet_name='Ortalama Sıcaklıklar')
print("'sehir_sicakliklari.xlsx' dosyası oluşturuldu.")
