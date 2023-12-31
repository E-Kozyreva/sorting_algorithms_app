from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
import sys
import time

from app_design.buttons import Buttons
from app_design.buttons_design import Design
from app_design.showhide_buttons import ShowButtons, HideButtons

import database.get_data as data
import algorithms.merge_algorithms as merge
import algorithms.tree_algorithm as tree


class MainWindow(QMainWindow, Buttons):
    def __init__(self):
        super().__init__()
        self.index = 0
        
        self.setWindowTitle("Sorting algorithms")
        self.main_layout = QHBoxLayout()

        self.left, self.top, self.width, self.height = 1100, 100, 360, 600
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setFixedSize(360, 600)
        self.setStyleSheet("background-color: #ffffff;")
        
        # time widget
        self.time = QLabel(self)
        self.time = Design.time_label(self.time)

        # name app widget
        self.name_app = QLabel(self)
        self.name_app = Design.name_app_label(self.name_app)
        
        # end app widget
        self.end_app = QLabel(self)
        self.end_app = Design.end_app_label(self.end_app)
        
        # button widget
        self.button_widget = QWidget(self)
        self.button_layout = QVBoxLayout(self.button_widget)
        self.button_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.button_widget = Design.button_widget(self.button_widget)
        
        # merge sort button
        self.merge_button = Buttons.merge_sort_button()
        self.button_layout.addWidget(self.merge_button)
        self.merge_button.clicked.connect(self.merge_sort_clicked)
        
        # tree sort button
        self.tree_button = Buttons.tree_sort_button()
        self.button_layout.addWidget(self.tree_button)
        self.tree_button.clicked.connect(self.tree_sort_clicked)
        
        # exit button
        self.exit_button = Buttons.exit_button()
        self.button_layout.addWidget(self.exit_button)
        self.exit_button.clicked.connect(self.exit_clicked)


    def merge_sort_clicked(self):
        self.index = 0
        
        # 2-way merge sort button
        self.t_way_button = Buttons.t_way_button()
        self.button_layout.addWidget(self.t_way_button)
        self.t_way_button.clicked.connect(self.t_way_clicked)

        # 4-way merge sort button
        self.f_way_button = Buttons.f_way_button()
        self.button_layout.addWidget(self.f_way_button)
        self.f_way_button.clicked.connect(self.f_way_clicked)

        # 8-way merge sort button
        self.e_way_button = Buttons.e_way_button() 
        self.button_layout.addWidget(self.e_way_button)
        self.e_way_button.clicked.connect(self.e_way_clicked)
        
        # back button
        self.back_button = Buttons.back_button()
        self.button_layout.addWidget(self.back_button)
        self.back_button.clicked.connect(self.back_clicked)
        
        self.name_app.setText("Merge sort")
        HideButtons.merge_algo(self.merge_button, self.tree_button, self.exit_button)
        ShowButtons.merge_algo(self.t_way_button, self.f_way_button, self.e_way_button, self.back_button)


    def t_way_clicked(self):
        self.index = 2

        # button random array
        self.random_array_button = Buttons.random_array_button()
        self.button_layout.addWidget(self.random_array_button)
        self.random_array_button.clicked.connect(self.random_array_clicked)

        # add array from file 
        self.add_array_from_file_button = Buttons.add_array_from_file_button()
        self.button_layout.addWidget(self.add_array_from_file_button)
        self.add_array_from_file_button.clicked.connect(self.add_array_from_file_clicked)

        # back button
        self.back_button_t = Buttons.back_button()
        self.button_layout.addWidget(self.back_button_t)
        self.back_button_t.clicked.connect(self.back_clicked)
        
        self.name_app.setText("2-way merge sort")
        HideButtons.tfe_way(self.t_way_button, self.f_way_button, self.e_way_button, self.back_button)
        ShowButtons.tfe_way(self.random_array_button, self.add_array_from_file_button, self.back_button_t)


    def f_way_clicked(self):
        self.index = 3

        # button random array
        self.random_array_button = Buttons.random_array_button()
        self.button_layout.addWidget(self.random_array_button)
        self.random_array_button.clicked.connect(self.random_array_clicked)

        # add array from file 
        self.add_array_from_file_button = Buttons.add_array_from_file_button()
        self.button_layout.addWidget(self.add_array_from_file_button)
        self.add_array_from_file_button.clicked.connect(self.add_array_from_file_clicked)

        # back button
        self.back_button_f = Buttons.back_button()
        self.button_layout.addWidget(self.back_button_f)
        self.back_button_f.clicked.connect(self.back_clicked)
        
        self.name_app.setText("4-way merge sort")
        HideButtons.tfe_way(self.t_way_button, self.f_way_button, self.e_way_button, self.back_button)
        ShowButtons.tfe_way(self.random_array_button, self.add_array_from_file_button, self.back_button_f)


    def e_way_clicked(self):
        self.index = 4

        # button random array
        self.random_array_button = Buttons.random_array_button()
        self.button_layout.addWidget(self.random_array_button)
        self.random_array_button.clicked.connect(self.random_array_clicked)

        # add array from file 
        self.add_array_from_file_button = Buttons.add_array_from_file_button()
        self.button_layout.addWidget(self.add_array_from_file_button)
        self.add_array_from_file_button.clicked.connect(self.add_array_from_file_clicked)

        # back button
        self.back_button_e = Buttons.back_button()
        self.button_layout.addWidget(self.back_button_e)
        self.back_button_e.clicked.connect(self.back_clicked)
        
        self.name_app.setText("8-way merge sort")
        HideButtons.tfe_way(self.t_way_button, self.f_way_button, self.e_way_button, self.back_button)
        ShowButtons.tfe_way(self.random_array_button, self.add_array_from_file_button, self.back_button_e)


    def tree_sort_clicked(self):
        self.index = 1
        
        # tree sort button
        self.avl_tree_button = Buttons.avl_button()
        self.button_layout.addWidget(self.avl_tree_button)
        self.avl_tree_button.clicked.connect(self.avl_clicked)

        # back button
        self.back_button = Buttons.back_button()
        self.button_layout.addWidget(self.back_button)
        self.back_button.clicked.connect(self.back_clicked)
        
        self.name_app.setText("Tree sort")
        HideButtons.tree_algo(self.merge_button, self.tree_button, self.exit_button)
        ShowButtons.tree_algo(self.avl_tree_button, self.back_button)


    def avl_clicked(self):
        self.index = 5

        # button random array
        self.random_array_button = Buttons.random_array_button()
        self.button_layout.addWidget(self.random_array_button)
        self.random_array_button.clicked.connect(self.random_array_clicked)
        
        # add array from file
        self.add_array_from_file_button = Buttons.add_array_from_file_button()
        self.button_layout.addWidget(self.add_array_from_file_button)
        self.add_array_from_file_button.clicked.connect(self.add_array_from_file_clicked)
        
        # back button
        self.back_button_avl = Buttons.back_button()
        self.button_layout.addWidget(self.back_button_avl)
        self.back_button_avl.clicked.connect(self.back_clicked)
        
        self.name_app.setText("AVL tree sort")
        HideButtons.avl_tree(self.avl_tree_button, self.back_button)
        ShowButtons.avl_tree(self.random_array_button, self.add_array_from_file_button, self.back_button_avl) 


    def random_array_clicked(self):
        garray = data.GenerateData(100_000).generate()
        len_garray = len(garray)
              
        # 2-way merge sort
        if self.index == 2:
            merge_sorter = merge.KMergeSort(2)
            merge2_start = time.time()
            merge_sorter.k_merge_sort(garray)
            merge2_end = time.time()

            with open("output/random_merge2.txt", "w") as file:
                text = ["Generated array:", "Length array:", "Time:"]
                file.write(f"""{text[0]} {garray}\n\n{text[1]} {len_garray}\n{text[2]} {merge2_end - merge2_start}\n""")

            self.array_widget = Buttons.randon_array_button_txt(len_garray, merge2_end - merge2_start, "Time:")
            self.button_layout.addWidget(self.array_widget)

            self.index = 6
            self.back_button_random = Buttons.back_button()
            self.button_layout.addWidget(self.back_button_random)
            self.back_button_random.clicked.connect(self.back_clicked)

            HideButtons.generate_array(self.random_array_button, self.add_array_from_file_button, self.back_button_t)
            ShowButtons.generate_array(self.back_button_random)
        # 4-way merge sort
        elif self.index == 3:
            merge_sorter = merge.KMergeSort(4)
            merge4_start = time.time()
            merge_sorter.k_merge_sort(garray)
            merge4_end = time.time()

            with open("output/random_merge4.txt", "w") as file:
                text = ["Generated array:", "Length array:", "Time:"]
                file.write(f"""{text[0]} {garray}\n\n{text[1]} {len_garray}\n{text[2]} {merge4_end - merge4_start}\n""")

            self.array_widget = Buttons.randon_array_button_txt(len_garray, merge4_end - merge4_start, "Time:")
            self.button_layout.addWidget(self.array_widget)

            self.index = 7
            self.back_button_random = Buttons.back_button()
            self.button_layout.addWidget(self.back_button_random)
            self.back_button_random.clicked.connect(self.back_clicked)

            HideButtons.generate_array(self.random_array_button, self.add_array_from_file_button, self.back_button_f)
            ShowButtons.generate_array(self.back_button_random)
        # 8-way merge sort
        elif self.index == 4:
            merge_sorter = merge.KMergeSort(8)
            merge8_start = time.time()
            merge_sorter.k_merge_sort(garray)
            merge8_end = time.time()

            with open("output/random_merge8.txt", "w") as file:
                text = ["Generated array:", "Length array:", "Time:"]
                file.write(f"""{text[0]} {garray}\n\n{text[1]} {len_garray}\n{text[2]} {merge8_end - merge8_start}\n""")

            self.array_widget = Buttons.randon_array_button_txt(len_garray, merge8_end - merge8_start, "Time:")
            self.button_layout.addWidget(self.array_widget)

            self.index = 8
            self.back_button_random = Buttons.back_button()
            self.button_layout.addWidget(self.back_button_random)
            self.back_button_random.clicked.connect(self.back_clicked)

            HideButtons.generate_array(self.random_array_button, self.add_array_from_file_button, self.back_button_e)
            ShowButtons.generate_array(self.back_button_random)
        # AVL tree sort
        elif self.index == 5: 
            sarray = [n for n in garray]
            avl_start = time.time()
            tree.tree_sort(sarray)
            avl_end = time.time()

            with open("output/random_avl.txt", "w") as file:
                text = ["Generated array:", "Length array:", "Time:"]
                file.write(f"""{text[0]} {garray}\n\n{text[1]} {len_garray}\n{text[2]} {avl_end - avl_start}\n""")

            self.array_widget = Buttons.randon_array_button_txt(len_garray, avl_end - avl_start, "Time:")
            self.button_layout.addWidget(self.array_widget)

            self.index = 9
            self.back_button_random = Buttons.back_button()
            self.button_layout.addWidget(self.back_button_random)
            self.back_button_random.clicked.connect(self.back_clicked)

            HideButtons.generate_array(self.random_array_button, self.add_array_from_file_button, self.back_button_avl)
            ShowButtons.generate_array(self.back_button_random)
            

    def add_array_from_file_clicked(self):
        filename = QFileDialog.getOpenFileName(self,'Open File')
        try:
            with open(filename[0], "r") as file:
                array = file.read().split()
                array = [int(n) for n in array]
                len_array = len(array)
        
            # 2-way merge sort
            if self.index == 2:
                merge_sorter = merge.KMergeSort(2)
                merge2_start = time.time()
                merge_sorter.k_merge_sort(array)
                merge2_end = time.time()

                with open("output/file_merge2.txt", "w") as file:
                    text = ["Array:", "Length array:", "Time:"]
                    file.write(f"""{text[0]} {array}\n\n{text[1]} {len_array}\n{text[2]} {merge2_end - merge2_start}\n""")

                self.array_widget = Buttons.randon_array_button_txt(len_array, merge2_end - merge2_start, "Time:")
                self.button_layout.addWidget(self.array_widget)

                self.index = 6
                self.back_button_random = Buttons.back_button()
                self.button_layout.addWidget(self.back_button_random)
                self.back_button_random.clicked.connect(self.back_clicked)

                HideButtons.generate_array(self.random_array_button, self.add_array_from_file_button, self.back_button_t)
                ShowButtons.generate_array(self.back_button_random)

            # 4-way merge sort
            elif self.index == 3:
                merge_sorter = merge.KMergeSort(4)
                merge4_start = time.time()
                merge_sorter.k_merge_sort(array)
                merge4_end = time.time()

                with open("output/file_merge4.txt", "w") as file:
                    text = ["Array:", "Length array:", "Time:"]
                    file.write(f"""{text[0]} {array}\n\n{text[1]} {len_array}\n{text[2]} {merge4_end - merge4_start}\n""")

                self.array_widget = Buttons.randon_array_button_txt(len_array, merge4_end - merge4_start, "Time:")
                self.button_layout.addWidget(self.array_widget)

                self.index = 7
                self.back_button_random = Buttons.back_button()
                self.button_layout.addWidget(self.back_button_random)
                self.back_button_random.clicked.connect(self.back_clicked)

                HideButtons.generate_array(self.random_array_button, self.add_array_from_file_button, self.back_button_f)
                ShowButtons.generate_array(self.back_button_random)
            # 8-way merge sort
            elif self.index == 4:
                merge_sorter = merge.KMergeSort(8)
                merge8_start = time.time()
                merge_sorter.k_merge_sort(array)
                merge8_end = time.time()

                with open("output/file_merge8.txt", "w") as file:
                    text = ["Array:", "Length array:", "Time:"]
                    file.write(f"""{text[0]} {array}\n\n{text[1]} {len_array}\n{text[2]} {merge8_end - merge8_start}\n""")

                self.array_widget = Buttons.randon_array_button_txt(len_array, merge8_end - merge8_start, "Time:")
                self.button_layout.addWidget(self.array_widget)

                self.index = 8
                self.back_button_random = Buttons.back_button()
                self.button_layout.addWidget(self.back_button_random)
                self.back_button_random.clicked.connect(self.back_clicked)

                HideButtons.generate_array(self.random_array_button, self.add_array_from_file_button, self.back_button_e)
                ShowButtons.generate_array(self.back_button_random)
            # AVL tree sort
            elif self.index == 5:
                sarray = [n for n in array]
                avl_start = time.time()
                tree.tree_sort(sarray)
                avl_end = time.time()

                with open("output/file_avl.txt", "w") as file:
                    text = ["Array:", "Length array:", "Time:"]
                    file.write(f"""{text[0]} {array}\n\n{text[1]} {len_array}\n{text[2]} {avl_end - avl_start}\n""")

                self.array_widget = Buttons.randon_array_button_txt(len_array, avl_end - avl_start, "Time:")
                self.button_layout.addWidget(self.array_widget)

                self.index = 9
                self.back_button_random = Buttons.back_button()
                self.button_layout.addWidget(self.back_button_random)
                self.back_button_random.clicked.connect(self.back_clicked)

                HideButtons.generate_array(self.random_array_button, self.add_array_from_file_button, self.back_button_avl)
                ShowButtons.generate_array(self.back_button_random)
        except:
            self.close()
            print("You didn't choose a file, app closed :(")


    def back_clicked(self):
        # merge sort
        if self.index == 0: 
            self.name_app.setText("Sorting algorithms")
            ShowButtons.merge_algo_back(self.merge_button, self.tree_button, self.exit_button), 
            HideButtons.merge_algo_back(self.t_way_button, self.f_way_button, self.e_way_button, self.back_button)
        # tree sort
        elif self.index == 1: 
            self.name_app.setText("Sorting algorithms")
            ShowButtons.tree_algo_back(self.merge_button, self.tree_button, self.exit_button)
            HideButtons.tree_algo_back(self.avl_tree_button, self.back_button)
        # 2-way merge sort
        elif self.index == 2: 
            self.index = 0
            self.name_app.setText("Merge sort")
            ShowButtons.tfe_way_back(self.t_way_button, self.f_way_button, self.e_way_button, self.back_button)
            HideButtons.tfe_way_back(self.random_array_button, self.add_array_from_file_button, self.back_button_t)
        # 4-way merge sort
        elif self.index == 3: 
            self.index = 0
            self.name_app.setText("Merge sort")
            ShowButtons.tfe_way_back(self.t_way_button, self.f_way_button, self.e_way_button, self.back_button)
            HideButtons.tfe_way_back(self.random_array_button, self.add_array_from_file_button, self.back_button_f)
        # 8-way merge sort
        elif self.index == 4: 
            self.index = 0
            self.name_app.setText("Merge sort")
            ShowButtons.tfe_way_back(self.t_way_button, self.f_way_button, self.e_way_button, self.back_button)
            HideButtons.tfe_way_back( self.random_array_button, self.add_array_from_file_button, self.back_button_e)
        # AVL tree sort
        elif self.index == 5: 
            self.index = 1
            self.name_app.setText("Tree sort")
            ShowButtons.avl_tree_back(self.avl_tree_button, self.back_button)
            HideButtons.avl_tree_back(self.random_array_button, self.add_array_from_file_button, self.back_button_avl)
        # back from 2-way merge sort
        elif self.index == 6: 
            self.index = 2
            self.name_app.setText("2-way merge sort")
            ShowButtons.generate_array_back(self.random_array_button, self.add_array_from_file_button, self.back_button_t)
            HideButtons.generate_array_back(self.back_button_random, self.array_widget)
        # back from 4-way merge sort
        elif self.index == 7:
            self.index = 3
            self.name_app.setText("4-way merge sort")
            ShowButtons.generate_array_back(self.random_array_button, self.add_array_from_file_button, self.back_button_f)
            HideButtons.generate_array_back(self.back_button_random, self.array_widget)
        elif self.index == 8:
            self.index = 4
            self.name_app.setText("8-way merge sort")
            ShowButtons.generate_array_back(self.random_array_button, self.add_array_from_file_button, self.back_button_e)
            HideButtons.generate_array_back(self.back_button_random, self.array_widget)
        # back from AVL tree sort
        elif self.index == 9: 
            self.index = 5
            self.name_app.setText("AVL tree sort")
            ShowButtons.generate_array_back(self.random_array_button, self.add_array_from_file_button, self.back_button_avl)
            HideButtons.generate_array_back(self.back_button_random, self.array_widget)    


    def exit_clicked(self):
        self.close()
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
