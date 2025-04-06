# Atomorph

[English](#english) | [中文](#chinese)

<a name="english"></a>
## English

### Introduction
Atomorph is a powerful tool for converting and manipulating crystal structure files. It supports various file formats and provides flexible options for structure manipulation.

### Features
- Convert between CIF, VASP, and other crystal structure formats
- Sort atoms by element type (alphabetical or custom order)
- Fix specific atoms, elements, or layers
- Support for multi-frame structures
- Batch processing capabilities

### Installation
#### Method 1: Using pip
```bash
pip install atomorph==0.3.0
```

#### Method 2: Manual Installation
1. Clone the repository:
```bash
git clone https://github.com/yyxwjq/atomorph.git
cd atomorph
```

2. Install the package:
```bash
pip install -e .
```

3. Add to PATH (optional):
Add the following line to your ~/.bashrc or ~/.zshrc:
```bash
export PATH=$PATH:/path/to/atomorph/bin
```

### Usage
Basic conversion:
```bash
atomorph convert input.cif -o output.vasp
```

Sort atoms:
```bash
atomorph convert input.cif -o output.vasp --sort-by element --order ascending
atomorph convert input.cif -o output.vasp --sort-by element --order descending
```

Custom element order:
```bash
atomorph convert input.cif -o output.vasp --element-order "Fe Cu Ag Pt Au"
```

Fix atoms:
```bash
# Fix all atoms
atomorph convert input.cif -o output.vasp --fix-all

# Fix specific elements
atomorph convert input.cif -o output.vasp --fix-elements "Fe Cu"

# Fix specific layers (using fractional coordinates)
atomorph convert input.cif -o output.vasp --fix-layers "0.0 0.2" --fractional

# Fix specific atom indices
atomorph convert input.cif -o output.vasp --fix-indices "1 2 3-6"
```

### License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

<a name="chinese"></a>
## 中文

### 简介
Atomorph 是一个用于转换和操作晶体结构文件的强大工具。它支持多种文件格式，并提供灵活的结构操作选项。

### 功能特点
- 在 CIF、VASP 和其他晶体结构格式之间转换
- 按元素类型排序（字母顺序或自定义顺序）
- 固定特定原子、元素或层
- 支持多帧结构
- 批量处理功能

### 安装方法
#### 方法一：使用 pip 安装
```bash
pip install atomorph==0.3.0
```

#### 方法二：手动安装
1. 克隆仓库：
```bash
git clone https://github.com/yyxwjq/atomorph.git
cd atomorph
```

2. 安装包：
```bash
pip install -e .
```

3. 添加到环境变量（可选）：
在 ~/.bashrc 或 ~/.zshrc 中添加以下行：
```bash
export PATH=$PATH:/path/to/atomorph/bin
```

### 使用方法
基本转换：
```bash
atomorph convert input.cif -o output.vasp
```

原子排序：
```bash
atomorph convert input.cif -o output.vasp --sort-by element --order ascending
atomorph convert input.cif -o output.vasp --sort-by element --order descending
```

自定义元素顺序：
```bash
atomorph convert input.cif -o output.vasp --element-order "Fe Cu Ag Pt Au"
```

固定原子：
```bash
# 固定所有原子
atomorph convert input.cif -o output.vasp --fix-all

# 固定特定元素
atomorph convert input.cif -o output.vasp --fix-elements "Fe Cu"

# 固定特定层（使用分数坐标）
atomorph convert input.cif -o output.vasp --fix-layers "0.0 0.2" --fractional

# 固定特定原子索引
atomorph convert input.cif -o output.vasp --fix-indices "1 2 3-6"
```

多帧转换：
```bash
atomorph convert input.cif -o output/ --mode multi
```

多帧转换（分别保存到不同目录）：
```bash
atomorph convert input.cif -o output/ --mode multi --separate-dirs
```

多帧转换（选择特定帧）：
```bash
atomorph convert input.cif -o output/ --mode multi --frames "1 2 3-6"
```

多帧转换（并行处理）：
```bash
atomorph convert input.cif -o output/ --mode multi --parallel
```

### 许可证
本项目采用 MIT 许可证 - 详情请参见 [LICENSE](LICENSE) 文件。

## Features

- Convert between various atomic structure formats (CIF, VASP, XYZ, etc.)
- Support for multi-frame structures
- Custom element ordering
- Atomic constraints (fix all atoms, specific elements, layers, or indices)
- Parallel processing for multi-frame conversion
- Progress bar for conversion progress
- File size limit check

## 功能特点

- 支持多种原子结构格式之间的转换（CIF、VASP、XYZ等）
- 支持多帧结构
- 自定义元素排序
- 原子约束（固定所有原子、特定元素、层或索引）
- 多帧转换的并行处理
- 转换进度条显示
- 文件大小限制检查

## Installation

```bash
pip install atomorph
```

## 安装

```bash
pip install atomorph
```

## Usage

Basic conversion:
```bash
atomorph convert input.cif -o output.vasp
```

Sort atoms by atomic number (ascending):
```bash
atomorph convert input.cif -o output.vasp --sort-by element --order ascending
```

Sort atoms by atomic number (descending):
```bash
atomorph convert input.cif -o output.vasp --sort-by element --order descending
```

Custom element order:
```bash
atomorph convert input.cif -o output.vasp --element-order "Ru Si Fe"
```

Fix all atoms:
```bash
atomorph convert input.cif -o output.vasp --fix-all
```

Fix specific elements:
```bash
atomorph convert input.cif -o output.vasp --fix-elements "Fe Cu"
```

Fix layers:
```bash
atomorph convert input.cif -o output.vasp --fix-layers "0.0 0.2" --fractional
```

Fix specific atom indices:
```bash
atomorph convert input.cif -o output.vasp --fix-indices "1 2 3-6"
```

Multi-frame conversion:
```bash
atomorph convert input.cif -o output/ --mode multi
```

Multi-frame conversion with separate directories:
```bash
atomorph convert input.cif -o output/ --mode multi --separate-dirs
```

Multi-frame conversion with frame selection:
```bash
atomorph convert input.cif -o output/ --mode multi --frames "1 2 3-6"
```

Multi-frame conversion with parallel processing:
```bash
atomorph convert input.cif -o output/ --mode multi --parallel
```

## 使用方法

基本转换：
```bash
atomorph convert input.cif -o output.vasp
```

按原子序数升序排序：
```bash
atomorph convert input.cif -o output.vasp --sort-by element --order ascending
```

按原子序数降序排序：
```bash
atomorph convert input.cif -o output.vasp --sort-by element --order descending
```

自定义元素顺序：
```bash
atomorph convert input.cif -o output.vasp --element-order "Ru Si Fe"
```

固定所有原子：
```bash
atomorph convert input.cif -o output.vasp --fix-all
```

固定特定元素：
```bash
atomorph convert input.cif -o output.vasp --fix-elements "Fe Cu"
```

固定特定层：
```bash
atomorph convert input.cif -o output.vasp --fix-layers "0.0 0.2" --fractional
```

固定特定原子索引：
```bash
atomorph convert input.cif -o output.vasp --fix-indices "1 2 3-6"
```

多帧转换：
```bash
atomorph convert input.cif -o output/ --mode multi
```

多帧转换（分别保存到不同目录）：
```bash
atomorph convert input.cif -o output/ --mode multi --separate-dirs
```

多帧转换（选择特定帧）：
```bash
atomorph convert input.cif -o output/ --mode multi --frames "1 2 3-6"
```

多帧转换（并行处理）：
```bash
atomorph convert input.cif -o output/ --mode multi --parallel
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 许可证

本项目采用MIT许可证 - 详情请参见 [LICENSE](LICENSE) 文件。

## Command Line Options

- `input_path`: Input file path
- `output_path`: Output file path
- `-m, --mode`: Conversion mode (single/multi)
- `-s, --sort`: Sort atoms by atomic number (ascending/descending)
- `-e, --elements`: Custom element order
- `-c, --constraints`: Atomic constraints
- `-d, --separate-dirs`: Save frames in separate directories
- `-f, --frames`: Frame selection
- `-p, --parallel`: Use parallel processing
- `-v, --version`: Show version information

## Supported File Formats

- VASP (POSCAR/CONTCAR)
- CIF
- XYZ
- XSF
- LAMMPS
- And more...

## Requirements

- Python >= 3.8
- ASE >= 3.22.0
- NumPy >= 1.21.0
- SciPy >= 1.7.0
- Matplotlib >= 3.4.0