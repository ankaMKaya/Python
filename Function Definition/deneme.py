def sistem_bilgisi_göster():
    import sys
    print("\nSistemde kurulu Python'ın;")
    print("\tana sürüm numarası:", sys.version_info.major)
    print("\talt sürüm numarası:", sys.version_info.minor)
    print("\tminik sürüm numarası:", sys.version_info.micro)

    print("\nKullanılan işletim sisteminin;")
    print("\tadı:", sys.platform)

sistem_bilgisi_göster()
