yaş_bilgisi = int(input("yaş bilginizi girin:"))
gelir_bilgisi = float(input("gelirinizi girin:"))
kredi_geçmişi = input("kredi geçmişinizi girin(iyi/kötü):")

if yaş_bilgisi < 18:
    print(yaş_bilgisi, "yaşı için kredi başvurusu reddedildi.")
elif 18 <= yaş_bilgisi <= 25:
    print(yaş_bilgisi, "yaşı için kredi başvurusu gözden geçirilir.")
elif 25 < yaş_bilgisi < 50:
    print(yaş_bilgisi, "yaşı için kredi başvurusu onaylandı")
else:
    print("kredi başvurusu yaş nedeniyle reddedildi.")

if gelir_bilgisi < 2000:
    print(gelir_bilgisi, "geliri için kredi başvurusu reddedildi.")
elif 2000 <= gelir_bilgisi <= 4000:
    print(gelir_bilgisi, "geliri için kredi başvurusu gözden geçirilir.")
else:
    print(gelir_bilgisi, "geliri için kredi başvurusu onaylanır.")

if kredi_geçmişi == "kötü":
    print(kredi_geçmişi, "durumundan dolayı kredi başvurusu reddedildi.")
else:
    print(kredi_geçmişi, "durumundan dolayı kredi başvurusu onaylandı.")

if yaş_bilgisi <= 50 and gelir_bilgisi > 2000 and kredi_geçmişi == "iyi":
    print(f"başvurunuz değerlendirilmiştir. yaş durumu: {yaş_bilgisi}, gelir durumu: {gelir_bilgisi}, kredi geçmişi: {kredi_geçmişi}")
