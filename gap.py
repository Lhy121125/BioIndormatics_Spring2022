import numpy as np
import sys
from Bio.Align import substitution_matrices 
from enum import IntEnum

sub_mat = substitution_matrices.load("BLOSUM62")

class Back(IntEnum):
    MAT = 0
    VRT = 1
    HRZ = 2

def read5J(filename):
    """Reads in two strings"""
    with open(filename, "r") as file:
        strings = [line.strip() for line in file.readlines()]
    return strings[0], strings[1]

def affine_alignment(v, w, scoring_matrix = sub_mat, open_penalty = -11, extn_penalty = -1):
    n, m = len(v), len(w)
    v_aligned, w_aligned = "", ""
    middle_matrix = np.zeros((n + 1, m + 1), dtype = int)
    lower_matrix = np.zeros((n + 1, m + 1), dtype = int)
    upper_matrix = np.zeros((n + 1, m + 1), dtype = int)
    bck_ptr = np.zeros((n + 1, m + 1), dtype = int)
    
    #need to make sure whether the starting nodes of each matrix are zero 
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            curr_lower = max(lower_matrix[i - 1, j] + extn_penalty, middle_matrix[i - 1, j] + open_penalty)
            lower_matrix[i, j] = curr_lower
            
            curr_upper = max(upper_matrix[i, j - 1] + extn_penalty, middle_matrix[i, j - 1] + open_penalty) 
            upper_matrix[i, j] = curr_upper
            
            mid_cross = middle_matrix[i - 1, j - 1] + scoring_matrix[(v[i - 1], w[j - 1])]
            curr_mid = max(mid_cross, lower_matrix[i, j], upper_matrix[i, j])
            
            middle_matrix[i, j] = curr_mid
            
            if curr_mid == lower_matrix[i, j]:
                bck_ptr[i, j] = Back.VRT
            elif curr_mid == curr_upper:
                bck_ptr[i, j] = Back.HRZ
            else:
                bck_ptr[i,j] = Back.MAT
            
    b_i, b_j = n, m
    high_val = max(middle_matrix[b_i, b_j], lower_matrix[b_i, b_j], upper_matrix[b_i, b_j])
    
    while True:
        ptr = bck_ptr[b_i, b_j]
        if ptr == Back.VRT:
            v_aligned += v[b_i - 1]
            w_aligned += "-"
            b_i -= 1
        elif ptr == Back.HRZ:
            v_aligned += "-"
            w_aligned += w[b_j - 1]
            b_j -= 1
        elif ptr == Back.MAT:
            v_aligned += v[b_i - 1]
            w_aligned += w[b_j - 1]
            b_i -= 1
            b_j -= 1
        
        if b_i == 0 or b_j == 0:
            break
        
    return high_val, v_aligned[::-1], w_aligned[::-1]
    
if __name__ == "__main__":
    v, w = read5J("input_18.txt")
    for stuff in affine_alignment(v, w):
        print(stuff)
      

