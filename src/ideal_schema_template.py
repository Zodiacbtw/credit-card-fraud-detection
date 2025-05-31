IDEAL_FRAUD_COLUMNS = {
    # I. İşlem Bilgileri
    "TransactionID": "string", # veya "int64"
    "TransactionDateTime": "datetime64[ns]",
    "TransactionAmt": "float32",
    "TransactionCurrency": "category", # veya "object"
    "TransactionType": "category",
    "TransactionStatus": "category",
    "ProductCD": "category", # IEEE'de var
    "MerchantID": "category", # IEEE'de yok, türetilemezse boş kalır
    "MerchantCategoryCode": "category", # IEEE'de 'M1'-'M9' gibi alanlar var, bunlar MCC'ye benzetilebilir veya bu alanlar kullanılabilir
    "MerchantName": "category",
    "MerchantCountry": "category",
    "MerchantCity": "category",
    "POS_EntryMode": "category",
    "POS_ConditionCode": "category",
    "InstallmentCount": "int8", # Türkiye için önemli, IEEE'de doğrudan yok

    # II. Kart Bilgileri (IEEE'de card1-card6, addr1, addr2, P_emaildomain, R_emaildomain var)
    "CardType": "category", # card4'ten (kart şeması) türetilebilir veya card6'dan (kredi/debit)
    "CardScheme": "category", # card4'ten gelir
    "CardBIN": "category", # card1'in bir kısmı olabilir ama tam BIN olmayabilir
    "CardLast4Digits": "category", # Genellikle ayrı verilmez, IEEE'de yok
    "IssuingBank": "category", # card1, card2'den çıkarım yapılabilir veya P_emaildomain'den
    "IssuingBankCountry": "category", # addr1, addr2, P_emaildomain'den çıkarım yapılabilir

    # III. Müşteri Bilgileri
    "UserID": "category", # Eğer birden fazla işlemi olan müşteri varsa oluşturulabilir, yoksa TransactionID ile aynı olabilir
    "EmailDomain_P": "category", # P_emaildomain'den gelir
    "EmailDomain_R": "category", # R_emaildomain'den gelir
    "BillingAddress_Country": "category", # addr1, addr2'den çıkarım
    "ShippingAddress_Country": "category", # addr1, addr2'den çıkarım
    "AddressesMatch": "bool", # addr1 ve addr2 karşılaştırılarak
    "CustomerIPAddress_Prefix": "category", # id_30 (OS) ve id_31 (tarayıcı) ile birlikte IP'den çıkarım yapılabilir, IEEE'de doğrudan IP yok
    "IP_Country": "category",

    # IV. Cihaz ve Tarayıcı Bilgileri (IEEE'de id_01-id_38 arası ve DeviceInfo)
    "DeviceType": "category", # DeviceType'dan gelir
    "DeviceID": "category", # DeviceInfo'dan anonim bir ID türetilebilir
    "DeviceInfo_Cleaned": "category", # DeviceInfo'dan gelir
    "Browser_Cleaned": "category", # id_31'den gelir
    "OS_Cleaned": "category", # id_30'dan gelir
    "ScreenResolution": "category", # id_03, id_04, id_24 gibi alanlardan çıkarım yapılabilir

    # V. Zaman ve Hız Bazlı Özellikler (Bunlar IEEE'de oluşturulacak)
    "TimeSinceLastTransaction_User": "float32",
    # ... diğer hız bazlı özellikler ...
    "TransactionHour": "int8", # TransactionDT'den türetilecek
    "TransactionDayOfWeek": "int8", # TransactionDT'den türetilecek

    # VI. Risk Skorları (IEEE'de yok, ama modelleme sonrası eklenebilir)
    "ModelRiskScore": "float32",

    # VII. Hedef Değişken
    "isFraud": "int8" # veya "bool"
}