from PySide6.QtWidgets import QMainWindow, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QToolBar, QLineEdit, QSizePolicy, QComboBox, QMenu, QMessageBox, QStatusBar, QScrollArea
from PySide6.QtCore import Qt, QSize, QRegularExpression
from PySide6.QtGui import QPixmap, QAction, QIcon, QFont, QImage, QGuiApplication, QPalette
import numpy as np
import re
import os



class MainWindow(QMainWindow):

    def __init__(self, app) -> None:
        super().__init__()

        self.app = app
        self.setWindowTitle("Geometry Calculator")
        # self.setFixedSize(800,600)
        self.setMinimumSize(800,600)
     

        base_path = os.path.abspath(os.path.dirname(__file__))
        image_path = os.path.join(base_path, 'img_project', 'geometry.ico')


        # self.setWindowIcon(QIcon("D:/Data_C2/Users/Documents/Tutorial_Python/pyside6/projek/img_project/geometry.ico"))
        self.setWindowIcon(QIcon(image_path))
        
        
        
        
        #TODO : Add menuBar
        # menu_bar = self.menuBar()
        # File_menu = menu_bar.addMenu("Edit")
        # copy = File_menu.addAction("Copy")
      

        menu_bar = self.menuBar()

        # file_menu = menu_bar.addMenu("Quit")
        menu_quit_action = menu_bar.addAction("Quit")
        menu_quit_action.triggered.connect(self.quit_app)

        menu_copyrigth = menu_bar.addAction("Copyrigth")
        menu_copyrigth.triggered.connect(self.copyright_app)

        menu_help = menu_bar.addAction("Help")
        menu_help.triggered.connect(self.help_menu)
        

        # self.combo_box_2_D = QComboBox()
        # self.combo_box_2_D.addItem("km")
        # self.combo_box_2_D.addItem("hm")
        # self.combo_box_2_D.addItem("dam")
        # self.combo_box_2_D.addItem("m")
        # self.combo_box_2_D.addItem("dm")
        # self.combo_box_2_D.addItem("cm")
        # self.combo_box_2_D.addItem("mm")
        # self.combo_box_2_D.setCurrentIndex(5)


        #SetStatusTip
        self.label_tip_2 = "Mencari Luas dan Keliling"
        self.label_tip_3 = "Mencari Volume dan Luas Permukaan"
        self.label_tip_shortcut = "\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tShortcut :"

        # Adding toolbar in left side
        toolbar = QToolBar("My Main Toolbar")
        toolbar.setIconSize(QSize(35,35))
        self.addToolBar(Qt.LeftToolBarArea, toolbar) # SETTING SUPAYA TOOLBAR DI SEBELAH KIRI

        


        # persegi = QAction(QIcon("D:/Data_C2/Users/Documents/Tutorial_Python/pyside6/projek/img_project/icon_persegi.png"), "Persegi", self)

        base_path = os.path.abspath(os.path.dirname(__file__))
        image_path = os.path.join(base_path, 'img_project', 'icon_persegi.png')

        persegi = QAction(QIcon(image_path), "Persegi", self)

        persegi.setShortcut("Ctrl+1")
        persegi.triggered.connect(self.toolbar_persegi)
        persegi.setStatusTip(f"{self.label_tip_2} Persegi {self.label_tip_shortcut} Ctrl + 1")
        toolbar.addAction(persegi)

        
        # persegi_panjang = QAction(QIcon("D:/Data_C2/Users/Documents/Tutorial_Python/pyside6/projek/img_project/icon_persegi_panjang.png"), "Persegi Panjang", self)
        base_path = os.path.abspath(os.path.dirname(__file__))
        image_path = os.path.join(base_path, 'img_project', 'icon_persegi_panjang.png')
        persegi_panjang = QAction(QIcon(image_path), "Persegi Panjang", self)
        persegi_panjang.setShortcut("Ctrl+2")
        persegi_panjang.triggered.connect(self.toolbar_persegi_panjang)
        persegi_panjang.setStatusTip(f"{self.label_tip_2} Persegi Panjang {self.label_tip_shortcut} Ctrl + 2")
        toolbar.addAction(persegi_panjang)

        
        # lingkaran = QAction(QIcon("D:/Data_C2/Users/Documents/Tutorial_Python/pyside6/projek/img_project/icon_lingkaran.png"), "Lingkaran", self)
        base_path = os.path.abspath(os.path.dirname(__file__))
        image_path = os.path.join(base_path, 'img_project', 'icon_lingkaran.png')
        lingkaran = QAction(QIcon(image_path), "Lingkaran", self)
        lingkaran.setShortcut("Ctrl+3")
        lingkaran.triggered.connect(self.toolbar_lingkaran)
        lingkaran.setStatusTip(f"{self.label_tip_2} Lingkaran {self.label_tip_shortcut} Ctrl + 3")
        toolbar.addAction(lingkaran)
        


        # layang_layang = QAction(QIcon("D:/Data_C2/Users/Documents/Tutorial_Python/pyside6/projek/img_project/kite2.png"), "Layang - Layang", self)
        base_path = os.path.abspath(os.path.dirname(__file__))
        image_path = os.path.join(base_path, 'img_project', 'kite2.png')
        layang_layang = QAction(QIcon(image_path), "Layang - Layang", self)
        layang_layang.setShortcut("Ctrl+4")
        layang_layang.triggered.connect(self.toolbar_layang_layang)
        layang_layang.setStatusTip(f"{self.label_tip_2} Layang - Layang {self.label_tip_shortcut} Ctrl + 4")
        toolbar.addAction(layang_layang)

        
        # segitiga = QAction(QIcon("D:/Data_C2/Users/Documents/Tutorial_Python/pyside6/projek/img_project/segitiga.png"), "Segitiga", self)
        base_path = os.path.abspath(os.path.dirname(__file__))
        image_path = os.path.join(base_path, 'img_project', 'segitiga.png')
        segitiga = QAction(QIcon(image_path), "Segitiga", self)
        segitiga.setShortcut("Ctrl+5")
        segitiga.triggered.connect(self.toolbar_segitiga)
        segitiga.setStatusTip(f"{self.label_tip_2} Segitiga {self.label_tip_shortcut} Ctrl + 5")
        toolbar.addAction(segitiga)


        # belah_ketupat = QAction(QIcon("D:/Data_C2/Users/Documents/Tutorial_Python/pyside6/projek/img_project/belah_ketupat.png"), "Belah Ketupat", self)
        base_path = os.path.abspath(os.path.dirname(__file__))
        image_path = os.path.join(base_path, 'img_project', 'belah_ketupat.png')
        belah_ketupat = QAction(QIcon(image_path), "Belah Ketupat", self)
        belah_ketupat.setShortcut("Ctrl+6")
        belah_ketupat.triggered.connect(self.toolbar_belah_ketupat)
        belah_ketupat.setStatusTip(f"{self.label_tip_2} Belah Ketupat {self.label_tip_shortcut} Ctrl + 6")
        toolbar.addAction(belah_ketupat)

        # trapesium = QAction(QIcon("D:/Data_C2/Users/Documents/Tutorial_Python/pyside6/projek/img_project/trapesium.png"), "Trapesium", self)
        base_path = os.path.abspath(os.path.dirname(__file__))
        image_path = os.path.join(base_path, 'img_project', 'trapesium.png')
        trapesium = QAction(QIcon(image_path), "Trapesium", self)
        # trapesium.setShortcut("Ctrl+7")
        # trapesium.setShortcut("Ctrl+8")
        trapesium.setStatusTip(f"{self.label_tip_2} Trapesium {self.label_tip_shortcut} Ctrl + 7 | Ctrl + 8")
        trapesium.setMenu(self.createTrapesiumMenu())
        toolbar.addAction(trapesium)

        # jajar_genjang = QAction(QIcon("D:/Data_C2/Users/Documents/Tutorial_Python/pyside6/projek/img_project/jajar_genjang.png"), "Jajar Genjang", self)
        base_path = os.path.abspath(os.path.dirname(__file__))
        image_path = os.path.join(base_path, 'img_project', 'jajar_genjang.png')
        jajar_genjang = QAction(QIcon(image_path), "Jajar Genjang", self)
        jajar_genjang.setShortcut("Ctrl+9")
        jajar_genjang.triggered.connect(self.toolbar_jajar_genjang)
        jajar_genjang.setStatusTip(f"{self.label_tip_2} Jajar Genjang {self.label_tip_shortcut} Ctrl + 9")
        toolbar.addAction(jajar_genjang)


        # kubus = QAction(QIcon("D:/Data_C2/Users/Documents/Tutorial_Python/pyside6/projek/img_project/kubus.png"), "Kubus", self)
        base_path = os.path.abspath(os.path.dirname(__file__))
        image_path = os.path.join(base_path, 'img_project', 'kubus.png')
        kubus = QAction(QIcon(image_path), "Kubus", self)
        kubus.setStatusTip(f"{self.label_tip_3} Kubus {self.label_tip_shortcut} Ctrl + Shift + 1")
        kubus.setShortcut("Ctrl+Shift+1")
        kubus.triggered.connect(self.toolbar_kubus)
        toolbar.addAction(kubus)

        # balok = QAction(QIcon("D:/Data_C2/Users/Documents/Tutorial_Python/pyside6/projek/img_project/balok.png"), "Balok", self)
        base_path = os.path.abspath(os.path.dirname(__file__))
        image_path = os.path.join(base_path, 'img_project', 'balok.png')
        balok = QAction(QIcon(image_path), "Balok", self)
        balok.setStatusTip(f"{self.label_tip_3} Balok {self.label_tip_shortcut} Ctrl + Shift + 2")
        balok.setShortcut("Ctrl+Shift+2")
        balok.triggered.connect(self.toolbar_balok)
        toolbar.addAction(balok)


        # tabung = QAction(QIcon("D:/Data_C2/Users/Documents/Tutorial_Python/pyside6/projek/img_project/tabung.png"), "Tabung", self)
        base_path = os.path.abspath(os.path.dirname(__file__))
        image_path = os.path.join(base_path, 'img_project', 'tabung.png')
        tabung = QAction(QIcon(image_path), "Tabung", self)
        tabung.setStatusTip(f"{self.label_tip_3} Tabung {self.label_tip_shortcut} Ctrl + Shift + 3")
        tabung.setShortcut("Ctrl+Shift+3")
        tabung.triggered.connect(self.toolbar_tabung)
        toolbar.addAction(tabung)

        # bola = QAction(QIcon("D:/Data_C2/Users/Documents/Tutorial_Python/pyside6/projek/img_project/bola.png"), "Bola", self)
        base_path = os.path.abspath(os.path.dirname(__file__))
        image_path = os.path.join(base_path, 'img_project', 'bola.png')
        bola = QAction(QIcon(image_path), "Bola", self)
        bola.setStatusTip(f"{self.label_tip_3} Bola {self.label_tip_shortcut} Ctrl + Shift + 4")
        bola.setShortcut("Ctrl+Shift+4")
        bola.triggered.connect(self.toolbar_bola)
        toolbar.addAction(bola)


        # prisma = QAction(QIcon("D:/Data_C2/Users/Documents/Tutorial_Python/pyside6/projek/img_project/prisma.png"), "Prisma", self)
        base_path = os.path.abspath(os.path.dirname(__file__))
        image_path = os.path.join(base_path, 'img_project', 'prisma.png')
        prisma = QAction(QIcon(image_path), "Prisma", self)
        prisma.setStatusTip(f"{self.label_tip_3} Prisma {self.label_tip_shortcut} Ctrl + Shift + 5 | Ctrl + Shift + 6 | Ctrl + Shift + 7 | Ctrl + Shift + 8")
        # prisma.setShortcut("Ctrl+Shift+5")
        # prisma.setShortcut("Ctrl+Shift+6")
        # prisma.setShortcut("Ctrl+Shift+7")
        # prisma.setShortcut("Ctrl+Shift+8")
        prisma.setMenu(self.createPrismaMenu())
        toolbar.addAction(prisma)

        

        self.my_font = QFont("Times", 20, QFont.Bold)
        self.label_font = QFont("Times", 15, QFont.DemiBold, True)
        self.answer_font = QFont("Times", 10, QFont.Black)
       

        self.color_answer_font = "color : red"
        self.color_rumus_font = "color : blue"
        # self.my_font.setPointSize(20)
        # self.my_font.


        self.setStatusBar(QStatusBar(self))



    def createTrapesiumMenu(self):
        trapesium_menu = QMenu(self)

        # trapesium_sama_kaki = QAction(QIcon("D:/Data_C2/Users/Documents/Tutorial_Python/pyside6/projek/img_project/trapesium.png"),'Trapesium Sama Kaki', self)
        base_path = os.path.abspath(os.path.dirname(__file__))
        image_path = os.path.join(base_path, 'img_project', 'trapesium.png')
        trapesium_sama_kaki = QAction(QIcon(image_path),'Trapesium Sama Kaki', self)
        trapesium_sama_kaki.setStatusTip(f"{self.label_tip_2} Trapesium Sama Kaki {self.label_tip_shortcut} Ctrl + 7")
        trapesium_sama_kaki.setShortcut("Ctrl+7")
        trapesium_sama_kaki.triggered.connect(self.toolbar_trapesium_sama_kaki)
        trapesium_menu.addAction(trapesium_sama_kaki)

        # trapesium_siku_siku = QAction(QIcon("D:/Data_C2/Users/Documents/Tutorial_Python/pyside6/projek/img_project/trapesium_1.png"),'Trapesium Siku - Siku', self)
        base_path = os.path.abspath(os.path.dirname(__file__))
        image_path = os.path.join(base_path, 'img_project', 'trapesium_1.png')
        trapesium_siku_siku = QAction(QIcon(image_path),'Trapesium Siku - Siku', self)
        trapesium_siku_siku.setStatusTip(f"{self.label_tip_2} Trapesium Siku - Siku {self.label_tip_shortcut} Ctrl + 8")
        trapesium_siku_siku.setShortcut("Ctrl+8")
        trapesium_siku_siku.triggered.connect(self.toolbar_trapesium_siku_siku)
        trapesium_menu.addAction(trapesium_siku_siku)

        return trapesium_menu


    def createPrismaMenu(self):
        Prisma_menu = QMenu(self)

        # prisma_segitiga = QAction(QIcon("D:/Data_C2/Users/Documents/Tutorial_Python/pyside6/projek/img_project/prisma_3.png"), "Prisma Segitiga", self)
        base_path = os.path.abspath(os.path.dirname(__file__))
        image_path = os.path.join(base_path, 'img_project', 'prisma_3.png')
        prisma_segitiga = QAction(QIcon(image_path), "Prisma Segitiga", self)
        prisma_segitiga.setStatusTip(f"{self.label_tip_3} Prisma Segitiga {self.label_tip_shortcut} Ctrl + Shift + 5")
        prisma_segitiga.setShortcut("Ctrl+Shift+5")
        prisma_segitiga.triggered.connect(self.toolbar_prisma_segitiga)
        Prisma_menu.addAction(prisma_segitiga)

        # prisma_segilima = QAction(QIcon("D:/Data_C2/Users/Documents/Tutorial_Python/pyside6/projek/img_project/prisma_segilima_10.png"), "Prisma Segilima", self)
        base_path = os.path.abspath(os.path.dirname(__file__))
        image_path = os.path.join(base_path, 'img_project', 'prisma_segilima_10.png')
        prisma_segilima = QAction(QIcon(image_path), "Prisma Segilima", self)
        prisma_segilima.setStatusTip(f"{self.label_tip_3} Prisma Segilima {self.label_tip_shortcut} Ctrl + Shift + 6")
        prisma_segilima.setShortcut("Ctrl+Shift+6")
        prisma_segilima.triggered.connect(self.toolbar_prisma_segilima)
        Prisma_menu.addAction(prisma_segilima)


        # prisma_segienam = QAction(QIcon("D:/Data_C2/Users/Documents/Tutorial_Python/pyside6/projek/img_project/prisma_segilima_3.png"), "Prisma Segienam", self)
        base_path = os.path.abspath(os.path.dirname(__file__))
        image_path = os.path.join(base_path, 'img_project', 'prisma_segilima_3.png')
        prisma_segienam = QAction(QIcon(image_path), "Prisma Segienam", self)
        prisma_segienam.setStatusTip(f"{self.label_tip_3} Prisma Segienam {self.label_tip_shortcut} Ctrl + Shift + 7")
        prisma_segienam.setShortcut("Ctrl+Shift+7")
        prisma_segienam.triggered.connect(self.toolbar_prisma_segienam)
        Prisma_menu.addAction(prisma_segienam)

        # prisma_segidelapan = QAction(QIcon("D:/Data_C2/Users/Documents/Tutorial_Python/pyside6/projek/img_project/prisma_segidelapan.jpg"), "Prisma Segidelapan", self)
        base_path = os.path.abspath(os.path.dirname(__file__))
        image_path = os.path.join(base_path, 'img_project', 'prisma_segidelapan.jpg')
        prisma_segidelapan = QAction(QIcon(image_path), "Prisma Segidelapan", self)
        prisma_segidelapan.setStatusTip(f"{self.label_tip_3} Prisma Segidelapan {self.label_tip_shortcut} Ctrl + Shift + 8")
        prisma_segidelapan.setShortcut("Ctrl+Shift+8")
        prisma_segidelapan.triggered.connect(self.toolbar_prisma_segidelapan)
        Prisma_menu.addAction(prisma_segidelapan)

        return Prisma_menu

    
    

    def toolbar_persegi(self):
        qwidget = QWidget()
    
        text_s = QLabel("panjang s :")
        self.input_s = QLineEdit()

        # text_s.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.MinimumExpanding)
        # self.input_s.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)

        self.combo_box_2_D_persegi = QComboBox()
        self.combo_box_2_D_persegi.addItem("km")
        self.combo_box_2_D_persegi.addItem("hm")
        self.combo_box_2_D_persegi.addItem("dam")
        self.combo_box_2_D_persegi.addItem("m")
        self.combo_box_2_D_persegi.addItem("dm")
        self.combo_box_2_D_persegi.addItem("cm")
        self.combo_box_2_D_persegi.addItem("mm")
        self.combo_box_2_D_persegi.setCurrentIndex(5)
        
        self.layout_combo_box = QVBoxLayout()
        self.layout_combo_box.addWidget(self.combo_box_2_D_persegi)

        layout_1_h_s = QHBoxLayout()
        layout_1_h_s.addWidget(text_s)
        layout_1_h_s.addWidget(self.input_s)
        layout_1_h_s.addLayout(self.layout_combo_box)

        self.button_submit = QPushButton("Submit")
        self.button_submit.setStyleSheet("""
            QPushButton {
                background-color: blue;
                border-radius: 10px;
                padding: 10px;
                color: white;
            }

            QPushButton:hover {
                background-color: lightgreen;
                color: black
            }
        """)
        self.button_submit.setShortcut(Qt.Key_Return)
        self.button_submit.clicked.connect(self.persegi)
        

        
        self.text_param_persegi = QLabel("Persegi")
        self.text_param_persegi.setAlignment(Qt.AlignHCenter)
        self.text_param_persegi.setFont(self.my_font)
        self.text_param_persegi.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        

        label = QLabel() 
        # label.setPixmap(QPixmap("D:/Data_C2/Users/Documents/Tutorial_Python/pyside6/projek/img_project/label_persegi.png"))
        base_path = os.path.abspath(os.path.dirname(__file__))
        image_path = os.path.join(base_path, 'img_project', 'label_persegi.png')

        label.setPixmap(QPixmap(image_path))
        
        label.setAlignment(Qt.AlignCenter)
        label.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)
        
        layout_2_v_s = QVBoxLayout()
        layout_2_v_s.addWidget(self.text_param_persegi)
        layout_2_v_s.addWidget(label)
        layout_2_v_s.addLayout(layout_1_h_s)
        layout_2_v_s.addWidget(self.button_submit)

        # Create a new QVBoxLayout for the answer label
        self.layout_v_answer_s = QVBoxLayout()
        layout_2_v_s.addLayout(self.layout_v_answer_s)

        qwidget.setLayout(layout_2_v_s)
        

        self.setCentralWidget(qwidget)
        # self.centralWidget().setStyleSheet("background-color: rgb(255, 235, 138)")
        # self.centralWidget().setStyleSheet("background-color: #00ff00")
        

    def persegi(self):
        try:
            if self.input_s.text() == "":
                s = 0
            else:
                s = float(self.input_s.text().replace(",","."))



            self.luas_persegi = float(s**2)
            self.keliling_persegi = float(4*s)

            def check_is_int_luas() -> str:
                if self.luas_persegi.is_integer():
                    self.luas_persegi = int(self.luas_persegi)
                    return f"{str(self.luas_persegi)}"
                else:
                    a = f"{self.luas_persegi:.2f}".replace('.',',')
                    return str(a)
                
            def check_is_int_kel() -> str:
                if self.keliling_persegi.is_integer():
                    self.keliling_persegi = int(self.keliling_persegi)
                    return f"{str(self.keliling_persegi)}"
                else:
                    a = f"{self.keliling_persegi:.2f}".replace('.',',')
                    return str(a)
             
                


            #### Rumus ##
            rumus_luas_persegi = QLabel(" L = s x s")
            rumus_luas_persegi.setFont(self.label_font)
            rumus_luas_persegi.setStyleSheet(self.color_rumus_font)

            rumus_keliling_persegi = QLabel("K = 4 x s")
            rumus_keliling_persegi.setFont(self.label_font)
            rumus_keliling_persegi.setStyleSheet(self.color_rumus_font)
            ###################################

            #### Label Luas dan Kelling
            self.answer_label_2 = QLabel("Luas Persegi : ")
            self.answer_label_2.setFont(self.label_font)

            self.answer_label_3 = QLabel("Keliling Persegi : ")
            self.answer_label_3.setFont(self.label_font)
            ################################################

            ########## Answer ####
            # self.jawab = QLabel(f"{str(luas)} {self.combo_box_2_D_persegi.currentText()}²")
            self.jawab = QLabel(f"{check_is_int_luas()} {self.combo_box_2_D_persegi.currentText()}²")
            self.jawab.setFont(self.answer_font)
            self.jawab.setStyleSheet(self.color_answer_font)

            # self.jawab_2 = QLabel(f"{str(keliling)} {self.combo_box_2_D_persegi.currentText()}")
            self.jawab_2 = QLabel(f"{check_is_int_kel()} {self.combo_box_2_D_persegi.currentText()}")
            self.jawab_2.setFont(self.answer_font)
            self.jawab_2.setStyleSheet(self.color_answer_font)
            

            while self.layout_v_answer_s.count():
                item = self.layout_v_answer_s.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.setParent(None)

            # Add the answer label to the new layout_v_answer_s

            hbox_layout1 = QHBoxLayout()
            hbox_layout1.addWidget(self.answer_label_2)
            hbox_layout1.addWidget(rumus_luas_persegi)

            hbox_layout2 = QHBoxLayout()
            hbox_layout2.addWidget(self.answer_label_3)
            hbox_layout2.addWidget(rumus_keliling_persegi)


            self.layout_v_answer_s.addLayout(hbox_layout1)
            self.layout_v_answer_s.addWidget(self.jawab)
            self.layout_v_answer_s.addLayout(hbox_layout2)
            self.layout_v_answer_s.addWidget(self.jawab_2)


            # self.layout_v_answer_s.addWidget(self.answer_label_2)
            # self.layout_v_answer_s.addWidget(self.jawab)
            # self.layout_v_answer_s.addWidget(self.answer_label_3)
            # self.layout_v_answer_s.addWidget(self.jawab_2)


        except ValueError:
            self.error_input()


        

        


    def toolbar_persegi_panjang(self):
        qwidget = QWidget()

        text_r_p = QLabel("Masukkan panjang\t:")
        text_r_l = QLabel("Masukkan lebar\t\t:")
        self.input_r_p = QLineEdit()
        self.input_r_l = QLineEdit()

        text_r_p.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        text_r_l.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.input_r_p.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.input_r_l.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)


        self.combo_box_2_D_persegi_panjang = QComboBox()
        self.combo_box_2_D_persegi_panjang.addItem("km")
        self.combo_box_2_D_persegi_panjang.addItem("hm")
        self.combo_box_2_D_persegi_panjang.addItem("dam")
        self.combo_box_2_D_persegi_panjang.addItem("m")
        self.combo_box_2_D_persegi_panjang.addItem("dm")
        self.combo_box_2_D_persegi_panjang.addItem("cm")
        self.combo_box_2_D_persegi_panjang.addItem("mm")
        self.combo_box_2_D_persegi_panjang.setCurrentIndex(5)

        self.layout_combo_box = QVBoxLayout()
        self.layout_combo_box.addWidget(self.combo_box_2_D_persegi_panjang)

        layout_1_h_r = QHBoxLayout()
        layout_1_h_r.addWidget(text_r_p)
        layout_1_h_r.addWidget(self.input_r_p)

        layout_2_h_r = QHBoxLayout()
        layout_2_h_r.addWidget(text_r_l)
        layout_2_h_r.addWidget(self.input_r_l)

        self.button_submit = QPushButton("Submit")
        self.button_submit.setStyleSheet("""
            QPushButton {
                background-color: blue;
                border-radius: 10px;
                padding: 10px;
                color: white;
            }

            QPushButton:hover {
                background-color: lightgreen;
                color: black
            }
        """)
        self.button_submit.setShortcut(Qt.Key_Return)
        self.button_submit.clicked.connect(self.persegi_panjang)

        layout_3_h_r = QHBoxLayout()
        label_satuan = QLabel("Satuan")
        layout_3_h_r.addWidget(label_satuan)
        layout_3_h_r.addLayout(self.layout_combo_box)

        self.text_param_persegi_panjang = QLabel("Persegi Panjang")
        self.text_param_persegi_panjang.setAlignment(Qt.AlignHCenter)
        self.text_param_persegi_panjang.setFont(self.my_font)
        self.text_param_persegi_panjang.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)

        label = QLabel() 
        # label.setPixmap(QPixmap("D:/Data_C2/Users/Documents/Tutorial_Python/pyside6/projek/img_project/label_rectangle.jpg"))
        base_path = os.path.abspath(os.path.dirname(__file__))
        image_path = os.path.join(base_path, 'img_project', 'label_rectangle.jpg')
        label.setPixmap(QPixmap(image_path))
        label.setAlignment(Qt.AlignCenter)
        label.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        layout_3_v_r = QVBoxLayout()
        layout_3_v_r.addWidget(self.text_param_persegi_panjang)
        layout_3_v_r.addWidget(label)
        layout_3_v_r.addLayout(layout_1_h_r)
        layout_3_v_r.addLayout(layout_2_h_r)
        layout_3_v_r.addLayout(layout_3_h_r)
        layout_3_v_r.addWidget(self.button_submit)

        # Create a new QVBoxLayout for the answer label
        self.layout_v_answer_r = QVBoxLayout()
        layout_3_v_r.addLayout(self.layout_v_answer_r)

        qwidget.setLayout(layout_3_v_r)

        self.setCentralWidget(qwidget)
        # self.centralWidget().setStyleSheet("background-color:  #FF0000")



    def persegi_panjang(self):
        try:
            if self.input_r_p.text() == "" or self.input_r_l.text() == "":
                p = 0
                l = 0
            else:
                p = float(self.input_r_p.text().replace(",","."))
                l = float(self.input_r_l.text().replace(",","."))

        



            self.luas_persegi_panjang = float(p*l)
            self.keliling_persegi_panjang = float(2*(p+l))

            def check_is_int_luas() -> str:
                if self.luas_persegi_panjang.is_integer():
                    self.luas_persegi_panjang = int(self.luas_persegi_panjang)
                    return f"{str(self.luas_persegi_panjang)}"
                else:
                    a = f"{self.luas_persegi_panjang:.2f}".replace('.',',')
                    return str(a)
                
            def check_is_int_kel() -> str:
                if self.keliling_persegi_panjang.is_integer():
                    self.keliling_persegi_panjang = int(self.keliling_persegi_panjang)
                    return f"{str(self.keliling_persegi_panjang)}"
                else:
                    a = f"{self.keliling_persegi_panjang:.2f}".replace('.',',')
                    return str(a)
                
            rumus_luas_persegiPanjang = QLabel("L = p x l")
            rumus_luas_persegiPanjang.setFont(self.label_font)
            rumus_luas_persegiPanjang.setStyleSheet(self.color_rumus_font)

            rumus_kel_persegiPanjang = QLabel("K = 2(p + l)")
            rumus_kel_persegiPanjang.setFont(self.label_font)
            rumus_kel_persegiPanjang.setStyleSheet(self.color_rumus_font)

            self.answer_label_luas_rect = QLabel("Luas Persegi Panjang : ")
            self.answer_label_luas_rect.setFont(self.label_font)
            
            self.answer_label_kel_rect = QLabel("Keliling Persegi Panjang : ")
            self.answer_label_kel_rect.setFont(self.label_font)


            self.jawab_luas_rect = QLabel(f"{check_is_int_luas()} {self.combo_box_2_D_persegi_panjang.currentText()}²")
            self.jawab_luas_rect.setFont(self.answer_font)
            self.jawab_luas_rect.setStyleSheet(self.color_answer_font)

            self.jawab_kel_rect = QLabel(f"{check_is_int_kel()} {self.combo_box_2_D_persegi_panjang.currentText()}")
            self.jawab_kel_rect.setFont(self.answer_font)
            self.jawab_kel_rect.setStyleSheet(self.color_answer_font)

            while self.layout_v_answer_r.count():
                item = self.layout_v_answer_r.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.setParent(None)

            # Add the answer label to the new layout_v_answer_r
        
            hbox_layout1 = QHBoxLayout()
            hbox_layout1.addWidget(self.answer_label_luas_rect)
            hbox_layout1.addWidget(rumus_luas_persegiPanjang)

            hbox_layout2 = QHBoxLayout()
            hbox_layout2.addWidget(self.answer_label_kel_rect)
            hbox_layout2.addWidget(rumus_kel_persegiPanjang)

            self.layout_v_answer_r.addLayout(hbox_layout1)
            self.layout_v_answer_r.addWidget(self.jawab_luas_rect)
            self.layout_v_answer_r.addLayout(hbox_layout2)
            self.layout_v_answer_r.addWidget(self.jawab_kel_rect)
            

        except ValueError:
            self.error_input()

        

        
    def toolbar_lingkaran(self):
        qwidget = QWidget()

        text_j = QLabel("Masukkan jari - jari (Radius)\t:")
        self.input_j = QLineEdit()

        text_j.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.input_j.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)


        self.combo_box_2_D_lingkaran = QComboBox()
        self.combo_box_2_D_lingkaran.addItem("km")
        self.combo_box_2_D_lingkaran.addItem("hm")
        self.combo_box_2_D_lingkaran.addItem("dam")
        self.combo_box_2_D_lingkaran.addItem("m")
        self.combo_box_2_D_lingkaran.addItem("dm")
        self.combo_box_2_D_lingkaran.addItem("cm")
        self.combo_box_2_D_lingkaran.addItem("mm")
        self.combo_box_2_D_lingkaran.setCurrentIndex(5)

        self.layout_combo_box = QVBoxLayout()
        self.layout_combo_box.addWidget(self.combo_box_2_D_lingkaran)

        layout_1_h_c = QHBoxLayout()
        layout_1_h_c.addWidget(text_j)
        layout_1_h_c.addWidget(self.input_j)
        layout_1_h_c.addLayout(self.layout_combo_box)

        self.button_submit = QPushButton("Submit")
        self.button_submit.setStyleSheet("""
            QPushButton {
                background-color: blue;
                border-radius: 10px;
                padding: 10px;
                color: white;
            }

            QPushButton:hover {
                background-color: lightgreen;
                color: black
            }
        """)
        self.button_submit.setShortcut(Qt.Key_Return)
        self.button_submit.clicked.connect(self.lingkaran)

        self.text_param_lingkaran = QLabel("Lingkaran")
        self.text_param_lingkaran.setAlignment(Qt.AlignHCenter)
        self.text_param_lingkaran.setFont(self.my_font)
        self.text_param_lingkaran.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)

        label = QLabel() 
        # label.setPixmap(QPixmap("D:/Data_C2/Users/Documents/Tutorial_Python/pyside6/projek/img_project/label_lingkaran2.png"))
        base_path = os.path.abspath(os.path.dirname(__file__))
        image_path = os.path.join(base_path, 'img_project', 'label_lingkaran2.png')
        label.setPixmap(QPixmap(image_path))
        label.setAlignment(Qt.AlignCenter)
        label.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        layout_2_v_c = QVBoxLayout()
        layout_2_v_c.addWidget(self.text_param_lingkaran)
        layout_2_v_c.addWidget(label)
        layout_2_v_c.addLayout(layout_1_h_c)
        layout_2_v_c.addWidget(self.button_submit)

        # Create a new QVBoxLayout for the answer label
        self.layout_v_answer_c = QVBoxLayout()
        layout_2_v_c.addLayout(self.layout_v_answer_c)

        qwidget.setLayout(layout_2_v_c)

        self.setCentralWidget(qwidget)

    def lingkaran(self):
        try:
            if self.input_j.text() == "":
                r = 0
            else:
                r = float(self.input_j.text().replace(",","."))

            self.luas_lingkaran = np.pi * (r**2)
            self.keliling_lingkaran = np.pi*(2*r)
            
            def check_is_int_luas() -> str:
                if self.luas_lingkaran.is_integer():
                    self.luas_lingkaran = int(self.luas_lingkaran)
                    return f"{str(self.luas_lingkaran)}"
                else:
                    a = f"{self.luas_lingkaran:.2f}".replace('.',',')
                    return str(a)
                
            def check_is_int_kel() -> str:
                if self.keliling_lingkaran.is_integer():
                    self.keliling_lingkaran = int(self.keliling_lingkaran)
                    return f"{str(self.keliling_lingkaran)}"
                else:
                    a = f"{self.keliling_lingkaran:.2f}".replace('.',',')
                    return str(a)

            rumus_luas_lingkaran = QLabel()
            rumus_luas_lingkaran.setText("L = \u03C0 x r x r")
            rumus_luas_lingkaran.setFont(self.label_font)
            rumus_luas_lingkaran.setStyleSheet(self.color_rumus_font)

            rumus_kel_lingkaran = QLabel()
            rumus_kel_lingkaran.setText("K = \u03C0 x (2 x r)")
            rumus_kel_lingkaran.setFont(self.label_font)
            rumus_kel_lingkaran.setStyleSheet(self.color_rumus_font)

            self.answer_label_luas_circle = QLabel("Luas Lingkaran : ")
            self.answer_label_luas_circle.setFont(self.label_font)
    
            self.answer_label_kel_circle = QLabel("Keliling Lingkaran : ")
            self.answer_label_kel_circle.setFont(self.label_font)


            # self.jawab_luas_circle = QLabel(f"{check_is_int_luas()} {self.combo_box_2_D_lingkaran.currentText()}²\t({str(np.round(luas))} {self.combo_box_2_D_lingkaran.currentText()}²)")
            # self.jawab_kel_circle = QLabel(f"{check_is_int_kel()} {self.combo_box_2_D_lingkaran.currentText()}\t({str(np.round(keliling))} {self.combo_box_2_D_lingkaran.currentText()})")

            self.jawab_luas_circle = QLabel(f"{check_is_int_luas()} {self.combo_box_2_D_lingkaran.currentText()}²")
            self.jawab_luas_circle.setFont(self.answer_font)
            self.jawab_luas_circle.setStyleSheet(self.color_answer_font)

            self.jawab_kel_circle = QLabel(f"{check_is_int_kel()} {self.combo_box_2_D_lingkaran.currentText()}")
            self.jawab_kel_circle.setFont(self.answer_font)
            self.jawab_kel_circle.setStyleSheet(self.color_answer_font)

            while self.layout_v_answer_c.count():
                item = self.layout_v_answer_c.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.setParent(None)

            hbox_layout1 = QHBoxLayout()
            hbox_layout1.addWidget(self.answer_label_luas_circle)
            hbox_layout1.addWidget(rumus_luas_lingkaran)

            hbox_layout2 = QHBoxLayout()
            hbox_layout2.addWidget(self.answer_label_kel_circle)
            hbox_layout2.addWidget(rumus_kel_lingkaran)

            # Add the answer label to the new layout_v_answer_s
            self.layout_v_answer_c.addLayout(hbox_layout1)
            self.layout_v_answer_c.addWidget(self.jawab_luas_circle)
            self.layout_v_answer_c.addLayout(hbox_layout2)
            self.layout_v_answer_c.addWidget(self.jawab_kel_circle)

        except ValueError:
            self.error_input()

    
    def toolbar_layang_layang(self):
        qwidget = QWidget()

        text_kite_luas = QLabel("Mencari Luas")
        text_kite_d1 = QLabel("Masukkan panjang d1\t\t:")
        text_kite_d2 = QLabel("Masukkan panjang d2\t\t:")
        text_kite_keliling = QLabel("Mencari keliling Diketahui [a] dan [b]")
        text_kite_a = QLabel("Masukkan panjang a\t\t:")
        text_kite_b = QLabel("Masukkan panjang b\t\t:")



        self.input_kite_d1 = QLineEdit()
        self.input_kite_d2 = QLineEdit()
        self.input_kite_a = QLineEdit()
        self.input_kite_b = QLineEdit()

        text_kite_luas.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        text_kite_d1.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        text_kite_d2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        text_kite_keliling.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        text_kite_a.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        text_kite_b.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        
        self.input_kite_d1.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.input_kite_d2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.input_kite_a.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.input_kite_b.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)


        self.combo_box_2_D_layang_layang = QComboBox()
        self.combo_box_2_D_layang_layang.addItem("km")
        self.combo_box_2_D_layang_layang.addItem("hm")
        self.combo_box_2_D_layang_layang.addItem("dam")
        self.combo_box_2_D_layang_layang.addItem("m")
        self.combo_box_2_D_layang_layang.addItem("dm")
        self.combo_box_2_D_layang_layang.addItem("cm")
        self.combo_box_2_D_layang_layang.addItem("mm")
        self.combo_box_2_D_layang_layang.setCurrentIndex(5)

        self.layout_combo_box = QVBoxLayout()
        self.layout_combo_box.addWidget(self.combo_box_2_D_layang_layang)

        layout_1_h_kite = QHBoxLayout()
        layout_1_h_kite.addWidget(text_kite_d1)
        layout_1_h_kite.addWidget(self.input_kite_d1)

        layout_2_h_kite = QHBoxLayout()
        layout_2_h_kite.addWidget(text_kite_d2)
        layout_2_h_kite.addWidget(self.input_kite_d2)

        layout_3_h_kite = QHBoxLayout()
        layout_3_h_kite.addWidget(text_kite_a)
        layout_3_h_kite.addWidget(self.input_kite_a)

        layout_4_h_kite = QHBoxLayout()
        layout_4_h_kite.addWidget(text_kite_b)
        layout_4_h_kite.addWidget(self.input_kite_b)


        layout_5_h_kite = QHBoxLayout()
        label_satuan = QLabel("Satuan")
        layout_5_h_kite.addWidget(label_satuan)
        layout_5_h_kite.addLayout(self.layout_combo_box)


        self.button_submit = QPushButton("Submit")
        self.button_submit.setStyleSheet("""
            QPushButton {
                background-color: blue;
                border-radius: 10px;
                padding: 10px;
                color: white;
            }

            QPushButton:hover {
                background-color: lightgreen;
                color: black
            }
        """)
        self.button_submit.setShortcut(Qt.Key_Return)
        self.button_submit.clicked.connect(self.layang_layang)

        label_kosong = QLabel()

        self.text_param_layang_layang = QLabel("Layang - Layang")
        self.text_param_layang_layang.setAlignment(Qt.AlignHCenter)
        self.text_param_layang_layang.setFont(self.my_font)
        self.text_param_layang_layang.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)

        label = QLabel() 
        # label.setPixmap(QPixmap("D:/Data_C2/Users/Documents/Tutorial_Python/pyside6/projek/img_project/label_layang-layang.jpg"))
        base_path = os.path.abspath(os.path.dirname(__file__))
        image_path = os.path.join(base_path, 'img_project', 'label_layang-layang.jpg')
        label.setPixmap(QPixmap(image_path))
        label.setAlignment(Qt.AlignCenter)
        label.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        layout_6_v_kite = QVBoxLayout()
        layout_6_v_kite.addWidget(self.text_param_layang_layang)
        layout_6_v_kite.addWidget(label)
        layout_6_v_kite.addWidget(text_kite_luas)
        layout_6_v_kite.addLayout(layout_1_h_kite)
        layout_6_v_kite.addLayout(layout_2_h_kite)
        layout_6_v_kite.addWidget(label_kosong)
        layout_6_v_kite.addWidget(text_kite_keliling)
        layout_6_v_kite.addLayout(layout_3_h_kite)
        layout_6_v_kite.addLayout(layout_4_h_kite)
        layout_6_v_kite.addWidget(label_kosong)
        layout_6_v_kite.addLayout(layout_5_h_kite)
        layout_6_v_kite.addWidget(self.button_submit)

        # Create a new QVBoxLayout for the answer label
        self.layout_v_answer_kite = QVBoxLayout()
        layout_6_v_kite.addLayout(self.layout_v_answer_kite)

        qwidget.setLayout(layout_6_v_kite)

        self.setCentralWidget(qwidget)



    def layang_layang(self):
        try: 
            global d1, d2, a, b
            if self.input_kite_d1.text() == "" or self.input_kite_d2.text() == "":
                d1 = 0
                d2 = 0

            elif self.input_kite_d1.text() != "" or self.input_kite_d2.text() != "":
                d1 = float(self.input_kite_d1.text().replace(",","."))
                d2 = float(self.input_kite_d2.text().replace(",","."))
            


            if self.input_kite_a.text() == "" or self.input_kite_b.text() == "":
                a = 0
                b = 0

            elif self.input_kite_a.text() != "" or self.input_kite_b.text() != "":
                a = float(self.input_kite_a.text().replace(",","."))
                b = float(self.input_kite_b.text().replace(",","."))
                
            
            self.luas_layang_layang = 1/2* (d1 * d2)
            self.keliling_layang_layang = float((a * 2) + (b * 2))

            def check_is_int_luas() -> str:
                if self.luas_layang_layang.is_integer():
                    self.luas_layang_layang = int(self.luas_layang_layang)
                    return f"{str(self.luas_layang_layang)}"
                else:
                    a = f"{self.luas_layang_layang:.2f}".replace('.',',')
                    return str(a)
                
            def check_is_int_kel() -> str:
                if self.keliling_layang_layang.is_integer():
                    self.keliling_layang_layang = int(self.keliling_layang_layang)
                    return f"{str(self.keliling_layang_layang)}"
                else:
                    a = f"{self.keliling_layang_layang:.2f}".replace('.',',')
                    return str(a)

            rumus_luas_layang_layang = QLabel("L = (d<sub>1</sub>&times;d<sub>2</sub>) / </<sub>2</sub>")
            rumus_luas_layang_layang.setFont(self.label_font)
            rumus_luas_layang_layang.setStyleSheet(self.color_rumus_font)

            rumus_kel_layang_layang = QLabel("K = (a x 2) + (b x 2)")
            rumus_kel_layang_layang.setFont(self.label_font)
            rumus_kel_layang_layang.setStyleSheet(self.color_rumus_font)

            
            #Luas

            self.answer_label_luas_kite = QLabel("Luas Layang - layang\t:")
            self.answer_label_luas_kite.setFont(self.label_font)

            self.answer_label_kel_kite = QLabel("Keliling layang - layang\t:")
            self.answer_label_kel_kite.setFont(self.label_font)


            self.jawab_luas_kite = QLabel(f"{check_is_int_luas()} {self.combo_box_2_D_layang_layang.currentText()}²")
            self.jawab_luas_kite.setFont(self.answer_font)
            self.jawab_luas_kite.setStyleSheet(self.color_answer_font)


            #Keliling
            self.jawab_kel_kite = QLabel(f"{check_is_int_kel()} {self.combo_box_2_D_layang_layang.currentText()}")
            self.jawab_kel_kite.setFont(self.answer_font)
            self.jawab_kel_kite.setStyleSheet(self.color_answer_font)


            while self.layout_v_answer_kite.count():
                item = self.layout_v_answer_kite.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.setParent(None)

            # Add the answer label to the new layout_v_answer_r

            hboxlayout1 = QHBoxLayout()
            hboxlayout1.addWidget(self.answer_label_luas_kite)
            hboxlayout1.addWidget(rumus_luas_layang_layang)

            hboxlayout2 = QHBoxLayout()
            hboxlayout2.addWidget(self.answer_label_kel_kite)
            hboxlayout2.addWidget(rumus_kel_layang_layang)

            self.layout_v_answer_kite.addLayout(hboxlayout1)
            self.layout_v_answer_kite.addWidget(self.jawab_luas_kite)
            self.layout_v_answer_kite.addLayout(hboxlayout2)
            self.layout_v_answer_kite.addWidget(self.jawab_kel_kite)
            

        except ValueError:
            self.error_input()




    def toolbar_segitiga(self):
        qwidget = QWidget()

        text_t_a = QLabel("Masukkan alas\t:")
        text_t_t = QLabel("Masukkan tinggi\t:")
        self.input_t_a = QLineEdit()
        self.input_t_t = QLineEdit()

        text_t_a.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        text_t_t.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.input_t_a.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.input_t_t.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)


        self.combo_box_2_D_segitiga = QComboBox()
        self.combo_box_2_D_segitiga.addItem("km")
        self.combo_box_2_D_segitiga.addItem("hm")
        self.combo_box_2_D_segitiga.addItem("dam")
        self.combo_box_2_D_segitiga.addItem("m")
        self.combo_box_2_D_segitiga.addItem("dm")
        self.combo_box_2_D_segitiga.addItem("cm")
        self.combo_box_2_D_segitiga.addItem("mm")
        self.combo_box_2_D_segitiga.setCurrentIndex(5)

        self.layout_combo_box = QVBoxLayout()
        self.layout_combo_box.addWidget(self.combo_box_2_D_segitiga)

        layout_1_h_t = QHBoxLayout()
        layout_1_h_t.addWidget(text_t_a)
        layout_1_h_t.addWidget(self.input_t_a)

        layout_2_h_t = QHBoxLayout()
        layout_2_h_t.addWidget(text_t_t)
        layout_2_h_t.addWidget(self.input_t_t)

        self.button_submit = QPushButton("Submit")
        self.button_submit.setStyleSheet("""
            QPushButton {
                background-color: blue;
                border-radius: 10px;
                padding: 10px;
                color: white;
            }

            QPushButton:hover {
                background-color: lightgreen;
                color: black
            }
        """)
        self.button_submit.setShortcut(Qt.Key_Return)
        self.button_submit.clicked.connect(self.segitiga)

        layout_3_h_t = QHBoxLayout()
        label_satuan = QLabel("Satuan")
        layout_3_h_t.addWidget(label_satuan)
        layout_3_h_t.addLayout(self.layout_combo_box)

        label_kosong = QLabel()

        self.text_param_segitiga = QLabel("Segitiga")
        self.text_param_segitiga.setAlignment(Qt.AlignHCenter)
        self.text_param_segitiga.setFont(self.my_font)
        self.text_param_segitiga.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)

        label = QLabel() 
        # label.setPixmap(QPixmap("D:/Data_C2/Users/Documents/Tutorial_Python/pyside6/projek/img_project/label_segitiga.png"))
        base_path = os.path.abspath(os.path.dirname(__file__))
        image_path = os.path.join(base_path, 'img_project', 'label_segitiga.png')
        label.setPixmap(QPixmap(image_path))
        label.setAlignment(Qt.AlignCenter)
        label.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)


        layout_3_v_segitiga = QVBoxLayout()
        layout_3_v_segitiga.addWidget(self.text_param_segitiga)
        layout_3_v_segitiga.addWidget(label)
        layout_3_v_segitiga.addLayout(layout_1_h_t)
        layout_3_v_segitiga.addLayout(layout_2_h_t)
        layout_3_v_segitiga.addWidget(label_kosong)
        layout_3_v_segitiga.addLayout(layout_3_h_t)
        layout_3_v_segitiga.addWidget(self.button_submit)

        # Create a new QVBoxLayout for the answer label
        self.layout_v_answer_triangle = QVBoxLayout()
        layout_3_v_segitiga.addLayout(self.layout_v_answer_triangle)

        qwidget.setLayout(layout_3_v_segitiga)

        self.setCentralWidget(qwidget)


    def segitiga(self):
        try:
            if self.input_t_a.text() == "" or self.input_t_t.text() == "":
                a = 0
                t = 0

            else:
                a = float(self.input_t_a.text().replace(",","."))
                t = float(self.input_t_t.text().replace(",","."))

            self.luas_segitiga = 1/2 * (a * t)
            self.keliling_segitiga = ((np.sqrt((a**2) + (t**2))) * 2) + a

            def check_is_int_luas() -> str:
                if self.luas_segitiga.is_integer():
                    self.luas_segitiga = int(self.luas_segitiga)
                    return f"{str(self.luas_segitiga)}"
                else:
                    a = f"{self.luas_segitiga:.2f}".replace('.',',')
                    return str(a)
                
            def check_is_int_kel() -> str:
                if self.keliling_segitiga.is_integer():
                    self.keliling_segitiga = int(self.keliling_segitiga)
                    return f"{str(self.keliling_segitiga)}"
                else:
                    a = f"{self.keliling_segitiga:.2f}".replace('.',',')
                    return str(a)

            #Luas
            # rumus_luas_segitiga = QLabel("L = (a x t) / 2")
            rumus_luas_segitiga = QLabel("L = <sup>a&times;t</sup>&frasl;<sub>2</sub>")
            rumus_luas_segitiga.setFont(self.label_font)
            rumus_luas_segitiga.setStyleSheet(self.color_rumus_font)

            rumus_kel_segitiga = QLabel("K = a + b + c")
            rumus_kel_segitiga.setFont(self.label_font)
            rumus_kel_segitiga.setStyleSheet(self.color_rumus_font)


            self.answer_label_luas_triangle = QLabel("Luas Segitiga : ")
            self.answer_label_luas_triangle.setFont(self.label_font)

            self.answer_label_kel_triangle = QLabel("Keliling Segitiga : ")
            self.answer_label_kel_triangle.setFont(self.label_font)


            self.jawab_luas_triangle = QLabel(f"{check_is_int_luas()} {self.combo_box_2_D_segitiga.currentText()}²")
            self.jawab_luas_triangle.setFont(self.answer_font)
            self.jawab_luas_triangle.setStyleSheet(self.color_answer_font)

            self.jawab_kel_triangle = QLabel(f"{check_is_int_kel()} {self.combo_box_2_D_segitiga.currentText()}")
            self.jawab_kel_triangle.setFont(self.answer_font)
            self.jawab_kel_triangle.setStyleSheet(self.color_answer_font)

            while self.layout_v_answer_triangle.count():
                item = self.layout_v_answer_triangle.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.setParent(None)

            # Add the answer label to the new layout_v_answer_r
            hboxlayout1 = QHBoxLayout()
            hboxlayout1.addWidget(self.answer_label_luas_triangle)
            hboxlayout1.addWidget(rumus_luas_segitiga)

            hboxlayout2 = QHBoxLayout()
            hboxlayout2.addWidget(self.answer_label_kel_triangle)
            hboxlayout2.addWidget(rumus_kel_segitiga)

            self.layout_v_answer_triangle.addLayout(hboxlayout1)
            self.layout_v_answer_triangle.addWidget(self.jawab_luas_triangle)
            self.layout_v_answer_triangle.addLayout(hboxlayout2)
            self.layout_v_answer_triangle.addWidget(self.jawab_kel_triangle)
      

        except ValueError:
            self.error_input()


    def toolbar_belah_ketupat(self):
        qwidget = QWidget()

        text_belahKetupat_d1 = QLabel("Masukkan panjang d1\t:")
        text_belahKetupat_d2 = QLabel("Masukkan panjang d2\t:")
        self.input_belahKetupat_d1 = QLineEdit()
        self.input_belahKetupat_d2 = QLineEdit()

        text_belahKetupat_d1.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        text_belahKetupat_d2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.input_belahKetupat_d1.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.input_belahKetupat_d2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)


        self.combo_box_2_D_belah_ketupat = QComboBox()
        self.combo_box_2_D_belah_ketupat.addItem("km")
        self.combo_box_2_D_belah_ketupat.addItem("hm")
        self.combo_box_2_D_belah_ketupat.addItem("dam")
        self.combo_box_2_D_belah_ketupat.addItem("m")
        self.combo_box_2_D_belah_ketupat.addItem("dm")
        self.combo_box_2_D_belah_ketupat.addItem("cm")
        self.combo_box_2_D_belah_ketupat.addItem("mm")
        self.combo_box_2_D_belah_ketupat.setCurrentIndex(5)

        self.layout_combo_box = QVBoxLayout()
        self.layout_combo_box.addWidget(self.combo_box_2_D_belah_ketupat)

        layout_1_h_belahKetupat = QHBoxLayout()
        layout_1_h_belahKetupat.addWidget(text_belahKetupat_d1)
        layout_1_h_belahKetupat.addWidget(self.input_belahKetupat_d1)

        layout_2_h_belahKetupat = QHBoxLayout()
        layout_2_h_belahKetupat.addWidget(text_belahKetupat_d2)
        layout_2_h_belahKetupat.addWidget(self.input_belahKetupat_d2)

        self.button_submit = QPushButton("Submit")
        self.button_submit.setStyleSheet("""
            QPushButton {
                background-color: blue;
                border-radius: 10px;
                padding: 10px;
                color: white;
            }

            QPushButton:hover {
                background-color: lightgreen;
                color: black
            }
        """)
        self.button_submit.setShortcut(Qt.Key_Return)
        self.button_submit.clicked.connect(self.belah_ketupat)

        layout_3_h_belahKetupat = QHBoxLayout()
        label_satuan = QLabel("Satuan")
        layout_3_h_belahKetupat.addWidget(label_satuan)
        layout_3_h_belahKetupat.addLayout(self.layout_combo_box)

        label_kosong = QLabel()

        self.text_param_belah_ketupat = QLabel("Belah Ketupat")
        self.text_param_belah_ketupat.setAlignment(Qt.AlignHCenter)
        self.text_param_belah_ketupat.setFont(self.my_font)
        self.text_param_belah_ketupat.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)

        label = QLabel() 
        # label.setPixmap(QPixmap("D:/Data_C2/Users/Documents/Tutorial_Python/pyside6/projek/img_project/label_belah_ketupat.png"))
        base_path = os.path.abspath(os.path.dirname(__file__))
        image_path = os.path.join(base_path, 'img_project', 'label_belah_ketupat.png')
        label.setPixmap(QPixmap(image_path))
        label.setAlignment(Qt.AlignCenter)
        label.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)


        layout_3_v_belahKetupat = QVBoxLayout()
        layout_3_v_belahKetupat.addWidget(self.text_param_belah_ketupat)
        layout_3_v_belahKetupat.addWidget(label)
        layout_3_v_belahKetupat.addLayout(layout_1_h_belahKetupat)
        layout_3_v_belahKetupat.addLayout(layout_2_h_belahKetupat)
        layout_3_v_belahKetupat.addWidget(label_kosong)
        layout_3_v_belahKetupat.addLayout(layout_3_h_belahKetupat)
        layout_3_v_belahKetupat.addWidget(self.button_submit)

        # Create a new QVBoxLayout for the answer label
        self.layout_v_answer_belahKetupat = QVBoxLayout()
        layout_3_v_belahKetupat.addLayout(self.layout_v_answer_belahKetupat)

        qwidget.setLayout(layout_3_v_belahKetupat)

        self.setCentralWidget(qwidget)


    def belah_ketupat(self):
        try:
            if self.input_belahKetupat_d1.text() == "" or self.input_belahKetupat_d2.text() == "":
                d1 = 0
                d2 = 0

            else:
                d1 = float(self.input_belahKetupat_d1.text().replace(",","."))
                d2 = float(self.input_belahKetupat_d2.text().replace(",","."))

            self.luas_belahKetupat = 1/2 * (d1 * d2)
            self.keliling_belahKetupat = 4 * (np.sqrt(((d2 // 2) **2) + ((d1 // 2) **2)))


            def check_is_int_luas() -> str:
                if self.luas_belahKetupat.is_integer():
                    self.luas_belahKetupat = int(self.luas_belahKetupat)
                    return f"{str(self.luas_belahKetupat)}"
                else:
                    a = f"{self.luas_belahKetupat:.2f}".replace('.',',')
                    return str(a)
                
            def check_is_int_kel() -> str:
                if self.keliling_belahKetupat.is_integer():
                    self.keliling_belahKetupat = int(self.keliling_belahKetupat)
                    return f"{str(self.keliling_belahKetupat)}"
                else:
                    a = f"{self.keliling_belahKetupat:.2f}".replace('.',',')
                    return str(a)
            #Luas

            rumus_luas_belahKetupat = QLabel("L = (d1 x d2) / 2")
            rumus_luas_belahKetupat.setFont(self.label_font)
            rumus_luas_belahKetupat.setStyleSheet(self.color_rumus_font)

            rumus_kel_belahKetupat = QLabel("K = (a x 2) + (b x 2)")
            rumus_kel_belahKetupat.setFont(self.label_font)
            rumus_kel_belahKetupat.setStyleSheet(self.color_rumus_font)

            self.answer_label_luas_belahKetupat = QLabel("Luas Belah Ketupat : ")
            self.answer_label_luas_belahKetupat.setFont(self.label_font)

            self.answer_label_kel_belahKetupat = QLabel("Keliling Belah Ketupat : ")
            self.answer_label_kel_belahKetupat.setFont(self.label_font)


            #Keliling
            self.jawab_luas_belahKetupat = QLabel(f"{check_is_int_luas()} {self.combo_box_2_D_belah_ketupat.currentText()}²")
            self.jawab_luas_belahKetupat.setFont(self.answer_font)
            self.jawab_luas_belahKetupat.setStyleSheet(self.color_answer_font)

            self.jawab_kel_belahKetupat = QLabel(f"{check_is_int_kel()} {self.combo_box_2_D_belah_ketupat.currentText()}")
            self.jawab_kel_belahKetupat.setFont(self.answer_font)
            self.jawab_kel_belahKetupat.setStyleSheet(self.color_answer_font)

            while self.layout_v_answer_belahKetupat.count():
                item = self.layout_v_answer_belahKetupat.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.setParent(None)

            # Add the answer label to the new layout_v_answer_r
            hboxlayout1 = QHBoxLayout()
            hboxlayout1.addWidget(self.answer_label_luas_belahKetupat)
            hboxlayout1.addWidget(rumus_luas_belahKetupat)

            hboxlayout2 = QHBoxLayout()
            hboxlayout2.addWidget(self.answer_label_kel_belahKetupat)
            hboxlayout2.addWidget(rumus_kel_belahKetupat)

            self.layout_v_answer_belahKetupat.addLayout(hboxlayout1)
            self.layout_v_answer_belahKetupat.addWidget(self.jawab_luas_belahKetupat)
            self.layout_v_answer_belahKetupat.addLayout(hboxlayout2)
            self.layout_v_answer_belahKetupat.addWidget(self.jawab_kel_belahKetupat)
            

        except ValueError:
            self.error_input()


    def toolbar_trapesium_sama_kaki(self):
        qwidget = QWidget()

        text_trapesiumSamaKaki_a = QLabel("Masukkan panjang a\t:")
        text_trapesiumSamaKaki_b = QLabel("Masukkan panjang b\t:")
        text_trapesiumSamaKaki_t = QLabel("Masukkan tinggi\t\t:")
        self.input_trapesiumSamaKaki_a = QLineEdit()
        self.input_trapesiumSamaKaki_b = QLineEdit()
        self.input_trapesiumSamaKaki_t = QLineEdit()

        text_trapesiumSamaKaki_a.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        text_trapesiumSamaKaki_b.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        text_trapesiumSamaKaki_t.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.input_trapesiumSamaKaki_a.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.input_trapesiumSamaKaki_b.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.input_trapesiumSamaKaki_t.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)


        self.combo_box_2_D_TrapesiumSamaKaki = QComboBox()
        self.combo_box_2_D_TrapesiumSamaKaki.addItem("km")
        self.combo_box_2_D_TrapesiumSamaKaki.addItem("hm")
        self.combo_box_2_D_TrapesiumSamaKaki.addItem("dam")
        self.combo_box_2_D_TrapesiumSamaKaki.addItem("m")
        self.combo_box_2_D_TrapesiumSamaKaki.addItem("dm")
        self.combo_box_2_D_TrapesiumSamaKaki.addItem("cm")
        self.combo_box_2_D_TrapesiumSamaKaki.addItem("mm")
        self.combo_box_2_D_TrapesiumSamaKaki.setCurrentIndex(5)

        self.layout_combo_box = QVBoxLayout()
        self.layout_combo_box.addWidget(self.combo_box_2_D_TrapesiumSamaKaki)

        layout_1_h_trapesiumSamaKaki = QHBoxLayout()
        layout_1_h_trapesiumSamaKaki.addWidget(text_trapesiumSamaKaki_a)
        layout_1_h_trapesiumSamaKaki.addWidget(self.input_trapesiumSamaKaki_a)

        layout_2_h_trapesiumSamaKaki = QHBoxLayout()
        layout_2_h_trapesiumSamaKaki.addWidget(text_trapesiumSamaKaki_b)
        layout_2_h_trapesiumSamaKaki.addWidget(self.input_trapesiumSamaKaki_b)

        layout_3_h_trapesiumSamaKaki = QHBoxLayout()
        layout_3_h_trapesiumSamaKaki.addWidget(text_trapesiumSamaKaki_t)
        layout_3_h_trapesiumSamaKaki.addWidget(self.input_trapesiumSamaKaki_t)

        self.button_submit = QPushButton("Submit")
        self.button_submit.setStyleSheet("""
            QPushButton {
                background-color: blue;
                border-radius: 10px;
                padding: 10px;
                color: white;
            }

            QPushButton:hover {
                background-color: lightgreen;
                color: black
            }
        """)
        self.button_submit.setShortcut(Qt.Key_Return)
        self.button_submit.clicked.connect(self.trapesiumSamaKaki)

        layout_4_h_trapesiumSamaKaki = QHBoxLayout()
        label_satuan = QLabel("Satuan")
        layout_4_h_trapesiumSamaKaki.addWidget(label_satuan)
        layout_4_h_trapesiumSamaKaki.addLayout(self.layout_combo_box)

        label_kosong = QLabel()

        self.text_param_trapesium_sama_kaki = QLabel("Trapesium Sama Kaki")
        self.text_param_trapesium_sama_kaki.setAlignment(Qt.AlignHCenter)
        self.text_param_trapesium_sama_kaki.setFont(self.my_font)
        self.text_param_trapesium_sama_kaki.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)

        label = QLabel() 
        # label.setPixmap(QPixmap("D:/Data_C2/Users/Documents/Tutorial_Python/pyside6/projek/img_project/label_trapesium_sama_kaki.png"))
        base_path = os.path.abspath(os.path.dirname(__file__))
        image_path = os.path.join(base_path, 'img_project', 'label_trapesium_sama_kaki.png')
        label.setPixmap(QPixmap(image_path))
        label.setAlignment(Qt.AlignCenter)
        label.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        layout_5_v_trapesiumSamaKaki = QVBoxLayout()
        layout_5_v_trapesiumSamaKaki.addWidget(self.text_param_trapesium_sama_kaki)
        layout_5_v_trapesiumSamaKaki.addWidget(label)
        layout_5_v_trapesiumSamaKaki.addLayout(layout_1_h_trapesiumSamaKaki)
        layout_5_v_trapesiumSamaKaki.addLayout(layout_2_h_trapesiumSamaKaki)
        layout_5_v_trapesiumSamaKaki.addLayout(layout_3_h_trapesiumSamaKaki)
        layout_5_v_trapesiumSamaKaki.addWidget(label_kosong)
        layout_5_v_trapesiumSamaKaki.addLayout(layout_4_h_trapesiumSamaKaki)
        layout_5_v_trapesiumSamaKaki.addWidget(self.button_submit)

        # Create a new QVBoxLayout for the answer label
        self.layout_v_answer_trapesiumSamaKaki = QVBoxLayout()
        layout_5_v_trapesiumSamaKaki.addLayout(self.layout_v_answer_trapesiumSamaKaki)

        qwidget.setLayout(layout_5_v_trapesiumSamaKaki)

        self.setCentralWidget(qwidget)


    def trapesiumSamaKaki(self):
        try:
            if self.input_trapesiumSamaKaki_a.text() == "" or self.input_trapesiumSamaKaki_b.text() == "" or self.input_trapesiumSamaKaki_t.text() == "":
                a = 0
                b = 0
                t = 0
            else:
                a = float(self.input_trapesiumSamaKaki_a.text().replace(",","."))
                b = float(self.input_trapesiumSamaKaki_b.text().replace(",","."))
                t = float(self.input_trapesiumSamaKaki_t.text().replace(",","."))

            self.luas_TrapesiumSamaKaki = 1/2 * (a + b) * t

            sisa_b_min_a = b - a
            sisi_miring = np.sqrt(((sisa_b_min_a ** 2) + (t ** 2))) 
            self.keliling_TrapesiumSamaKaki = a + b + (sisi_miring * 2)

            #luas

            def check_is_int_luas() -> str:
                if self.luas_TrapesiumSamaKaki.is_integer():
                    self.luas_TrapesiumSamaKaki = int(self.luas_TrapesiumSamaKaki)
                    return f"{str(self.luas_TrapesiumSamaKaki)}"
                else:
                    a = f"{self.luas_TrapesiumSamaKaki:.2f}".replace('.',',')
                    return str(a)
                
            def check_is_int_kel() -> str:
                if self.keliling_TrapesiumSamaKaki.is_integer():
                    self.keliling_TrapesiumSamaKaki = int(self.keliling_TrapesiumSamaKaki)
                    return f"{str(self.keliling_TrapesiumSamaKaki)}"
                else:
                    a = f"{self.keliling_TrapesiumSamaKaki:.2f}".replace('.',',')
                    return str(a)
                
            rumus_luas_TrapesiumSamaKaki = QLabel("L = ((a + b) x t) / 2")
            rumus_luas_TrapesiumSamaKaki.setFont(self.label_font)
            rumus_luas_TrapesiumSamaKaki.setStyleSheet(self.color_rumus_font)

            rumus_kel_TrapesiumSamaKaki = QLabel("K = a + b + c + d")
            rumus_kel_TrapesiumSamaKaki.setFont(self.label_font)
            rumus_kel_TrapesiumSamaKaki.setStyleSheet(self.color_rumus_font)


            self.answer_label_luas_TrapesiumSamaKaki = QLabel("Luas Trapesium Sama Kaki : ")
            self.answer_label_luas_TrapesiumSamaKaki.setFont(self.label_font)

            self.answer_label_kel_TrapesiumSamaKaki = QLabel("Keliling Trapesium Sama Kaki : ")
            self.answer_label_kel_TrapesiumSamaKaki.setFont(self.label_font)


            #Keiling
            self.jawab_luas_TrapesiumSamaKaki = QLabel(f"{check_is_int_luas()} {self.combo_box_2_D_TrapesiumSamaKaki.currentText()}²")
            self.jawab_luas_TrapesiumSamaKaki.setFont(self.answer_font)
            self.jawab_luas_TrapesiumSamaKaki.setStyleSheet(self.color_answer_font)

            self.jawab_kel_TrapesiumSamaKaki = QLabel(f"{check_is_int_kel()} {self.combo_box_2_D_TrapesiumSamaKaki.currentText()}")
            self.jawab_kel_TrapesiumSamaKaki.setFont(self.answer_font)
            self.jawab_kel_TrapesiumSamaKaki.setStyleSheet(self.color_answer_font)

            while self.layout_v_answer_trapesiumSamaKaki.count():
                item = self.layout_v_answer_trapesiumSamaKaki.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.setParent(None)

            # Add the answer label to the new layout_v_answer_r
            hboxlayout1 = QHBoxLayout()
            hboxlayout1.addWidget(self.answer_label_luas_TrapesiumSamaKaki)
            hboxlayout1.addWidget(rumus_luas_TrapesiumSamaKaki)

            hboxlayout2 = QHBoxLayout()
            hboxlayout2.addWidget(self.answer_label_kel_TrapesiumSamaKaki)
            hboxlayout2.addWidget(rumus_kel_TrapesiumSamaKaki)

            self.layout_v_answer_trapesiumSamaKaki.addLayout(hboxlayout1)
            self.layout_v_answer_trapesiumSamaKaki.addWidget(self.jawab_luas_TrapesiumSamaKaki)
            self.layout_v_answer_trapesiumSamaKaki.addLayout(hboxlayout2)
            self.layout_v_answer_trapesiumSamaKaki.addWidget(self.jawab_kel_TrapesiumSamaKaki)

        except ValueError:
            self.error_input()


    def toolbar_trapesium_siku_siku(self):
        qwidget = QWidget()

        text_trapesiumSikuSiku_a = QLabel("Masukkan panjang a\t:")
        text_trapesiumSikuSiku_b = QLabel("Masukkan panjang b\t:")
        text_trapesiumSikuSiku_t = QLabel("Masukkan tinggi\t\t:")
        self.input_trapesiumSikuSiku_a = QLineEdit()
        self.input_trapesiumSikuSiku_b = QLineEdit()
        self.input_trapesiumSikuSiku_t = QLineEdit()

        text_trapesiumSikuSiku_a.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        text_trapesiumSikuSiku_b.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        text_trapesiumSikuSiku_t.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.input_trapesiumSikuSiku_a.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.input_trapesiumSikuSiku_b.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.input_trapesiumSikuSiku_t.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)


        self.combo_box_2_D_trapesiumSikuSIKU = QComboBox()
        self.combo_box_2_D_trapesiumSikuSIKU.addItem("km")
        self.combo_box_2_D_trapesiumSikuSIKU.addItem("hm")
        self.combo_box_2_D_trapesiumSikuSIKU.addItem("dam")
        self.combo_box_2_D_trapesiumSikuSIKU.addItem("m")
        self.combo_box_2_D_trapesiumSikuSIKU.addItem("dm")
        self.combo_box_2_D_trapesiumSikuSIKU.addItem("cm")
        self.combo_box_2_D_trapesiumSikuSIKU.addItem("mm")
        self.combo_box_2_D_trapesiumSikuSIKU.setCurrentIndex(5)

        self.layout_combo_box = QVBoxLayout()
        self.layout_combo_box.addWidget(self.combo_box_2_D_trapesiumSikuSIKU)

        layout_1_h_trapesiumSikuSiku = QHBoxLayout()
        layout_1_h_trapesiumSikuSiku.addWidget(text_trapesiumSikuSiku_a)
        layout_1_h_trapesiumSikuSiku.addWidget(self.input_trapesiumSikuSiku_a)

        layout_2_h_trapesiumSikuSiku = QHBoxLayout()
        layout_2_h_trapesiumSikuSiku.addWidget(text_trapesiumSikuSiku_b)
        layout_2_h_trapesiumSikuSiku.addWidget(self.input_trapesiumSikuSiku_b)

        layout_3_h_trapesiumSikuSiku = QHBoxLayout()
        layout_3_h_trapesiumSikuSiku.addWidget(text_trapesiumSikuSiku_t)
        layout_3_h_trapesiumSikuSiku.addWidget(self.input_trapesiumSikuSiku_t)

        self.button_submit = QPushButton("Submit")
        self.button_submit.setStyleSheet("""
            QPushButton {
                background-color: blue;
                border-radius: 10px;
                padding: 10px;
                color: white;
            }

            QPushButton:hover {
                background-color: lightgreen;
                color: black
            }
        """)
        self.button_submit.setShortcut(Qt.Key_Return)
        self.button_submit.clicked.connect(self.trapesiumSikuSiku)

        layout_4_h_trapesiumSikuSiku = QHBoxLayout()
        label_satuan = QLabel("Satuan")
        layout_4_h_trapesiumSikuSiku.addWidget(label_satuan)
        layout_4_h_trapesiumSikuSiku.addLayout(self.layout_combo_box)

        label_kosong = QLabel()

        self.text_param_trapesium_siku_siku = QLabel("Trapesium Siku - Siku")
        self.text_param_trapesium_siku_siku.setAlignment(Qt.AlignHCenter)
        self.text_param_trapesium_siku_siku.setFont(self.my_font)
        self.text_param_trapesium_siku_siku.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)

        label = QLabel() 
        # label.setPixmap(QPixmap("D:/Data_C2/Users/Documents/Tutorial_Python/pyside6/projek/img_project/label_trapesium_siku_siku.png"))
        base_path = os.path.abspath(os.path.dirname(__file__))
        image_path = os.path.join(base_path, 'img_project', 'label_trapesium_siku_siku.png')
        label.setPixmap(QPixmap(image_path))
        label.setAlignment(Qt.AlignCenter)
        label.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        layout_5_v_trapesiumSikuSiku = QVBoxLayout()
        layout_5_v_trapesiumSikuSiku.addWidget(self.text_param_trapesium_siku_siku)
        layout_5_v_trapesiumSikuSiku.addWidget(label)
        layout_5_v_trapesiumSikuSiku.addLayout(layout_1_h_trapesiumSikuSiku)
        layout_5_v_trapesiumSikuSiku.addLayout(layout_2_h_trapesiumSikuSiku)
        layout_5_v_trapesiumSikuSiku.addLayout(layout_3_h_trapesiumSikuSiku)
        layout_5_v_trapesiumSikuSiku.addWidget(label_kosong)
        layout_5_v_trapesiumSikuSiku.addLayout(layout_4_h_trapesiumSikuSiku)
        layout_5_v_trapesiumSikuSiku.addWidget(self.button_submit)

        # Create a new QVBoxLayout for the answer label
        self.layout_v_answer_trapesiumSikuSiku = QVBoxLayout()
        layout_5_v_trapesiumSikuSiku.addLayout(self.layout_v_answer_trapesiumSikuSiku)

        qwidget.setLayout(layout_5_v_trapesiumSikuSiku)

        self.setCentralWidget(qwidget)


    def trapesiumSikuSiku(self):
        try:
            if self.input_trapesiumSikuSiku_a.text() == "" or self.input_trapesiumSikuSiku_b.text() == "" or self.input_trapesiumSikuSiku_t.text() == "":
                a = 0
                b = 0
                t = 0
            else:
                a = float(self.input_trapesiumSikuSiku_a.text().replace(",","."))
                b = float(self.input_trapesiumSikuSiku_b.text().replace(",","."))
                t = float(self.input_trapesiumSikuSiku_t.text().replace(",","."))

            self.luas_TrapesiumSikuSiku = 1/2 * (a + b) * t

            sisa_b_min_a = b - a
            sisi_miring = np.sqrt(((sisa_b_min_a ** 2) + (t ** 2))) 
            self.keliling_TrapesiumSikuSiku = a + b + sisi_miring + t

            def check_is_int_luas() -> str:
                if self.luas_TrapesiumSikuSiku.is_integer():
                    self.luas_TrapesiumSikuSiku = int(self.luas_TrapesiumSikuSiku)
                    return f"{str(self.luas_TrapesiumSikuSiku)}"
                else:
                    a = f"{self.luas_TrapesiumSikuSiku:.2f}".replace('.',',')
                    return str(a)
                
            def check_is_int_kel() -> str:
                if self.keliling_TrapesiumSikuSiku.is_integer():
                    self.keliling_TrapesiumSikuSiku = int(self.keliling_TrapesiumSikuSiku)
                    return f"{str(self.keliling_TrapesiumSikuSiku)}"
                else:
                    a = f"{self.keliling_TrapesiumSikuSiku:.2f}".replace('.',',')
                    return str(a)
            

            #luas
            rumus_luas_TrapesiumSikuSiku = QLabel("L = ((a + b) x t) / 2")
            rumus_luas_TrapesiumSikuSiku.setFont(self.label_font)
            rumus_luas_TrapesiumSikuSiku.setStyleSheet(self.color_rumus_font)

            rumus_kel_TrapesiumSikuSiku = QLabel("K = a + b + t + d")
            rumus_kel_TrapesiumSikuSiku.setFont(self.label_font)
            rumus_kel_TrapesiumSikuSiku.setStyleSheet(self.color_rumus_font)


            #Keiling
            self.answer_label_luas_trapesiumSikuSiku = QLabel("Luas Trapesium Siku - Siku : ")
            self.answer_label_luas_trapesiumSikuSiku.setFont(self.label_font)

            self.answer_label_kel_trapesiumSikuSiku = QLabel("Keliling Trapesium Siku - Siku : ")
            self.answer_label_kel_trapesiumSikuSiku.setFont(self.label_font)

            self.jawab_luas_trapesiumSikuSiku = QLabel(f"{check_is_int_luas()} {self.combo_box_2_D_trapesiumSikuSIKU.currentText()}²")
            self.jawab_luas_trapesiumSikuSiku.setFont(self.answer_font)
            self.jawab_luas_trapesiumSikuSiku.setStyleSheet(self.color_answer_font)

            self.jawab_kel_trapesiumSikuSiku = QLabel(f"{check_is_int_kel()} {self.combo_box_2_D_trapesiumSikuSIKU.currentText()}")
            self.jawab_kel_trapesiumSikuSiku.setFont(self.answer_font)
            self.jawab_kel_trapesiumSikuSiku.setStyleSheet(self.color_answer_font)

            while self.layout_v_answer_trapesiumSikuSiku.count():
                item = self.layout_v_answer_trapesiumSikuSiku.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.setParent(None)

            # Add the answer label to the new layout_v_answer_r

            hboxlayout1 = QHBoxLayout()
            hboxlayout1.addWidget(self.answer_label_luas_trapesiumSikuSiku)
            hboxlayout1.addWidget(rumus_luas_TrapesiumSikuSiku)

            hboxlayout2 = QHBoxLayout()
            hboxlayout2.addWidget(self.answer_label_kel_trapesiumSikuSiku)
            hboxlayout2.addWidget(rumus_kel_TrapesiumSikuSiku)

            self.layout_v_answer_trapesiumSikuSiku.addLayout(hboxlayout1)
            self.layout_v_answer_trapesiumSikuSiku.addWidget(self.jawab_luas_trapesiumSikuSiku)
            self.layout_v_answer_trapesiumSikuSiku.addLayout(hboxlayout2)
            self.layout_v_answer_trapesiumSikuSiku.addWidget(self.jawab_kel_trapesiumSikuSiku)
            
        except ValueError:
            self.error_input()



    def toolbar_jajar_genjang(self):
        qwidget = QWidget()

        text_jajarGenjang_luas = QLabel("Mencari Luas")
        text_jajarGenjang_a = QLabel("Masukkan panjang a (alas)\t\t:")
        text_jajarGenjang_t = QLabel("Masukkan tinggi\t\t\t:")
        text_jajarGenjang_keliling = QLabel("Mencari keliling Diketahui [a] dan [b]")
        text_jajarGenjang_a_2 = QLabel("Masukkan panjang a (alas)\t\t:")
        text_jajarGenjang_b = QLabel("Masukkan panjang b\t\t:")



        self.input_jajarGenjang_a = QLineEdit()
        self.input_jajarGenjang_t = QLineEdit()
        self.input_jajarGenjang_a_2 = QLineEdit()
        self.input_jajarGenjang_b = QLineEdit()

        text_jajarGenjang_luas.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        text_jajarGenjang_a.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        text_jajarGenjang_t.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        text_jajarGenjang_keliling.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        text_jajarGenjang_a_2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        text_jajarGenjang_b.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        
        self.input_jajarGenjang_a.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.input_jajarGenjang_t.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.input_jajarGenjang_a_2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.input_jajarGenjang_b.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)



        self.combo_box_2_D_jajarGenjang = QComboBox()
        self.combo_box_2_D_jajarGenjang.addItem("km")
        self.combo_box_2_D_jajarGenjang.addItem("hm")
        self.combo_box_2_D_jajarGenjang.addItem("dam")
        self.combo_box_2_D_jajarGenjang.addItem("m")
        self.combo_box_2_D_jajarGenjang.addItem("dm")
        self.combo_box_2_D_jajarGenjang.addItem("cm")
        self.combo_box_2_D_jajarGenjang.addItem("mm")
        self.combo_box_2_D_jajarGenjang.setCurrentIndex(5)

        self.layout_combo_box = QVBoxLayout()
        self.layout_combo_box.addWidget(self.combo_box_2_D_jajarGenjang)

        layout_1_h_jajarGenjang = QHBoxLayout()
        layout_1_h_jajarGenjang.addWidget(text_jajarGenjang_a)
        layout_1_h_jajarGenjang.addWidget(self.input_jajarGenjang_a)

        layout_2_h_jajarGenjang = QHBoxLayout()
        layout_2_h_jajarGenjang.addWidget(text_jajarGenjang_t)
        layout_2_h_jajarGenjang.addWidget(self.input_jajarGenjang_t)

        layout_3_h_jajarGenjang = QHBoxLayout()
        layout_3_h_jajarGenjang.addWidget(text_jajarGenjang_a_2)
        layout_3_h_jajarGenjang.addWidget(self.input_jajarGenjang_a_2)

        layout_4_h_jajarGenjang = QHBoxLayout()
        layout_4_h_jajarGenjang.addWidget(text_jajarGenjang_b)
        layout_4_h_jajarGenjang.addWidget(self.input_jajarGenjang_b)


        layout_5_h_jajarGenjang = QHBoxLayout()
        label_satuan = QLabel("Satuan")
        layout_5_h_jajarGenjang.addWidget(label_satuan)
        layout_5_h_jajarGenjang.addLayout(self.layout_combo_box)


        self.button_submit = QPushButton("Submit")
        self.button_submit.setStyleSheet("""
            QPushButton {
                background-color: blue;
                border-radius: 10px;
                padding: 10px;
                color: white;
            }

            QPushButton:hover {
                background-color: lightgreen;
                color: black
            }
        """)
        self.button_submit.setShortcut(Qt.Key_Return)
        self.button_submit.clicked.connect(self.jajar_genjang)

        label_kosong = QLabel()

        self.text_param_jajar_genjang = QLabel("Jajar Genjang")
        self.text_param_jajar_genjang.setAlignment(Qt.AlignHCenter)
        self.text_param_jajar_genjang.setFont(self.my_font)
        self.text_param_jajar_genjang.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)

        label = QLabel() 
        # label.setPixmap(QPixmap("D:/Data_C2/Users/Documents/Tutorial_Python/pyside6/projek/img_project/label_jajar_genjang.png"))
        base_path = os.path.abspath(os.path.dirname(__file__))
        image_path = os.path.join(base_path, 'img_project', 'label_jajar_genjang.png')
        label.setPixmap(QPixmap(image_path))
        label.setAlignment(Qt.AlignCenter)
        label.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)


        layout_6_v_jajarGenjang = QVBoxLayout()
        layout_6_v_jajarGenjang.addWidget(self.text_param_jajar_genjang)
        layout_6_v_jajarGenjang.addWidget(label)
        layout_6_v_jajarGenjang.addWidget(text_jajarGenjang_luas)
        layout_6_v_jajarGenjang.addLayout(layout_1_h_jajarGenjang)
        layout_6_v_jajarGenjang.addLayout(layout_2_h_jajarGenjang)
        layout_6_v_jajarGenjang.addWidget(label_kosong)
        layout_6_v_jajarGenjang.addWidget(text_jajarGenjang_keliling)
        layout_6_v_jajarGenjang.addLayout(layout_3_h_jajarGenjang)
        layout_6_v_jajarGenjang.addLayout(layout_4_h_jajarGenjang)
        layout_6_v_jajarGenjang.addWidget(label_kosong)
        layout_6_v_jajarGenjang.addLayout(layout_5_h_jajarGenjang)
        layout_6_v_jajarGenjang.addWidget(self.button_submit)

        # Create a new QVBoxLayout for the answer label
        self.layout_v_answer_jajarGenjang = QVBoxLayout()
        layout_6_v_jajarGenjang.addLayout(self.layout_v_answer_jajarGenjang)

        qwidget.setLayout(layout_6_v_jajarGenjang)

        self.setCentralWidget(qwidget)



    def jajar_genjang(self):   
        try:
            if self.input_jajarGenjang_a.text() == "" or self.input_jajarGenjang_t.text() == "":
                a = 0
                t = 0

            elif self.input_jajarGenjang_a.text() != "" or self.input_jajarGenjang_t.text() != "":
                a = float(self.input_jajarGenjang_a.text().replace(",","."))
                t = float(self.input_jajarGenjang_t.text().replace(",","."))
            


            if self.input_jajarGenjang_a_2.text() == "" or self.input_jajarGenjang_b.text() == "":
                a2 = 0
                b = 0

            elif self.input_jajarGenjang_a_2.text() != "" or self.input_jajarGenjang_b.text() != "":
                a2 = float(self.input_jajarGenjang_a_2.text().replace(",","."))
                b = float(self.input_jajarGenjang_b.text().replace(",","."))
                
            
            self.luas_jajarGenjang = float(a * t)
            self.keliling_jajarGenjang = float(2 * (a2 + b))

            def check_is_int_luas() -> str:
                if self.luas_jajarGenjang.is_integer():
                    self.luas_jajarGenjang = int(self.luas_jajarGenjang)
                    return f"{str(self.luas_jajarGenjang)}"
                else:
                    a = f"{self.luas_jajarGenjang:.2f}".replace('.',',')
                    return str(a)
                
            def check_is_int_kel() -> str:
                if self.keliling_jajarGenjang.is_integer():
                    self.keliling_jajarGenjang = int(self.keliling_jajarGenjang)
                    return f"{str(self.keliling_jajarGenjang)}"
                else:
                    a = f"{self.keliling_jajarGenjang:.2f}".replace('.',',')
                    return str(a)
             

            #Luas
            rumus_luas_jajarGenjang = QLabel("L = a x t")
            rumus_luas_jajarGenjang.setFont(self.label_font)
            rumus_luas_jajarGenjang.setStyleSheet(self.color_rumus_font)

            rumus_kel_jajarGenjang = QLabel("K = 2 x (a + b)")
            rumus_kel_jajarGenjang.setFont(self.label_font)
            rumus_kel_jajarGenjang.setStyleSheet(self.color_rumus_font)


            self.answer_label_luas_jajarGenjang = QLabel("Luas Jajar Genjang\t:")
            self.answer_label_luas_jajarGenjang.setFont(self.label_font)
            self.answer_label_kel_jajarGenjang = QLabel("Keliling Jajar Genjang\t:")
            self.answer_label_kel_jajarGenjang.setFont(self.label_font)


            #Keliling
            self.jawab_luas_jajarGenjang = QLabel(f"{check_is_int_luas()} {self.combo_box_2_D_jajarGenjang.currentText()}²")
            self.jawab_luas_jajarGenjang.setFont(self.answer_font)
            self.jawab_luas_jajarGenjang.setStyleSheet(self.color_answer_font)
            self.jawab_kel_jajarGenjang = QLabel(f"{check_is_int_kel()} {self.combo_box_2_D_jajarGenjang.currentText()}")
            self.jawab_kel_jajarGenjang.setFont(self.answer_font)
            self.jawab_kel_jajarGenjang.setStyleSheet(self.color_answer_font)


            while self.layout_v_answer_jajarGenjang.count():
                item = self.layout_v_answer_jajarGenjang.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.setParent(None)

            # Add the answer label to the new layout_v_answer_r

            hboxlayout1 = QHBoxLayout()
            hboxlayout1.addWidget(self.answer_label_luas_jajarGenjang)
            hboxlayout1.addWidget(rumus_luas_jajarGenjang)

            hboxlayout2 = QHBoxLayout()
            hboxlayout2.addWidget(self.answer_label_kel_jajarGenjang)
            hboxlayout2.addWidget(rumus_kel_jajarGenjang)

            self.layout_v_answer_jajarGenjang.addLayout(hboxlayout1)
            self.layout_v_answer_jajarGenjang.addWidget(self.jawab_luas_jajarGenjang)
            self.layout_v_answer_jajarGenjang.addLayout(hboxlayout2)
            self.layout_v_answer_jajarGenjang.addWidget(self.jawab_kel_jajarGenjang)
            

        except ValueError:
            self.error_input()



    def toolbar_kubus(self):
        qwidget = QWidget()

        text_cubic = QLabel("Masukkan s :")
        self.input_cubic = QLineEdit()

        text_cubic.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.input_cubic.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        self.combo_box_2_D_kubus = QComboBox()
        self.combo_box_2_D_kubus.addItem("km")
        self.combo_box_2_D_kubus.addItem("hm")
        self.combo_box_2_D_kubus.addItem("dam")
        self.combo_box_2_D_kubus.addItem("m")
        self.combo_box_2_D_kubus.addItem("dm")
        self.combo_box_2_D_kubus.addItem("cm")
        self.combo_box_2_D_kubus.addItem("mm")
        self.combo_box_2_D_kubus.setCurrentIndex(5)

        self.layout_combo_box = QVBoxLayout()
        self.layout_combo_box.addWidget(self.combo_box_2_D_kubus)

        layout_1_h_cubic = QHBoxLayout()
        layout_1_h_cubic.addWidget(text_cubic)
        layout_1_h_cubic.addWidget(self.input_cubic)
        layout_1_h_cubic.addLayout(self.layout_combo_box)

        self.button_submit = QPushButton("Submit")
        self.button_submit.setStyleSheet("""
            QPushButton {
                background-color: blue;
                border-radius: 10px;
                padding: 10px;
                color: white;
            }

            QPushButton:hover {
                background-color: lightgreen;
                color: black
            }
        """)
        self.button_submit.setShortcut(Qt.Key_Return)
        self.button_submit.clicked.connect(self.kubus)

        self.text_param_kubus = QLabel("Kubus")
        self.text_param_kubus.setAlignment(Qt.AlignHCenter)
        self.text_param_kubus.setFont(self.my_font)
        self.text_param_kubus.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)

        label = QLabel() 
        # label.setPixmap(QPixmap("D:/Data_C2/Users/Documents/Tutorial_Python/pyside6/projek/img_project/label_kubus.jpg"))
        base_path = os.path.abspath(os.path.dirname(__file__))
        image_path = os.path.join(base_path, 'img_project', 'label_kubus.jpg')
        label.setPixmap(QPixmap(image_path))
        label.setAlignment(Qt.AlignCenter)
        label.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        layout_2_v_cubic = QVBoxLayout()
        layout_2_v_cubic.addWidget(self.text_param_kubus)
        layout_2_v_cubic.addWidget(label)
        layout_2_v_cubic.addLayout(layout_1_h_cubic)
        layout_2_v_cubic.addWidget(self.button_submit)

        # Create a new QVBoxLayout for the answer label
        self.layout_v_answer_cubic = QVBoxLayout()
        layout_2_v_cubic.addLayout(self.layout_v_answer_cubic)

        qwidget.setLayout(layout_2_v_cubic)

        self.setCentralWidget(qwidget)

    def kubus(self):
        try:
            if self.input_cubic.text() == "":
                s = 0

            else:
                s = float(self.input_cubic.text().replace(",","."))

            self.volume_kubus = float(s**3)
            self.luas_permukaan_kubus = float(6*(s**2))

            def check_is_int_volume() -> str:
                if self.volume_kubus.is_integer():
                    self.volume_kubus = int(self.volume_kubus)
                    return f"{str(self.volume_kubus)}"
                else:
                    a = f"{self.volume_kubus:.2f}".replace('.',',')
                    return str(a)
                
            def check_is_int_luasPer() -> str:
                if self.luas_permukaan_kubus.is_integer():
                    self.luas_permukaan_kubus = int(self.luas_permukaan_kubus)
                    return f"{str(self.luas_permukaan_kubus)}"
                else:
                    a = f"{self.luas_permukaan_kubus:.2f}".replace('.',',')
                    return str(a)

            rumus_vol_kubus = QLabel("V = s x s x s")
            rumus_vol_kubus.setFont(self.label_font)
            rumus_vol_kubus.setStyleSheet(self.color_rumus_font)

            rumus_lp_kubus = QLabel("Lp = 6 x (s x s)")
            rumus_lp_kubus.setFont(self.label_font)
            rumus_lp_kubus.setStyleSheet(self.color_rumus_font)

            self.answer_label_vol_cubic = QLabel("Volume Persegi : ")
            self.answer_label_vol_cubic.setFont(self.label_font)
            self.answer_label_lp_cubic = QLabel("Luas permukaan Persegi : ")
            self.answer_label_lp_cubic.setFont(self.label_font)



            self.jawab_vol_cubic = QLabel(f"{check_is_int_volume()} {self.combo_box_2_D_kubus.currentText()}³")
            self.jawab_vol_cubic.setFont(self.answer_font)
            self.jawab_vol_cubic.setStyleSheet(self.color_answer_font)

            self.jawab_lp_cubic = QLabel(f"{check_is_int_luasPer()} {self.combo_box_2_D_kubus.currentText()}²")
            self.jawab_lp_cubic.setFont(self.answer_font)
            self.jawab_lp_cubic.setStyleSheet(self.color_answer_font)

            while self.layout_v_answer_cubic.count():
                item = self.layout_v_answer_cubic.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.setParent(None)

            # Add the answer label to the new layout_v_answer_s
            hboxlayout1 = QHBoxLayout()
            hboxlayout1.addWidget(self.answer_label_vol_cubic)
            hboxlayout1.addWidget(rumus_vol_kubus)

            hboxlayout2 = QHBoxLayout()
            hboxlayout2.addWidget(self.answer_label_lp_cubic)
            hboxlayout2.addWidget(rumus_lp_kubus)

            self.layout_v_answer_cubic.addLayout(hboxlayout1)
            self.layout_v_answer_cubic.addWidget(self.jawab_vol_cubic )
            self.layout_v_answer_cubic.addLayout(hboxlayout2)
            self.layout_v_answer_cubic.addWidget(self.jawab_lp_cubic)
           

        except ValueError:
            self.error_input()





    def toolbar_balok(self):
        qwidget = QWidget()

        text_balok_p = QLabel("Masukkan panjang\t:")
        text_balok_l = QLabel("Masukkan lebar\t\t:")
        text_balok_t = QLabel("Masukkan tinggi\t\t:")
        self.input_balok_p = QLineEdit()
        self.input_balok_l = QLineEdit()
        self.input_balok_t = QLineEdit()

        text_balok_p.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        text_balok_l.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        text_balok_t.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.input_balok_p.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.input_balok_l.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.input_balok_t.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)


        self.combo_box_2_D_balok = QComboBox()
        self.combo_box_2_D_balok.addItem("km")
        self.combo_box_2_D_balok.addItem("hm")
        self.combo_box_2_D_balok.addItem("dam")
        self.combo_box_2_D_balok.addItem("m")
        self.combo_box_2_D_balok.addItem("dm")
        self.combo_box_2_D_balok.addItem("cm")
        self.combo_box_2_D_balok.addItem("mm")
        self.combo_box_2_D_balok.setCurrentIndex(5)

        self.layout_combo_box = QVBoxLayout()
        self.layout_combo_box.addWidget(self.combo_box_2_D_balok)

        layout_1_h_balok = QHBoxLayout()
        layout_1_h_balok.addWidget(text_balok_p)
        layout_1_h_balok.addWidget(self.input_balok_p)

        layout_2_h_balok = QHBoxLayout()
        layout_2_h_balok.addWidget(text_balok_l)
        layout_2_h_balok.addWidget(self.input_balok_l)

        layout_3_h_balok = QHBoxLayout()
        layout_3_h_balok.addWidget(text_balok_t)
        layout_3_h_balok.addWidget(self.input_balok_t)

        self.button_submit = QPushButton("Submit")
        self.button_submit.setStyleSheet("""
            QPushButton {
                background-color: blue;
                border-radius: 10px;
                padding: 10px;
                color: white;
            }

            QPushButton:hover {
                background-color: lightgreen;
                color: black
            }
        """)
        self.button_submit.setShortcut(Qt.Key_Return)
        self.button_submit.clicked.connect(self.balok)

        layout_4_h_balok = QHBoxLayout()
        label_satuan = QLabel("Satuan")
        layout_4_h_balok.addWidget(label_satuan)
        layout_4_h_balok.addLayout(self.layout_combo_box)

        label_kosong = QLabel()

        self.text_param_balok = QLabel("Balok")
        self.text_param_balok.setAlignment(Qt.AlignHCenter)
        self.text_param_balok.setFont(self.my_font)
        self.text_param_balok.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)

        label = QLabel() 
        # label.setPixmap(QPixmap("D:/Data_C2/Users/Documents/Tutorial_Python/pyside6/projek/img_project/label_balok.jpg"))
        base_path = os.path.abspath(os.path.dirname(__file__))
        image_path = os.path.join(base_path, 'img_project', 'label_balok.jpg')
        label.setPixmap(QPixmap(image_path))
        label.setAlignment(Qt.AlignCenter)
        label.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        layout_5_v_balok = QVBoxLayout()
        layout_5_v_balok.addWidget(self.text_param_balok)
        layout_5_v_balok.addWidget(label)
        layout_5_v_balok.addLayout(layout_1_h_balok)
        layout_5_v_balok.addLayout(layout_2_h_balok)
        layout_5_v_balok.addLayout(layout_3_h_balok)
        layout_5_v_balok.addWidget(label_kosong)
        layout_5_v_balok.addLayout(layout_4_h_balok)
        layout_5_v_balok.addWidget(self.button_submit)

        # Create a new QVBoxLayout for the answer label
        self.layout_v_answer_balok = QVBoxLayout()
        layout_5_v_balok.addLayout(self.layout_v_answer_balok)

        qwidget.setLayout(layout_5_v_balok)

        self.setCentralWidget(qwidget)


    def balok(self):
        try:
            if self.input_balok_p.text() == "" or self.input_balok_l.text() == "" or self.input_balok_t.text() == "":
                p = 0
                l = 0
                t = 0
            else:
                p = float(self.input_balok_p.text().replace(",","."))
                l = float(self.input_balok_l.text().replace(",","."))
                t = float(self.input_balok_t.text().replace(",","."))

            self.volume_balok = float(p*l*t)
            self.luas_permukaan_balok = float(2*((p*l) + (p*t) + (l*t)))

            #volume

            def check_is_int_volume() -> str:
                if self.volume_balok.is_integer():
                    self.volume_balok = int(self.volume_balok)
                    return f"{str(self.volume_balok)}"
                else:
                    a = f"{self.volume_balok:.2f}".replace('.',',')
                    return str(a)
                
            def check_is_int_luasPer() -> str:
                if self.luas_permukaan_balok.is_integer():
                    self.luas_permukaan_balok = int(self.luas_permukaan_balok)
                    return f"{str(self.luas_permukaan_balok)}"
                else:
                    a = f"{self.luas_permukaan_balok:.2f}".replace('.',',')
                    return str(a)

            rumus_vol_balok = QLabel("V = p x l x t")
            rumus_vol_balok.setFont(self.label_font)
            rumus_vol_balok.setStyleSheet(self.color_rumus_font)\
            
            rumus_lp_balok = QLabel("Lp = 2 x ((p x l) + (p x t) + (l x t))")
            rumus_lp_balok.setFont(self.label_font)
            rumus_lp_balok.setStyleSheet(self.color_rumus_font)

            self.answer_label_vol_balok = QLabel("Volume Balok : ")
            self.answer_label_vol_balok.setFont(self.label_font)
            self.answer_label_lp_balok = QLabel("Luas permukaan Balok : ")
            self.answer_label_lp_balok.setFont(self.label_font)
            


            self.jawab_vol_balok = QLabel(f"{check_is_int_volume()} {self.combo_box_2_D_balok.currentText()}³")
            self.jawab_vol_balok.setFont(self.answer_font)
            self.jawab_vol_balok.setStyleSheet(self.color_answer_font)

            self.jawab_lp_balok = QLabel(f"{check_is_int_luasPer()} {self.combo_box_2_D_balok.currentText()}²")
            self.jawab_lp_balok.setFont(self.answer_font)
            self.jawab_lp_balok.setStyleSheet(self.color_answer_font)


            #luas permukaan

            while self.layout_v_answer_balok.count():
                item = self.layout_v_answer_balok.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.setParent(None)

            # Add the answer label to the new layout_v_answer_r

            hboxlayout1 = QHBoxLayout()
            hboxlayout1.addWidget(self.answer_label_vol_balok)
            hboxlayout1.addWidget(rumus_vol_balok)

            hboxlayout2 = QHBoxLayout()
            hboxlayout2.addWidget(self.answer_label_lp_balok)
            hboxlayout2.addWidget(rumus_lp_balok)

            self.layout_v_answer_balok.addLayout(hboxlayout1)
            self.layout_v_answer_balok.addWidget(self.jawab_vol_balok)
            self.layout_v_answer_balok.addLayout(hboxlayout2)
            self.layout_v_answer_balok.addWidget(self.jawab_lp_balok)
         

        except ValueError:
            self.error_input()

    def toolbar_tabung(self):
        qwidget = QWidget()

        text_tabung_r = QLabel("Masukkan radius\t:")
        text_tabung_t = QLabel("Masukkan tinggi\t:")
        self.input_tabung_r = QLineEdit()
        self.input_tabung_t = QLineEdit()

        text_tabung_r.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        text_tabung_t.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.input_tabung_r.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.input_tabung_t.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)


        self.combo_box_2_D_tabung = QComboBox()
        self.combo_box_2_D_tabung.addItem("km")
        self.combo_box_2_D_tabung.addItem("hm")
        self.combo_box_2_D_tabung.addItem("dam")
        self.combo_box_2_D_tabung.addItem("m")
        self.combo_box_2_D_tabung.addItem("dm")
        self.combo_box_2_D_tabung.addItem("cm")
        self.combo_box_2_D_tabung.addItem("mm")
        self.combo_box_2_D_tabung.setCurrentIndex(5)

        self.layout_combo_box = QVBoxLayout()
        self.layout_combo_box.addWidget(self.combo_box_2_D_tabung)

        layout_1_h_tabung = QHBoxLayout()
        layout_1_h_tabung.addWidget(text_tabung_r)
        layout_1_h_tabung.addWidget(self.input_tabung_r)

        layout_2_h_tabung = QHBoxLayout()
        layout_2_h_tabung.addWidget(text_tabung_t)
        layout_2_h_tabung.addWidget(self.input_tabung_t)

        self.button_submit = QPushButton("Submit")
        self.button_submit.setStyleSheet("""
            QPushButton {
                background-color: blue;
                border-radius: 10px;
                padding: 10px;
                color: white;
            }

            QPushButton:hover {
                background-color: lightgreen;
                color: black
            }
        """)
        self.button_submit.setShortcut(Qt.Key_Return)
        self.button_submit.clicked.connect(self.tabung)

        layout_3_h_tabung = QHBoxLayout()
        label_satuan = QLabel("Satuan")
        layout_3_h_tabung.addWidget(label_satuan)
        layout_3_h_tabung.addLayout(self.layout_combo_box)

        label_kosong = QLabel()

        self.text_param_tabung = QLabel("Tabung")
        self.text_param_tabung.setAlignment(Qt.AlignHCenter)
        self.text_param_tabung.setFont(self.my_font)
        self.text_param_tabung.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)

        label = QLabel() 
        # label.setPixmap(QPixmap("D:/Data_C2/Users/Documents/Tutorial_Python/pyside6/projek/img_project/label_tabung.jpg"))
        base_path = os.path.abspath(os.path.dirname(__file__))
        image_path = os.path.join(base_path, 'img_project', 'label_tabung.jpg')
        label.setPixmap(QPixmap(image_path))
        label.setAlignment(Qt.AlignCenter)
        label.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        layout_3_v_tabung = QVBoxLayout()
        layout_3_v_tabung.addWidget(self.text_param_tabung)
        layout_3_v_tabung.addWidget(label)
        layout_3_v_tabung.addLayout(layout_1_h_tabung)
        layout_3_v_tabung.addLayout(layout_2_h_tabung)
        layout_3_v_tabung.addWidget(label_kosong)
        layout_3_v_tabung.addLayout(layout_3_h_tabung)
        layout_3_v_tabung.addWidget(self.button_submit)

        # Create a new QVBoxLayout for the answer label
        self.layout_v_answer_tabung = QVBoxLayout()
        layout_3_v_tabung.addLayout(self.layout_v_answer_tabung)

        qwidget.setLayout(layout_3_v_tabung)

        self.setCentralWidget(qwidget)


    def tabung(self):
        try:
            if self.input_tabung_r.text() == "" or self.input_tabung_t.text() == "":
                r = 0
                t = 0

            else:
                r = float(self.input_tabung_r.text().replace(",","."))
                t = float(self.input_tabung_t.text().replace(",","."))

            self.volume_tabung = (np.pi * r**2) * t
            self.luas_permukaan_tabung = 2 * np.pi * r * (r + t)

            #volume
            def check_is_int_volume() -> str:
                if self.volume_tabung.is_integer():
                    self.volume_tabung = int(self.volume_tabung)
                    return f"{str(self.volume_tabung)}"
                else:
                    a = f"{self.volume_tabung:.2f}".replace('.',',')
                    return str(a)
                
            def check_is_int_luasPer() -> str:
                if self.luas_permukaan_tabung.is_integer():
                    self.luas_permukaan_tabung = int(self.luas_permukaan_tabung)
                    return f"{str(self.luas_permukaan_tabung)}"
                else:
                    a = f"{self.luas_permukaan_tabung:.2f}".replace('.',',')
                    return str(a)

            rumus_vol_tabung = QLabel("V = (\u03C0 x r²) x t")
            rumus_vol_tabung.setFont(self.label_font)
            rumus_vol_tabung.setStyleSheet(self.color_rumus_font)

            rumus_lp_tabung = QLabel("Lp = 2 x (\u03C0 x r) x (r + t)")
            rumus_lp_tabung.setFont(self.label_font)
            rumus_lp_tabung.setStyleSheet(self.color_rumus_font)

            self.answer_label_vol_tabung = QLabel("Volume Tabung : ")
            self.answer_label_vol_tabung.setFont(self.label_font)
            self.answer_label_lp_tabung = QLabel("Luas Permukaan Tabung : ")
            self.answer_label_lp_tabung.setFont(self.label_font)
            



            #luas Permukaan
            # self.jawab_vol_tabung = QLabel(f"{str(volume)} {self.combo_box_2_D_tabung.currentText()}³\t({str(np.round(volume))} {self.combo_box_2_D_tabung.currentText()}³)")
            self.jawab_vol_tabung = QLabel(f"{check_is_int_volume()} {self.combo_box_2_D_tabung.currentText()}³")
            self.jawab_vol_tabung.setFont(self.answer_font)
            self.jawab_vol_tabung.setStyleSheet(self.color_answer_font)

            # self.jawab_lp_tabung = QLabel(f"{str(luas_permukaan)} {self.combo_box_2_D_tabung.currentText()}²\t({str(np.round(luas_permukaan))} {self.combo_box_2_D_tabung.currentText()}²)")
            self.jawab_lp_tabung = QLabel(f"{check_is_int_luasPer()} {self.combo_box_2_D_tabung.currentText()}²")
            self.jawab_lp_tabung.setFont(self.answer_font)
            self.jawab_lp_tabung.setStyleSheet(self.color_answer_font)

            while self.layout_v_answer_tabung.count():
                item = self.layout_v_answer_tabung.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.setParent(None)

            # Add the answer label to the new layout_v_answer_r
            hboxlayout1 = QHBoxLayout()
            hboxlayout1.addWidget(self.answer_label_vol_tabung)
            hboxlayout1.addWidget(rumus_vol_tabung)

            hboxlayout2 = QHBoxLayout()
            hboxlayout2.addWidget(self.answer_label_lp_tabung)
            hboxlayout2.addWidget(rumus_lp_tabung)

            self.layout_v_answer_tabung.addLayout(hboxlayout1)
            self.layout_v_answer_tabung.addWidget(self.jawab_vol_tabung)
            self.layout_v_answer_tabung.addLayout(hboxlayout2)
            self.layout_v_answer_tabung.addWidget(self.jawab_lp_tabung)
       

        except ValueError:
            self.error_input()


    def toolbar_bola(self):
        qwidget = QWidget()

        text_bola_r = QLabel("Masukkan radius\t:")
        self.input_bola_r = QLineEdit()

        text_bola_r.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.input_bola_r.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)



        self.combo_box_2_D_bola = QComboBox()
        self.combo_box_2_D_bola.addItem("km")
        self.combo_box_2_D_bola.addItem("hm")
        self.combo_box_2_D_bola.addItem("dam")
        self.combo_box_2_D_bola.addItem("m")
        self.combo_box_2_D_bola.addItem("dm")
        self.combo_box_2_D_bola.addItem("cm")
        self.combo_box_2_D_bola.addItem("mm")
        self.combo_box_2_D_bola.setCurrentIndex(5)

        self.layout_combo_box = QVBoxLayout()
        self.layout_combo_box.addWidget(self.combo_box_2_D_bola)

        layout_1_h_bola = QHBoxLayout()
        layout_1_h_bola.addWidget(text_bola_r)
        layout_1_h_bola.addWidget(self.input_bola_r)
        layout_1_h_bola.addLayout(self.layout_combo_box)

        self.button_submit = QPushButton("Submit")
        self.button_submit.setStyleSheet("""
            QPushButton {
                background-color: blue;
                border-radius: 10px;
                padding: 10px;
                color: white;
            }

            QPushButton:hover {
                background-color: lightgreen;
                color: black
            }
        """)
        self.button_submit.setShortcut(Qt.Key_Return)
        self.button_submit.clicked.connect(self.bola)

        self.text_param_bola = QLabel("Bola")
        self.text_param_bola.setAlignment(Qt.AlignHCenter)
        self.text_param_bola.setFont(self.my_font)
        self.text_param_bola.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)

        label = QLabel() 
        # label.setPixmap(QPixmap("D:/Data_C2/Users/Documents/Tutorial_Python/pyside6/projek/img_project/label_bola.jpg"))
        base_path = os.path.abspath(os.path.dirname(__file__))
        image_path = os.path.join(base_path, 'img_project', 'label_bola.jpg')
        label.setPixmap(QPixmap(image_path))
        label.setAlignment(Qt.AlignCenter)
        label.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        layout_2_v_bola = QVBoxLayout()
        layout_2_v_bola.addWidget(self.text_param_bola)
        layout_2_v_bola.addWidget(label)
        layout_2_v_bola.addLayout(layout_1_h_bola)
        layout_2_v_bola.addWidget(self.button_submit)

        # Create a new QVBoxLayout for the answer label
        self.layout_v_answer_bola = QVBoxLayout()
        layout_2_v_bola.addLayout(self.layout_v_answer_bola)

        qwidget.setLayout(layout_2_v_bola)

        self.setCentralWidget(qwidget)

    def bola(self):
        try:
            if self.input_bola_r.text() == "":
                r = 0

            else:
                r = float(self.input_bola_r.text().replace(",","."))

            self.volume_bola = 4/3 * np.pi * (r**3)
            self.luas_permukaan_bola = 4 * np.pi * (r**2)

            def check_is_int_volume() -> str:
                if self.volume_bola.is_integer():
                    self.volume_bola = int(self.volume_bola)
                    return f"{str(self.volume_bola)}"
                else:
                    a = f"{self.volume_bola:.2f}".replace('.',',')
                    return str(a)
                
            def check_is_int_luasPer() -> str:
                if self.luas_permukaan_bola.is_integer():
                    self.luas_permukaan_bola = int(self.luas_permukaan_bola)
                    return f"{str(self.luas_permukaan_bola)}"
                else:
                    a = f"{self.luas_permukaan_bola:.2f}".replace('.',',')
                    return str(a)
            
            # rumus_vol_bola = QLabel("V = 4/3 x \u03C0 x r³")
            rumus_vol_bola = QLabel("V = <sup>4</sup>&frasl;<sub>3</sub> x \u03C0 x r³")
            rumus_vol_bola.setFont(self.label_font)
            rumus_vol_bola.setStyleSheet(self.color_rumus_font)
            
            rumus_lp_bola = QLabel("Lp = 4 x \u03C0 x r²")
            rumus_lp_bola.setFont(self.label_font)
            rumus_lp_bola.setStyleSheet(self.color_rumus_font)


            self.answer_label_vol_bola = QLabel("Volume Bola : ")
            self.answer_label_vol_bola.setFont(self.label_font)

            self.answer_label_lp_bola = QLabel("Luas permukaan Bola : ")
            self.answer_label_lp_bola.setFont(self.label_font)



            # self.jawab_vol_bola = QLabel(f"{str(volume)} {self.combo_box_2_D_bola.currentText()}³\t({str(np.round(volume))} {self.combo_box_2_D_bola.currentText()}³)")
            self.jawab_vol_bola = QLabel(f"{check_is_int_volume()} {self.combo_box_2_D_bola.currentText()}³")
            self.jawab_vol_bola.setFont(self.answer_font)
            self.jawab_vol_bola.setStyleSheet(self.color_answer_font)

            # self.jawab_lp_bola = QLabel(f"{str(luas_permukaan)} {self.combo_box_2_D_bola.currentText()}²\t({str(np.round(luas_permukaan))} {self.combo_box_2_D_bola.currentText()}²)")
            self.jawab_lp_bola = QLabel(f"{check_is_int_luasPer()} {self.combo_box_2_D_bola.currentText()}²")
            self.jawab_lp_bola.setFont(self.answer_font)
            self.jawab_lp_bola.setStyleSheet(self.color_answer_font)

            while self.layout_v_answer_bola.count():
                item = self.layout_v_answer_bola.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.setParent(None)

            # Add the answer label to the new layout_v_answer_s
            hboxlayout1 = QHBoxLayout()
            hboxlayout1.addWidget(self.answer_label_vol_bola)
            hboxlayout1.addWidget(rumus_vol_bola)

            hboxlayout2 = QHBoxLayout()
            hboxlayout2.addWidget(self.answer_label_lp_bola)
            hboxlayout2.addWidget(rumus_lp_bola)

            self.layout_v_answer_bola.addLayout(hboxlayout1)
            self.layout_v_answer_bola.addWidget(self.jawab_vol_bola )
            self.layout_v_answer_bola.addLayout(hboxlayout2)
            self.layout_v_answer_bola.addWidget(self.jawab_lp_bola)
           

        except ValueError:
            self.error_input()


    


    def toolbar_prisma_segitiga(self):
        qwidget = QWidget()

        text_prismaSegitiga_a = QLabel("Masukkan panjang alas segitiga\t:")
        text_prismaSegitiga_t = QLabel("Masukkan tinggi segitiga\t\t:")
        text_prismaSegitiga_tPS = QLabel("Masukkan tinggi Prisma\t\t:")
        self.input_prismaSegitiga_a = QLineEdit()
        self.input_prismaSegitiga_t = QLineEdit()
        self.input_prismaSegitiga_tPS = QLineEdit()

        text_prismaSegitiga_a.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        text_prismaSegitiga_t.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        text_prismaSegitiga_tPS.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.input_prismaSegitiga_a.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.input_prismaSegitiga_t.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.input_prismaSegitiga_tPS.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)


        self.combo_box_2_D_prismaSegitiga = QComboBox()
        self.combo_box_2_D_prismaSegitiga.addItem("km")
        self.combo_box_2_D_prismaSegitiga.addItem("hm")
        self.combo_box_2_D_prismaSegitiga.addItem("dam")
        self.combo_box_2_D_prismaSegitiga.addItem("m")
        self.combo_box_2_D_prismaSegitiga.addItem("dm")
        self.combo_box_2_D_prismaSegitiga.addItem("cm")
        self.combo_box_2_D_prismaSegitiga.addItem("mm")
        self.combo_box_2_D_prismaSegitiga.setCurrentIndex(5)

        self.layout_combo_box = QVBoxLayout()
        self.layout_combo_box.addWidget(self.combo_box_2_D_prismaSegitiga)

        layout_1_h_prismaSegitiga = QHBoxLayout()
        layout_1_h_prismaSegitiga.addWidget(text_prismaSegitiga_a)
        layout_1_h_prismaSegitiga.addWidget(self.input_prismaSegitiga_a)

        layout_2_h_prismaSegitiga = QHBoxLayout()
        layout_2_h_prismaSegitiga.addWidget(text_prismaSegitiga_t)
        layout_2_h_prismaSegitiga.addWidget(self.input_prismaSegitiga_t)

        layout_3_h_prismaSegitiga = QHBoxLayout()
        layout_3_h_prismaSegitiga.addWidget(text_prismaSegitiga_tPS)
        layout_3_h_prismaSegitiga.addWidget(self.input_prismaSegitiga_tPS)

        self.button_submit = QPushButton("Submit")
        self.button_submit.setStyleSheet("""
            QPushButton {
                background-color: blue;
                border-radius: 10px;
                padding: 10px;
                color: white;
            }

            QPushButton:hover {
                background-color: lightgreen;
                color: black
            }
        """)
        self.button_submit.setShortcut(Qt.Key_Return)
        self.button_submit.clicked.connect(self.prismaSegitiga)

        layout_4_h_prismaSegitiga = QHBoxLayout()
        label_satuan = QLabel("Satuan")
        layout_4_h_prismaSegitiga.addWidget(label_satuan)
        layout_4_h_prismaSegitiga.addLayout(self.layout_combo_box)

        label_kosong = QLabel()

        self.text_param_Prismasegitiga = QLabel("Prisma Segitiga")
        self.text_param_Prismasegitiga.setAlignment(Qt.AlignHCenter)
        self.text_param_Prismasegitiga.setFont(self.my_font)
        self.text_param_Prismasegitiga.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)

        label = QLabel() 
        # label.setPixmap(QPixmap("D:/Data_C2/Users/Documents/Tutorial_Python/pyside6/projek/img_project/label_prisma_segitiga_2.png"))
        base_path = os.path.abspath(os.path.dirname(__file__))
        image_path = os.path.join(base_path, 'img_project', 'label_prisma_segitiga_2.png')
        label.setPixmap(QPixmap(image_path))
        label.setAlignment(Qt.AlignCenter)
        label.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)


        layout_5_v_prismaSegitiga = QVBoxLayout()
        layout_5_v_prismaSegitiga.addWidget(self.text_param_Prismasegitiga)
        layout_5_v_prismaSegitiga.addWidget(label)
        layout_5_v_prismaSegitiga.addLayout(layout_1_h_prismaSegitiga)
        layout_5_v_prismaSegitiga.addLayout(layout_2_h_prismaSegitiga)
        layout_5_v_prismaSegitiga.addLayout(layout_3_h_prismaSegitiga)
        layout_5_v_prismaSegitiga.addWidget(label_kosong)
        layout_5_v_prismaSegitiga.addLayout(layout_4_h_prismaSegitiga)
        layout_5_v_prismaSegitiga.addWidget(self.button_submit)

        # Create a new QVBoxLayout for the answer label
        self.layout_v_answer_prismaSegitiga = QVBoxLayout()
        layout_5_v_prismaSegitiga.addLayout(self.layout_v_answer_prismaSegitiga)

        qwidget.setLayout(layout_5_v_prismaSegitiga)

        self.setCentralWidget(qwidget)


    def prismaSegitiga(self): 
        try:
            if self.input_prismaSegitiga_a.text() == "" or self.input_prismaSegitiga_t.text() == "" or self.input_prismaSegitiga_tPS.text() == "":
                a = 0
                t = 0
                tPS = 0

            
            else:
                a = float(self.input_prismaSegitiga_a.text().replace(",","."))
                t = float(self.input_prismaSegitiga_t.text().replace(",","."))
                tPS = float(self.input_prismaSegitiga_tPS.text().replace(",","."))


            self.volume_prismaSegitiga = (1/2 * a * t) * tPS
            sisi_miring_alas = np.sqrt((a**2 + t**2))
            self.luas_permukaan_prismaSegitiga = (2* (1/2 * a * t)) + ((a + t + sisi_miring_alas) * tPS)

            #volume

            def check_is_int_volume() -> str:
                if self.volume_prismaSegitiga.is_integer():
                    self.volume_prismaSegitiga = int(self.volume_prismaSegitiga)
                    return f"{str(self.volume_prismaSegitiga)}"
                else:
                    a = f"{self.volume_prismaSegitiga:.2f}".replace('.',',')
                    return str(a)
                
            def check_is_int_luasPer() -> str:
                if self.luas_permukaan_prismaSegitiga.is_integer():
                    self.luas_permukaan_prismaSegitiga = int(self.luas_permukaan_prismaSegitiga)
                    return f"{str(self.luas_permukaan_prismaSegitiga)}"
                else:
                    a = f"{self.luas_permukaan_prismaSegitiga:.2f}".replace('.',',')
                    return str(a)


            rumus_vol_prismaSegitiga = QLabel("V = (a x ts / 2) x t ")
            rumus_vol_prismaSegitiga.setFont(self.label_font)
            rumus_vol_prismaSegitiga.setStyleSheet(self.color_rumus_font)

            rumus_lp_prismaSegitiga = QLabel("Lp = (2 x (a x ts / 2)) + ((a + ts + sisi miring alas) x t)")
            rumus_lp_prismaSegitiga.setFont(self.label_font)
            rumus_lp_prismaSegitiga.setStyleSheet(self.color_rumus_font)

            self.answer_label_vol_prismaSegitiga = QLabel("Volume prisma Segitiga : ")
            self.answer_label_vol_prismaSegitiga.setFont(self.label_font)

            self.answer_label_lp_prismaSegitiga = QLabel("Luas permukaan prisma Segitiga : ")
            self.answer_label_lp_prismaSegitiga.setFont(self.label_font)


            


            #luas permukaan
            self.jawab_vol_prismaSegitiga = QLabel(f"{check_is_int_volume()} {self.combo_box_2_D_prismaSegitiga.currentText()}³")
            self.jawab_vol_prismaSegitiga.setFont(self.answer_font)
            self.jawab_vol_prismaSegitiga.setStyleSheet(self.color_answer_font)

            self.jawab_lp_prismaSegitiga = QLabel(f"{check_is_int_luasPer()} {self.combo_box_2_D_prismaSegitiga.currentText()}²")
            self.jawab_lp_prismaSegitiga.setFont(self.answer_font)
            self.jawab_lp_prismaSegitiga.setStyleSheet(self.color_answer_font)

            while self.layout_v_answer_prismaSegitiga.count():
                item = self.layout_v_answer_prismaSegitiga.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.setParent(None)

            # Add the answer label to the new layout_v_answer_r
            hboxlayout1 = QHBoxLayout()
            hboxlayout1.addWidget(self.answer_label_vol_prismaSegitiga)
            hboxlayout1.addWidget(rumus_vol_prismaSegitiga)

            hboxlayout2 = QHBoxLayout()
            hboxlayout2.addWidget(self.answer_label_lp_prismaSegitiga)
            hboxlayout2.addWidget(rumus_lp_prismaSegitiga)

            self.layout_v_answer_prismaSegitiga.addLayout(hboxlayout1)
            self.layout_v_answer_prismaSegitiga.addWidget(self.jawab_vol_prismaSegitiga)
            self.layout_v_answer_prismaSegitiga.addLayout(hboxlayout2)
            self.layout_v_answer_prismaSegitiga.addWidget(self.jawab_lp_prismaSegitiga)
     

        except ValueError:
            self.error_input()




    def toolbar_prisma_segilima(self):
        qwidget = QWidget()

        text_prismaSegilima_a = QLabel("Masukkan panjang alas Segitiga\t\t:")
        text_prismaSegilima_t = QLabel("Masukkan tinggi segitiga\t\t\t:")
        text_prismaSegilima_tPS = QLabel("Masukkan tinggi Prisma Segilima\t\t:")
        self.input_prismaSegilima_a = QLineEdit()
        self.input_prismaSegilima_t = QLineEdit()
        self.input_prismaSegilima_tPS = QLineEdit()

        text_prismaSegilima_a.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        text_prismaSegilima_t.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        text_prismaSegilima_tPS.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.input_prismaSegilima_a.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.input_prismaSegilima_t.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.input_prismaSegilima_tPS.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)


        self.combo_box_2_D_prismaegilima = QComboBox()
        self.combo_box_2_D_prismaegilima.addItem("km")
        self.combo_box_2_D_prismaegilima.addItem("hm")
        self.combo_box_2_D_prismaegilima.addItem("dam")
        self.combo_box_2_D_prismaegilima.addItem("m")
        self.combo_box_2_D_prismaegilima.addItem("dm")
        self.combo_box_2_D_prismaegilima.addItem("cm")
        self.combo_box_2_D_prismaegilima.addItem("mm")
        self.combo_box_2_D_prismaegilima.setCurrentIndex(5)

        self.layout_combo_box = QVBoxLayout()
        self.layout_combo_box.addWidget(self.combo_box_2_D_prismaegilima)

        layout_1_h_prismaSegilima = QHBoxLayout()
        layout_1_h_prismaSegilima.addWidget(text_prismaSegilima_a)
        layout_1_h_prismaSegilima.addWidget(self.input_prismaSegilima_a)

        layout_2_h_prismaSegilima = QHBoxLayout()
        layout_2_h_prismaSegilima.addWidget(text_prismaSegilima_t)
        layout_2_h_prismaSegilima.addWidget(self.input_prismaSegilima_t)

        layout_3_h_prismaSegilima = QHBoxLayout()
        layout_3_h_prismaSegilima.addWidget(text_prismaSegilima_tPS)
        layout_3_h_prismaSegilima.addWidget(self.input_prismaSegilima_tPS)

        self.button_submit = QPushButton("Submit")
        self.button_submit.setStyleSheet("""
            QPushButton {
                background-color: blue;
                border-radius: 10px;
                padding: 10px;
                color: white;
            }

            QPushButton:hover {
                background-color: lightgreen;
                color: black
            }
        """)
        self.button_submit.setShortcut(Qt.Key_Return)
        self.button_submit.clicked.connect(self.prismaSegilima)

        layout_4_h_prismaSegilima = QHBoxLayout()
        label_satuan = QLabel("Satuan")
        layout_4_h_prismaSegilima.addWidget(label_satuan)
        layout_4_h_prismaSegilima.addLayout(self.layout_combo_box)

        label_kosong = QLabel()

        self.text_param_Prismasegilima = QLabel("Prisma Segilima")
        self.text_param_Prismasegilima.setAlignment(Qt.AlignHCenter)
        self.text_param_Prismasegilima.setFont(self.my_font)
        self.text_param_Prismasegilima.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)

        label = QLabel() 
        # label.setPixmap(QPixmap("D:/Data_C2/Users/Documents/Tutorial_Python/pyside6/projek/img_project/label_prisma_segilima.png"))
        base_path = os.path.abspath(os.path.dirname(__file__))
        image_path = os.path.join(base_path, 'img_project', 'label_prisma_segilima.png')
        label.setPixmap(QPixmap(image_path))
        label.setAlignment(Qt.AlignCenter)
        label.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)


        layout_5_v_prismaSegilima = QVBoxLayout()
        layout_5_v_prismaSegilima.addWidget(self.text_param_Prismasegilima)
        layout_5_v_prismaSegilima.addWidget(label)
        layout_5_v_prismaSegilima.addLayout(layout_1_h_prismaSegilima)
        layout_5_v_prismaSegilima.addLayout(layout_2_h_prismaSegilima)
        layout_5_v_prismaSegilima.addLayout(layout_3_h_prismaSegilima)
        layout_5_v_prismaSegilima.addWidget(label_kosong)
        layout_5_v_prismaSegilima.addLayout(layout_4_h_prismaSegilima)
        layout_5_v_prismaSegilima.addWidget(self.button_submit)

        # Create a new QVBoxLayout for the answer label
        self.layout_v_answer_prismaSegilima = QVBoxLayout()
        layout_5_v_prismaSegilima.addLayout(self.layout_v_answer_prismaSegilima)

        qwidget.setLayout(layout_5_v_prismaSegilima)

        self.setCentralWidget(qwidget)


    def prismaSegilima(self): 
        try:
            if self.input_prismaSegilima_a.text() == "" or self.input_prismaSegilima_t.text() == "" or self.input_prismaSegilima_tPS.text() == "":
                a = 0
                t = 0
                tPS = 0
            else:
                a = float(self.input_prismaSegilima_a.text().replace(",","."))
                t = float(self.input_prismaSegilima_t.text().replace(",","."))
                tPS = float(self.input_prismaSegilima_tPS.text().replace(",","."))

            self.volume_prismaSegilima = ((1/2 * a * t) * 5)  * tPS
            self.luas_permukaan_prismaSegilima = (2 * ((1/2 * a * t) * 5)) + (5 * (a * tPS))
            #volume

            def check_is_int_volume() -> str:
                if self.volume_prismaSegilima.is_integer():
                    self.volume_prismaSegilima = int(self.volume_prismaSegilima)
                    return f"{str(self.volume_prismaSegilima)}"
                else:
                    a = f"{self.volume_prismaSegilima:.2f}".replace('.',',')
                    return str(a)
                
            def check_is_int_luasPer() -> str:
                if self.luas_permukaan_prismaSegilima.is_integer():
                    self.luas_permukaan_prismaSegilima = int(self.luas_permukaan_prismaSegilima)
                    return f"{str(self.luas_permukaan_prismaSegilima)}"
                else:
                    a = f"{self.luas_permukaan_prismaSegilima:.2f}".replace('.',',')
                    return str(a)

            rumus_vol_prismaSegilima = QLabel("V = (a x ts / 2) x 5 x tp")
            rumus_vol_prismaSegilima.setFont(self.label_font)
            rumus_vol_prismaSegilima.setStyleSheet(self.color_rumus_font)

            # rumus_lp_prismaSegilima = QLabel("Lp = (2 x ((1/2 x a x ts) x 5)) + (5 x (a x tp)) ")
            rumus_lp_prismaSegilima = QLabel("Lp = (2 x ((<sup>1</sup>&frasl;<sub>2</sub> x a x ts) x 5)) + (5 x (a x tp)) ")
            rumus_lp_prismaSegilima.setFont(self.label_font)
            rumus_lp_prismaSegilima.setStyleSheet(self.color_rumus_font)

            #luas permukaan
            self.answer_label_vol_prismaSegilima = QLabel("Volume prisma Segilima : ")
            self.answer_label_vol_prismaSegilima.setFont(self.label_font)

            self.answer_label_lp_prismaSegilima = QLabel("Luas permukaan prisma Segilima : ")
            self.answer_label_lp_prismaSegilima.setFont(self.label_font)



            self.jawab_vol_prismaSegilima = QLabel(f"{check_is_int_volume()} {self.combo_box_2_D_prismaegilima.currentText()}³")
            self.jawab_vol_prismaSegilima.setFont(self.answer_font)
            self.jawab_vol_prismaSegilima.setStyleSheet(self.color_answer_font)

            self.jawab_lp_prismaSegilima = QLabel(f"{check_is_int_luasPer()} {self.combo_box_2_D_prismaegilima.currentText()}²")
            self.jawab_lp_prismaSegilima.setFont(self.answer_font)
            self.jawab_lp_prismaSegilima.setStyleSheet(self.color_answer_font)


            while self.layout_v_answer_prismaSegilima.count():
                item = self.layout_v_answer_prismaSegilima.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.setParent(None)

            # Add the answer label to the new layout_v_answer_r
            hboxlayout1 = QHBoxLayout()
            hboxlayout1.addWidget(self.answer_label_vol_prismaSegilima)
            hboxlayout1.addWidget(rumus_vol_prismaSegilima)

            hboxlayout2 = QHBoxLayout()
            hboxlayout2.addWidget(self.answer_label_lp_prismaSegilima)
            hboxlayout2.addWidget(rumus_lp_prismaSegilima)

            self.layout_v_answer_prismaSegilima.addLayout(hboxlayout1)
            self.layout_v_answer_prismaSegilima.addWidget(self.jawab_vol_prismaSegilima)
            self.layout_v_answer_prismaSegilima.addLayout(hboxlayout2)
            self.layout_v_answer_prismaSegilima.addWidget(self.jawab_lp_prismaSegilima)
           

        except ValueError:
            self.error_input()



    def toolbar_prisma_segienam(self):
        qwidget = QWidget()

        text_prismaSegienam_a = QLabel("Masukkan panjang alas Segitiga\t\t:")
        text_prismaSegienam_tPS = QLabel("Masukkan tinggi Prisma Segienam\t\t:")
        self.input_prismaSegienam_a = QLineEdit()
        self.input_prismaSegienam_tPS = QLineEdit()

        text_prismaSegienam_a.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        text_prismaSegienam_tPS.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.input_prismaSegienam_a.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed) 
        self.input_prismaSegienam_tPS.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        self.combo_box_2_D_prismaSegienam = QComboBox()
        self.combo_box_2_D_prismaSegienam.addItem("km")
        self.combo_box_2_D_prismaSegienam.addItem("hm")
        self.combo_box_2_D_prismaSegienam.addItem("dam")
        self.combo_box_2_D_prismaSegienam.addItem("m")
        self.combo_box_2_D_prismaSegienam.addItem("dm")
        self.combo_box_2_D_prismaSegienam.addItem("cm")
        self.combo_box_2_D_prismaSegienam.addItem("mm")
        self.combo_box_2_D_prismaSegienam.setCurrentIndex(5)

        self.layout_combo_box = QVBoxLayout()
        self.layout_combo_box.addWidget(self.combo_box_2_D_prismaSegienam)

        layout_1_h_prismaSegienam = QHBoxLayout()
        layout_1_h_prismaSegienam.addWidget(text_prismaSegienam_a)
        layout_1_h_prismaSegienam.addWidget(self.input_prismaSegienam_a)

        layout_2_h_prismaSegienam = QHBoxLayout()
        layout_2_h_prismaSegienam.addWidget(text_prismaSegienam_tPS)
        layout_2_h_prismaSegienam.addWidget(self.input_prismaSegienam_tPS)


        self.button_submit = QPushButton("Submit")
        self.button_submit.setStyleSheet("""
            QPushButton {
                background-color: blue;
                border-radius: 10px;
                padding: 10px;
                color: white;
            }

            QPushButton:hover {
                background-color: lightgreen;
                color: black
            }
        """)
        self.button_submit.setShortcut(Qt.Key_Return)
        self.button_submit.clicked.connect(self.prismaSegienam)

        layout_3_h_prismaSegienam = QHBoxLayout()
        label_satuan = QLabel("Satuan")
        layout_3_h_prismaSegienam.addWidget(label_satuan)
        layout_3_h_prismaSegienam.addLayout(self.layout_combo_box)

        label_kosong = QLabel()

        self.text_param_Prismasegienam = QLabel("Prisma Segienam")
        self.text_param_Prismasegienam.setAlignment(Qt.AlignHCenter)
        self.text_param_Prismasegienam.setFont(self.my_font)
        self.text_param_Prismasegienam.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)

        label = QLabel() 
        # label.setPixmap(QPixmap("D:/Data_C2/Users/Documents/Tutorial_Python/pyside6/projek/img_project/label_prisma_segienam.png"))
        base_path = os.path.abspath(os.path.dirname(__file__))
        image_path = os.path.join(base_path, 'img_project', 'label_prisma_segienam.png')
        label.setPixmap(QPixmap(image_path))
        label.setAlignment(Qt.AlignCenter)
        label.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        layout_4_v_prismaSegienam = QVBoxLayout()
        layout_4_v_prismaSegienam.addWidget(self.text_param_Prismasegienam)
        layout_4_v_prismaSegienam.addWidget(label)
        layout_4_v_prismaSegienam.addLayout(layout_1_h_prismaSegienam)
        layout_4_v_prismaSegienam.addLayout(layout_2_h_prismaSegienam)
        layout_4_v_prismaSegienam.addWidget(label_kosong)
        layout_4_v_prismaSegienam.addLayout(layout_3_h_prismaSegienam)
        layout_4_v_prismaSegienam.addWidget(self.button_submit)

        # Create a new QVBoxLayout for the answer label
        self.layout_v_answer_prismaSegienam = QVBoxLayout()
        layout_4_v_prismaSegienam.addLayout(self.layout_v_answer_prismaSegienam)

        qwidget.setLayout(layout_4_v_prismaSegienam)

        self.setCentralWidget(qwidget)


    def prismaSegienam(self):
        try: 
            if self.input_prismaSegienam_a.text() == "" or self.input_prismaSegienam_tPS.text() == "":
                a = 0
                tPS = 0
            else:
                a = float(self.input_prismaSegienam_a.text().replace(",","."))
                tPS = float(self.input_prismaSegienam_tPS.text().replace(",","."))

            sisi_miring = np.sqrt(((a**2) - ((a / 2)**2)))
            luas_alas = (1/2 * a * sisi_miring) * 6
            self.volume_prismaSegienam = luas_alas * tPS
            self.luas_permukaan_prismaSegienam = (luas_alas * 2) + ((a * tPS) * 6)
            #volume

            def check_is_int_volume() -> str:
                if self.volume_prismaSegienam.is_integer():
                    self.volume_prismaSegienam = int(self.volume_prismaSegienam)
                    return f"{str(self.volume_prismaSegienam)}"
                else:
                    a = f"{self.volume_prismaSegienam:.2f}".replace('.',',')
                    return str(a)
                
            def check_is_int_luasPer() -> str:
                if self.luas_permukaan_prismaSegienam.is_integer():
                    self.luas_permukaan_prismaSegienam = int(self.luas_permukaan_prismaSegienam)
                    return f"{str(self.luas_permukaan_prismaSegienam)}"
                else:
                    a = f"{self.luas_permukaan_prismaSegienam:.2f}".replace('.',',')
                    return str(a)


            rumus_vol_prismaSegienam = QLabel("V = luas alas x t")
            rumus_vol_prismaSegienam.setFont(self.label_font)
            rumus_vol_prismaSegienam.setStyleSheet(self.color_rumus_font)

            rumus_lp_prismaSegienam = QLabel("Lp = (luas alas x 2) + ((a x t) x 6)")
            rumus_lp_prismaSegienam.setFont(self.label_font)
            rumus_lp_prismaSegienam.setStyleSheet(self.color_rumus_font)


            self.answer_label_vol_prismaSegienam = QLabel("Volume prisma Segilima : ")
            self.answer_label_vol_prismaSegienam.setFont(self.label_font)

            self.answer_label_lp_prismaSegienam = QLabel("Luas permukaan prisma Segilima : ")
            self.answer_label_lp_prismaSegienam.setFont(self.label_font)



            #luas permukaan
            self.jawab_vol_prismaSegienam = QLabel(f"{check_is_int_volume()} {self.combo_box_2_D_prismaSegienam.currentText()}³")
            self.jawab_vol_prismaSegienam.setFont(self.answer_font)
            self.jawab_vol_prismaSegienam.setStyleSheet(self.color_answer_font)

            self.jawab_lp_prismaSegienam = QLabel(f"{check_is_int_luasPer()} {self.combo_box_2_D_prismaSegienam.currentText()}²")
            self.jawab_lp_prismaSegienam.setFont(self.answer_font)
            self.jawab_lp_prismaSegienam.setStyleSheet(self.color_answer_font)

            while self.layout_v_answer_prismaSegienam.count():
                item = self.layout_v_answer_prismaSegienam.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.setParent(None)

            # Add the answer label to the new layout_v_answer_r
            hboxlayout1 = QHBoxLayout()
            hboxlayout1.addWidget(self.answer_label_vol_prismaSegienam)
            hboxlayout1.addWidget(rumus_vol_prismaSegienam)

            hboxlayout2 = QHBoxLayout()
            hboxlayout2.addWidget(self.answer_label_lp_prismaSegienam)
            hboxlayout2.addWidget(rumus_lp_prismaSegienam)

            self.layout_v_answer_prismaSegienam.addLayout(hboxlayout1)
            self.layout_v_answer_prismaSegienam.addWidget(self.jawab_vol_prismaSegienam)
            self.layout_v_answer_prismaSegienam.addLayout(hboxlayout2)
            self.layout_v_answer_prismaSegienam.addWidget(self.jawab_lp_prismaSegienam)
          

        except ValueError:
            self.error_input()




    def toolbar_prisma_segidelapan(self):
        qwidget = QWidget()

        text_prismaSegidelapan_a = QLabel("Masukkan panjang sisi alas Segidelapan\t\t:")
        text_prismaSegidelapan_tPS = QLabel("Masukkan tinggi Prisma Segidelapan\t\t:")
        self.input_prismaSegidelapan_a = QLineEdit()
        self.input_prismaSegidelapan_tPS = QLineEdit()

        text_prismaSegidelapan_a.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        text_prismaSegidelapan_tPS.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.input_prismaSegidelapan_a.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed) 
        self.input_prismaSegidelapan_tPS.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)


        self.combo_box_2_D_prismaSegidelapan = QComboBox()
        self.combo_box_2_D_prismaSegidelapan.addItem("km")
        self.combo_box_2_D_prismaSegidelapan.addItem("hm")
        self.combo_box_2_D_prismaSegidelapan.addItem("dam")
        self.combo_box_2_D_prismaSegidelapan.addItem("m")
        self.combo_box_2_D_prismaSegidelapan.addItem("dm")
        self.combo_box_2_D_prismaSegidelapan.addItem("cm")
        self.combo_box_2_D_prismaSegidelapan.addItem("mm")
        self.combo_box_2_D_prismaSegidelapan.setCurrentIndex(5)

        self.layout_combo_box = QVBoxLayout()
        self.layout_combo_box.addWidget(self.combo_box_2_D_prismaSegidelapan)

        layout_1_h_prismaSegidelapan = QHBoxLayout()
        layout_1_h_prismaSegidelapan.addWidget(text_prismaSegidelapan_a)
        layout_1_h_prismaSegidelapan.addWidget(self.input_prismaSegidelapan_a)

        layout_2_h_prismaSegidelapan = QHBoxLayout()
        layout_2_h_prismaSegidelapan.addWidget(text_prismaSegidelapan_tPS)
        layout_2_h_prismaSegidelapan.addWidget(self.input_prismaSegidelapan_tPS)


        self.button_submit = QPushButton("Submit")
        self.button_submit.setStyleSheet("""
            QPushButton {
                background-color: blue;
                border-radius: 10px;
                padding: 10px;
                color: white;
            }

            QPushButton:hover {
                background-color: lightgreen;
                color: black
            }
        """)
        self.button_submit.setShortcut(Qt.Key_Return)
        self.button_submit.clicked.connect(self.prismaSegidelapan)

        layout_3_h_prismaSegidelapan = QHBoxLayout()
        label_satuan = QLabel("Satuan")
        layout_3_h_prismaSegidelapan.addWidget(label_satuan)
        layout_3_h_prismaSegidelapan.addLayout(self.layout_combo_box)

        label_kosong = QLabel()

        self.text_param_Prismasegidelapan = QLabel("Prisma Segidelapan")
        self.text_param_Prismasegidelapan.setAlignment(Qt.AlignHCenter)
        self.text_param_Prismasegidelapan.setFont(self.my_font)
        self.text_param_Prismasegidelapan.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)

        label = QLabel() 
        # label.setPixmap(QPixmap("D:/Data_C2/Users/Documents/Tutorial_Python/pyside6/projek/img_project/label_prisma_segidelapan.jpg"))
        base_path = os.path.abspath(os.path.dirname(__file__))
        image_path = os.path.join(base_path, 'img_project', 'label_prisma_segidelapan.jpg')
        label.setPixmap(QPixmap(image_path))
        # label.setPixmap(QPixmap("label_prisma_segienam.png"))
        label.setAlignment(Qt.AlignCenter)
        label.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)



        layout_4_v_prismaSegidelapan = QVBoxLayout()
        layout_4_v_prismaSegidelapan.addWidget(self.text_param_Prismasegidelapan)
        layout_4_v_prismaSegidelapan.addWidget(label)
        layout_4_v_prismaSegidelapan.addLayout(layout_1_h_prismaSegidelapan)
        layout_4_v_prismaSegidelapan.addLayout(layout_2_h_prismaSegidelapan)
        layout_4_v_prismaSegidelapan.addWidget(label_kosong)
        layout_4_v_prismaSegidelapan.addLayout(layout_3_h_prismaSegidelapan)
        layout_4_v_prismaSegidelapan.addWidget(self.button_submit)

        # Create a new QVBoxLayout for the answer label
        self.layout_v_answer_prismaSegidelapan = QVBoxLayout()
        layout_4_v_prismaSegidelapan.addLayout(self.layout_v_answer_prismaSegidelapan)

        qwidget.setLayout(layout_4_v_prismaSegidelapan)

        self.setCentralWidget(qwidget)


    def prismaSegidelapan(self): 
        try:
            if self.input_prismaSegidelapan_a.text() == "" or self.input_prismaSegidelapan_tPS.text() == "":
                a = 0
                tPS = 0
            else:
                a = float(self.input_prismaSegidelapan_a.text().replace(",","."))
                tPS = float(self.input_prismaSegidelapan_tPS.text().replace(",","."))

            sisi_miring = np.sqrt(((a**2) - ((a / 2)**2)))
            luas_alas = (2 + (2*np.sqrt(2))) * a**2
            self.volume_prismaSegidelapan = luas_alas * tPS
            self.luas_permukaan_prismaSegidelapan = (luas_alas * 2) + ((a * tPS) * 8)
            #volume

            def check_is_int_volume() -> str:
                if self.volume_prismaSegidelapan.is_integer():
                    self.volume_prismaSegidelapan = int(self.volume_prismaSegidelapan)
                    return f"{str(self.volume_prismaSegidelapan)}"
                else:
                    a = f"{self.volume_prismaSegidelapan:.2f}".replace('.',',')
                    return str(a)
                
            def check_is_int_luasPer() -> str:
                if self.luas_permukaan_prismaSegidelapan.is_integer():
                    self.luas_permukaan_prismaSegidelapan = int(self.luas_permukaan_prismaSegidelapan)
                    return f"{str(self.luas_permukaan_prismaSegidelapan)}"
                else:
                    a = f"{self.luas_permukaan_prismaSegidelapan:.2f}".replace('.',',')
                    return str(a)
                
            rumus_vol_prismaSegidelapan = QLabel("V = luas alas x T")
            rumus_vol_prismaSegidelapan.setFont(self.label_font)
            rumus_vol_prismaSegidelapan.setStyleSheet(self.color_rumus_font)

            rumus_lp_prismaSegidelapan = QLabel("Lp = (luas alas x 2) + ((a x t) x 8)")
            rumus_lp_prismaSegidelapan.setFont(self.label_font)
            rumus_lp_prismaSegidelapan.setStyleSheet(self.color_rumus_font)


            self.answer_label_vol_prismaSegidelapan = QLabel("Volume prisma Segidelapan : ")
            self.answer_label_vol_prismaSegidelapan.setFont(self.label_font)

            self.answer_label_lp_prismaSegidelapan = QLabel("Luas permukaan prisma Segidelapan : ")
            self.answer_label_lp_prismaSegidelapan.setFont(self.label_font)



            #luas permukaan
            self.jawab_vol_prismaSegidelapan = QLabel(f"{check_is_int_volume()} {self.combo_box_2_D_prismaSegidelapan.currentText()}³")
            self.jawab_vol_prismaSegidelapan.setFont(self.answer_font)
            self.jawab_vol_prismaSegidelapan.setStyleSheet(self.color_answer_font)

            self.jawab_lp_prismaSegidelapan = QLabel(f"{check_is_int_luasPer()} {self.combo_box_2_D_prismaSegidelapan.currentText()}²")
            self.jawab_lp_prismaSegidelapan.setFont(self.answer_font)
            self.jawab_lp_prismaSegidelapan.setStyleSheet(self.color_answer_font)

            while self.layout_v_answer_prismaSegidelapan.count():
                item = self.layout_v_answer_prismaSegidelapan.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.setParent(None)

            # Add the answer label to the new layout_v_answer_r

            hboxlayout1 = QHBoxLayout()
            hboxlayout1.addWidget(self.answer_label_vol_prismaSegidelapan)
            hboxlayout1.addWidget(rumus_vol_prismaSegidelapan)

            hboxlayout2 = QHBoxLayout()
            hboxlayout2.addWidget(self.answer_label_lp_prismaSegidelapan)
            hboxlayout2.addWidget(rumus_lp_prismaSegidelapan)

            self.layout_v_answer_prismaSegidelapan.addLayout(hboxlayout1)
            self.layout_v_answer_prismaSegidelapan.addWidget(self.jawab_vol_prismaSegidelapan)
            self.layout_v_answer_prismaSegidelapan.addLayout(hboxlayout2)
            self.layout_v_answer_prismaSegidelapan.addWidget(self.jawab_lp_prismaSegidelapan)
         

        except ValueError:
            self.error_input()


   

    def error_input(self) -> QMessageBox.critical:
        message = QMessageBox()
        message.setMinimumSize(700,200)
        message.setWindowTitle("Error Message!!!")
        # message.setWindowIcon(QIcon("D:/Data_C2/Users/Documents/Tutorial_Python/pyside6/projek/img_project/browser.png"))
        base_path = os.path.abspath(os.path.dirname(__file__))
        image_path = os.path.join(base_path, 'img_project', 'browser.png')
        message.setWindowIcon(QIcon(image_path))
        message.setText("Input Invalid")
        message.setInformativeText("Input yang Anda Masukkan tidak sesuai.\nInput harus berupa :\n1. Bilangan Bulat       --> e.g. (1)\n2. Bilangan Desimal  --> e.g. (1,2)\n3. None")
        message.setIcon(QMessageBox.Critical)
        # message.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)     # menampilkan 2 button click
        message.setStandardButtons(QMessageBox.Ok)                        # menampilkan 1 button click
        message.setDefaultButton(QMessageBox.Ok)

        ret = message.exec()
        if ret == QMessageBox.Ok:
            None

    

    def quit_app(self):
        message = QMessageBox()
        message.setMinimumSize(600,100)
        message.setWindowTitle("Exit The Program!!!")
        message.setIcon(QMessageBox.Warning)
        # message.setWindowIcon(QIcon("D:/Data_C2/Users/Documents/Tutorial_Python/pyside6/projek/img_project/logout.png"))
        base_path = os.path.abspath(os.path.dirname(__file__))
        image_path = os.path.join(base_path, 'img_project', 'logout.png')
        message.setWindowIcon(QIcon(image_path))

        font = QFont("Times", 12,QFont.DemiBold)
        message.setFont(font)
        message.setStyleSheet("QLabel{color: red;}")
        message.setText("Are You Sure To Quit the Program ?")
        message.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

        ret = message.exec()
        if ret == QMessageBox.Ok:
            self.app.quit()
        
        else:
            pass



    def copyright_app(self):
        MIT_LICENSE = """
        Copyright <2023> <COPYRIGHT HOLDER>

        Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

        The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

        THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
        """

       
        font = QFont("Times", 12)
        

        message = QMessageBox()

   
      

        license_text = "Copyright 2023\t@fandigit7@gmail.com\n\n"\
                    "Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:\n\n"\
                    "The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.\n\n"\
                    "THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE."

     
        message.setTextFormat(Qt.PlainText)
        message.setText(license_text)
        message.setTextInteractionFlags(Qt.TextSelectableByMouse)
   




        message.setMinimumSize(500,500)
        # message.setMaximumSize(500,500)
        # message.setText(MIT_LICENSE)
        message.setFont(font)
        # message.setStyleSheet()

        message.setWindowTitle("Copyrigth")
        # message.setInformativeText(MIT_LICENSE)
        # message.setWindowIcon(QIcon("D:/Data_C2/Users/Documents/Tutorial_Python/pyside6/projek/img_project/law.png"))
        base_path = os.path.abspath(os.path.dirname(__file__))
        image_path = os.path.join(base_path, 'img_project', 'law.png')
        message.setWindowIcon(QIcon(image_path))

        ret = message.exec()


    def help_menu(self):
        # qwidget = QWidget()
    
        KEY_BANGUN_DATAR = '''
        1. Persegi\t\t>>> Ctrl + 1
        2. Persegi Panjang\t>>> Ctrl + 2
        3. Lingkaran\t\t>>> Ctrl + 3
        4. Layang - Layang\t>>> Ctrl + 4
        5. Segitiga\t\t>>> Ctrl + 5
        6. Belah Ketupat\t\t>>> Ctrl + 6
        7. Trapesium Sama Kaki\t>>> Ctrl + 7
        8. Trapesium Siku - Siku\t>>> Ctrl + 8
        9. Jajar Genjang\t\t>>> Ctrl + 9\n
        '''
       

        KEY_BANGUN_RUANG = '''
        1. Kubus\t\t>>> Ctrl + Shift + 1
        2. Balok\t\t>>> Ctrl + Shift + 2
        3. Tabung\t\t>>> Ctrl + Shift + 3
        4. Bola\t\t>>> Ctrl + Shift + 4
        5. Prisma Segitiga\t>>> Ctrl + Shift + 5
        6. Prisma Segilima\t>>> Ctrl + Shift + 6
        7. Prisma Segienam\t>>> Ctrl + Shift + 7
        8. Prisma Segidelapan\t>>> Ctrl + Shift + 8
        '''

        text_title = QLabel("SELAMAT DATANG DI APLIKASI KALKULATOR SEDERHANA KAMI")
        text_title.setTextInteractionFlags(Qt.TextSelectableByMouse)

        text_Note = QLabel("\n\n\nBantuan Untuk Menggunakan Aplikasi Kalkulator Ini.\n")
        text_Note.setTextInteractionFlags(Qt.TextSelectableByMouse)

        text_tutorial_1 = QLabel("1. Pilih Bangun Datar atau Bangun Ruang yang ingin dipilih di Toolbar sebelah kiri\n    Note : Memilih Bangun dapat dengan menggunakan shortcut. Untuk lebih Jelasnya, cek di bagian 'Shortcut Key' di bawah.")
        text_tutorial_1.setTextInteractionFlags(Qt.TextSelectableByMouse)
        
        gambar_1 = QLabel() 
        # gambar_1.setPixmap(QPixmap("D:/Data_C2/Users/Documents/Tutorial_Python/pyside6/projek/img_project/help_1.png"))
        base_path = os.path.abspath(os.path.dirname(__file__))
        image_path = os.path.join(base_path, 'img_project', 'help_1.png')
        gambar_1.setPixmap(QPixmap(image_path))
        gambar_2 = QLabel()
        # gambar_2.setPixmap(QPixmap("D:/Data_C2/Users/Documents/Tutorial_Python/pyside6/projek/img_project/help_2.png"))
        base_path = os.path.abspath(os.path.dirname(__file__))
        image_path = os.path.join(base_path, 'img_project', 'help_2.png')
        gambar_2.setPixmap(QPixmap(image_path))
        text_tutorial_2 = QLabel("2. Masukkan Angka yang ingin dihitung di kotak yang disediakan")
        text_tutorial_2.setTextInteractionFlags(Qt.TextSelectableByMouse)

        text_tutorial_3 = QLabel("3. Setelah Memasukkan Angka tekan tombol 'Submit' atau tekan 'Enter' di Keyboard")
        text_tutorial_3.setTextInteractionFlags(Qt.TextSelectableByMouse)

        text_tutorial_4 = QLabel("4. Dan, Anda akan mendapatkan jawaban di bagian bawah.\n\n")
        text_tutorial_4.setTextInteractionFlags(Qt.TextSelectableByMouse)

        text_Note_2 = QLabel("\n\n\n\n\n\n\n\n\n\nShortcut Key Bangun Datar And Bangun Ruang :")
        text_Note_2.setTextInteractionFlags(Qt.TextSelectableByMouse)

        text_key_class_bangunDatar = QLabel("class Bangun Datar :")
        text_key_class_bangunDatar.setTextInteractionFlags(Qt.TextSelectableByMouse)
        
        text_key_bangunDatar = QLabel(KEY_BANGUN_DATAR)
        text_key_bangunDatar.setTextInteractionFlags(Qt.TextSelectableByMouse)
        

        text_key_class_bangunRuang = QLabel("class Bangun Ruang :")
        text_key_class_bangunRuang.setTextInteractionFlags(Qt.TextSelectableByMouse)

        text_key_bangunRuang = QLabel(KEY_BANGUN_RUANG)
        text_key_bangunRuang.setTextInteractionFlags(Qt.TextSelectableByMouse)





        ### DESIGN
        title_font = QFont("Times", 16, QFont.ExtraBold)
        note_1_font = QFont("Times", 14, QFont.Medium)
        tutorial_font = QFont("Times", 12, QFont.Normal)
        note_2_font = QFont("Times", 14, QFont.DemiBold)
        key_font = QFont("Times",12, QFont.Medium)


        ## Implementation
        text_title.setFont(title_font)
        text_title.setStyleSheet("color : green")
        text_Note.setFont(note_1_font)
        text_tutorial_1.setFont(tutorial_font)
        text_tutorial_2.setFont(tutorial_font)
        text_tutorial_3.setFont(tutorial_font)
        text_tutorial_4.setFont(tutorial_font)
        text_Note_2.setFont(note_2_font)
        text_Note_2.setStyleSheet("color : red")
        text_key_class_bangunDatar.setFont(key_font)
        text_key_bangunDatar.setFont(key_font)
        text_key_class_bangunRuang.setFont(key_font)
        text_key_bangunRuang.setFont(key_font)

        scroll_widget = QScrollArea()

        # text_s.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.MinimumExpanding)
        # self.input_s.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)

        vboxlayout = QVBoxLayout()
        vboxlayout.addWidget(text_title)
        vboxlayout.addWidget(text_Note)
        vboxlayout.addWidget(text_tutorial_1)
        vboxlayout.addWidget(text_tutorial_2)
        vboxlayout.addWidget(text_tutorial_3)
        vboxlayout.addWidget(text_tutorial_4)
        vboxlayout.addWidget(text_Note_2)
        vboxlayout.addWidget(text_key_class_bangunDatar)
        vboxlayout.addWidget(text_key_bangunDatar)
        vboxlayout.addWidget(text_key_class_bangunRuang)
        vboxlayout.addWidget(text_key_bangunRuang)
        vboxlayout.addWidget(scroll_widget)



        # qwidget.setLayout(vboxlayout)
        
        # self.setCentralWidget(qwidget)
        # self.centralWidget().setStyleSheet("background-color: rgb(255, 235, 138)")


        widget = QWidget()

        # membuat layout vertikal
        layout = QVBoxLayout(widget)

        # membuat QScrollArea
        scroll_area = QScrollArea()

        # membuat widget yang akan di-scroll
        scroll_widget = QWidget()
        scroll_layout = QVBoxLayout(scroll_widget)

        # menambahkan beberapa label ke dalam scroll_widget
        # for i in range(50):
        #     label = QLabel(f"Label {i}")
        #     scroll_layout.addWidget(label)
        # scroll_layout.addLayout(vboxlayout)
        scroll_layout.addWidget(text_title)
        scroll_layout.addWidget(text_Note)
        scroll_layout.addWidget(text_tutorial_1)
        scroll_layout.addWidget(gambar_1)
        scroll_layout.addWidget(text_tutorial_2)
        scroll_layout.addWidget(text_tutorial_3)
        scroll_layout.addWidget(text_tutorial_4)
        scroll_layout.addWidget(gambar_2)
        scroll_layout.addWidget(text_Note_2)
        scroll_layout.addWidget(text_key_class_bangunDatar)
        scroll_layout.addWidget(text_key_bangunDatar)
        scroll_layout.addWidget(text_key_class_bangunRuang)
        scroll_layout.addWidget(text_key_bangunRuang)
        scroll_layout.addWidget(scroll_widget)
        # menetapkan ukuran minimum widget di dalam QScrollArea
        scroll_widget.setMinimumSize(800, 600)
        # scroll_widget.setFixedSize(800, 600)

        # menambahkan scroll_widget ke dalam QScrollArea
        scroll_area.setWidget(scroll_widget)

        # menambahkan QScrollArea ke dalam layout utama
        layout.addWidget(scroll_area)

        self.setCentralWidget(widget)        

       
            #TODO : Add Bangun Ruang 3 Dimensi : Kerucut, Limas



    #TODO : Add Bangun Datar 3 Dimensi : Kerucut, Limas