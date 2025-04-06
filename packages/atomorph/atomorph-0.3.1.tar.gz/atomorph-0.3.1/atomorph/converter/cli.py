"""
Command-line interface for the Atomorph converter.
"""

import argparse
import json
import os
import sys
from pathlib import Path
from atomorph.converter.core.converter import StructureConverter
from typing import Optional, List, Dict, Union

def parse_args() -> argparse.Namespace:
    """
    Parse command line arguments.
    
    Returns:
        Parsed command line arguments
    """
    parser = argparse.ArgumentParser(
        prog="conv",
        description="""
        Convert atomic structure files.
        
        Examples:
            # Basic conversion
            conv input.cif output.vasp
            
            # Sort atoms by atomic number (ascending)
            conv input.cif output.vasp -s ascending
            
            # Sort atoms by atomic number (descending)
            conv input.cif output.vasp -s descending
            
            # Custom element order
            conv input.cif output.vasp -e Ru Si Fe
            
            # Fix all atoms
            conv input.cif output.vasp -c fixed
            
            # Fix specific elements
            conv input.cif output.vasp -c elements Fe Cu
            
            # Fix layers
            conv input.cif output.vasp -c layers 0,1 1,2
            
            # Multi-frame conversion
            conv input.cif output/ -m multi
            
            # Multi-frame conversion with separate directories
            conv input.cif output/ -m multi -d
            
            # Multi-frame conversion with frame selection
            conv input.cif output/ -m multi -f 1 2 3-6
            
            # Multi-frame conversion with parallel processing
            conv input.cif output/ -m multi -p
            
            # Specify output format for multi-frame conversion
            conv input.vasp output/ -m multi -fmt cif
        """,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    # Add arguments
    parser.add_argument(
        "input_path",
        type=str,
        help="Input file path"
    )
    
    parser.add_argument(
        "output_path",
        type=str,
        help="Output file path or directory"
    )
    
    parser.add_argument(
        "-m", "--mode",
        type=str,
        choices=["single", "multi"],
        help="Conversion mode (single or multi)"
    )
    
    parser.add_argument(
        "-f", "--frames",
        type=str,
        nargs="+",
        help="Frame selection (e.g., '1 2 3-6')"
    )
    
    parser.add_argument(
        "-e", "--elements",
        type=str,
        nargs="+",
        help="Custom element order"
    )
    
    parser.add_argument(
        "-c", "--constraints",
        type=str,
        nargs="+",
        help="Atomic constraints (fixed, elements, layers, indices)"
    )
    
    parser.add_argument(
        "-s", "--sort",
        type=str,
        choices=["ascending", "descending"],
        help="Sort atoms by element type"
    )
    
    parser.add_argument(
        "-p", "--parallel",
        action="store_true",
        help="Use parallel processing for multi-frame conversion"
    )
    
    parser.add_argument(
        "-d", "--separate-dirs",
        action="store_true",
        help="Save frames in separate directories"
    )
    
    parser.add_argument(
        "-fmt", "--format",
        type=str,
        help="Output format (e.g., vasp, cif, xyz)"
    )
    
    return parser.parse_args()

def parse_constraints(constraints_list: List[str]) -> Optional[Union[str, List[str], List[Dict[str, float]], List[int]]]:
    """
    Parse constraints list into appropriate format.
    
    Args:
        constraints_list: List of constraint arguments
        
    Returns:
        Parsed constraints in one of four formats:
        - 'fixed': Fix all atoms
        - List[str]: List of elements to fix
        - List[Dict[str, float]]: List of layer ranges to fix
        - List[int]: List of atom indices to fix
    """
    if not constraints_list:
        return None
        
    if constraints_list[0] == 'fixed':
        return 'fixed'
        
    if constraints_list[0] == 'elements':
        return ['elements'] + constraints_list[1:]
        
    if constraints_list[0] == 'layers':
        return ['layers'] + constraints_list[1:]
        
    if constraints_list[0] == 'indices':
        return ['indices'] + constraints_list[1:]
        
    return None

def main() -> None:
    """Main entry point for the command-line interface."""
    args = parse_args()
    
    try:
        # Create converter
        converter = StructureConverter()
        
        # Parse constraints
        constraints = parse_constraints(args.constraints)
        
        # Get output format
        output_format = None
        if args.format:
            output_format = args.format
        
        # Convert file
        converter.convert(
            input_path=args.input_path,
            output_path=args.output_path,
            output_format=output_format,
            mode=args.mode,
            frame=" ".join(args.frames) if args.frames else None,
            element_mapping=args.elements,
            constraints=constraints,
            sort_type=args.sort,
            parallel=args.parallel,
            multi_frame=args.mode == "multi",
            separate_dirs=args.separate_dirs
        )
    except Exception as e:
        print(f"Error: {str(e)}")
        exit(1)
    
    return 0

if __name__ == '__main__':
    exit(main()) 