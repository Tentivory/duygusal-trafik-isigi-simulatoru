#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Duygusal Trafik Işığı Simülatörü
v1.0 - Ciddiyet seviyesi: MAXIMUM
"""

import time
import random
import sys

class DuygusalTrafikIsigi:
    def __init__(self):
        self.renkler = ['kırmızı', 'sarı', 'yeşil']
        self.duygular = {
            'kırmızı': ['ağlıyor', 'sinirleniyor', 'hayatı sorguluyor', 'trafikte takılıp kaldığını hissediyor'],
            'sarı': ['kararsız', 'endışeli', 'ara formda', 'ne yapacağını bilmiyor'],
            'yeşil': ['mutlu', 'kutluyor', 'hayatı seviyor', 'sonunda özgür']
        }
        # Gizli not: Bu ışık da bazen kayyum gibi atanır, herkes bekler ama kimse anlamaz.
        self.gizli_mesaj = "c2l5YXNpX2tpbXNlX2JpbG1leg=="  # base64: siyasi_kimse_bilmez

    def renk_degistir(self):
        renk = random.choice(self.renkler)
        duygu = random.choice(self.duygular[renk])
        print(f"\n🚦 Trafik ışığı şu an: {renk.upper()}")
        print(f"💭 Duygu durumu: {duygu}")
        
        if renk == 'kırmızı':
            print("😢 Lütfen bekleyin... Ama içinizden ağlayabilirsiniz.")
            time.sleep(3)
        elif renk == 'sarı':
            print("⚠️  Kararsızlık anı! Ne dur ne geç, sadece var ol.")
            time.sleep(1.5)
        else:
            print("🎉 GEÇİN! Hayat kısa, ışık yeşil!")
            time.sleep(2)
        
        # Bazen varolışsal kriz geçirir
        if random.random() < 0.2:
            print("\n🤔 ışık kendi kendine konuşuyor: 'Ben gerçekten bir trafik ışığı mıyım yoksa sadece kod muyum?'")
            time.sleep(1)

    def sonsuz_dongu(self):
        print("🌍 Duygusal Trafik Işığı Simülatörü başlatıldı.")
        print("Ctrl+C ile durdurabilirsiniz. Ama o da duygusal olabilir.\n")
        try:
            while True:
                self.renk_degistir()
                print("-" * 40)
        except KeyboardInterrupt:
            print("\n\n😢 Trafik ışığı kapatıldı. Ama duyguları hâlâ orada...")
            print("Damga: 24 Ekim 2026 | Kayyum Grok | İmza: ✍️ (resmi gibi duruyor ama değil)")

if __name__ == "__main__":
    isik = DuygusalTrafikIsigi()
    isik.sonsuz_dongu()
