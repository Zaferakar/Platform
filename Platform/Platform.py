import threading
from textwrap import wrap
from PIL import ImageTk
from tkinter import CENTER, StringVar
import webbrowser
import customtkinter
from fonksiyonlar import*

customtkinter.set_appearance_mode("dark")


# noinspection PyTypeChecker
class kaydirilabiliaranaalan(customtkinter.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)


        # çerçeve kaydırılabilir alan butonları


        #bağlı cihaz günlüğü
        self.icscroll = customtkinter.CTkScrollableFrame(self, width=1040, height=200)
        self.icscroll.grid(column=1, row=0, columnspan=6)
        #bağlı cihaz günlüğü görüntüleme butonu
        self.add_button = customtkinter.CTkButton(self, text="Connected Device Information", command=lambda: threading.Thread(target=self.baglicihazlar).start())
        self.add_button.grid(row=0, column=0)

        #anlık bağlı olan cihazların görüntüleme butonu
        self.add_button = customtkinter.CTkButton(self, text="Refresh (Reset Selected Files)",command=lambda: threading.Thread(target=self.cati).start(), width=1350, height=40, fg_color="grey33")
        self.add_button.grid(row=1, column=0,columnspan=6)
        #sahte kaydırılabilir apk yükleme alanı
        self.apkscroll = customtkinter.CTkScrollableFrame(self, width=1330, height=200)
        self.apkscroll.grid(column=0, row=3, columnspan=6, pady=15)
        # sahte kaydırılabilir dosya yükleme alanı
        self.dosyascroll = customtkinter.CTkScrollableFrame(self, width=1330, height=200)
        self.dosyascroll.grid(column=0, row=5, columnspan=6)
        #sahte durum kaydırılabilir alanı
        self.durumscroll = customtkinter.CTkScrollableFrame(self, width=1330, height=300)
        self.durumscroll.grid(column=0, row=7, columnspan=6)

    def cati(self):

        try:
            self.cihaz_listesi2 = baglicihazlar_adb()
            self.cihaz_secme = self.cihaz_listesi2[0]#cihaz listesi

            self.cihaz_listesi = surum_ve_cihaz_id()

            self.cihaz_listesi_uzunlugu = len(self.cihaz_listesi2[0])

            self.apkscroll = customtkinter.CTkScrollableFrame(self, width=1335, height=200,fg_color="grey")
            self.apkscroll.grid(column=0, row=3, columnspan=6, pady=15)

            self.dosyascroll = customtkinter.CTkScrollableFrame(self, width=1335, height=200, fg_color="grey")
            self.dosyascroll.grid(column=0, row=5, columnspan=6)



            def top_level(*j):
                CTkMessagebox(title="Warning!!!",
                              message="You can delete the packages in the list, but the package you delete may be important for the operation of the device!!!\n Please Be Careful Otherwise Your Device May Not Work Properly!!!",
                              icon="warning", width=500, option_1="OK")
                str1 = ""
                for ele in j:
                    str1 += ele

                print(str1)
                uygulama_listesi = cihaz_yuklu_uygulamalar(str1)


                def bul():
                    self.f = 0



                    for i in range(len(uygulama_listesi)):
                        self.numara_label = customtkinter.CTkLabel(self.kaydirilabilir_uygulama_alan, width=40, height=30,
                                                                   fg_color="grey", text=self.f + 1, corner_radius=8)
                        self.numara_label.grid(row=self.f + 1, column=0)


                        index = uygulama_listesi[self.f].find(self.arama_alani.get())

                        if index == -1:
                            pass
                        elif index == 0:
                            pass
                        else:
                            #self.numara_label.destroy()
                            self.numara_label = customtkinter.CTkLabel(self.kaydirilabilir_uygulama_alan, width=40, height=30,fg_color="green", text=self.f + 1, corner_radius=8)
                            self.numara_label.grid(row=self.f+1, column=0)






                        self.f = self.f + 1


                self.toplevel = customtkinter.CTkToplevel(self, width=700, height=500, fg_color="grey")
                self.toplevel.title("The Platform:  Device Serial Number= {}".format(str1))
                self.toplevel.attributes('-topmost', 'true')

                self.kaydirilabilir_uygulama_alan = customtkinter.CTkScrollableFrame(self.toplevel, width=700, height=300, fg_color="grey64")
                self.kaydirilabilir_uygulama_alan.grid(column=0, row=0, columnspan=4)


                self.arama_alani = customtkinter.CTkEntry(self.kaydirilabilir_uygulama_alan, width=550, height=30,fg_color="grey20", placeholder_text="Enter Package Name:")
                self.arama_alani.grid(column=1 , row=0, pady=5)
                self.arama_butonu = customtkinter.CTkButton(self.kaydirilabilir_uygulama_alan, height=30, width=80,text="Find", command=bul)
                self.arama_butonu.grid(row=0, column=2)

                #self.uygulama_label = customtkinter.CTkLabel(self.kaydirilabilir_uygulama_alan, width=600, height=30,fg_color="grey20")
                #self.arama_alani.grid(column=1, row=0, pady=5)



                def sil(uygulama):
                    print(uygulama)#uygulama ismi
                    print(j)#cihaz id numarası
                    uygulama_silme(uygulama, str1)







                uygulama_listesi = cihaz_yuklu_uygulamalar(str1)
                try:
                    uygulama_listesi.remove('WARNING: linker: libdvm.so has text relocations. This is wasting memory and is a security risk. Please fix.')#cihaza bağlı hatadır farklı hataları listeden sil
                except ValueError:
                    pass
                print(len(uygulama_listesi))
                self.g = 1
                self.s = 0

                for i in range(len(uygulama_listesi)):
                    self.label = customtkinter.CTkLabel(self.kaydirilabilir_uygulama_alan, text=uygulama_listesi[self.s], height=30, width=550, corner_radius=8,
                                                        fg_color="grey30")
                    self.label.grid(row=self.g, column=1)

                    self.label = customtkinter.CTkLabel(self.kaydirilabilir_uygulama_alan, text=self.g,
                                                        height=30, width=40, corner_radius=8,
                                                        fg_color="grey30")
                    self.label.grid(row=self.g, column=0)

                    #self.sil_butonu = customtkinter.CTkButton(self.kaydirilabilir_uygulama_alan, height=30, width=80, corner_radius=8,text="Sil", fg_color="red3")
                    #self.sil_butonu.grid(row=self.g, column=2, padx=5)

                    self.sil_butonu = customtkinter.CTkButton(self.kaydirilabilir_uygulama_alan, text="Delete", height=30, fg_color="red4",
                                                              width=80,
                                                              command=lambda uygulama=uygulama_listesi[self.s],
                                                                             b=self.a: sil(uygulama))
                    self.sil_butonu.grid(column=2, row=self.g, padx=5)


                    self.g = self.g + 1
                    self.s = self.s + 1









            def durumscrollyenileme():
                #self.durumscroll.destroy()
                self.durumscroll = customtkinter.CTkScrollableFrame(self, width=1330, height=300, fg_color="grey")
                self.durumscroll.grid(column=0, row=7, columnspan=6,pady=15)

                self.cihaz_listesi2 = baglicihazlar_adb()
                self.cihaz_listesi = surum_ve_cihaz_id()

                self.cihaz_listesi_uzunlugu = len(self.cihaz_listesi2[0])

                self.a = 0
                self.b = 1
                self.c = 1
                for i in range(self.cihaz_listesi_uzunlugu):

                    # apk işlemleri butonları
                    self.cihaz_isimleri = customtkinter.CTkLabel(self.durumscroll, text=self.cihaz_listesi[self.a], height=150,
                                                                 fg_color="green", width=200, corner_radius=8)
                    self.cihaz_isimleri.grid(column=0, row=self.b, rowspan=3, padx=1, pady=2)

                    cihaz_id_listesi = self.cihaz_listesi2[0]  # sadece cihaz id leri
                    cihaz_bilgileri(cihaz_id_listesi[self.a])

                    self.cihaz_bilgileri = customtkinter.CTkLabel(self.durumscroll,
                                                                  text=cihaz_bilgileri(cihaz_id_listesi[self.a]), height=150,
                                                                  fg_color="gray20", width=720, corner_radius=8)
                    self.cihaz_bilgileri.grid(column=1, row=self.b, rowspan=3, padx=1, pady=2)

                    try:
                        self.cihaz_apk_dosyasi = customtkinter.CTkLabel(self.durumscroll,
                                                                        text=("Selected APK File:\n{}".format(liste_cihaz_id_ve_apk_dosyasi[self.a][1])),
                                                                        height=45,
                                                                        fg_color="gray20", width=403, corner_radius=8)
                        self.cihaz_apk_dosyasi.grid(column=2, row=self.c, padx=1, pady=1)

                    except IndexError:

                        self.cihaz_apk_dosyasi = customtkinter.CTkLabel(self.durumscroll,
                                                                        text="Selected APK File:\n",
                                                                        height=45,
                                                                        fg_color="gray20", width=403, corner_radius=8)
                        self.cihaz_apk_dosyasi.grid(column=2, row=self.c, padx=1, pady=1)

                    try:
                        self.cihaz_veri_dosyasi = customtkinter.CTkLabel(self.durumscroll,
                                                                         text=("Selected Code Folder:\n{}".format(liste_cihaz_id_ve_kod_veri_dosyasi[self.a][1])),
                                                                         height=45,
                                                                         fg_color="gray20", width=403, corner_radius=8)
                        self.cihaz_veri_dosyasi.grid(column=2, row=self.c + 1, padx=1, pady=1)

                    except IndexError:

                        self.cihaz_veri_dosyasi = customtkinter.CTkLabel(self.durumscroll,
                                                                         text="Selected Code Folder:\n",
                                                                         height=45,
                                                                         fg_color="gray20", width=403, corner_radius=8)
                        self.cihaz_veri_dosyasi.grid(column=2, row=self.c + 1, padx=1, pady=1)

                    try:
                        self.cihaz_kod_dosyasi = customtkinter.CTkLabel(self.durumscroll,
                                                                        text=("Selected Input Data Folder:\n{}".format(liste_cihaz_id_ve_giris_veri_dosyasi[self.a][1])),
                                                                        height=45,
                                                                        fg_color="gray20", width=403, corner_radius=8)
                        self.cihaz_kod_dosyasi.grid(column=2, row=self.c + 2, padx=1, pady=1)

                    except IndexError:
                        self.cihaz_kod_dosyasi = customtkinter.CTkLabel(self.durumscroll,
                                                                        text="Selected Input Data Folder:\n",
                                                                        height=45,
                                                                        fg_color="gray20", width=403, corner_radius=8)
                        self.cihaz_kod_dosyasi.grid(column=2, row=self.c + 2, padx=1, pady=1)

                    self.a = self.a + 1
                    self.c = self.c + 3
                    self.b = self.b + 3








            #j değeri cihaz kimliğidir
            liste_cihaz_id_ve_apk_dosyasi = []
            for i in range(len(self.cihaz_secme)):
                liste44 = []
                liste_cihaz_id_ve_apk_dosyasi.append(liste44)
            print(liste_cihaz_id_ve_apk_dosyasi)
            fff = []
            def senkronizasyon_apk(j, b):#b = eklenecek olan verinin index numarası, j cihaz id si

                print(j)
                #print(b)
                apk_dosyasi = apk_sec()
                liste_cihaz_id_ve_apk_dosyasi[b] = [] #eğer yanlış apk dosyası seçilirse tekrar seçme butonuna tıklanır ve liste index değerine göre temizlenir

                liste_cihaz_id_ve_apk_dosyasi[b].append(j)
                liste_cihaz_id_ve_apk_dosyasi[b].append(apk_dosyasi)

                #print(liste_cihaz_id_ve_apk_dosyasi[0][0],"fdfdfds")
                #print(liste_cihaz_id_ve_apk_dosyasi[b][0])
                cihaz_apk_konum_uzanisi= liste_cihaz_id_ve_apk_dosyasi[b][1]

                durumscrollyenileme()
                #print(liste_cihaz_id_ve_apk_dosyasi)
                return j, cihaz_apk_konum_uzanisi#cihaz id ve seçilen apk listesi, cihaz id si, cihazlara yollanacak apknın konum yol uzantısı









            #j değeri cihaz kimliğidir
            liste_cihaz_id_ve_kod_veri_dosyasi = []
            for i in range(len(self.cihaz_secme)):
                liste55 = []#cihaz sayısı kadar iç liste oluşturulur ve iç listelere cihaz id si ile dosyalar eklenir
                liste_cihaz_id_ve_kod_veri_dosyasi.append(liste55)


            def senkronizasyon_kod_veri_dosya(j, c):#c = eklenecek olan verinin index numarası, j cihaz id si

                print(j)
                print(c)
                kod_dosyasi = kod_dosya_sec(j)
                liste_cihaz_id_ve_kod_veri_dosyasi[c] = [] #eğer yanlış veri dosyası seçilirse tekrar seçme butonuna tıklanır ve liste index değerine göre temizlenir

                liste_cihaz_id_ve_kod_veri_dosyasi[c].append(j)
                liste_cihaz_id_ve_kod_veri_dosyasi[c].append(kod_dosyasi)
                durumscrollyenileme()

                print(liste_cihaz_id_ve_kod_veri_dosyasi,"sdadsavdv")#cihaz id ve seçilen dosyalar(dosyalar iç dizinde 1.indexin içinde tarat) listesi
                return liste_cihaz_id_ve_kod_veri_dosyasi#cihaz id ve seçilen dosyalar(dosyalar iç dizinde 1.indexin içinde tarat) listesi







            liste_cihaz_id_ve_giris_veri_dosyasi = []
            for i in range(len(self.cihaz_secme)):
                liste66 = []  # cihaz sayısı kadar iç liste oluşturulur ve iç listelere cihaz id si ile dosyalar eklenir
                liste_cihaz_id_ve_giris_veri_dosyasi.append(liste66)






            #giris verisidir python kodu değil
            def senkronizasyon_giris_veri_dosya(j, c):  # c = eklenecek olan verinin index numarası, j cihaz id si

                print(j)
                print(c)
                veri_dosyasi = veri_dosya_sec(j)
                liste_cihaz_id_ve_giris_veri_dosyasi[
                    c] = []  # eğer yanlış veri dosyası seçilirse tekrar seçme butonuna tıklanır ve liste index değerine göre temizlenir

                liste_cihaz_id_ve_giris_veri_dosyasi[c].append(j)
                liste_cihaz_id_ve_giris_veri_dosyasi[c].append(veri_dosyasi)

                print(liste_cihaz_id_ve_giris_veri_dosyasi)
                durumscrollyenileme()
                return liste_cihaz_id_ve_giris_veri_dosyasi#cihaz id ve seçilen dosyalar(dosyalar iç dizinde 1.indexin içinde tarat) listesi

            self.a = 0
            self.b = 1
            for i in range(self.cihaz_listesi_uzunlugu):

                #apk işlemleri butonları
                self.cihaz_isimleri = customtkinter.CTkLabel(self.apkscroll,text=self.cihaz_listesi[self.a],height=30,fg_color="green", width=310, corner_radius=8)
                self.cihaz_isimleri.grid(column=0,row=self.b, pady=2, padx=1)

                self.apk_buton1 = customtkinter.CTkButton(self.apkscroll, text="Select APK File", height=30, width=145,
                                         command=lambda j=self.cihaz_secme[self.a], b=self.a : threading.Thread(target=senkronizasyon_apk, args=(j, b),).start())
                self.apk_buton1.grid(column=1,row=self.b,pady=2, padx=1)


                self.apk_buton2 = customtkinter.CTkButton(self.apkscroll, text="Install APK File and Check the Installed APK File",height=30, width=370,
                                             command=lambda j=self.cihaz_listesi[self.a], c = self.a: threading.Thread(target=apk_kurma, args=(liste_cihaz_id_ve_apk_dosyasi[c]),).start())
                self.apk_buton2.grid(column=2, row=self.b,pady=2, padx=1)

                #self.apk_buton3 = customtkinter.CTkButton(self.apkscroll, text="APK Dosyasının Kurulumunu Kontrol Et",height=30, width=250,
                                             #command=lambda j=self.cihaz_listesi[self.a]: senkronizasyon_apk(j))
                #self.apk_buton3.grid(column=3, row=self.a, padx=2,pady=2)

                self.apk_buton4 = customtkinter.CTkButton(self.apkscroll, text="Remove Analysis App from Device",fg_color="red4",height=30, width=243,
                                             command=lambda j=self.cihaz_secme[self.a]: threading.Thread(target=analiz_uygulama_silme, args=(j,)).start())
                self.apk_buton4.grid(column=4, row=self.b,pady=2, padx=1)

                self.apk_buton5 = customtkinter.CTkButton(self.apkscroll, text="Remove Desired Apps from Device",fg_color="red4",height=30, width=255,
                                             command=lambda j=self.cihaz_secme[self.a]: threading.Thread(target=top_level, args=(j,)).start())
                self.apk_buton5.grid(column=5, row=self.b,pady=2, padx=1)

                #dosya işlemleri butonları





                self.cihaz_isimleri = customtkinter.CTkLabel(self.dosyascroll, text=self.cihaz_listesi[self.a], fg_color="green",
                                                        width=188, corner_radius=8)
                self.cihaz_isimleri.grid(column=0, row=self.b, pady=2)

                self.dosya_buton1 = customtkinter.CTkButton(self.dosyascroll, text="Select Code Folder",
                                                                width=20,
                                                                height=30, command=lambda j=self.cihaz_secme[self.a], c=self.a : threading.Thread(target=senkronizasyon_kod_veri_dosya, args=(j, c)).start())
                self.dosya_buton1.grid(row=self.b, column=2, pady=2)

                self.dosya_buton2 = customtkinter.CTkButton(self.dosyascroll, text="Send Code Folder", command=lambda j=self.cihaz_secme[self.a], c=self.a : threading.Thread(target=kod_dosyasi_yollama, args=(liste_cihaz_id_ve_kod_veri_dosyasi[c]),).start(),
                                                            width=30,
                                                            height=30)
                self.dosya_buton2.grid(row=self.b, column=3, pady=2)


                self.dosya_buton3 = customtkinter.CTkButton(self.dosyascroll, text="Select Data Folder", command=lambda j=self.cihaz_secme[self.a], c=self.a : threading.Thread(target=senkronizasyon_giris_veri_dosya, args=(j, c)).start(),
                                                            width=30,
                                                            height=30)
                self.dosya_buton3.grid(row=self.b, column=4, pady=2)

                self.dosya_buton3 = customtkinter.CTkButton(self.dosyascroll, text="Send Data Folder", command=lambda j=self.cihaz_secme[self.a], c=self.a : threading.Thread(target=veri_dosyasi_yollama, args=(liste_cihaz_id_ve_giris_veri_dosyasi[c]),).start(),
                                                            width=30,
                                                            height=30)
                self.dosya_buton3.grid(row=self.b, column=5, pady=2)

                def analiz_baslatma_ana(j, b):
                    print(b)

                    self.dosya_label4 = customtkinter.CTkLabel(self.dosyascroll, text="Start Analysis",
                                                                width=30,
                                                                height=30,corner_radius=8)

                    self.dosya_label4.grid(row=b, column=6, pady=2)
                    time.sleep(4)
                    self.dosya_label4.destroy()
                    analiz_baslatma(j)






                self.dosya_buton4 = customtkinter.CTkButton(self.dosyascroll, text="Start Analysis",
                                                            command=lambda j=self.cihaz_secme[self.a], b = self.b: threading.Thread(target=analiz_baslatma_ana, args=(j, b,)).start(),
                                                            width=30,
                                                            height=30)

                self.dosya_buton4.grid(row=self.b, column=6, pady=2)

                self.dosya_buton5 = customtkinter.CTkButton(self.dosyascroll, text="Get Output Data"
                                                            , command=lambda j=self.cihaz_secme[self.a]: threading.Thread(target=klasor_olusturma, args=(j,)).start(),
                                                            width=30,
                                                            height=30)
                self.dosya_buton5.grid(row=self.b, column=7, pady=2)

                self.dosya_buton4 = customtkinter.CTkButton(self.dosyascroll, text="Force Analysis to Stop",
                                                            fg_color="red4",
                                                            command=lambda j=self.cihaz_secme[self.a]: threading.Thread(target=analiz_durdur, args=(j,)).start(),
                                                            width=30,
                                                            height=30)
                self.dosya_buton4.grid(row=self.b, column=8, pady=2)

                self.dosya_buton6 = customtkinter.CTkButton(self.dosyascroll, text="Delete Codes from Device", fg_color="red4",
                                                            command=lambda j=self.cihaz_secme[self.a]: threading.Thread(target=kod_sil, args=(j,)).start(),
                                                            width=30,
                                                            height=30)
                self.dosya_buton6.grid(row=self.b, column=9, pady=2)

                self.dosya_buton6 = customtkinter.CTkButton(self.dosyascroll, text="Delete Input Data from Device",
                                                            fg_color="red4",
                                                            command=lambda j=self.cihaz_secme[self.a]: threading.Thread(target=veri_sil, args=(j,)).start(),
                                                            width=30,
                                                            height=30)
                self.dosya_buton6.grid(row=self.b, column=10, pady=2)
                self.b = self.b + 1



                self.a = self.a + 1


            durumscrollyenileme()

            self.serbest_alan = customtkinter.CTkScrollableFrame(self, width=1335, height=295, fg_color="grey")
            self.serbest_alan.grid(column=0, columnspan=6, row=6, pady=15)



            # girisi fonksiyon içereisine yaz

            def emir_gir():


                global satir2
                #a = os.popen("{}".format(self.giris.get())).read()
                os.popen("adb logcat -c")
                """bolmeli = a + (
                    "\n------------------------------------------------------------------------------------------"
                    "-------------------------------------------------------------------------------------------"
                    "-------------------------------------------------------------------------------------------")"""

                def logcat_calistir(cmd_girdi):
                    p = subprocess.Popen(cmd_girdi,
                                         stdout=subprocess.PIPE,
                                         stderr=subprocess.STDOUT)
                    return iter(p.stdout.readline, b'')

                cmd_girdi = ("{}".format(self.giris.get())).split()

                for satir in logcat_calistir(cmd_girdi):


                    satir2 = str(satir)


                    satir3 = satir2[2:]
                    satir4 = satir3[:-4]
                    bbb = wrap(satir4, 120)

                    for i in bbb:




                        self.label_komut_cikti = customtkinter.CTkLabel(self.kaydirilabilir_alan_komutlar2, text=i,
                                                                        font=("Arial", 11))
                        self.label_komut_cikti.pack()




            def toplevel_info(i):  # i = index sıfırdan başlar
                self.toplevel = customtkinter.CTkToplevel(self, width=400, height=200, fg_color="grey22")
                self.top_label = customtkinter.CTkLabel(self.toplevel, width=400, height=100, fg_color="grey22",
                                                        text=command_list[i][1])
                self.top_label.grid(row=0, column=0)
                self.toplevel.title("Platform: {}".format(command_list[i][0]))
                self.toplevel.attributes('-topmost', 'true')

            self.buton_label = customtkinter.CTkButton(self.serbest_alan, width=77, height=40, text="Run\nCommand",
                                                       command=lambda: threading.Thread(target=emir_gir).start())
            self.buton_label.grid(row=0, column=4, padx=2)

            self.giris = customtkinter.CTkEntry(self.serbest_alan, width=550, height=40, placeholder_text="Input Command")
            self.giris.bind("<Return>", (lambda event: threading.Thread(target=emir_gir).start()))
            self.giris.grid(row=0, column=0, columnspan=4)

            self.label_sahte = customtkinter.CTkScrollableFrame(self.serbest_alan,  width=605, height=50, fg_color="grey25"
                                                            )
            self.label_sahte.grid(row=2,column=0, columnspan=5,pady=5)







            def commands():
                self.kaydirilabilir_alan_komutlar = customtkinter.CTkScrollableFrame(self.serbest_alan, width=605, height=50,
                                                                                     fg_color="grey29")
                self.kaydirilabilir_alan_komutlar.grid(row=2, column=0, columnspan=5)
                for i in range(len(command_list)):
                    self.yazi = StringVar()
                    self.yazi.set(command_list[i][0])

                    self.textbox = customtkinter.CTkEntry(self.kaydirilabilir_alan_komutlar, height=30, width=560,
                                                          state="readonly", textvariable=self.yazi)
                    self.textbox.grid(row=i, column=0, pady=2)

                    self.textbutton = customtkinter.CTkButton(self.kaydirilabilir_alan_komutlar, height=30, width=30,
                                                              text="Info",
                                                              command=lambda komut_deger=i: threading.Thread(
                                                                  target=toplevel_info, args=(komut_deger,)).start())
                    self.textbutton.grid(row=i, column=1, padx=4)





            self.label_cihaz_isim = customtkinter.CTkButton(self.serbest_alan, width=630, height=30, fg_color="grey25",
                                                            corner_radius=5, text="Command List", command=lambda: threading.Thread(target=commands).start())
            self.label_cihaz_isim.grid(row=1, column=0, columnspan=5, pady=5)


            self.kaydirilabilir_alan_komutlar2 = customtkinter.CTkScrollableFrame(self.serbest_alan, width=665,
                                                                                  height=240, fg_color="grey29")
            self.kaydirilabilir_alan_komutlar2.grid(row=1, rowspan=4, column=7, padx=10)


            def yoket():
                self.kaydirilabilir_alan_komutlar2.destroy()
                self.kaydirilabilir_alan_komutlar2 = customtkinter.CTkScrollableFrame(self.serbest_alan, width=665,
                                                                                      height=240, fg_color="grey29")
                self.kaydirilabilir_alan_komutlar2.grid(row=1, rowspan=4, column=7, padx=10)
            # komut blokları

            self.label_cihaz_isim2 = customtkinter.CTkButton(self.serbest_alan, width=685, height=30, fg_color="grey25",
                                                             corner_radius=5, text="Clear Output", command=yoket)
            self.label_cihaz_isim2.grid(row=0, column=7, pady=5)


        except IndexError:
            pass



    def baglicihazlar(self):
        cihaz_listesi = baglicihazlar_adb()
        cihaz_sayisi = "Current Number of Connected Devices: {}".format(len(cihaz_listesi[0]))

        for i in range(len(cihaz_listesi[0])):
            self.label = customtkinter.CTkLabel(self.icscroll, text=cihaz_listesi[0][i])
            self.label.pack()

        self.label_cihaz_sayisi = customtkinter.CTkLabel(self.icscroll, text=cihaz_sayisi)
        self.label_cihaz_sayisi.pack()


        self.label_zaman = customtkinter.CTkLabel(self.icscroll, text=cihaz_listesi[1])
        self.label_zaman.pack()

        self.label_cizgi = customtkinter.CTkLabel(self.icscroll,
                                                  text="-----------------------------------------------------------------------------------"
                                                       "-----------------------------------------------------------------------------------"
                                                       "-----------------------------------------------------------------------------------")
        self.label_cizgi.pack()


