#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Core conversion functionality for atomic structure files.
"""

import os
import warnings
from pathlib import Path
from typing import Dict, List, Optional, Union, Any
import ase.io
from ase import Atoms
import sys
from ase.io import read, write
from ase.constraints import FixAtoms
import numpy as np
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor, as_completed
from functools import partial
import multiprocessing

# Filter out ASE spacegroup warnings
warnings.filterwarnings("ignore", category=UserWarning, module="ase.spacegroup.spacegroup")

class StructureConverter:
    """A class for converting atomic structure files between different formats."""
    
    # Default element order (periodic table order)
    DEFAULT_ELEMENT_ORDER = [
        "H", "He",
        "Li", "Be", "B", "C", "N", "O", "F", "Ne",
        "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar",
        "K", "Ca", "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn", "Ga", "Ge", "As", "Se", "Br", "Kr",
        "Rb", "Sr", "Y", "Zr", "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn", "Sb", "Te", "I", "Xe",
        "Cs", "Ba", "La", "Ce", "Pr", "Nd", "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb", "Lu",
        "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg", "Tl", "Pb", "Bi", "Po", "At", "Rn",
        "Fr", "Ra", "Ac", "Th", "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm", "Md", "No", "Lr",
        "Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds", "Rg", "Cn", "Nh", "Fl", "Mc", "Lv", "Ts", "Og"
    ]

    def __init__(self):
        """Initialize the StructureConverter."""
        self.single_frame_only_formats = ["vasp"]
        self.format_mapping = {
            "xyz": "extxyz",  # Map xyz to extxyz
            "extxyz": "extxyz"
        }
        self._element_order = None
        self._constraints = None
        self._layer_constraints = None
        self.sort_order = "ascending"  # Default ascending sort
        self.MAX_FILE_SIZE = 100 * 1024 * 1024 * 1024  # 100GB
        self.MAX_WORKERS = os.cpu_count() or 4  # Use CPU cores or default to 4 threads
    
    def _get_element_sort(self, element: str) -> int:
        """
        Get the position of an element in the periodic table.
        
        Args:
            element: Element symbol
            
        Returns:
            Position in the periodic table
        """
        try:
            return self.DEFAULT_ELEMENT_ORDER.index(element)
        except ValueError:
            return len(self.DEFAULT_ELEMENT_ORDER)  # Put unknown elements at the end
    
    def _check_file_size(self, file_path):
        """Check if file size exceeds limit"""
        file_size = os.path.getsize(file_path)
        if file_size > self.MAX_FILE_SIZE:
            raise ValueError(f"""File size ({file_size/1024/1024/1024:.2f}GB) 
                             , exceeds limit ({self.MAX_FILE_SIZE/1024/1024/1024:.2f}GB)""")

    def _show_progress(self, total, desc="Processing"):
        """Show progress bar"""
        return tqdm(total=total, desc=desc, unit="frame")

    def _process_frame(self, frame, output_path, constraints):
        """Process a single structure frame"""
        try:
            self._write_vasp(frame, output_path, constraints)
            return True, output_path
        except Exception as e:
            return False, str(e)

    def convert(
        self,
        input_path: Union[str, Path],
        output_path: Union[str, Path],
        input_format: Optional[str] = None,
        output_format: Optional[str] = None,
        mode: Optional[str] = None,
        frame: Optional[str] = None,
        element_mapping: Optional[List[str]] = None,
        constraints: Optional[Union[str, List[str]]] = None,
        layer_constraints: Optional[List[Dict[str, float]]] = None,
        sort_type: Optional[str] = None,
        parallel: bool = True,
        multi_frame: bool = False,
        separate_dirs: bool = False
    ) -> None:
        """
        Convert atomic structure file.
        
        Args:
            input_path: Input file path
            output_path: Output file path
            input_format: Input file format
            output_format: Output file format
            mode: Conversion mode ('single' or 'multi')
            frame: Frame selection string
            element_mapping: Element mapping list
            constraints: Atomic constraints
            layer_constraints: Layer-based constraints
            sort_type: Sort type for atoms
            parallel: Whether to use parallel processing
            multi_frame: Whether to process multiple frames
            separate_dirs: Whether to save frames in separate directories
        """
        try:
            # Check file size
            self._check_file_size(input_path)
            
            # Set options
            self._element_order = element_mapping
            self._constraints = constraints
            self._layer_constraints = layer_constraints
            
            # Convert paths to Path objects
            input_path = Path(input_path)
            output_path = Path(output_path)
            
            # Auto-detect file format
            if input_format is None:
                input_format = input_path.suffix[1:] if input_path.suffix else "vasp"
            if output_format is None:
                output_format = output_path.suffix[1:] if output_path.suffix else "vasp"
            
            # Map file formats
            input_format = self.format_mapping.get(input_format, input_format)
            output_format = self.format_mapping.get(output_format, output_format)
            
            # Auto-detect mode
            if mode is None:
                mode = "multi" if multi_frame else "single"
            
            # Validate mode
            self._validate_mode(mode, output_format)
            
            # Parse frame selection
            frame_indices = self._parse_frame_selection(frame) if frame else None
            
            # Read structures
            structures = self._read_structures(input_path, input_format, frame)
            
            # Apply transformations
            if sort_type:
                structures = self._sort_atoms(structures, sort_type)
            if self._element_order:
                structures = self._apply_element_order(structures)
            
            # Handle output
            if output_format == "vasp":
                # For VASP format, use custom write function
                if mode == "single":
                    self._write_vasp(structures[0], output_path, self._constraints)
                else:
                    # Create output directory
                    output_path.mkdir(parents=True, exist_ok=True)
                    if parallel:
                        # Parallel processing for multi-frame
                        print(f"Using {self.MAX_WORKERS} threads for parallel processing...")
                        with ThreadPoolExecutor(max_workers=self.MAX_WORKERS) as executor:
                            # Create task list
                            futures = []
                            for i, structure in enumerate(structures):
                                if separate_dirs:
                                    # Use original frame index for directory name
                                    frame_idx = frame_indices[i] if frame_indices else i
                                    frame_dir = output_path / f"frame_{frame_idx+1}"
                                    frame_dir.mkdir(exist_ok=True)
                                    frame_output = frame_dir / "POSCAR"
                                else:
                                    frame_output = output_path / f"frame_{i+1}.vasp"
                                future = executor.submit(self._process_frame, structure, frame_output, self._constraints)
                                futures.append(future)
                            
                            # Show progress with progress bar
                            with self._show_progress(len(futures), "Processing frames") as pbar:
                                for future in as_completed(futures):
                                    success, result = future.result()
                                    if not success:
                                        print(f"Warning: Processing failed - {result}")
                                    pbar.update(1)
                    else:
                        # Serial processing for multi-frame
                        with self._show_progress(len(structures), "Processing frames") as pbar:
                            for i, structure in enumerate(structures):
                                if separate_dirs:
                                    # Use original frame index for directory name
                                    frame_idx = frame_indices[i] if frame_indices else i
                                    frame_dir = output_path / f"frame_{frame_idx+1}"
                                    frame_dir.mkdir(exist_ok=True)
                                    frame_output = frame_dir / "POSCAR"
                                else:
                                    frame_output = output_path / f"frame_{i+1}.vasp"
                                self._write_vasp(structure, frame_output, self._constraints)
                                pbar.update(1)
            else:
                # For other formats, use ASE's write function
                if mode == "single":
                    ase.io.write(output_path, structures[0], format=output_format)
                else:
                    if output_format in self.single_frame_only_formats:
                        # Create output directory
                        output_path.mkdir(parents=True, exist_ok=True)
                        for i, structure in enumerate(structures):
                            if separate_dirs:
                                # Use original frame index for directory name
                                frame_idx = frame_indices[i] if frame_indices else i
                                frame_dir = output_path / f"frame_{frame_idx+1}"
                                frame_dir.mkdir(exist_ok=True)
                                frame_output = frame_dir / f"structure.{output_format}"
                            else:
                                frame_output = output_path / f"frame_{i+1}.{output_format}"
                            ase.io.write(frame_output, structure, format=output_format)
                    else:
                        ase.io.write(output_path, structures, format=output_format)
            
            print(f"Conversion completed! Output file: {output_path}")
            
        except Exception as e:
            raise ValueError(f"Conversion failed: {str(e)}")
    
    def _detect_mode(self, input_path: Path, input_format: str) -> str:
        """Detect conversion mode"""
        try:
            structures = ase.io.read(input_path, format=input_format, index=":")
            return "multi" if len(structures) > 1 else "single"
        except Exception:
            return "single"
    
    def _validate_mode(self, mode: str, output_format: str) -> None:
        """Validate conversion mode"""
        if mode == "multi" and output_format in self.single_frame_only_formats:
            if isinstance(output_format, str) and Path(output_format).suffix:
                raise ValueError(f"Output format {output_format} does not support multi-frame structures. Please choose another output format or use single-frame mode.")

    def _parse_frame_selection(self, frame_str: str) -> List[int]:
        """
        Parse frame selection string into a list of frame indices.
        
        Args:
            frame_str: Frame selection string (e.g., "1 2 3-6")
            
        Returns:
            List of frame indices (0-based)
        """
        if not frame_str:
            return []
            
        indices = set()
        parts = frame_str.split()
        
        for part in parts:
            if '-' in part:
                start, end = map(int, part.split('-'))
                indices.update(range(start-1, end))
            else:
                try:
                    indices.add(int(part)-1)
                except ValueError:
                    raise ValueError(f"Invalid frame number: {part}")
                
        return sorted(list(indices))

    def _read_structures(
        self,
        input_path: Path,
        input_format: str,
        frame: Optional[str] = None,
    ) -> List[Atoms]:
        """Read structures"""
        try:
            # Read all frames first
            all_structures = ase.io.read(input_path, format=input_format, index=":")
            if not isinstance(all_structures, list):
                all_structures = [all_structures]
            
            if frame is not None:
                # Parse frame selection
                frame_indices = self._parse_frame_selection(frame)
                if not frame_indices:
                    raise ValueError("Invalid frame selection format")
                
                # Select specified frames
                structures = []
                for idx in frame_indices:
                    if 0 <= idx < len(all_structures):
                        structures.append(all_structures[idx])
                    else:
                        print(f"Warning: Frame {idx+1} out of range, skipping")
                
                if not structures:
                    raise ValueError("No valid frames selected")
            else:
                structures = all_structures
            
            # Ensure all structures have lattice
            for idx, structure in enumerate(structures):
                if structure.cell.rank < 3:
                    raise ValueError(f'Image {idx} lose the Lattice informations,')
            
            return structures
        except Exception as e:
            raise ValueError(f"Failed to read file: {str(e)}")
    
    def _sort_atoms(self, structures: List[Atoms], sort_type: str) -> List[Atoms]:
        """Sort atoms by element type"""
        for structure in structures:
            # Get current element order
            elements = structure.get_chemical_symbols()
            
            # Sort indices based on element order
            if sort_type == "ascending":
                indices = sorted(range(len(elements)), key=lambda i: self._get_element_sort(elements[i]))
            else:  # descending
                indices = sorted(range(len(elements)), key=lambda i: -self._get_element_sort(elements[i]))
            
            # Reorder atoms
            structure.positions = structure.positions[indices]
            structure.numbers = structure.numbers[indices]
            if structure.has('initial_magmoms'):
                structure.set_initial_magmoms(structure.get_initial_magmoms()[indices])
            if structure.has('initial_charges'):
                structure.set_initial_charges(structure.get_initial_charges()[indices])
        
        return structures
    
    def _apply_element_order(self, structures: List[Atoms]) -> List[Atoms]:
        """Apply custom element order"""
        for structure in structures:
            # Get current element order
            elements = structure.get_chemical_symbols()
            
            # Create mapping from element to desired position
            element_positions = {elem: i for i, elem in enumerate(self._element_order)}
            
            # Sort indices based on element order
            indices = sorted(range(len(elements)), key=lambda i: element_positions.get(elements[i], len(self._element_order)))
            
            # Reorder atoms
            structure.positions = structure.positions[indices]
            structure.numbers = structure.numbers[indices]
            if structure.has('initial_magmoms'):
                structure.set_initial_magmoms(structure.get_initial_magmoms()[indices])
            if structure.has('initial_charges'):
                structure.set_initial_charges(structure.get_initial_charges()[indices])
        
        return structures
    
    def _apply_constraints(self, structures: List[Atoms]) -> List[Atoms]:
        """Apply atomic constraints"""
        for structure in structures:
            if self._constraints == "fixed":
                # Fix all atoms
                structure.set_constraint(FixAtoms(indices=list(range(len(structure)))))
            elif isinstance(self._constraints, list):
                if all(isinstance(x, str) for x in self._constraints):
                    # Fix specific elements
                    indices = []
                    for i, symbol in enumerate(structure.get_chemical_symbols()):
                        if symbol in self._constraints:
                            indices.append(i)
                    if indices:
                        structure.set_constraint(FixAtoms(indices=indices))
                elif all(isinstance(x, int) for x in self._constraints):
                    # Fix specific atom indices
                    structure.set_constraint(FixAtoms(indices=self._constraints))
        
        return structures
    
    def _apply_layer_constraints(self, structures: List[Atoms]) -> List[Atoms]:
        """Apply layer-based constraints"""
        for structure in structures:
            indices = []
            for layer in self._layer_constraints:
                # Get atoms in layer
                z_positions = structure.positions[:, 2]
                layer_indices = np.where((z_positions >= layer['start']) & (z_positions < layer['end']))[0]
                indices.extend(layer_indices)
            if indices:
                structure.set_constraint(FixAtoms(indices=indices))
        
        return structures
    
    def _write_vasp(self, structure: Atoms, output_path: Union[str, Path], constraints: Optional[Union[str, List[str]]] = None) -> None:
        """Write structure in VASP format."""
        # Create output directory if needed
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Get chemical symbols and counts
        elements = structure.get_chemical_symbols()
        unique_elements = sorted(set(elements))
        
        # Write VASP file
        with open(output_path, 'w') as f:
            # Write elements
            f.write(' '.join(unique_elements) + '\n')
            
            # Write scale factor
            f.write('1.0\n')
            
            # Write cell
            cell = structure.get_cell()
            for i in range(3):
                f.write(f'{cell[i,0]:20.16f} {cell[i,1]:20.16f} {cell[i,2]:20.16f}\n')
            
            # Write elements and counts
            f.write(' '.join(unique_elements) + '\n')
            counts = [elements.count(e) for e in unique_elements]
            f.write(' '.join(map(str, counts)) + '\n')
            
            # Write selective dynamics and coordinates
            f.write('Selective dynamics\n')
            f.write('Cartesian\n')
            
            # Write positions with constraints
            positions = structure.get_positions()
            for i, pos in enumerate(positions):
                is_fixed = False
                if constraints == 'fixed':
                    is_fixed = True
                elif isinstance(constraints, list):
                    if constraints[0] == 'elements':
                        is_fixed = elements[i] in constraints[1:]
                    elif constraints[0] == 'layers':
                        z = pos[2]
                        for layer_range in constraints[1:]:
                            start, end = map(float, layer_range.split(','))
                            if start <= z <= end:
                                is_fixed = True
                                break
                    elif constraints[0] == 'indices':
                        indices = []
                        for idx in constraints[1:]:
                            if '-' in str(idx):
                                start, end = map(int, idx.split('-'))
                                indices.extend(range(start, end + 1))
                            else:
                                indices.append(int(idx))
                        is_fixed = i + 1 in indices  # Convert to 1-based indexing
                
                if is_fixed:
                    f.write(f'{pos[0]:20.16f} {pos[1]:20.16f} {pos[2]:20.16f} F F F\n')
                else:
                    f.write(f'{pos[0]:20.16f} {pos[1]:20.16f} {pos[2]:20.16f} T T T\n')