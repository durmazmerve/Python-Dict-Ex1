#dict tipindeki bir değişkenin hem anahtarların toplamını hem de bu anahtarlara karşılık gelen elamanlarının toplamı

sozluk = {1: 10, 2: 20, 3: 30} 
def toplama(sozluk):

    print(sum(sozluk.keys()))
    print(sum(sozluk.values()))