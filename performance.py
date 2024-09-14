import time
"""
TODO: Gunakan file performance.py ini untuk membuat class Performance yang 
nantinya akan digunakan untuk menghitung akurasi (Best Match Accuracy & Candidate Match) 
dan runtime
"""
class Performance:
    def __init__(self, model):
        self.__model = model
    
    def calculate_performance(self):
        return {
            'cand_acc': -1, 
            'best_acc': -1, 
            'time': -1
        }