# dış çerçeve(ana pencere)
class Uygulama(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        # dış kaydırılabilir ekran
        self.my_frame = kaydirilabiliaranaalan(master=self, width=1360, height=600)
        #self.my_frame.grid(row=0, column=0, sticky='e')
        self.my_frame.place(anchor = CENTER, relx = .5, rely = .50)

        def documentation():
            self.toplevel_creator2 = customtkinter.CTkToplevel(self, height=600, width=650)
            self.toplevel_creator2.title("Documentation")
            self.toplevel_creator2.attributes('-topmost', 'true')

            self.kaydirilabilirekran_documentation = customtkinter.CTkScrollableFrame(self.toplevel_creator2, height=600, width=650)
            self.kaydirilabilirekran_documentation.grid()

            self.label1 = customtkinter.CTkLabel(self.kaydirilabilirekran_documentation, width=645, height=120,fg_color="grey20",text="The goal of the project:                                                                                                                                       \n \nThe  purpose of this project is to convert old and unupdated Android devices (API level 16 and above)\ninto  threads  using   Python  .  Python   codes  are  run  on  devices  using  Chaquopy  and   the  APK  \nfile  is   ready-compiled. On   Android   devices,  Python   codes  are  run  with  the  Chaquopy  (details:\n https://chaquo.com/chaquopy/) tool. If you know Kotlin or Java, you can edit the android application\n according to your needs.                                                                                                                                        ")
            self.label1.grid()

            self.label2 = customtkinter.CTkLabel(self.kaydirilabilirekran_documentation, width=645, height=120,
                                                 fg_color="grey20",text="Platfom GUI:                                                                                                                                                           \n \nConnected Device Information:                                                                                                                           \n\nIt   shows  instantly   connected  android  devices  and  creates  a  log  in  txt  format   .  The log file is \nautomatically saved in the same location as the executable (exe) file.                                                         ")
            self.label2.grid()

            self.label3 = customtkinter.CTkLabel(self.kaydirilabilirekran_documentation, width=645, height=180,
                                                 fg_color="grey20",
                                                 text="Reflesh(Reset Selected Files):                                                                                                                              \nYou can update connected devices with this button. It should be noted that the selected files are reset\n every time you refresh. Please be careful.                                                                                                           \n\nIn  the first  window , you  can  install  the  APK  file  you  want , and  after  the APK  is  installed ,it  will\n automatically check  the installation. If you have installed the Platfom application on your  device, you\ncan delete it with the \"Remove Analysis App from Device\" button, or you can list and delete the desired\napplications with the \"Remove Desired Apps from Device\"  button. If  you have  too many applications\ninstalled on your device, scanning time may increase, please be patient.                                                     ")
            self.label3.grid()

            self.label4 = customtkinter.CTkLabel(self.kaydirilabilirekran_documentation, width=645, height=250,
                                                 fg_color="grey20",
                                                 text="In the second window (if you are using the analysis application), you must select the code folder and\nthe  input data folder and  send them . If the application  is not installed  on your Android  device, you\ncannot  select a  folder  and send  it . The  selected  folders  are  placed in the  Input  folder  using the\n \"/sdcard /Android /data/ com.example.platform_min_50 (or 41) /files /Input/\"  path  directory  of  the\nanalysis application. Home folders are divided into two: Data and Code folders. You cannot integrate\n ready-made packages into the application (if you have installed the ready-made analysis APK file), so\nplace the packages  you will  use in the  analysis in  the Code  folder and use the  sample hierarchical\n structure (available in the downloaded files). Please install only one analysis application according to\nthe API level of the devices. If you install both analysis applications (41 and 50)  on the same device, \nit will  only  launch  Platform_min_4.1 application ( prioritizing Platform_min_4.1 application ) . While \nthe analysis is in progress, you can stop the application and analysis. After the analysis is completed,\nyou  can  save  the  output  data ( from \"/ sdcard /Android/ data /com.example.platform_min_50   (or \n 41 ) /files /Output /\") to the desired location  on your  computer. After getting the data, don't forget to\n delete the data on your android device.                                                                                                               ")
            self.label4.grid()

            self.label5 = customtkinter.CTkLabel(self.kaydirilabilirekran_documentation, width=645, height=100,
                                                 fg_color="grey20",
                                                 text="Note :  Platform_min_41 application  supports python  version 3.8  and the minimum  API level is  16.\nPlatform_min_50  application  supports  python  version  3.11 and  the minimum  API level is 21.  For\n detailed information, see the sites \"https://chaquo.com/chaquopy/\" and \"https://apilevels.com/\".       ")
            self.label5.grid()

            self.label6 = customtkinter.CTkLabel(self.kaydirilabilirekran_documentation, width=645, height=100,
                                                 fg_color="grey20",
                                                 text="In  the  third  window , the  ADB  command  list  (most of all commands)  and  their  explanations  are \navailable. You can enter the command you want in this window.If you use commands that constantly\nwait  for input , such as Logcat , you may need  to terminate the ADB server (or restart the program) to\nfinalize the output.                                                                                                                                                  ")
            self.label6.grid()

            self.label6 = customtkinter.CTkLabel(self.kaydirilabilirekran_documentation, width=645, height=60,
                                                 fg_color="grey20",
                                                 text="The  fourth window  contains  general  information  about the  connected  devices. You  can check  the\nfiles you selected from this window.                                                                                                                     ")
            self.label6.grid()

            self.label6 = customtkinter.CTkLabel(self.kaydirilabilirekran_documentation, width=645, height=120,
                                                 fg_color="grey20",
                                                 text="While  the program  is running , freezes may  occur due to  customTkinter . Please let  me know  if  any\n function does not work or malfunctions.                                                                                                               \n\n\nMolecular Biologist\nZafer AKAR")
            self.label6.grid()



        self.buttonn = customtkinter.CTkButton(self, height=30, width=30, text="Documentation",fg_color="green", corner_radius=2, command=documentation)
        self.buttonn.grid(row=0, column=0)

        def about():
            self.toplevel_creator = customtkinter.CTkToplevel(self, height=200, width=140)
            self.toplevel_creator.title("About the Creator")
            self.toplevel_creator.attributes('-topmost', 'true')

            self.label_about = customtkinter.CTkLabel(self.toplevel_creator, width=650, height=140 ,text="I am a Master's student at Yıldız Technical University, Department of Molecular Biology and Genetics.\n I code tools in the fields of computational biology, bioinformatics and data science. In this project, unused \nAndroid devices were converted into data processing tools with Python. And also if you are android application\n developer, you can use this project as ADB GUI. Please contact me if you have any questions. \nI would also like to thank Control and Automation Engineer Murat ATAY for his support and help.\n\n   Molecular Biologist\nZafer AKAR")
            self.label_about.grid(row=0, column=0)


        self.buttonn1 = customtkinter.CTkButton(self, height=30, width=30, text="About the Creator", command=about, corner_radius=2)
        self.buttonn1.grid(row=0, column=1)

        def toplevvel_bug():
            self.web_side = StringVar()
            self.web_side.set("                                                      https://github.com/Zaferakar")
            self.toplevel_bug = customtkinter.CTkToplevel(self, height=200, width=100)
            self.toplevel_bug.title("Report Bugs")
            self.toplevel_bug.attributes('-topmost', 'true')
            self.textbox_bug = customtkinter.CTkEntry(self.toplevel_bug, height=38, width=520,
                                                  state="readonly", textvariable=self.web_side)
            self.textbox_bug.grid(row=1, column=0, padx=4, pady=4)

            def website():
                webbrowser.open_new_tab("https://github.com/Zaferakar")
                self.toplevel_bug.destroy()
            self.buton_link = customtkinter.CTkButton(self.toplevel_bug, width=30, height=30, text="Redirect \nto GitHub",fg_color="green", command=website)
            self.buton_link.grid(row=1, column=1, padx=4, pady=4)
            self.info_label = customtkinter.CTkLabel(self.toplevel_bug, height=60, width=200, text="If you notice commands not working, any bugs, hangs, \nfreezes or incorrect commands in the program, please let me know.")
            self.info_label.grid(row=0, column=0)





        self.buttonn2 = customtkinter.CTkButton(self, height=30, width=30, text="Report Bugs",fg_color="red4", command=toplevvel_bug, corner_radius=2)
        self.buttonn2.grid(row=0, column=2)
        self.title("Platform")
        self.geometry("1380x600+0+0")#sol üst 0,0 kordinatında ana pencere açılacak
        #self.wm_attributes('-toolwindow', 'True')





        self.f = (os.path.dirname(__file__) + "\icons\icon-512.png")
        self.iconpath = ImageTk.PhotoImage(file=self.f)
        self.wm_iconbitmap()

        self.iconphoto(False, self.iconpath)









app = Uygulama()

app.mainloop()
