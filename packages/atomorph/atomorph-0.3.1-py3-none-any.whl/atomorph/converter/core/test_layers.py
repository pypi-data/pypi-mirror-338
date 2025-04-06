#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
测试固定层功能的脚本。
"""

import os
from pathlib import Path
import numpy as np
from atomorph.converter.core.converter import StructureConverter
from ase.io import read, write

def main():
    # 设置路径
    input_file = "/Users/wx/Desktop/AI project/new/IGRSI-ts.extxyz"
    output_file = "/Users/wx/Desktop/AI project/new/direct_test.vasp"
    
    print(f"读取文件: {input_file}")
    structure = read(input_file, index=0)
    
    # 打印晶胞信息
    cell = structure.get_cell()
    print("晶胞矩阵:")
    print(cell)
    
    # 获取原子Z坐标的分数范围
    positions = structure.positions
    cell_inv = np.linalg.inv(cell)
    frac_positions = np.dot(positions, cell_inv)
    frac_z = frac_positions[:, 2]
    print(f"分数Z坐标范围: {frac_z.min()} - {frac_z.max()}")
    
    # 统计在约束范围内的原子
    start, end = 0.31, 0.4
    elements = structure.get_chemical_symbols()
    in_range_indices = []
    
    for i, frac_pos in enumerate(frac_positions):
        if start <= frac_pos[2] <= end:
            in_range_indices.append(i)
            print(f"原子 {i+1} ({elements[i]}): 分数Z坐标 = {frac_pos[2]}")
    
    print(f"\n在范围 {start}-{end} 内的原子数量: {len(in_range_indices)}")
    
    # 手动创建VASP文件
    unique_elements = sorted(set(elements))
    
    with open(output_file, 'w') as f:
        # 写入元素名称
        f.write(' '.join(unique_elements) + '\n')
        
        # 写入尺度因子
        f.write('1.0\n')
        
        # 写入晶胞
        for i in range(3):
            f.write(f'{cell[i,0]:20.16f} {cell[i,1]:20.16f} {cell[i,2]:20.16f}\n')
        
        # 写入元素及其数量
        f.write(' '.join(unique_elements) + '\n')
        counts = [elements.count(e) for e in unique_elements]
        f.write(' '.join(map(str, counts)) + '\n')
        
        # 选择性动力学标记
        f.write('Selective dynamics\n')
        f.write('Cartesian\n')
        
        # 写入原子坐标及选择性动力学标记
        fixed_count = 0
        for element in unique_elements:
            element_indices = [i for i, symbol in enumerate(elements) if symbol == element]
            for i in element_indices:
                pos = positions[i]
                is_fixed = i in in_range_indices
                
                if is_fixed:
                    f.write(f'{pos[0]:20.16f} {pos[1]:20.16f} {pos[2]:20.16f} F F F\n')
                    fixed_count += 1
                else:
                    f.write(f'{pos[0]:20.16f} {pos[1]:20.16f} {pos[2]:20.16f} T T T\n')
        
        print(f"VASP文件已写入: {output_file}")
        print(f"总原子数: {len(structure)}, 固定原子数: {fixed_count}")
    
    # 检查VASP文件中的选择性动力学标记
    fixed_count = 0
    total_count = 0
    with open(output_file, 'r') as f:
        lines = f.readlines()
        
    # 找到 Selective dynamics 行
    for i, line in enumerate(lines):
        if "Selective" in line:
            sd_line = i
            break
    
    # 计算固定原子
    for line in lines[sd_line+2:]:  # 跳过 Selective dynamics 和 Cartesian 行
        if len(line.strip()) > 0:
            if "F F F" in line:
                fixed_count += 1
            total_count += 1
    
    print(f"\n文件检查结果:")
    print(f"总原子数: {total_count}")
    print(f"固定原子数: {fixed_count}")
    print(f"固定比例: {fixed_count/total_count*100:.2f}%")

if __name__ == "__main__":
    main() 