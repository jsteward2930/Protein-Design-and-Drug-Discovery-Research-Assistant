#!/usr/bin/env python3

import requests
import os
import json
from pathlib import Path

def get_api_key():
    return os.getenv("NVCF_RUN_KEY") or input("Paste the Run Key: ")

def get_pdb_content():
    return """
HEADER    VIRAL PROTEIN/ISOMERASE                 28-MAY-97   1AK4              
TITLE     HUMAN CYCLOPHILIN A BOUND TO THE AMINO-TERMINAL DOMAIN OF HIV-1 CAPSID
COMPND    MOL_ID: 1;                                                            
COMPND   2 MOLECULE: CYCLOPHILIN A;                                             
COMPND   3 CHAIN: A, B;                                                         
COMPND   4 EC: 5.2.1.8;                                                         
COMPND   5 ENGINEERED: YES;                                                     
COMPND   6 MOL_ID: 2;                                                           
COMPND   7 MOLECULE: HIV-1 CAPSID;                                              
COMPND   8 CHAIN: C, D;                                                         
COMPND   9 FRAGMENT: N-TERMINAL DOMAIN;                                         
COMPND  10 ENGINEERED: YES;                                                     
COMPND  11 MUTATION: YES                                                        
SOURCE    MOL_ID: 1;                                                            
SOURCE   2 ORGANISM_SCIENTIFIC: HOMO SAPIENS;                                   
SOURCE   3 ORGANISM_COMMON: HUMAN;                                              
SOURCE   4 ORGANISM_TAXID: 9606;                                                
SOURCE   5 CELL_LINE: BL21;                                                     
SOURCE   6 GENE: CYCLOPHILIN;                                                   
SOURCE   7 EXPRESSION_SYSTEM: ESCHERICHIA COLI BL21(DE3);                       
SOURCE   8 EXPRESSION_SYSTEM_TAXID: 469008;                                     
SOURCE   9 EXPRESSION_SYSTEM_STRAIN: BL21 (DE3);                                
SOURCE  10 EXPRESSION_SYSTEM_VECTOR: PET3A;                                     
SOURCE  11 EXPRESSION_SYSTEM_PLASMID: WISP94-1;                                 
SOURCE  12 EXPRESSION_SYSTEM_GENE: CYCLOPHILIN;                                 
SOURCE  13 MOL_ID: 2;                                                           
SOURCE  14 ORGANISM_SCIENTIFIC: HUMAN IMMUNODEFICIENCY VIRUS 1;                 
SOURCE  15 ORGANISM_TAXID: 11676;                                               
SOURCE  16 CELL_LINE: BL21;                                                     
SOURCE  17 GENE: CYCLOPHILIN;                                                   
SOURCE  18 EXPRESSION_SYSTEM: ESCHERICHIA COLI BL21(DE3);                       
SOURCE  19 EXPRESSION_SYSTEM_TAXID: 469008;                                     
SOURCE  20 EXPRESSION_SYSTEM_STRAIN: BL21 (DE3);                                
SOURCE  21 EXPRESSION_SYSTEM_VECTOR: PET11A;                                    
SOURCE  22 EXPRESSION_SYSTEM_PLASMID: WISP95-69;                                
SOURCE  23 EXPRESSION_SYSTEM_GENE: CYCLOPHILIN                                  
KEYWDS    CAPSID, HIV-1, CYCLOPHILIN A, ISOMERASE, ROTAMASE COMPLEX (CAPSID     
KEYWDS   2 PROTEIN-CYCLOSPORIN), VIRAL PROTEIN-ISOMERASE COMPLEX                
EXPDTA    X-RAY DIFFRACTION                                                     
AUTHOR    C.P.HILL,T.R.GAMBLE,F.F.VAJDOS,D.K.WORTHYLAKE,W.I.SUNDQUIST           
REVDAT   4   22-MAY-24 1AK4    1       REMARK                                   
REVDAT   3   02-AUG-23 1AK4    1       REMARK                                   
REVDAT   2   24-FEB-09 1AK4    1       VERSN                                    
REVDAT   1   15-OCT-97 1AK4    0                                                
JRNL        AUTH   T.R.GAMBLE,F.F.VAJDOS,S.YOO,D.K.WORTHYLAKE,M.HOUSEWEART,     
JRNL        AUTH 2 W.I.SUNDQUIST,C.P.HILL                                       
JRNL        TITL   CRYSTAL STRUCTURE OF HUMAN CYCLOPHILIN A BOUND TO THE        
JRNL        TITL 2 AMINO-TERMINAL DOMAIN OF HIV-1 CAPSID.                       
JRNL        REF    CELL(CAMBRIDGE,MASS.)         V.  87  1285 1996              
JRNL        REFN                   ISSN 0092-8674                               
JRNL        PMID   8980234                                                      
JRNL        DOI    10.1016/S0092-8674(00)81823-1                                
REMARK   1                                                                      
REMARK   1 REFERENCE 1                                                          
REMARK   1  AUTH   H.KE,D.MAYROSE,W.CAO                                         
REMARK   1  TITL   CRYSTAL STRUCTURE OF CYCLOPHILIN A COMPLEXED WITH SUBSTRATE  
REMARK   1  TITL 2 ALA-PRO SUGGESTS A SOLVENT-ASSISTED MECHANISM OF CIS-TRANS   
REMARK   1  TITL 3 ISOMERIZATION                                                
REMARK   1  REF    PROC.NATL.ACAD.SCI.USA        V.  90  3324 1993              
REMARK   1  REFN                   ISSN 0027-8424                               
REMARK   2                                                                      
REMARK   2 RESOLUTION.    2.36 ANGSTROMS.                                       
REMARK   3                                                                      
REMARK   3 REFINEMENT.                                                          
REMARK   3   PROGRAM     : X-PLOR 3.843                                         
REMARK   3   AUTHORS     : BRUNGER                                              
REMARK   3                                                                      
REMARK   3  DATA USED IN REFINEMENT.                                            
REMARK   3   RESOLUTION RANGE HIGH (ANGSTROMS) : 2.36                           
REMARK   3   RESOLUTION RANGE LOW  (ANGSTROMS) : 6.00                           
REMARK   3   DATA CUTOFF            (SIGMA(F)) : 0.000                          
REMARK   3   DATA CUTOFF HIGH         (ABS(F)) : NULL                           
REMARK   3   DATA CUTOFF LOW          (ABS(F)) : NULL                           
REMARK   3   COMPLETENESS (WORKING+TEST)   (%) : 97.0                           
REMARK   3   NUMBER OF REFLECTIONS             : 21128                          
REMARK   3                                                                      
REMARK   3  FIT TO DATA USED IN REFINEMENT.                                     
REMARK   3   CROSS-VALIDATION METHOD          : THROUGHOUT                      
REMARK   3   FREE R VALUE TEST SET SELECTION  : RANDOM                          
REMARK   3   R VALUE            (WORKING SET) : 0.238                           
REMARK   3   FREE R VALUE                     : 0.306                           
REMARK   3   FREE R VALUE TEST SET SIZE   (%) : NULL                            
REMARK   3   FREE R VALUE TEST SET COUNT      : NULL                            
REMARK   3   ESTIMATED ERROR OF FREE R VALUE  : NULL                            
REMARK   3                                                                      
REMARK   3  FIT IN THE HIGHEST RESOLUTION BIN.                                  
REMARK   3   TOTAL NUMBER OF BINS USED           : 8                            
REMARK   3   BIN RESOLUTION RANGE HIGH       (A) : 2.36                         
REMARK   3   BIN RESOLUTION RANGE LOW        (A) : 2.46                         
REMARK   3   BIN COMPLETENESS (WORKING+TEST) (%) : 91.00                        
REMARK   3   REFLECTIONS IN BIN    (WORKING SET) : 1049                         
REMARK   3   BIN R VALUE           (WORKING SET) : 0.3500                       
REMARK   3   BIN FREE R VALUE                    : 0.4020                       
REMARK   3   BIN FREE R VALUE TEST SET SIZE  (%) : NULL                         
REMARK   3   BIN FREE R VALUE TEST SET COUNT     : NULL                         
REMARK   3   ESTIMATED ERROR OF BIN FREE R VALUE : NULL                         
REMARK   3                                                                      
REMARK   3  NUMBER OF NON-HYDROGEN ATOMS USED IN REFINEMENT.                    
REMARK   3   PROTEIN ATOMS            : 4777                                    
REMARK   3   NUCLEIC ACID ATOMS       : 0                                       
REMARK   3   HETEROGEN ATOMS          : 0                                       
REMARK   3   SOLVENT ATOMS            : 107                                     
REMARK   3                                                                      
REMARK   3  B VALUES.                                                           
REMARK   3   FROM WILSON PLOT           (A**2) : NULL                           
REMARK   3   MEAN B VALUE      (OVERALL, A**2) : 25.00                          
REMARK   3   OVERALL ANISOTROPIC B VALUE.                                       
REMARK   3    B11 (A**2) : NULL                                                 
REMARK   3    B22 (A**2) : NULL                                                 
REMARK   3    B33 (A**2) : NULL                                                 
REMARK   3    B12 (A**2) : NULL                                                 
REMARK   3    B13 (A**2) : NULL                                                 
REMARK   3    B23 (A**2) : NULL                                                 
REMARK   3                                                                      
REMARK   3  ESTIMATED COORDINATE ERROR.                                         
REMARK   3   ESD FROM LUZZATI PLOT        (A) : NULL                            
REMARK   3   ESD FROM SIGMAA              (A) : NULL                            
REMARK   3   LOW RESOLUTION CUTOFF        (A) : NULL                            
REMARK   3                                                                      
REMARK   3  CROSS-VALIDATED ESTIMATED COORDINATE ERROR.                         
REMARK   3   ESD FROM C-V LUZZATI PLOT    (A) : NULL                            
REMARK   3   ESD FROM C-V SIGMAA          (A) : NULL                            
REMARK   3                                                                      
REMARK   3  RMS DEVIATIONS FROM IDEAL VALUES.                                   
REMARK   3   BOND LENGTHS                 (A) : 0.005                           
REMARK   3   BOND ANGLES            (DEGREES) : 1.300                           
REMARK   3   DIHEDRAL ANGLES        (DEGREES) : NULL                            
REMARK   3   IMPROPER ANGLES        (DEGREES) : NULL                            
REMARK   3                                                                      
REMARK   3  ISOTROPIC THERMAL MODEL : INDIVIDUAL ATOMIC                         
REMARK   3                                                                      
REMARK   3  ISOTROPIC THERMAL FACTOR RESTRAINTS.    RMS    SIGMA                
REMARK   3   MAIN-CHAIN BOND              (A**2) : NULL  ; NULL                 
REMARK   3   MAIN-CHAIN ANGLE             (A**2) : NULL  ; NULL                 
REMARK   3   SIDE-CHAIN BOND              (A**2) : NULL  ; NULL                 
REMARK   3   SIDE-CHAIN ANGLE             (A**2) : NULL  ; NULL                 
REMARK   3                                                                      
REMARK   3  NCS MODEL : NULL                                                    
REMARK   3                                                                      
REMARK   3  NCS RESTRAINTS.                         RMS   SIGMA/WEIGHT          
REMARK   3   GROUP  1  POSITIONAL            (A) : NULL  ; NULL                 
REMARK   3   GROUP  1  B-FACTOR           (A**2) : NULL  ; NULL                 
REMARK   3                                                                      
REMARK   3  PARAMETER FILE  1  : CYPFRAG_PARTEST.PRO                            
REMARK   3  PARAMETER FILE  2  : NULL                                           
REMARK   3  PARAMETER FILE  3  : NULL                                           
REMARK   3  TOPOLOGY FILE  1   : TOPHCSDX.PRO                                   
REMARK   3  TOPOLOGY FILE  2   : NULL                                           
REMARK   3  TOPOLOGY FILE  3   : NULL                                           
REMARK   3                                                                      
REMARK   3  OTHER REFINEMENT REMARKS: NULL                                      
REMARK   4                                                                      
REMARK   4 1AK4 COMPLIES WITH FORMAT V. 3.30, 13-JUL-11                         
REMARK 100                                                                      
REMARK 100 THIS ENTRY HAS BEEN PROCESSED BY BNL.                                
REMARK 100 THE DEPOSITION ID IS D_1000170915.                                   
REMARK 200                                                                      
REMARK 200 EXPERIMENTAL DETAILS                                                 
REMARK 200  EXPERIMENT TYPE                : X-RAY DIFFRACTION                  
REMARK 200  DATE OF DATA COLLECTION        : JUN-96                             
REMARK 200  TEMPERATURE           (KELVIN) : 100                                
REMARK 200  PH                             : 7.0                                
REMARK 200  NUMBER OF CRYSTALS USED        : 1                                  
REMARK 200                                                                      
REMARK 200  SYNCHROTRON              (Y/N) : Y                                  
REMARK 200  RADIATION SOURCE               : NSLS                               
REMARK 200  BEAMLINE                       : X12B                               
REMARK 200  X-RAY GENERATOR MODEL          : NULL                               
REMARK 200  MONOCHROMATIC OR LAUE    (M/L) : M                                  
REMARK 200  WAVELENGTH OR RANGE        (A) : 0.978                              
REMARK 200  MONOCHROMATOR                  : SI(111)                            
REMARK 200  OPTICS                         : COLLIMATOR                         
REMARK 200                                                                      
REMARK 200  DETECTOR TYPE                  : IMAGE PLATE                        
REMARK 200  DETECTOR MANUFACTURER          : MARRESEARCH                        
REMARK 200  INTENSITY-INTEGRATION SOFTWARE : DENZO                              
REMARK 200  DATA SCALING SOFTWARE          : SCALEPACK                          
REMARK 200                                                                      
REMARK 200  NUMBER OF UNIQUE REFLECTIONS   : 21503                              
REMARK 200  RESOLUTION RANGE HIGH      (A) : 2.360                              
REMARK 200  RESOLUTION RANGE LOW       (A) : 20.000                             
REMARK 200  REJECTION CRITERIA  (SIGMA(I)) : 0.000                              
REMARK 200                                                                      
REMARK 200 OVERALL.                                                             
REMARK 200  COMPLETENESS FOR RANGE     (%) : 97.0                               
REMARK 200  DATA REDUNDANCY                : NULL                               
REMARK 200  R MERGE                    (I) : NULL                               
REMARK 200  R SYM                      (I) : 0.11000                            
REMARK 200  <I/SIGMA(I)> FOR THE DATA SET  : 10.5000                            
REMARK 200                                                                      
REMARK 200 IN THE HIGHEST RESOLUTION SHELL.                                     
REMARK 200  HIGHEST RESOLUTION SHELL, RANGE HIGH (A) : 2.36                     
REMARK 200  HIGHEST RESOLUTION SHELL, RANGE LOW  (A) : 2.40                     
REMARK 200  COMPLETENESS FOR SHELL     (%) : 91.0                               
REMARK 200  DATA REDUNDANCY IN SHELL       : NULL                               
REMARK 200  R MERGE FOR SHELL          (I) : NULL                               
REMARK 200  R SYM FOR SHELL            (I) : 0.39900                            
REMARK 200  <I/SIGMA(I)> FOR SHELL         : 3.500                              
REMARK 200                                                                      
REMARK 200 DIFFRACTION PROTOCOL: NULL                                           
REMARK 200 METHOD USED TO DETERMINE THE STRUCTURE: MOLECULAR REPLACEMENT        
REMARK 200 SOFTWARE USED: X-PLOR 3.843                                          
REMARK 200 STARTING MODEL: CYPA STRUCTURE (PDB ENTRY 2CYH)                      
REMARK 200                                                                      
REMARK 200 REMARK: NULL                                                         
REMARK 280                                                                      
REMARK 280 CRYSTAL                                                              
REMARK 280 SOLVENT CONTENT, VS   (%): 36.00                                     
REMARK 280 MATTHEWS COEFFICIENT, VM (ANGSTROMS**3/DA): 2.10                     
REMARK 280                                                                      
REMARK 280 CRYSTALLIZATION CONDITIONS: THE PROTEIN SOLUTION WAS 0.25 MM CYPA    
REMARK 280  AND 0.25 MM CA(151) IN 10 MM TRISHCL (PH 8.0) AND 1 MM 2-           
REMARK 280  MERCAPTOETHANOL. THE RESERVOIR SOLUTION WAS 1ML OF 1.0 M LICL,      
REMARK 280  0.1 M BICINE (PH 7.0), AND 22% POLYETHYLENE GLYCOL 8000. THE        
REMARK 280  INITIAL DROP WAS 6 MICROL OF A 1:1 MIX OF PROTEIN AND RESERVOIR     
REMARK 280  SOLUTIONS.                                                          
REMARK 290                                                                      
REMARK 290 CRYSTALLOGRAPHIC SYMMETRY                                            
REMARK 290 SYMMETRY OPERATORS FOR SPACE GROUP: P 1 21 1                         
REMARK 290                                                                      
REMARK 290      SYMOP   SYMMETRY                                                
REMARK 290     NNNMMM   OPERATOR                                                
REMARK 290       1555   X,Y,Z                                                   
REMARK 290       2555   -X,Y+1/2,-Z                                             
REMARK 290                                                                      
REMARK 290     WHERE NNN -> OPERATOR NUMBER                                     
REMARK 290           MMM -> TRANSLATION VECTOR                                  
REMARK 290                                                                      
REMARK 290 CRYSTALLOGRAPHIC SYMMETRY TRANSFORMATIONS                            
REMARK 290 THE FOLLOWING TRANSFORMATIONS OPERATE ON THE ATOM/HETATM             
REMARK 290 RECORDS IN THIS ENTRY TO PRODUCE CRYSTALLOGRAPHICALLY                
REMARK 290 RELATED MOLECULES.                                                   
REMARK 290   SMTRY1   1  1.000000  0.000000  0.000000        0.00000            
REMARK 290   SMTRY2   1  0.000000  1.000000  0.000000        0.00000            
REMARK 290   SMTRY3   1  0.000000  0.000000  1.000000        0.00000            
REMARK 290   SMTRY1   2 -1.000000  0.000000  0.000000        0.00000            
REMARK 290   SMTRY2   2  0.000000  1.000000  0.000000       56.55000            
REMARK 290   SMTRY3   2  0.000000  0.000000 -1.000000        0.00000            
REMARK 290                                                                      
REMARK 290 REMARK: NULL                                                         
REMARK 300                                                                      
REMARK 300 BIOMOLECULE: 1, 2                                                    
REMARK 300 SEE REMARK 350 FOR THE AUTHOR PROVIDED AND/OR PROGRAM                
REMARK 300 GENERATED ASSEMBLY INFORMATION FOR THE STRUCTURE IN                  
REMARK 300 THIS ENTRY. THE REMARK MAY ALSO PROVIDE INFORMATION ON               
REMARK 300 BURIED SURFACE AREA.                                                 
REMARK 350                                                                      
REMARK 350 COORDINATES FOR A COMPLETE MULTIMER REPRESENTING THE KNOWN           
REMARK 350 BIOLOGICALLY SIGNIFICANT OLIGOMERIZATION STATE OF THE                
REMARK 350 MOLECULE CAN BE GENERATED BY APPLYING BIOMT TRANSFORMATIONS          
REMARK 350 GIVEN BELOW.  BOTH NON-CRYSTALLOGRAPHIC AND                          
REMARK 350 CRYSTALLOGRAPHIC OPERATIONS ARE GIVEN.                               
REMARK 350                                                                      
REMARK 350 BIOMOLECULE: 1                                                       
REMARK 350 AUTHOR DETERMINED BIOLOGICAL UNIT: DIMERIC                           
REMARK 350 APPLY THE FOLLOWING TO CHAINS: A, D                                  
REMARK 350   BIOMT1   1  1.000000  0.000000  0.000000        0.00000            
REMARK 350   BIOMT2   1  0.000000  1.000000  0.000000        0.00000            
REMARK 350   BIOMT3   1  0.000000  0.000000  1.000000        0.00000            
REMARK 350                                                                      
REMARK 350 BIOMOLECULE: 2                                                       
REMARK 350 AUTHOR DETERMINED BIOLOGICAL UNIT: DIMERIC                           
REMARK 350 APPLY THE FOLLOWING TO CHAINS: B, C                                  
REMARK 350   BIOMT1   1  1.000000  0.000000  0.000000        0.00000            
REMARK 350   BIOMT2   1  0.000000  1.000000  0.000000        0.00000            
REMARK 350   BIOMT3   1  0.000000  0.000000  1.000000        0.00000            
REMARK 465                                                                      
REMARK 465 MISSING RESIDUES                                                     
REMARK 465 THE FOLLOWING RESIDUES WERE NOT LOCATED IN THE                       
REMARK 465 EXPERIMENT. (M=MODEL NUMBER; RES=RESIDUE NAME; C=CHAIN               
REMARK 465 IDENTIFIER; SSSEQ=SEQUENCE NUMBER; I=INSERTION CODE.)                
REMARK 465                                                                      
REMARK 465   M RES C SSSEQI                                                     
REMARK 465     MET B     1                                                      
REMARK 465     VAL B     2                                                      
REMARK 480                                                                      
REMARK 480 ZERO OCCUPANCY ATOM                                                  
REMARK 480 THE FOLLOWING RESIDUES HAVE ATOMS MODELED WITH ZERO                  
REMARK 480 OCCUPANCY. THE LOCATION AND PROPERTIES OF THESE ATOMS                
REMARK 480 MAY NOT BE RELIABLE. (M=MODEL NUMBER; RES=RESIDUE NAME;              
REMARK 480 C=CHAIN IDENTIFIER; SSEQ=SEQUENCE NUMBER; I=INSERTION CODE):         
REMARK 480   M RES C SSEQI ATOMS                                                
REMARK 480     MET A    1   SD   CE                                             
REMARK 480     GLU A   15   CG   CD   OE1  OE2                                  
REMARK 480     ARG A   69   CG   CD   NE   CZ   NH1  NH2                        
REMARK 480     GLY A   80   N    CA   C    O                                    
REMARK 480     GLU A   81   N    CA   C    O    CB   CG   CD                    
REMARK 480     GLU A   81   OE1  OE2                                            
REMARK 480     ARG A  144   CG   CD   NE   CZ   NH1  NH2                        
REMARK 480     ARG A  148   CG   CD   NE   CZ   NH1  NH2                        
REMARK 480     LYS A  151   CG   CD   CE   NZ                                   
REMARK 480     LYS A  155   CG   CD   CE   NZ                                   
REMARK 480     GLU B   15   CG   CD   OE1  OE2                                  
REMARK 480     GLY B   80   N    CA   C    O                                    
REMARK 480     GLU B   81   N    CA   C    O    CB   CG   CD                    
REMARK 480     GLU B   81   OE1  OE2                                            
REMARK 480     LYS B   91   CG   CD   CE   NZ                                   
REMARK 480     ARG B  144   CG   CD   NE   CZ   NH1  NH2                        
REMARK 480     GLU B  165   N    CA   C    O    CB   CG   CD                    
REMARK 480     GLU B  165   OE1  OE2  OXT                                       
REMARK 480     GLN C  404   CG   CD   OE1  NE2                                  
REMARK 480     LEU C  406   N    CA   C    O    CB   CG   CD1                   
REMARK 480     LEU C  406   CD2                                                 
REMARK 480     GLN C  407   N    CA   C    O    CB   CG   CD                    
REMARK 480     GLN C  407   OE1  NE2                                            
REMARK 480     GLY C  408   N    CA   C    O                                    
REMARK 480     ARG C  418   CG   CD   NE   CZ   NH1  NH2                        
REMARK 480     LYS C  425   CG   CD   CE   NZ                                   
REMARK 480     LYS C  430   CG   CD   CE   NZ                                   
REMARK 480     GLU C  435   CG   CD   OE1  OE2                                  
REMARK 480     GLN C  463   CG   CD   OE1  NE2                                  
REMARK 480     GLN C  495   CG   CD   OE1  NE2                                  
REMARK 480     GLN C  512   CG   CD   OE1  NE2                                  
REMARK 480     ASN C  521   CG   OD1  ND2                                       
REMARK 480     GLU C  528   CG   CD   OE1  OE2                                  
REMARK 480     TYR C  545   O    OXT                                            
REMARK 480     PRO D  401   N    CA   C    O    CB   CG   CD                    
REMARK 480     ILE D  402   N    CA   C    O    CB   CG1  CG2                   
REMARK 480     ILE D  402   CD1                                                 
REMARK 480     VAL D  403   N    CA   C    O    CB   CG1  CG2                   
REMARK 480     GLN D  404   N    CA   C    O    CB   CG   CD                    
REMARK 480     GLN D  404   OE1  NE2                                            
REMARK 480     ASN D  405   N    CA   C    O    CB   CG   OD1                   
REMARK 480     ASN D  405   ND2                                                 
REMARK 480     LEU D  406   N    CA   C    O    CB   CG   CD1                   
REMARK 480     LEU D  406   CD2                                                 
REMARK 480     GLN D  407   N    CA   C    O    CB   CG   CD                    
REMARK 480     GLN D  407   OE1  NE2                                            
REMARK 480     GLY D  408   N    CA   C    O                                    
REMARK 480     GLN D  409   N    CA   C    O    CB   CG   CD                    
REMARK 480     GLN D  409   OE1  NE2                                            
REMARK 480     MET D  410   N    CA   C    O    CB   CG   SD                    
REMARK 480     MET D  410   CE                                                  
REMARK 480     VAL D  411   N    CA   C    O    CB   CG1  CG2                   
REMARK 480     ARG D  418   CG   CD   NE   CZ   NH1  NH2                        
REMARK 480     ASN D  421   CG   OD1  ND2                                       
REMARK 480     GLU D  428   CG   CD   OE1  OE2                                  
REMARK 480     GLU D  429   CG   CD   OE1  OE2                                  
REMARK 480     LYS D  430   CG   CD   CE   NZ                                   
REMARK 480     ALA D  431   N    CA   C    O    CB                              
REMARK 480     GLU D  435   CG   CD   OE1  OE2                                  
REMARK 480     SER D  441   OG                                                  
REMARK 480     GLU D  445   CG   CD   OE1  OE2                                  
REMARK 480     GLN D  450   CG   CD   OE1  NE2                                  
REMARK 480     GLY D  460   N    CA   C    O                                    
REMARK 480     GLY D  461   N    CA   C    O                                    
REMARK 480     HIS D  462   N    CA   C    O    CB   CG   ND1                   
REMARK 480     HIS D  462   CD2  CE1  NE2                                       
REMARK 480     GLN D  463   N    CA   C    O    CB   CG   CD                    
REMARK 480     GLN D  463   OE1  NE2                                            
REMARK 480     GLN D  467   CG   CD   OE1  NE2                                  
REMARK 480     LYS D  470   CG   CD   CE   NZ                                   
REMARK 480     GLU D  471   CG   CD   OE1  OE2                                  
REMARK 480     GLN D  495   N    CA   C    O    CB   CG   CD                    
REMARK 480     GLN D  495   OE1  NE2                                            
REMARK 480     MET D  496   N    CA   C    O    CB   CG   SD                    
REMARK 480     MET D  496   CE                                                  
REMARK 480     GLN D  512   CG   CD   OE1  NE2                                  
REMARK 480     GLU D  528   CG   CD   OE1  OE2                                  
REMARK 480     LYS D  540   CG   CD   CE   NZ                                   
REMARK 500                                                                      
REMARK 500 GEOMETRY AND STEREOCHEMISTRY                                         
REMARK 500 SUBTOPIC: TORSION ANGLES                                             
REMARK 500                                                                      
REMARK 500 TORSION ANGLES OUTSIDE THE EXPECTED RAMACHANDRAN REGIONS:            
REMARK 500 (M=MODEL NUMBER; RES=RESIDUE NAME; C=CHAIN IDENTIFIER;               
REMARK 500 SSEQ=SEQUENCE NUMBER; I=INSERTION CODE).                             
REMARK 500                                                                      
REMARK 500 STANDARD TABLE:                                                      
REMARK 500 FORMAT:(10X,I3,1X,A3,1X,A1,I4,A1,4X,F7.2,3X,F7.2)                    
REMARK 500                                                                      
REMARK 500 EXPECTED VALUES: GJ KLEYWEGT AND TA JONES (1996). PHI/PSI-           
REMARK 500 CHOLOGY: RAMACHANDRAN REVISITED. STRUCTURE 4, 1395 - 1400            
REMARK 500                                                                      
REMARK 500  M RES CSSEQI        PSI       PHI                                   
REMARK 500    PHE A  60      -77.53   -115.52                                   
REMARK 500    THR A  68      -66.34    -90.84                                   
REMARK 500    GLU A  81     -106.73   -149.30                                   
REMARK 500    PHE B  60      -77.65   -115.70                                   
REMARK 500    GLU B  81      -70.21    -68.63                                   
REMARK 500    LEU C 406       71.85    -68.87                                   
REMARK 500    GLN C 407      -35.75    176.71                                   
REMARK 500    ALA C 431     -170.48     54.58                                   
REMARK 500    ALA D 414     -179.20    -55.97                                   
REMARK 500    ALA D 431     -170.87     62.37                                   
REMARK 500    HIS D 462       57.73   -148.16                                   
REMARK 500                                                                      
REMARK 500 REMARK: NULL                                                         
DBREF  1AK4 A    2   165  UNP    P62937   PPIA_HUMAN       1    164             
DBREF  1AK4 B    2   165  UNP    P62937   PPIA_HUMAN       1    164             
DBREF  1AK4 C  401   545  UNP    P12497   POL_HV1N5      132    276             
DBREF  1AK4 D  401   545  UNP    P12497   POL_HV1N5      132    276             
SEQRES   1 A  165  MET VAL ASN PRO THR VAL PHE PHE ASP ILE ALA VAL ASP          
SEQRES   2 A  165  GLY GLU PRO LEU GLY ARG VAL SER PHE GLU LEU PHE ALA          
SEQRES   3 A  165  ASP LYS VAL PRO LYS THR ALA GLU ASN PHE ARG ALA LEU          
SEQRES   4 A  165  SER THR GLY GLU LYS GLY PHE GLY TYR LYS GLY SER CYS          
SEQRES   5 A  165  PHE HIS ARG ILE ILE PRO GLY PHE MET CYS GLN GLY GLY          
SEQRES   6 A  165  ASP PHE THR ARG HIS ASN GLY THR GLY GLY LYS SER ILE          
SEQRES   7 A  165  TYR GLY GLU LYS PHE GLU ASP GLU ASN PHE ILE LEU LYS          
SEQRES   8 A  165  HIS THR GLY PRO GLY ILE LEU SER MET ALA ASN ALA GLY          
SEQRES   9 A  165  PRO ASN THR ASN GLY SER GLN PHE PHE ILE CYS THR ALA          
SEQRES  10 A  165  LYS THR GLU TRP LEU ASP GLY LYS HIS VAL VAL PHE GLY          
SEQRES  11 A  165  LYS VAL LYS GLU GLY MET ASN ILE VAL GLU ALA MET GLU          
SEQRES  12 A  165  ARG PHE GLY SER ARG ASN GLY LYS THR SER LYS LYS ILE          
SEQRES  13 A  165  THR ILE ALA ASP CYS GLY GLN LEU GLU                          
SEQRES   1 B  165  MET VAL ASN PRO THR VAL PHE PHE ASP ILE ALA VAL ASP          
SEQRES   2 B  165  GLY GLU PRO LEU GLY ARG VAL SER PHE GLU LEU PHE ALA          
SEQRES   3 B  165  ASP LYS VAL PRO LYS THR ALA GLU ASN PHE ARG ALA LEU          
SEQRES   4 B  165  SER THR GLY GLU LYS GLY PHE GLY TYR LYS GLY SER CYS          
SEQRES   5 B  165  PHE HIS ARG ILE ILE PRO GLY PHE MET CYS GLN GLY GLY          
SEQRES   6 B  165  ASP PHE THR ARG HIS ASN GLY THR GLY GLY LYS SER ILE          
SEQRES   7 B  165  TYR GLY GLU LYS PHE GLU ASP GLU ASN PHE ILE LEU LYS          
SEQRES   8 B  165  HIS THR GLY PRO GLY ILE LEU SER MET ALA ASN ALA GLY          
SEQRES   9 B  165  PRO ASN THR ASN GLY SER GLN PHE PHE ILE CYS THR ALA          
SEQRES  10 B  165  LYS THR GLU TRP LEU ASP GLY LYS HIS VAL VAL PHE GLY          
SEQRES  11 B  165  LYS VAL LYS GLU GLY MET ASN ILE VAL GLU ALA MET GLU          
SEQRES  12 B  165  ARG PHE GLY SER ARG ASN GLY LYS THR SER LYS LYS ILE          
SEQRES  13 B  165  THR ILE ALA ASP CYS GLY GLN LEU GLU                          
SEQRES   1 C  145  PRO ILE VAL GLN ASN LEU GLN GLY GLN MET VAL HIS GLN          
SEQRES   2 C  145  ALA ILE SER PRO ARG THR LEU ASN ALA TRP VAL LYS VAL          
SEQRES   3 C  145  VAL GLU GLU LYS ALA PHE SER PRO GLU VAL ILE PRO MET          
SEQRES   4 C  145  PHE SER ALA LEU SER GLU GLY ALA THR PRO GLN ASP LEU          
SEQRES   5 C  145  ASN THR MET LEU ASN THR VAL GLY GLY HIS GLN ALA ALA          
SEQRES   6 C  145  MET GLN MET LEU LYS GLU THR ILE ASN GLU GLU ALA ALA          
SEQRES   7 C  145  GLU TRP ASP ARG LEU HIS PRO VAL HIS ALA GLY PRO ILE          
SEQRES   8 C  145  ALA PRO GLY GLN MET ARG GLU PRO ARG GLY SER ASP ILE          
SEQRES   9 C  145  ALA GLY THR THR SER THR LEU GLN GLU GLN ILE GLY TRP          
SEQRES  10 C  145  MET THR HIS ASN PRO PRO ILE PRO VAL GLY GLU ILE TYR          
SEQRES  11 C  145  LYS ARG TRP ILE ILE LEU GLY LEU ASN LYS ILE VAL ARG          
SEQRES  12 C  145  MET TYR                                                      
SEQRES   1 D  145  PRO ILE VAL GLN ASN LEU GLN GLY GLN MET VAL HIS GLN          
SEQRES   2 D  145  ALA ILE SER PRO ARG THR LEU ASN ALA TRP VAL LYS VAL          
SEQRES   3 D  145  VAL GLU GLU LYS ALA PHE SER PRO GLU VAL ILE PRO MET          
SEQRES   4 D  145  PHE SER ALA LEU SER GLU GLY ALA THR PRO GLN ASP LEU          
SEQRES   5 D  145  ASN THR MET LEU ASN THR VAL GLY GLY HIS GLN ALA ALA          
SEQRES   6 D  145  MET GLN MET LEU LYS GLU THR ILE ASN GLU GLU ALA ALA          
SEQRES   7 D  145  GLU TRP ASP ARG LEU HIS PRO VAL HIS ALA GLY PRO ILE          
SEQRES   8 D  145  ALA PRO GLY GLN MET ARG GLU PRO ARG GLY SER ASP ILE          
SEQRES   9 D  145  ALA GLY THR THR SER THR LEU GLN GLU GLN ILE GLY TRP          
SEQRES  10 D  145  MET THR HIS ASN PRO PRO ILE PRO VAL GLY GLU ILE TYR          
SEQRES  11 D  145  LYS ARG TRP ILE ILE LEU GLY LEU ASN LYS ILE VAL ARG          
SEQRES  12 D  145  MET TYR                                                      
FORMUL   5  HOH   *107(H2 O)                                                    
HELIX    1   1 PRO A   30  THR A   41  1                                  12    
HELIX    2   2 GLU A  120  LEU A  122  5                                   3    
HELIX    3   3 MET A  136  PHE A  145  1                                  10    
HELIX    4   4 PRO B   30  THR B   41  1                                  12    
HELIX    5   5 GLU B  120  LEU B  122  5                                   3    
HELIX    6   6 MET B  136  PHE B  145  1                                  10    
HELIX    7   7 PRO C  417  GLU C  429  1                                  13    
HELIX    8   8 PRO C  434  LEU C  443  5                                  10    
HELIX    9   9 PRO C  449  ASN C  457  1                                   9    
HELIX   10  10 GLN C  463  ARG C  482  1                                  20    
HELIX   11  11 GLY C  501  ILE C  504  1                                   4    
HELIX   12  12 LEU C  511  THR C  519  1                                   9    
HELIX   13  13 VAL C  526  ARG C  543  1                                  18    
HELIX   14  14 PRO D  417  GLU D  429  1                                  13    
HELIX   15  15 PRO D  434  LEU D  443  1                                  10    
HELIX   16  16 PRO D  449  ASN D  457  1                                   9    
HELIX   17  17 GLN D  463  ARG D  482  1                                  20    
HELIX   18  18 GLY D  501  ILE D  504  1                                   4    
HELIX   19  19 LEU D  511  MET D  518  1                                   8    
HELIX   20  20 VAL D  526  ARG D  543  1                                  18    
SHEET    1   A 8 ILE A 156  GLN A 163  0                                        
SHEET    2   A 8 THR A   5  VAL A  12 -1  N  ALA A  11   O  THR A 157           
SHEET    3   A 8 GLU A  15  LEU A  24 -1  N  PHE A  22   O  VAL A   6           
SHEET    4   A 8 VAL A 128  GLU A 134 -1  N  GLU A 134   O  SER A  21           
SHEET    5   A 8 ILE A  97  MET A 100 -1  N  LEU A  98   O  PHE A 129           
SHEET    6   A 8 PHE A 112  CYS A 115 -1  N  PHE A 113   O  SER A  99           
SHEET    7   A 8 MET A  61  GLY A  64 -1  N  GLY A  64   O  PHE A 112           
SHEET    8   A 8 PHE A  53  ILE A  57 -1  N  ILE A  57   O  MET A  61           
SHEET    1   B 8 ILE B 156  ILE B 158  0                                        
SHEET    2   B 8 THR B   5  VAL B  12 -1  N  ALA B  11   O  THR B 157           
SHEET    3   B 8 GLU B  15  LEU B  24 -1  N  PHE B  22   O  VAL B   6           
SHEET    4   B 8 VAL B 128  GLU B 134 -1  N  GLU B 134   O  SER B  21           
SHEET    5   B 8 ILE B  97  MET B 100 -1  N  LEU B  98   O  PHE B 129           
SHEET    6   B 8 PHE B 112  CYS B 115 -1  N  PHE B 113   O  SER B  99           
SHEET    7   B 8 MET B  61  GLY B  64 -1  N  GLY B  64   O  PHE B 112           
SHEET    8   B 8 PHE B  53  ILE B  57 -1  N  ILE B  57   O  MET B  61           
SHEET    1   C 2 THR B   5  ASP B   9  0                                        
SHEET    2   C 2 ASP B 160  GLU B 165 -1  N  GLU B 165   O  THR B   5           
SHEET    1   D 2 ILE C 402  GLN C 404  0                                        
SHEET    2   D 2 MET C 410  HIS C 412 -1  N  VAL C 411   O  VAL C 403           
SHEET    1   E 2 ILE D 402  GLN D 404  0                                        
SHEET    2   E 2 MET D 410  HIS D 412 -1  N  VAL D 411   O  VAL D 403           
CISPEP   1 ASN C  521    PRO C  522          0       -15.01                     
CISPEP   2 ASN D  521    PRO D  522          0       -22.50                     
CRYST1   38.600  113.100   67.000  90.00 100.70  90.00 P 1 21 1      4          
ORIGX1      1.000000  0.000000  0.000000        0.00000                         
ORIGX2      0.000000  1.000000  0.000000        0.00000                         
ORIGX3      0.000000  0.000000  1.000000        0.00000                         
SCALE1      0.025907  0.000000  0.004895        0.00000                         
SCALE2      0.000000  0.008842  0.000000        0.00000                         
SCALE3      0.000000  0.000000  0.015189        0.00000                         
ATOM      1  N   MET A   1      12.053  75.365  58.778  1.00 24.90           N  
ATOM      2  CA  MET A   1      13.487  75.384  58.363  1.00 26.17           C  
ATOM      3  C   MET A   1      13.644  74.828  56.945  1.00 25.70           C  
ATOM      4  O   MET A   1      12.856  73.985  56.527  1.00 31.65           O  
ATOM      5  CB  MET A   1      14.323  74.549  59.341  1.00 29.53           C  
ATOM      6  CG  MET A   1      14.560  75.215  60.694  1.00 33.93           C  
ATOM      7  SD  MET A   1      15.212  76.888  60.537  0.00 36.20           S  
ATOM      8  CE  MET A   1      16.976  76.568  60.518  0.00 37.48           C  
ATOM      9  H1  MET A   1      11.668  74.411  58.594  1.00  0.00           H  
ATOM     10  H2  MET A   1      11.925  75.609  59.777  1.00  0.00           H  
ATOM     11  H3  MET A   1      11.479  76.023  58.210  1.00  0.00           H  
ATOM     12  N   VAL A   2      14.673  75.273  56.227  1.00 20.71           N  
ATOM     13  CA  VAL A   2      14.881  74.858  54.839  1.00 18.11           C  
ATOM     14  C   VAL A   2      15.228  73.376  54.712  1.00 17.69           C  
ATOM     15  O   VAL A   2      14.551  72.631  54.007  1.00 21.06           O  
ATOM     16  CB  VAL A   2      15.991  75.700  54.166  1.00 19.85           C  
ATOM     17  CG1 VAL A   2      16.210  75.247  52.727  1.00 19.97           C  
ATOM     18  CG2 VAL A   2      15.610  77.169  54.195  1.00 16.23           C  
ATOM     19  H   VAL A   2      15.298  75.925  56.607  1.00  0.00           H  
ATOM     20  N   ASN A   3      16.254  72.945  55.436  1.00 19.76           N  
ATOM     21  CA  ASN A   3      16.668  71.545  55.424  1.00 18.61           C  
ATOM     22  C   ASN A   3      15.764  70.659  56.285  1.00 18.47           C  
ATOM     23  O   ASN A   3      15.585  70.911  57.479  1.00 15.76           O  
ATOM     24  CB  ASN A   3      18.120  71.422  55.890  1.00 18.00           C  
ATOM     25  CG  ASN A   3      19.093  72.088  54.941  1.00 22.71           C  
ATOM     26  OD1 ASN A   3      18.723  72.527  53.856  1.00 23.79           O  
ATOM     27  ND2 ASN A   3      20.346  72.168  55.344  1.00 24.49           N  
ATOM     28  H   ASN A   3      16.750  73.599  55.960  1.00  0.00           H  
ATOM     29 HD21 ASN A   3      20.948  72.636  54.738  1.00  0.00           H  
ATOM     30 HD22 ASN A   3      20.588  71.790  56.204  1.00  0.00           H  
ATOM     31  N   PRO A   4      15.149  69.634  55.672  1.00 23.87           N  
ATOM     32  CA  PRO A   4      14.294  68.645  56.338  1.00 22.88           C  
ATOM     33  C   PRO A   4      15.072  67.553  57.073  1.00 24.63           C  
ATOM     34  O   PRO A   4      16.235  67.277  56.762  1.00 24.94           O  
ATOM     35  CB  PRO A   4      13.460  68.070  55.190  1.00 23.82           C  
ATOM     36  CG  PRO A   4      14.341  68.207  54.000  1.00 23.60           C  
ATOM     37  CD  PRO A   4      15.092  69.497  54.203  1.00 27.49           C  
ATOM     38  N   THR A   5      14.416  66.941  58.053  1.00 21.61           N  
ATOM     39  CA  THR A   5      15.000  65.844  58.821  1.00 19.31           C  
ATOM     40  C   THR A   5      14.145  64.598  58.636  1.00 13.66           C  
ATOM     41  O   THR A   5      12.920  64.677  58.641  1.00 14.81           O  
ATOM     42  CB  THR A   5      15.072  66.193  60.334  1.00 18.64           C  
ATOM     43  OG1 THR A   5      15.900  67.348  60.516  1.00 22.85           O  
ATOM     44  CG2 THR A   5      15.650  65.030  61.138  1.00 10.24           C  
ATOM     45  H   THR A   5      13.506  67.256  58.253  1.00  0.00           H  
ATOM     46  HG1 THR A   5      15.589  68.061  59.953  1.00  0.00           H  
ATOM     47  N   VAL A   6      14.788  63.468  58.380  1.00 12.08           N  
ATOM     48  CA  VAL A   6      14.072  62.206  58.219  1.00 18.04           C  
ATOM     49  C   VAL A   6      14.651  61.156  59.157  1.00 17.08           C  
ATOM     50  O   VAL A   6      15.767  61.315  59.649  1.00 19.32           O  
ATOM     51  CB  VAL A   6      14.144  61.681  56.752  1.00 20.18           C  
ATOM     52  CG1 VAL A   6      13.439  62.649  55.808  1.00 19.49           C  
ATOM     53  CG2 VAL A   6      15.586  61.481  56.330  1.00 21.43           C  
ATOM     54  H   VAL A   6      15.771  63.502  58.331  1.00  0.00           H  
ATOM     55  N   PHE A   7      13.879  60.111  59.440  1.00 16.67           N  
ATOM     56  CA  PHE A   7      14.348  59.027  60.300  1.00 11.47           C  
ATOM     57  C   PHE A   7      14.187  57.648  59.667  1.00 15.04           C  
ATOM     58  O   PHE A   7      13.307  57.434  58.833  1.00 20.29           O  
ATOM     59  CB  PHE A   7      13.625  59.064  61.653  1.00 15.03           C  
ATOM     60  CG  PHE A   7      12.193  58.594  61.600  1.00  9.92           C  
ATOM     61  CD1 PHE A   7      11.164  59.488  61.328  1.00  5.70           C  
ATOM     62  CD2 PHE A   7      11.876  57.257  61.825  1.00  7.27           C  
ATOM     63  CE1 PHE A   7       9.846  59.059  61.278  1.00  5.35           C  
ATOM     64  CE2 PHE A   7      10.558  56.814  61.778  1.00  3.72           C  
ATOM     65  CZ  PHE A   7       9.543  57.716  61.504  1.00  8.94           C  
ATOM     66  H   PHE A   7      12.996  60.058  59.015  1.00  0.00           H  
ATOM     67  N   PHE A   8      15.065  56.728  60.054  1.00 17.44           N  
ATOM     68  CA  PHE A   8      14.935  55.308  59.727  1.00 18.12           C  
ATOM     69  C   PHE A   8      14.841  54.538  61.040  1.00 17.27           C  
ATOM     70  O   PHE A   8      15.615  54.786  61.965  1.00 21.64           O  
ATOM     71  CB  PHE A   8      16.170  54.792  58.968  1.00 20.39           C  
ATOM     72  CG  PHE A   8      16.241  55.208  57.519  1.00 25.15           C  
ATOM     73  CD1 PHE A   8      15.228  55.964  56.928  1.00 22.01           C  
ATOM     74  CD2 PHE A   8      17.349  54.859  56.750  1.00 14.79           C  
ATOM     75  CE1 PHE A   8      15.319  56.365  55.598  1.00 23.00           C  
ATOM     76  CE2 PHE A   8      17.448  55.257  55.420  1.00 26.85           C  
ATOM     77  CZ  PHE A   8      16.429  56.012  54.843  1.00 22.80           C  
ATOM     78  H   PHE A   8      15.808  57.012  60.607  1.00  0.00           H  
ATOM     79  N   ASP A   9      13.921  53.585  61.108  1.00 15.50           N  
ATOM     80  CA  ASP A   9      13.891  52.628  62.204  1.00 15.74           C  
ATOM     81  C   ASP A   9      14.454  51.300  61.724  1.00 13.66           C  
ATOM     82  O   ASP A   9      13.805  50.567  60.980  1.00 17.54           O  
ATOM     83  CB  ASP A   9      12.463  52.442  62.729  1.00 22.21           C  
ATOM     84  CG  ASP A   9      11.990  53.618  63.573  1.00 29.36           C  
ATOM     85  OD1 ASP A   9      12.831  54.260  64.239  1.00 33.15           O  
ATOM     86  OD2 ASP A   9      10.775  53.907  63.567  1.00 35.70           O  
ATOM     87  H   ASP A   9      13.293  53.525  60.375  1.00  0.00           H  
ATOM     88  N   ILE A  10      15.690  51.023  62.113  1.00 14.65           N  
ATOM     89  CA  ILE A  10      16.405  49.860  61.610  1.00 13.99           C  
ATOM     90  C   ILE A  10      16.068  48.605  62.408  1.00 17.39           C  
ATOM     91  O   ILE A  10      15.891  48.658  63.627  1.00 23.51           O  
ATOM     92  CB  ILE A  10      17.931  50.098  61.640  1.00 13.87           C  
ATOM     93  CG1 ILE A  10      18.270  51.399  60.903  1.00 12.36           C  
ATOM     94  CG2 ILE A  10      18.667  48.918  61.010  1.00 11.82           C  
ATOM     95  CD1 ILE A  10      18.010  51.356  59.413  1.00  8.44           C  
ATOM     96  H   ILE A  10      16.112  51.620  62.771  1.00  0.00           H  
ATOM     97  N   ALA A  11      15.891  47.497  61.698  1.00 16.34           N  
ATOM     98  CA  ALA A  11      15.619  46.212  62.324  1.00 14.04           C  
ATOM     99  C   ALA A  11      16.596  45.165  61.820  1.00 18.40           C  
ATOM    100  O   ALA A  11      17.071  45.238  60.687  1.00 28.11           O  
ATOM    101  CB  ALA A  11      14.189  45.775  62.035  1.00 13.13           C  
ATOM    102  H   ALA A  11      15.944  47.561  60.718  1.00  0.00           H  
ATOM    103  N   VAL A  12      16.963  44.247  62.705  1.00 22.69           N  
ATOM    104  CA  VAL A  12      17.858  43.145  62.375  1.00 26.08           C  
ATOM    105  C   VAL A  12      17.083  41.838  62.511  1.00 31.86           C  
ATOM    106  O   VAL A  12      16.635  41.488  63.603  1.00 39.49           O  
ATOM    107  CB  VAL A  12      19.072  43.109  63.334  1.00 23.15           C  
ATOM    108  CG1 VAL A  12      20.017  41.993  62.940  1.00 26.00           C  
ATOM    109  CG2 VAL A  12      19.790  44.449  63.325  1.00 19.26           C  
ATOM    110  H   VAL A  12      16.644  44.333  63.621  1.00  0.00           H  
ATOM    111  N   ASP A  13      16.828  41.182  61.383  1.00 33.39           N  
ATOM    112  CA  ASP A  13      15.975  39.994  61.359  1.00 34.05           C  
ATOM    113  C   ASP A  13      14.633  40.209  62.068  1.00 32.92           C  
ATOM    114  O   ASP A  13      14.135  39.321  62.756  1.00 37.45           O  
ATOM    115  CB  ASP A  13      16.708  38.805  61.988  1.00 40.73           C  
ATOM    116  CG  ASP A  13      17.606  38.084  61.004  1.00 50.92           C  
ATOM    117  OD1 ASP A  13      17.172  37.848  59.857  1.00 60.75           O  
ATOM    118  OD2 ASP A  13      18.736  37.719  61.388  1.00 57.01           O  
ATOM    119  H   ASP A  13      17.313  41.478  60.588  1.00  0.00           H  
ATOM    120  N   GLY A  14      14.071  41.404  61.929  1.00 28.31           N  
ATOM    121  CA  GLY A  14      12.811  41.704  62.586  1.00 32.05           C  
ATOM    122  C   GLY A  14      12.946  42.370  63.945  1.00 32.20           C  
ATOM    123  O   GLY A  14      12.103  43.178  64.327  1.00 41.57           O  
ATOM    124  H   GLY A  14      14.479  42.074  61.347  1.00  0.00           H  
ATOM    125  N   GLU A  15      14.033  42.086  64.653  1.00 29.75           N  
ATOM    126  CA  GLU A  15      14.269  42.672  65.973  1.00 27.05           C  
ATOM    127  C   GLU A  15      14.784  44.112  65.877  1.00 22.19           C  
ATOM    128  O   GLU A  15      15.776  44.386  65.208  1.00 23.56           O  
ATOM    129  CB  GLU A  15      15.272  41.821  66.761  1.00 27.72           C  
ATOM    130  CG  GLU A  15      15.023  40.321  66.700  0.00 32.03           C  
ATOM    131  CD  GLU A  15      16.253  39.512  67.069  0.00 34.80           C  
ATOM    132  OE1 GLU A  15      17.205  39.470  66.260  0.00 33.03           O  
ATOM    133  OE2 GLU A  15      16.270  38.919  68.168  0.00 33.28           O  
ATOM    134  H   GLU A  15      14.696  41.472  64.272  1.00  0.00           H  
ATOM    135  N   PRO A  16      14.107  45.054  66.544  1.00 22.40           N  
ATOM    136  CA  PRO A  16      14.507  46.465  66.530  1.00 23.86           C  
ATOM    137  C   PRO A  16      15.935  46.730  67.011  1.00 26.33           C  
ATOM    138  O   PRO A  16      16.330  46.294  68.090  1.00 36.74           O  
ATOM    139  CB  PRO A  16      13.475  47.130  67.438  1.00 21.17           C  
ATOM    140  CG  PRO A  16      12.270  46.266  67.292  1.00 23.69           C  
ATOM    141  CD  PRO A  16      12.807  44.867  67.212  1.00 17.93           C  
ATOM    142  N   LEU A  17      16.694  47.470  66.211  1.00 29.02           N  
ATOM    143  CA  LEU A  17      18.042  47.895  66.583  1.00 25.92           C  
ATOM    144  C   LEU A  17      18.024  49.324  67.136  1.00 26.04           C  
ATOM    145  O   LEU A  17      18.448  49.576  68.268  1.00 25.28           O  
ATOM    146  CB  LEU A  17      18.967  47.823  65.364  1.00 27.16           C  
ATOM    147  CG  LEU A  17      20.444  48.171  65.573  1.00 34.04           C  
ATOM    148  CD1 LEU A  17      21.146  47.032  66.298  1.00 27.08           C  
ATOM    149  CD2 LEU A  17      21.104  48.424  64.227  1.00 28.95           C  
ATOM    150  H   LEU A  17      16.317  47.712  65.340  1.00  0.00           H  
ATOM    151  N   GLY A  18      17.528  50.256  66.328  1.00 19.90           N  
ATOM    152  CA  GLY A  18      17.398  51.631  66.773  1.00 15.53           C  
ATOM    153  C   GLY A  18      17.087  52.603  65.655  1.00 16.09           C  
ATOM    154  O   GLY A  18      16.904  52.202  64.505  1.00 20.23           O  
ATOM    155  H   GLY A  18      17.227  50.002  65.432  1.00  0.00           H  
ATOM    156  N   ARG A  19      17.053  53.889  65.982  1.00 18.49           N  
ATOM    157  CA  ARG A  19      16.695  54.910  65.006  1.00 22.18           C  
ATOM    158  C   ARG A  19      17.887  55.751  64.574  1.00 21.06           C  
ATOM    159  O   ARG A  19      18.668  56.210  65.403  1.00 19.35           O  
ATOM    160  CB  ARG A  19      15.600  55.828  65.557  1.00 21.41           C  
ATOM    161  CG  ARG A  19      15.305  57.029  64.663  1.00 20.77           C  
ATOM    162  CD  ARG A  19      14.169  57.857  65.219  1.00 20.69           C  
ATOM    163  NE  ARG A  19      12.901  57.145  65.121  1.00 16.04           N  
ATOM    164  CZ  ARG A  19      11.711  57.730  65.190  1.00 13.58           C  
ATOM    165  NH1 ARG A  19      11.618  59.029  65.443  1.00 18.97           N  
ATOM    166  NH2 ARG A  19      10.613  57.015  64.989  1.00 14.32           N  
ATOM    167  H   ARG A  19      17.304  54.150  66.897  1.00  0.00           H  
ATOM    168  HE  ARG A  19      12.920  56.176  65.009  1.00  0.00           H  
ATOM    169 HH11 ARG A  19      12.442  59.577  65.589  1.00  0.00           H  
ATOM    170 HH12 ARG A  19      10.719  59.463  65.494  1.00  0.00           H  
ATOM    171 HH21 ARG A  19      10.681  56.041  64.773  1.00  0.00           H  
ATOM    172 HH22 ARG A  19       9.717  57.458  65.035  1.00  0.00           H  
ATOM    173  N   VAL A  20      18.018  55.935  63.265  1.00 22.39           N  
ATOM    174  CA  VAL A  20      18.960  56.898  62.704  1.00 15.05           C  
ATOM    175  C   VAL A  20      18.178  58.049  62.065  1.00 15.97           C  
ATOM    176  O   VAL A  20      17.225  57.823  61.320  1.00 17.70           O  
ATOM    177  CB  VAL A  20      19.848  56.253  61.613  1.00 16.19           C  
ATOM    178  CG1 VAL A  20      21.051  57.142  61.318  1.00 13.78           C  
ATOM    179  CG2 VAL A  20      20.290  54.867  62.044  1.00  8.70           C  
ATOM    180  H   VAL A  20      17.408  55.434  62.680  1.00  0.00           H  
ATOM    181  N   SER A  21      18.554  59.280  62.383  1.00 12.21           N  
ATOM    182  CA  SER A  21      17.961  60.438  61.727  1.00 15.30           C  
ATOM    183  C   SER A  21      18.988  61.185  60.879  1.00 17.69           C  
ATOM    184  O   SER A  21      20.194  61.095  61.118  1.00 12.67           O  
ATOM    185  CB  SER A  21      17.338  61.389  62.755  1.00 14.80           C  
ATOM    186  OG  SER A  21      18.285  61.825  63.714  1.00 27.72           O  
ATOM    187  H   SER A  21      19.231  59.395  63.073  1.00  0.00           H  
ATOM    188  HG  SER A  21      17.792  62.409  64.304  1.00  0.00           H  
ATOM    189  N   PHE A  22      18.504  61.874  59.851  1.00 14.54           N  
ATOM    190  CA  PHE A  22      19.369  62.537  58.882  1.00 11.14           C  
ATOM    191  C   PHE A  22      18.925  63.973  58.677  1.00  9.71           C  
ATOM    192  O   PHE A  22      17.732  64.255  58.638  1.00 16.33           O  
ATOM    193  CB  PHE A  22      19.318  61.820  57.525  1.00  9.05           C  
ATOM    194  CG  PHE A  22      19.515  60.332  57.605  1.00  6.70           C  
ATOM    195  CD1 PHE A  22      20.785  59.783  57.527  1.00  6.07           C  
ATOM    196  CD2 PHE A  22      18.423  59.479  57.705  1.00  2.29           C  
ATOM    197  CE1 PHE A  22      20.963  58.408  57.541  1.00  2.25           C  
ATOM    198  CE2 PHE A  22      18.595  58.105  57.723  1.00  5.23           C  
ATOM    199  CZ  PHE A  22      19.865  57.568  57.639  1.00  3.75           C  
ATOM    200  H   PHE A  22      17.532  61.926  59.749  1.00  0.00           H  
ATOM    201  N   GLU A  23      19.882  64.875  58.514  1.00 11.60           N  
ATOM    202  CA  GLU A  23      19.580  66.199  57.985  1.00 16.09           C  
ATOM    203  C   GLU A  23      19.852  66.218  56.484  1.00 19.32           C  
ATOM    204  O   GLU A  23      20.881  65.720  56.027  1.00 21.84           O  
ATOM    205  CB  GLU A  23      20.434  67.267  58.665  1.00 17.82           C  
ATOM    206  CG  GLU A  23      20.089  68.684  58.216  1.00 25.71           C  
ATOM    207  CD  GLU A  23      21.236  69.666  58.372  1.00 29.45           C  
ATOM    208  OE1 GLU A  23      22.296  69.287  58.915  1.00 40.00           O  
ATOM    209  OE2 GLU A  23      21.075  70.828  57.943  1.00 28.21           O  
ATOM    210  H   GLU A  23      20.800  64.628  58.742  1.00  0.00           H  
ATOM    211  N   LEU A  24      18.919  66.769  55.718  1.00 18.64           N  
ATOM    212  CA  LEU A  24      19.051  66.801  54.264  1.00 14.34           C  
ATOM    213  C   LEU A  24      19.333  68.215  53.788  1.00 13.62           C  
ATOM    214  O   LEU A  24      18.568  69.141  54.062  1.00 20.97           O  
ATOM    215  CB  LEU A  24      17.776  66.278  53.595  1.00 12.08           C  
ATOM    216  CG  LEU A  24      17.285  64.884  53.990  1.00  4.45           C  
ATOM    217  CD1 LEU A  24      16.043  64.549  53.190  1.00 11.55           C  
ATOM    218  CD2 LEU A  24      18.365  63.853  53.740  1.00  2.42           C  
ATOM    219  H   LEU A  24      18.096  67.084  56.152  1.00  0.00           H  
ATOM    220  N   PHE A  25      20.439  68.382  53.076  1.00 15.10           N  
ATOM    221  CA  PHE A  25      20.894  69.711  52.684  1.00 22.32           C  
ATOM    222  C   PHE A  25      20.165  70.220  51.448  1.00 21.97           C  
ATOM    223  O   PHE A  25      20.775  70.491  50.414  1.00 29.85           O  
ATOM    224  CB  PHE A  25      22.411  69.706  52.453  1.00 20.54           C  
ATOM    225  CG  PHE A  25      23.191  69.130  53.599  1.00 15.15           C  
ATOM    226  CD1 PHE A  25      23.029  69.628  54.885  1.00 17.43           C  
ATOM    227  CD2 PHE A  25      24.063  68.068  53.398  1.00 17.02           C  
ATOM    228  CE1 PHE A  25      23.723  69.075  55.954  1.00 14.33           C  
ATOM    229  CE2 PHE A  25      24.764  67.512  54.460  1.00 15.83           C  
ATOM    230  CZ  PHE A  25      24.592  68.017  55.740  1.00 10.36           C  
ATOM    231  H   PHE A  25      20.936  67.576  52.821  1.00  0.00           H  
ATOM    232  N   ALA A  26      18.874  70.480  51.610  1.00 20.73           N  
ATOM    233  CA  ALA A  26      18.051  70.985  50.522  1.00 18.59           C  
ATOM    234  C   ALA A  26      18.480  72.390  50.109  1.00 14.72           C  
ATOM    235  O   ALA A  26      18.185  72.841  49.005  1.00 21.40           O  
ATOM    236  CB  ALA A  26      16.581  70.972  50.928  1.00 18.97           C  
ATOM    237  H   ALA A  26      18.469  70.300  52.486  1.00  0.00           H  
ATOM    238  N   ASP A  27      19.228  73.056  50.978  1.00 10.62           N  
ATOM    239  CA  ASP A  27      19.796  74.362  50.660  1.00 12.27           C  
ATOM    240  C   ASP A  27      20.961  74.284  49.671  1.00 13.51           C  
ATOM    241  O   ASP A  27      21.330  75.285  49.056  1.00 17.73           O  
ATOM    242  CB  ASP A  27      20.241  75.082  51.947  1.00 20.35           C  
ATOM    243  CG  ASP A  27      21.328  74.321  52.726  1.00 23.35           C  
ATOM    244  OD1 ASP A  27      21.470  73.088  52.572  1.00 21.90           O  
ATOM    245  OD2 ASP A  27      22.025  74.965  53.535  1.00 35.19           O  
ATOM    246  H   ASP A  27      19.286  72.697  51.888  1.00  0.00           H  
ATOM    247  N   LYS A  28      21.529  73.091  49.514  1.00 14.79           N  
ATOM    248  CA  LYS A  28      22.632  72.876  48.575  1.00 22.25           C  
ATOM    249  C   LYS A  28      22.199  71.997  47.404  1.00 22.07           C  
ATOM    250  O   LYS A  28      22.544  72.258  46.253  1.00 27.25           O  
ATOM    251  CB  LYS A  28      23.819  72.213  49.285  1.00 29.17           C  
ATOM    252  CG  LYS A  28      24.413  73.023  50.427  1.00 32.11           C  
ATOM    253  CD  LYS A  28      25.202  74.210  49.915  1.00 29.85           C  
ATOM    254  CE  LYS A  28      25.718  75.055  51.062  1.00 34.03           C  
ATOM    255  NZ  LYS A  28      24.617  75.774  51.751  1.00 44.70           N  
ATOM    256  H   LYS A  28      21.202  72.360  50.070  1.00  0.00           H  
ATOM    257  HZ1 LYS A  28      24.118  76.349  51.044  1.00  0.00           H  
ATOM    258  HZ2 LYS A  28      23.953  75.092  52.168  1.00  0.00           H  
ATOM    259  HZ3 LYS A  28      24.998  76.396  52.491  1.00  0.00           H  
ATOM    260  N   VAL A  29      21.466  70.933  47.719  1.00 18.93           N  
ATOM    261  CA  VAL A  29      20.998  69.976  46.719  1.00 12.64           C  
ATOM    262  C   VAL A  29      19.503  69.667  46.859  1.00  9.15           C  
ATOM    263  O   VAL A  29      19.112  68.560  47.244  1.00  4.87           O  
ATOM    264  CB  VAL A  29      21.803  68.654  46.789  1.00 13.63           C  
ATOM    265  CG1 VAL A  29      23.152  68.831  46.117  1.00 18.15           C  
ATOM    266  CG2 VAL A  29      21.992  68.226  48.232  1.00 14.21           C  
ATOM    267  H   VAL A  29      21.273  70.793  48.661  1.00  0.00           H  
ATOM    268  N   PRO A  30      18.644  70.632  46.494  1.00 11.80           N  
ATOM    269  CA  PRO A  30      17.200  70.505  46.724  1.00 16.95           C  
ATOM    270  C   PRO A  30      16.554  69.296  46.051  1.00 15.82           C  
ATOM    271  O   PRO A  30      15.862  68.516  46.700  1.00 23.13           O  
ATOM    272  CB  PRO A  30      16.625  71.828  46.198  1.00 13.29           C  
ATOM    273  CG  PRO A  30      17.749  72.507  45.490  1.00 13.24           C  
ATOM    274  CD  PRO A  30      19.007  72.004  46.108  1.00 10.37           C  
ATOM    275  N   LYS A  31      16.854  69.094  44.773  1.00 20.54           N  
ATOM    276  CA  LYS A  31      16.260  67.997  44.005  1.00 23.32           C  
ATOM    277  C   LYS A  31      16.641  66.611  44.546  1.00 19.84           C  
ATOM    278  O   LYS A  31      15.833  65.681  44.542  1.00 24.91           O  
ATOM    279  CB  LYS A  31      16.668  68.119  42.532  1.00 25.48           C  
ATOM    280  CG  LYS A  31      15.883  67.225  41.592  1.00 37.47           C  
ATOM    281  CD  LYS A  31      16.257  67.467  40.141  1.00 43.73           C  
ATOM    282  CE  LYS A  31      15.473  66.548  39.215  1.00 42.02           C  
ATOM    283  NZ  LYS A  31      16.002  66.583  37.825  1.00 52.78           N  
ATOM    284  H   LYS A  31      17.413  69.758  44.330  1.00  0.00           H  
ATOM    285  HZ1 LYS A  31      17.024  66.385  37.851  1.00  0.00           H  
ATOM    286  HZ2 LYS A  31      15.529  65.866  37.241  1.00  0.00           H  
ATOM    287  HZ3 LYS A  31      15.849  67.527  37.417  1.00  0.00           H  
ATOM    288  N   THR A  32      17.849  66.504  45.088  1.00 24.32           N  
ATOM    289  CA  THR A  32      18.358  65.236  45.615  1.00 18.93           C  
ATOM    290  C   THR A  32      17.866  64.978  47.044  1.00 15.80           C  
ATOM    291  O   THR A  32      17.489  63.855  47.393  1.00 11.41           O  
ATOM    292  CB  THR A  32      19.904  65.213  45.595  1.00 19.99           C  
ATOM    293  OG1 THR A  32      20.382  65.758  44.354  1.00  9.20           O  
ATOM    294  CG2 THR A  32      20.415  63.794  45.739  1.00 10.55           C  
ATOM    295  H   THR A  32      18.392  67.308  45.136  1.00  0.00           H  
ATOM    296  HG1 THR A  32      20.906  66.538  44.567  1.00  0.00           H  
ATOM    297  N   ALA A  33      17.806  66.041  47.841  1.00 15.31           N  
ATOM    298  CA  ALA A  33      17.203  65.992  49.172  1.00 13.63           C  
ATOM    299  C   ALA A  33      15.708  65.661  49.107  1.00 14.59           C  
ATOM    300  O   ALA A  33      15.226  64.775  49.821  1.00 12.34           O  
ATOM    301  CB  ALA A  33      17.413  67.327  49.879  1.00  6.16           C  
ATOM    302  H   ALA A  33      18.191  66.883  47.530  1.00  0.00           H  
ATOM    303  N   GLU A  34      15.004  66.311  48.181  1.00 10.40           N  
ATOM    304  CA  GLU A  34      13.579  66.072  47.963  1.00 11.15           C  
ATOM    305  C   GLU A  34      13.265  64.628  47.579  1.00 11.25           C  
ATOM    306  O   GLU A  34      12.379  64.004  48.167  1.00 15.81           O  
ATOM    307  CB  GLU A  34      13.041  67.031  46.893  1.00 19.58           C  
ATOM    308  CG  GLU A  34      11.563  66.841  46.532  1.00 23.90           C  
ATOM    309  CD  GLU A  34      10.605  66.972  47.717  1.00 23.52           C  
ATOM    310  OE1 GLU A  34      10.911  67.701  48.684  1.00 26.84           O  
ATOM    311  OE2 GLU A  34       9.511  66.376  47.654  1.00 26.11           O  
ATOM    312  H   GLU A  34      15.453  67.023  47.693  1.00  0.00           H  
ATOM    313  N   ASN A  35      14.047  64.067  46.663  1.00 10.71           N  
ATOM    314  CA  ASN A  35      13.888  62.660  46.300  1.00  9.08           C  
ATOM    315  C   ASN A  35      13.949  61.749  47.522  1.00  9.28           C  
ATOM    316  O   ASN A  35      13.055  60.937  47.745  1.00 19.72           O  
ATOM    317  CB  ASN A  35      14.959  62.237  45.292  1.00  7.67           C  
ATOM    318  CG  ASN A  35      14.760  60.819  44.799  1.00 12.78           C  
ATOM    319  OD1 ASN A  35      13.720  60.498  44.238  1.00 19.68           O  
ATOM    320  ND2 ASN A  35      15.728  59.953  45.051  1.00 11.30           N  
ATOM    321  H   ASN A  35      14.701  64.631  46.199  1.00  0.00           H  
ATOM    322 HD21 ASN A  35      15.629  59.056  44.674  1.00  0.00           H  
ATOM    323 HD22 ASN A  35      16.494  60.259  45.582  1.00  0.00           H  
ATOM    324  N   PHE A  36      14.987  61.917  48.336  1.00 14.54           N  
ATOM    325  CA  PHE A  36      15.184  61.081  49.520  1.00  9.73           C  
ATOM    326  C   PHE A  36      14.090  61.292  50.572  1.00  5.76           C  
ATOM    327  O   PHE A  36      13.592  60.334  51.160  1.00 10.97           O  
ATOM    328  CB  PHE A  36      16.559  61.368  50.131  1.00 10.01           C  
ATOM    329  CG  PHE A  36      16.964  60.397  51.204  1.00 10.03           C  
ATOM    330  CD1 PHE A  36      17.612  59.209  50.874  1.00  5.63           C  
ATOM    331  CD2 PHE A  36      16.702  60.671  52.545  1.00  7.30           C  
ATOM    332  CE1 PHE A  36      17.993  58.304  51.864  1.00  7.21           C  
ATOM    333  CE2 PHE A  36      17.082  59.773  53.544  1.00  9.58           C  
ATOM    334  CZ  PHE A  36      17.730  58.587  53.201  1.00  8.24           C  
ATOM    335  H   PHE A  36      15.657  62.590  48.090  1.00  0.00           H  
ATOM    336  N   ARG A  37      13.723  62.550  50.804  1.00  9.66           N  
ATOM    337  CA  ARG A  37      12.668  62.901  51.760  1.00 13.09           C  
ATOM    338  C   ARG A  37      11.325  62.236  51.428  1.00 18.02           C  
ATOM    339  O   ARG A  37      10.769  61.495  52.248  1.00 20.55           O  
ATOM    340  CB  ARG A  37      12.491  64.425  51.807  1.00 14.89           C  
ATOM    341  CG  ARG A  37      11.509  64.909  52.865  1.00  8.64           C  
ATOM    342  CD  ARG A  37      10.981  66.296  52.540  1.00 12.73           C  
ATOM    343  NE  ARG A  37      10.156  66.290  51.334  1.00 22.86           N  
ATOM    344  CZ  ARG A  37       8.939  65.754  51.260  1.00 24.54           C  
ATOM    345  NH1 ARG A  37       8.333  65.306  52.352  1.00 20.75           N  
ATOM    346  NH2 ARG A  37       8.303  65.716  50.099  1.00 25.02           N  
ATOM    347  H   ARG A  37      14.201  63.256  50.324  1.00  0.00           H  
ATOM    348  HE  ARG A  37      10.523  66.709  50.532  1.00  0.00           H  
ATOM    349 HH11 ARG A  37       8.786  65.366  53.241  1.00  0.00           H  
ATOM    350 HH12 ARG A  37       7.424  64.899  52.283  1.00  0.00           H  
ATOM    351 HH21 ARG A  37       8.727  66.120  49.298  1.00  0.00           H  
ATOM    352 HH22 ARG A  37       7.394  65.304  50.035  1.00  0.00           H  
ATOM    353  N   ALA A  38      10.856  62.430  50.196  1.00 17.97           N  
ATOM    354  CA  ALA A  38       9.580  61.871  49.746  1.00  9.77           C  
ATOM    355  C   ALA A  38       9.567  60.346  49.764  1.00 10.79           C  
ATOM    356  O   ALA A  38       8.545  59.733  50.076  1.00 15.35           O  
ATOM    357  CB  ALA A  38       9.249  62.381  48.352  1.00 10.93           C  
ATOM    358  H   ALA A  38      11.388  62.988  49.584  1.00  0.00           H  
ATOM    359  N   LEU A  39      10.711  59.731  49.476  1.00 15.70           N  
ATOM    360  CA  LEU A  39      10.834  58.271  49.530  1.00 16.04           C  
ATOM    361  C   LEU A  39      10.865  57.742  50.970  1.00 16.47           C  
ATOM    362  O   LEU A  39      10.599  56.561  51.218  1.00 13.78           O  
ATOM    363  CB  LEU A  39      12.097  57.814  48.790  1.00 13.19           C  
ATOM    364  CG  LEU A  39      12.151  57.982  47.269  1.00 18.64           C  
ATOM    365  CD1 LEU A  39      13.532  57.599  46.761  1.00 11.00           C  
ATOM    366  CD2 LEU A  39      11.090  57.119  46.609  1.00 17.29           C  
ATOM    367  H   LEU A  39      11.465  60.267  49.139  1.00  0.00           H  
ATOM    368  N   SER A  40      11.211  58.616  51.910  1.00 17.22           N  
ATOM    369  CA  SER A  40      11.220  58.268  53.329  1.00 18.31           C  
ATOM    370  C   SER A  40       9.834  58.377  53.953  1.00 16.37           C  
ATOM    371  O   SER A  40       9.469  57.573  54.809  1.00 22.79           O  
ATOM    372  CB  SER A  40      12.201  59.162  54.094  1.00  9.47           C  
ATOM    373  OG  SER A  40      13.526  58.947  53.640  1.00 15.22           O  
ATOM    374  H   SER A  40      11.542  59.495  51.621  1.00  0.00           H  
ATOM    375  HG  SER A  40      13.625  59.254  52.729  1.00  0.00           H  
ATOM    376  N   THR A  41       9.055  59.358  53.505  1.00 17.18           N  
ATOM    377  CA  THR A  41       7.671  59.509  53.959  1.00 15.62           C  
ATOM    378  C   THR A  41       6.696  58.567  53.250  1.00 18.62           C  
ATOM    379  O   THR A  41       5.610  58.306  53.754  1.00 24.47           O  
ATOM    380  CB  THR A  41       7.152  60.934  53.749  1.00 14.49           C  
ATOM    381  OG1 THR A  41       6.982  61.169  52.348  1.00 16.73           O  
ATOM    382  CG2 THR A  41       8.117  61.956  54.327  1.00  6.02           C  
ATOM    383  H   THR A  41       9.441  60.005  52.874  1.00  0.00           H  
ATOM    384  HG1 THR A  41       6.418  61.944  52.309  1.00  0.00           H  
ATOM    385  N   GLY A  42       7.034  58.157  52.033  1.00 23.24           N  
ATOM    386  CA  GLY A  42       6.193  57.221  51.304  1.00 21.03           C  
ATOM    387  C   GLY A  42       4.976  57.863  50.655  1.00 27.18           C  
ATOM    388  O   GLY A  42       4.090  57.170  50.155  1.00 29.36           O  
ATOM    389  H   GLY A  42       7.850  58.518  51.635  1.00  0.00           H  
ATOM    390  N   GLU A  43       5.005  59.186  50.534  1.00 26.80           N  
ATOM    391  CA  GLU A  43       3.879  59.945  50.003  1.00 20.44           C  
ATOM    392  C   GLU A  43       3.571  59.713  48.520  1.00 26.56           C  
ATOM    393  O   GLU A  43       2.547  60.183  48.015  1.00 30.80           O  
ATOM    394  CB  GLU A  43       4.090  61.439  50.255  1.00 15.45           C  
ATOM    395  CG  GLU A  43       5.397  62.005  49.734  1.00  7.98           C  
ATOM    396  CD  GLU A  43       5.635  63.423  50.219  1.00 14.27           C  
ATOM    397  OE1 GLU A  43       5.945  63.607  51.412  1.00 22.51           O  
ATOM    398  OE2 GLU A  43       5.483  64.365  49.418  1.00 24.56           O  
ATOM    399  H   GLU A  43       5.811  59.639  50.861  1.00  0.00           H  
ATOM    400  N   LYS A  44       4.438  58.978  47.831  1.00 24.60           N  
ATOM    401  CA  LYS A  44       4.222  58.658  46.419  1.00 22.39           C  
ATOM    402  C   LYS A  44       3.597  57.276  46.244  1.00 21.34           C  
ATOM    403  O   LYS A  44       3.282  56.865  45.128  1.00 28.07           O  
ATOM    404  CB  LYS A  44       5.543  58.712  45.645  1.00 21.88           C  
ATOM    405  CG  LYS A  44       6.362  59.971  45.862  1.00 20.35           C  
ATOM    406  CD  LYS A  44       5.729  61.173  45.199  1.00 21.77           C  
ATOM    407  CE  LYS A  44       6.430  62.451  45.625  1.00 25.28           C  
ATOM    408  NZ  LYS A  44       5.829  63.651  44.988  1.00 27.20           N  
ATOM    409  H   LYS A  44       5.266  58.679  48.262  1.00  0.00           H  
ATOM    410  HZ1 LYS A  44       5.876  63.571  43.952  1.00  0.00           H  
ATOM    411  HZ2 LYS A  44       4.837  63.736  45.287  1.00  0.00           H  
ATOM    412  HZ3 LYS A  44       6.353  64.497  45.293  1.00  0.00           H  
ATOM    413  N   GLY A  45       3.453  56.549  47.346  1.00 18.63           N  
ATOM    414  CA  GLY A  45       2.904  55.205  47.283  1.00 15.86           C  
ATOM    415  C   GLY A  45       3.966  54.123  47.306  1.00 19.11           C  
ATOM    416  O   GLY A  45       3.656  52.937  47.419  1.00 27.79           O  
ATOM    417  H   GLY A  45       3.702  56.939  48.209  1.00  0.00           H  
ATOM    418  N   PHE A  46       5.224  54.533  47.174  1.00 18.11           N  
ATOM    419  CA  PHE A  46       6.358  53.613  47.238  1.00 16.87           C  
ATOM    420  C   PHE A  46       7.536  54.298  47.946  1.00 20.24           C  
ATOM    421  O   PHE A  46       7.540  55.518  48.121  1.00 15.34           O  
ATOM    422  CB  PHE A  46       6.766  53.166  45.821  1.00  5.91           C  
ATOM    423  CG  PHE A  46       7.073  54.307  44.882  1.00  6.70           C  
ATOM    424  CD1 PHE A  46       8.337  54.881  44.853  1.00  8.71           C  
ATOM    425  CD2 PHE A  46       6.065  54.879  44.115  1.00  9.65           C  
ATOM    426  CE1 PHE A  46       8.589  56.017  44.092  1.00  6.91           C  
ATOM    427  CE2 PHE A  46       6.307  56.012  43.351  1.00 11.49           C  
ATOM    428  CZ  PHE A  46       7.574  56.586  43.344  1.00 12.49           C  
ATOM    429  H   PHE A  46       5.391  55.487  47.039  1.00  0.00           H  
ATOM    430  N   GLY A  47       8.516  53.513  48.381  1.00 18.60           N  
ATOM    431  CA  GLY A  47       9.685  54.095  49.014  1.00 16.57           C  
ATOM    432  C   GLY A  47      10.467  53.148  49.903  1.00 16.17           C  
ATOM    433  O   GLY A  47      10.313  51.926  49.822  1.00 16.48           O  
ATOM    434  H   GLY A  47       8.404  52.545  48.319  1.00  0.00           H  
ATOM    435  N   TYR A  48      11.246  53.722  50.815  1.00 17.24           N  
ATOM    436  CA  TYR A  48      12.247  52.967  51.569  1.00 18.02           C  
ATOM    437  C   TYR A  48      11.675  52.005  52.615  1.00 17.30           C  
ATOM    438  O   TYR A  48      12.313  51.013  52.958  1.00 19.70           O  
ATOM    439  CB  TYR A  48      13.230  53.925  52.251  1.00 10.64           C  
ATOM    440  CG  TYR A  48      14.033  54.794  51.306  1.00  2.00           C  
ATOM    441  CD1 TYR A  48      14.653  54.256  50.182  1.00  6.73           C  
ATOM    442  CD2 TYR A  48      14.197  56.151  51.558  1.00  4.20           C  
ATOM    443  CE1 TYR A  48      15.426  55.051  49.331  1.00  4.63           C  
ATOM    444  CE2 TYR A  48      14.957  56.956  50.710  1.00  4.69           C  
ATOM    445  CZ  TYR A  48      15.571  56.398  49.600  1.00  3.13           C  
ATOM    446  OH  TYR A  48      16.329  57.192  48.769  1.00  6.04           O  
ATOM    447  H   TYR A  48      11.101  54.673  51.003  1.00  0.00           H  
ATOM    448  HH  TYR A  48      16.878  56.634  48.207  1.00  0.00           H  
ATOM    449  N   LYS A  49      10.501  52.317  53.157  1.00 19.14           N  
ATOM    450  CA  LYS A  49       9.936  51.529  54.252  1.00 22.22           C  
ATOM    451  C   LYS A  49       9.758  50.056  53.902  1.00 18.35           C  
ATOM    452  O   LYS A  49       9.048  49.714  52.960  1.00 26.41           O  
ATOM    453  CB  LYS A  49       8.596  52.109  54.700  1.00 28.78           C  
ATOM    454  CG  LYS A  49       7.977  51.374  55.877  1.00 32.21           C  
ATOM    455  CD  LYS A  49       6.680  52.031  56.314  1.00 43.40           C  
ATOM    456  CE  LYS A  49       5.992  51.219  57.402  1.00 41.06           C  
ATOM    457  NZ  LYS A  49       4.822  51.944  57.966  1.00 42.60           N  
ATOM    458  H   LYS A  49      10.044  53.124  52.840  1.00  0.00           H  
ATOM    459  HZ1 LYS A  49       4.149  52.166  57.203  1.00  0.00           H  
ATOM    460  HZ2 LYS A  49       4.353  51.348  58.676  1.00  0.00           H  
ATOM    461  HZ3 LYS A  49       5.145  52.826  58.411  1.00  0.00           H  
ATOM    462  N   GLY A  50      10.424  49.192  54.662  1.00 16.02           N  
ATOM    463  CA  GLY A  50      10.391  47.765  54.390  1.00  7.63           C  
ATOM    464  C   GLY A  50      11.597  47.284  53.603  1.00 16.34           C  
ATOM    465  O   GLY A  50      11.869  46.088  53.544  1.00 21.18           O  
ATOM    466  H   GLY A  50      10.919  49.551  55.416  1.00  0.00           H  
ATOM    467  N   SER A  51      12.328  48.218  53.000  1.00 19.30           N  
ATOM    468  CA  SER A  51      13.504  47.878  52.200  1.00 24.54           C  
ATOM    469  C   SER A  51      14.701  47.524  53.083  1.00 24.48           C  
ATOM    470  O   SER A  51      14.708  47.815  54.274  1.00 24.47           O  
ATOM    471  CB  SER A  51      13.866  49.037  51.257  1.00 19.04           C  
ATOM    472  OG  SER A  51      14.498  50.106  51.943  1.00 16.12           O  
ATOM    473  H   SER A  51      12.032  49.143  53.100  1.00  0.00           H  
ATOM    474  HG  SER A  51      13.972  50.360  52.716  1.00  0.00           H  
ATOM    475  N   CYS A  52      15.692  46.854  52.505  1.00 27.48           N  
ATOM    476  CA  CYS A  52      16.841  46.378  53.272  1.00 19.92           C  
ATOM    477  C   CYS A  52      18.156  47.043  52.862  1.00 22.34           C  
ATOM    478  O   CYS A  52      18.248  47.660  51.796  1.00 23.33           O  
ATOM    479  CB  CYS A  52      16.972  44.863  53.126  1.00 17.34           C  
ATOM    480  SG  CYS A  52      17.560  44.317  51.500  1.00 40.02           S  
ATOM    481  H   CYS A  52      15.571  46.587  51.572  1.00  0.00           H  
ATOM    482  N   PHE A  53      19.141  46.992  53.752  1.00 21.25           N  
ATOM    483  CA  PHE A  53      20.519  47.322  53.408  1.00 18.33           C  
ATOM    484  C   PHE A  53      21.208  46.085  52.848  1.00 18.72           C  
ATOM    485  O   PHE A  53      21.513  45.145  53.582  1.00 17.34           O  
ATOM    486  CB  PHE A  53      21.270  47.837  54.642  1.00 16.35           C  
ATOM    487  CG  PHE A  53      20.963  49.267  54.979  1.00  8.67           C  
ATOM    488  CD1 PHE A  53      19.800  49.599  55.659  1.00  4.75           C  
ATOM    489  CD2 PHE A  53      21.796  50.290  54.545  1.00  7.25           C  
ATOM    490  CE1 PHE A  53      19.467  50.930  55.893  1.00  2.00           C  
ATOM    491  CE2 PHE A  53      21.472  51.625  54.776  1.00  5.26           C  
ATOM    492  CZ  PHE A  53      20.303  51.943  55.450  1.00  7.08           C  
ATOM    493  H   PHE A  53      18.935  46.782  54.678  1.00  0.00           H  
ATOM    494  N   HIS A  54      21.373  46.060  51.528  1.00 19.96           N  
ATOM    495  CA  HIS A  54      21.823  44.856  50.828  1.00 18.81           C  
ATOM    496  C   HIS A  54      23.347  44.757  50.720  1.00 20.68           C  
ATOM    497  O   HIS A  54      23.886  43.688  50.429  1.00 19.24           O  
ATOM    498  CB  HIS A  54      21.201  44.792  49.427  1.00 14.88           C  
ATOM    499  CG  HIS A  54      21.724  45.832  48.483  1.00 11.69           C  
ATOM    500  ND1 HIS A  54      21.279  47.137  48.494  1.00  8.88           N  
ATOM    501  CD2 HIS A  54      22.726  45.785  47.571  1.00  2.00           C  
ATOM    502  CE1 HIS A  54      21.996  47.853  47.647  1.00  9.87           C  
ATOM    503  NE2 HIS A  54      22.881  47.057  47.074  1.00  6.10           N  
ATOM    504  H   HIS A  54      21.185  46.905  51.075  1.00  0.00           H  
ATOM    505  HD1 HIS A  54      20.492  47.503  48.950  1.00  0.00           H  
ATOM    506  HE2 HIS A  54      23.538  47.344  46.400  1.00  0.00           H  
ATOM    507  N   ARG A  55      24.027  45.885  50.900  1.00 21.13           N  
ATOM    508  CA  ARG A  55      25.479  45.946  50.754  1.00 22.21           C  
ATOM    509  C   ARG A  55      26.101  46.786  51.873  1.00 22.52           C  
ATOM    510  O   ARG A  55      25.883  47.998  51.944  1.00 23.56           O  
ATOM    511  CB  ARG A  55      25.828  46.539  49.387  1.00 16.65           C  
ATOM    512  CG  ARG A  55      27.302  46.602  49.069  1.00 17.33           C  
ATOM    513  CD  ARG A  55      27.517  47.142  47.668  1.00 21.99           C  
ATOM    514  NE  ARG A  55      28.932  47.247  47.324  1.00 16.61           N  
ATOM    515  CZ  ARG A  55      29.570  48.395  47.117  1.00 29.45           C  
ATOM    516  NH1 ARG A  55      28.937  49.554  47.258  1.00 25.16           N  
ATOM    517  NH2 ARG A  55      30.853  48.386  46.785  1.00 38.47           N  
ATOM    518  H   ARG A  55      23.554  46.683  51.216  1.00  0.00           H  
ATOM    519  HE  ARG A  55      29.450  46.419  47.247  1.00  0.00           H  
ATOM    520 HH11 ARG A  55      27.975  49.566  47.527  1.00  0.00           H  
ATOM    521 HH12 ARG A  55      29.421  50.415  47.105  1.00  0.00           H  
ATOM    522 HH21 ARG A  55      31.329  47.511  46.704  1.00  0.00           H  
ATOM    523 HH22 ARG A  55      31.362  49.234  46.673  1.00  0.00           H  
ATOM    524  N   ILE A  56      26.748  46.115  52.820  1.00 24.85           N  
ATOM    525  CA  ILE A  56      27.410  46.790  53.940  1.00 25.75           C  
ATOM    526  C   ILE A  56      28.880  46.374  54.056  1.00 20.61           C  
ATOM    527  O   ILE A  56      29.188  45.204  54.298  1.00 15.40           O  
ATOM    528  CB  ILE A  56      26.700  46.485  55.282  1.00 19.31           C  
ATOM    529  CG1 ILE A  56      25.297  47.094  55.287  1.00 13.96           C  
ATOM    530  CG2 ILE A  56      27.513  47.040  56.443  1.00 19.39           C  
ATOM    531  CD1 ILE A  56      24.435  46.625  56.439  1.00 10.14           C  
ATOM    532  H   ILE A  56      26.755  45.140  52.767  1.00  0.00           H  
ATOM    533  N   ILE A  57      29.782  47.332  53.875  1.00 22.64           N  
ATOM    534  CA  ILE A  57      31.213  47.048  53.953  1.00 21.83           C  
ATOM    535  C   ILE A  57      31.865  47.767  55.139  1.00 22.52           C  
ATOM    536  O   ILE A  57      31.934  49.005  55.179  1.00 19.78           O  
ATOM    537  CB  ILE A  57      31.943  47.438  52.639  1.00 22.64           C  
ATOM    538  CG1 ILE A  57      31.328  46.685  51.452  1.00 23.75           C  
ATOM    539  CG2 ILE A  57      33.430  47.095  52.741  1.00 18.57           C  
ATOM    540  CD1 ILE A  57      31.876  47.097  50.101  1.00 15.13           C  
ATOM    541  H   ILE A  57      29.460  48.248  53.712  1.00  0.00           H  
ATOM    542  N   PRO A  58      32.281  46.997  56.159  1.00 21.37           N  
ATOM    543  CA  PRO A  58      32.909  47.533  57.373  1.00 22.65           C  
ATOM    544  C   PRO A  58      34.087  48.462  57.090  1.00 23.28           C  
ATOM    545  O   PRO A  58      34.987  48.125  56.326  1.00 28.16           O  
ATOM    546  CB  PRO A  58      33.337  46.281  58.127  1.00 19.29           C  
ATOM    547  CG  PRO A  58      32.326  45.257  57.713  1.00 13.92           C  
ATOM    548  CD  PRO A  58      32.070  45.541  56.257  1.00 17.00           C  
ATOM    549  N   GLY A  59      34.009  49.676  57.627  1.00 26.78           N  
ATOM    550  CA  GLY A  59      35.055  50.662  57.412  1.00 26.51           C  
ATOM    551  C   GLY A  59      34.853  51.509  56.168  1.00 28.21           C  
ATOM    552  O   GLY A  59      35.596  52.461  55.928  1.00 31.30           O  
ATOM    553  H   GLY A  59      33.249  49.885  58.192  1.00  0.00           H  
ATOM    554  N   PHE A  60      33.841  51.168  55.377  1.00 26.00           N  
ATOM    555  CA  PHE A  60      33.573  51.874  54.127  1.00 18.78           C  
ATOM    556  C   PHE A  60      32.219  52.594  54.181  1.00 18.07           C  
ATOM    557  O   PHE A  60      32.161  53.804  54.416  1.00 17.14           O  
ATOM    558  CB  PHE A  60      33.628  50.881  52.959  1.00 13.49           C  
ATOM    559  CG  PHE A  60      33.475  51.513  51.605  1.00 15.92           C  
ATOM    560  CD1 PHE A  60      33.885  52.827  51.375  1.00 19.07           C  
ATOM    561  CD2 PHE A  60      32.884  50.802  50.563  1.00 15.53           C  
ATOM    562  CE1 PHE A  60      33.702  53.424  50.127  1.00 17.32           C  
ATOM    563  CE2 PHE A  60      32.699  51.391  49.314  1.00  6.56           C  
ATOM    564  CZ  PHE A  60      33.107  52.702  49.097  1.00  7.11           C  
ATOM    565  H   PHE A  60      33.293  50.400  55.621  1.00  0.00           H  
ATOM    566  N   MET A  61      31.131  51.845  54.018  1.00 19.66           N  
ATOM    567  CA  MET A  61      29.792  52.435  54.046  1.00 12.71           C  
ATOM    568  C   MET A  61      28.676  51.405  54.172  1.00  9.99           C  
ATOM    569  O   MET A  61      28.903  50.200  54.012  1.00  9.10           O  
ATOM    570  CB  MET A  61      29.561  53.296  52.795  1.00 14.85           C  
ATOM    571  CG  MET A  61      29.796  52.576  51.466  1.00 20.97           C  
ATOM    572  SD  MET A  61      28.362  51.692  50.850  1.00 19.74           S  
ATOM    573  CE  MET A  61      28.986  50.013  50.729  1.00  2.00           C  
ATOM    574  H   MET A  61      31.231  50.874  53.939  1.00  0.00           H  
ATOM    575  N   CYS A  62      27.486  51.889  54.526  1.00 13.26           N  
ATOM    576  CA  CYS A  62      26.262  51.086  54.498  1.00 11.49           C  
ATOM    577  C   CYS A  62      25.373  51.532  53.333  1.00 15.82           C  
ATOM    578  O   CYS A  62      25.064  52.716  53.210  1.00 12.13           O  
ATOM    579  CB  CYS A  62      25.488  51.254  55.809  1.00 14.43           C  
ATOM    580  SG  CYS A  62      26.279  50.549  57.270  1.00 25.67           S  
ATOM    581  H   CYS A  62      27.455  52.820  54.824  1.00  0.00           H  
ATOM    582  N   GLN A  63      24.958  50.589  52.490  1.00 16.98           N  
ATOM    583  CA  GLN A  63      24.177  50.918  51.300  1.00 18.54           C  
ATOM    584  C   GLN A  63      22.772  50.305  51.274  1.00 21.08           C  
ATOM    585  O   GLN A  63      22.596  49.085  51.417  1.00 18.85           O  
ATOM    586  CB  GLN A  63      24.935  50.506  50.032  1.00 19.65           C  
ATOM    587  CG  GLN A  63      24.331  51.069  48.744  1.00 20.99           C  
ATOM    588  CD  GLN A  63      24.958  50.492  47.491  1.00 25.45           C  
ATOM    589  OE1 GLN A  63      26.154  50.240  47.439  1.00 25.47           O  
ATOM    590  NE2 GLN A  63      24.149  50.293  46.466  1.00 25.00           N  
ATOM    591  H   GLN A  63      25.232  49.662  52.649  1.00  0.00           H  
ATOM    592 HE21 GLN A  63      24.631  49.979  45.675  1.00  0.00           H  
ATOM    593 HE22 GLN A  63      23.200  50.512  46.502  1.00  0.00           H  
ATOM    594  N   GLY A  64      21.792  51.144  50.959  1.00 14.67           N  
ATOM    595  CA  GLY A  64      20.420  50.681  50.835  1.00 17.43           C  
ATOM    596  C   GLY A  64      19.654  51.462  49.783  1.00 13.32           C  
ATOM    597  O   GLY A  64      20.254  52.126  48.940  1.00  9.74           O  
ATOM    598  H   GLY A  64      22.026  52.082  50.772  1.00  0.00           H  
ATOM    599  N   GLY A  65      18.330  51.351  49.806  1.00 16.53           N  
ATOM    600  CA  GLY A  65      17.499  52.170  48.939  1.00 16.50           C  
ATOM    601  C   GLY A  65      16.934  51.466  47.718  1.00 18.94           C  
ATOM    602  O   GLY A  65      16.144  52.040  46.978  1.00 21.10           O  
ATOM    603  H   GLY A  65      17.941  50.771  50.485  1.00  0.00           H  
ATOM    604  N   ASP A  66      17.338  50.222  47.492  1.00 18.36           N  
ATOM    605  CA  ASP A  66      16.835  49.456  46.357  1.00 23.92           C  
ATOM    606  C   ASP A  66      15.535  48.735  46.721  1.00 25.17           C  
ATOM    607  O   ASP A  66      15.532  47.528  46.979  1.00 23.34           O  
ATOM    608  CB  ASP A  66      17.897  48.451  45.886  1.00 28.48           C  
ATOM    609  CG  ASP A  66      17.492  47.703  44.618  1.00 35.35           C  
ATOM    610  OD1 ASP A  66      16.410  47.973  44.055  1.00 38.58           O  
ATOM    611  OD2 ASP A  66      18.257  46.817  44.189  1.00 34.61           O  
ATOM    612  H   ASP A  66      18.016  49.864  48.099  1.00  0.00           H  
ATOM    613  N   PHE A  67      14.423  49.461  46.662  1.00 24.11           N  
ATOM    614  CA  PHE A  67      13.141  48.910  47.081  1.00 22.73           C  
ATOM    615  C   PHE A  67      12.429  48.071  46.014  1.00 26.09           C  
ATOM    616  O   PHE A  67      11.563  47.254  46.334  1.00 27.43           O  
ATOM    617  CB  PHE A  67      12.219  50.025  47.609  1.00 19.07           C  
ATOM    618  CG  PHE A  67      12.088  51.216  46.692  1.00 15.89           C  
ATOM    619  CD1 PHE A  67      11.113  51.243  45.699  1.00 18.52           C  
ATOM    620  CD2 PHE A  67      12.849  52.357  46.906  1.00 12.88           C  
ATOM    621  CE1 PHE A  67      10.896  52.390  44.941  1.00 14.25           C  
ATOM    622  CE2 PHE A  67      12.639  53.510  46.155  1.00  9.84           C  
ATOM    623  CZ  PHE A  67      11.659  53.528  45.172  1.00 18.30           C  
ATOM    624  H   PHE A  67      14.515  50.413  46.430  1.00  0.00           H  
ATOM    625  N   THR A  68      12.902  48.159  44.773  1.00 28.11           N  
ATOM    626  CA  THR A  68      12.336  47.351  43.692  1.00 23.90           C  
ATOM    627  C   THR A  68      13.044  45.996  43.511  1.00 28.59           C  
ATOM    628  O   THR A  68      12.485  44.957  43.858  1.00 29.45           O  
ATOM    629  CB  THR A  68      12.321  48.129  42.343  1.00 18.84           C  
ATOM    630  OG1 THR A  68      13.654  48.271  41.836  1.00 17.17           O  
ATOM    631  CG2 THR A  68      11.717  49.513  42.533  1.00 12.26           C  
ATOM    632  H   THR A  68      13.567  48.847  44.584  1.00  0.00           H  
ATOM    633  HG1 THR A  68      13.557  48.327  40.869  1.00  0.00           H  
ATOM    634  N   ARG A  69      14.309  46.018  43.096  1.00 30.66           N  
ATOM    635  CA  ARG A  69      15.068  44.785  42.854  1.00 34.03           C  
ATOM    636  C   ARG A  69      15.835  44.227  44.071  1.00 41.19           C  
ATOM    637  O   ARG A  69      16.304  43.090  44.044  1.00 45.06           O  
ATOM    638  CB  ARG A  69      16.040  44.988  41.687  1.00 27.97           C  
ATOM    639  CG  ARG A  69      15.371  45.231  40.344  0.00 30.13           C  
ATOM    640  CD  ARG A  69      15.652  44.093  39.379  0.00 28.13           C  
ATOM    641  NE  ARG A  69      16.336  44.546  38.170  0.00 28.40           N  
ATOM    642  CZ  ARG A  69      17.549  44.148  37.799  0.00 27.01           C  
ATOM    643  NH1 ARG A  69      18.243  43.311  38.560  0.00 27.23           N  
ATOM    644  NH2 ARG A  69      18.072  44.587  36.662  0.00 26.25           N  
ATOM    645  H   ARG A  69      14.664  46.881  42.813  1.00  0.00           H  
ATOM    646  HE  ARG A  69      15.869  45.180  37.587  1.00  0.00           H  
ATOM    647 HH11 ARG A  69      17.865  42.968  39.419  1.00  0.00           H  
ATOM    648 HH12 ARG A  69      19.149  43.009  38.261  1.00  0.00           H  
ATOM    649 HH21 ARG A  69      17.546  45.201  36.075  1.00  0.00           H  
ATOM    650 HH22 ARG A  69      18.977  44.271  36.375  1.00  0.00           H  
ATOM    651  N   HIS A  70      16.022  45.044  45.107  1.00 38.78           N  
ATOM    652  CA  HIS A  70      16.632  44.593  46.371  1.00 41.83           C  
ATOM    653  C   HIS A  70      18.110  44.149  46.333  1.00 40.66           C  
ATOM    654  O   HIS A  70      18.671  43.799  47.372  1.00 35.28           O  
ATOM    655  CB  HIS A  70      15.810  43.453  46.993  1.00 47.31           C  
ATOM    656  CG  HIS A  70      14.328  43.657  46.927  1.00 53.46           C  
ATOM    657  ND1 HIS A  70      13.658  44.545  47.742  1.00 56.69           N  
ATOM    658  CD2 HIS A  70      13.382  43.064  46.160  1.00 55.78           C  
ATOM    659  CE1 HIS A  70      12.365  44.492  47.479  1.00 59.18           C  
ATOM    660  NE2 HIS A  70      12.172  43.602  46.522  1.00 59.15           N  
ATOM    661  H   HIS A  70      15.662  45.948  45.033  1.00  0.00           H  
ATOM    662  HD1 HIS A  70      14.046  45.091  48.460  1.00  0.00           H  
ATOM    663  HE2 HIS A  70      11.336  43.482  46.023  1.00  0.00           H  
ATOM    664  N   ASN A  71      18.759  44.242  45.173  1.00 36.04           N  
ATOM    665  CA  ASN A  71      20.071  43.609  44.977  1.00 30.16           C  
ATOM    666  C   ASN A  71      21.188  44.522  44.450  1.00 22.03           C  
ATOM    667  O   ASN A  71      22.285  44.061  44.138  1.00 23.33           O  
ATOM    668  CB  ASN A  71      19.919  42.410  44.039  1.00 27.03           C  
ATOM    669  CG  ASN A  71      19.251  42.779  42.733  1.00 31.44           C  
ATOM    670  OD1 ASN A  71      19.316  43.927  42.290  1.00 30.49           O  
ATOM    671  ND2 ASN A  71      18.563  41.826  42.134  1.00 37.60           N  
ATOM    672  H   ASN A  71      18.272  44.576  44.398  1.00  0.00           H  
ATOM    673 HD21 ASN A  71      18.102  42.093  41.320  1.00  0.00           H  
ATOM    674 HD22 ASN A  71      18.521  40.944  42.549  1.00  0.00           H  
ATOM    675  N   GLY A  72      20.907  45.813  44.344  1.00 25.32           N  
ATOM    676  CA  GLY A  72      21.877  46.734  43.778  1.00 20.50           C  
ATOM    677  C   GLY A  72      21.550  47.153  42.356  1.00 27.86           C  
ATOM    678  O   GLY A  72      21.946  48.224  41.906  1.00 26.68           O  
ATOM    679  H   GLY A  72      20.078  46.122  44.737  1.00  0.00           H  
ATOM    680  N   THR A  73      20.751  46.345  41.674  1.00 34.96           N  
ATOM    681  CA  THR A  73      20.437  46.589  40.270  1.00 42.28           C  
ATOM    682  C   THR A  73      19.018  47.115  40.099  1.00 43.89           C  
ATOM    683  O   THR A  73      18.317  46.734  39.165  1.00 55.04           O  
ATOM    684  CB  THR A  73      20.584  45.303  39.432  1.00 41.95           C  
ATOM    685  OG1 THR A  73      21.209  44.281  40.221  1.00 54.24           O  
ATOM    686  CG2 THR A  73      21.430  45.566  38.200  1.00 47.99           C  
ATOM    687  H   THR A  73      20.395  45.548  42.113  1.00  0.00           H  
ATOM    688  HG1 THR A  73      20.555  43.978  40.861  1.00  0.00           H  
ATOM    689  N   GLY A  74      18.591  47.978  41.016  1.00 42.58           N  
ATOM    690  CA  GLY A  74      17.239  48.503  40.960  1.00 29.54           C  
ATOM    691  C   GLY A  74      17.040  49.831  41.666  1.00 25.40           C  
ATOM    692  O   GLY A  74      18.000  50.536  41.979  1.00 29.40           O  
ATOM    693  H   GLY A  74      19.246  48.344  41.639  1.00  0.00           H  
ATOM    694  N   GLY A  75      15.793  50.106  42.027  1.00 23.95           N  
ATOM    695  CA  GLY A  75      15.454  51.367  42.664  1.00 18.14           C  
ATOM    696  C   GLY A  75      14.960  52.392  41.663  1.00 14.14           C  
ATOM    697  O   GLY A  75      15.193  52.250  40.464  1.00 18.78           O  
ATOM    698  H   GLY A  75      15.095  49.476  41.785  1.00  0.00           H  
ATOM    699  N   LYS A  76      14.226  53.391  42.139  1.00  9.06           N  
ATOM    700  CA  LYS A  76      13.787  54.479  41.272  1.00 10.92           C  
ATOM    701  C   LYS A  76      13.444  55.736  42.053  1.00  9.09           C  
ATOM    702  O   LYS A  76      13.121  55.674  43.237  1.00 11.99           O  
ATOM    703  CB  LYS A  76      12.592  54.041  40.403  1.00 21.17           C  
ATOM    704  CG  LYS A  76      11.297  53.737  41.135  1.00 16.82           C  
ATOM    705  CD  LYS A  76      10.181  53.508  40.142  1.00 13.15           C  
ATOM    706  CE  LYS A  76       8.820  53.634  40.789  1.00 16.27           C  
ATOM    707  NZ  LYS A  76       8.527  52.453  41.645  1.00 31.22           N  
ATOM    708  H   LYS A  76      14.049  53.444  43.101  1.00  0.00           H  
ATOM    709  HZ1 LYS A  76       8.609  51.592  41.067  1.00  0.00           H  
ATOM    710  HZ2 LYS A  76       9.220  52.407  42.419  1.00  0.00           H  
ATOM    711  HZ3 LYS A  76       7.567  52.513  42.040  1.00  0.00           H  
ATOM    712  N   SER A  77      13.641  56.883  41.416  1.00  6.56           N  
ATOM    713  CA  SER A  77      13.415  58.167  42.063  1.00 11.76           C  
ATOM    714  C   SER A  77      11.942  58.573  42.081  1.00 19.58           C  
ATOM    715  O   SER A  77      11.073  57.840  41.599  1.00 25.58           O  
ATOM    716  CB  SER A  77      14.228  59.250  41.361  1.00  9.66           C  
ATOM    717  OG  SER A  77      13.678  59.556  40.096  1.00 11.64           O  
ATOM    718  H   SER A  77      13.928  56.845  40.481  1.00  0.00           H  
ATOM    719  HG  SER A  77      14.281  59.122  39.473  1.00  0.00           H  
ATOM    720  N   ILE A  78      11.667  59.760  42.610  1.00 17.32           N  
ATOM    721  CA  ILE A  78      10.319  60.316  42.574  1.00 19.79           C  
ATOM    722  C   ILE A  78      10.105  61.107  41.283  1.00 23.02           C  
ATOM    723  O   ILE A  78       9.055  61.708  41.071  1.00 24.51           O  
ATOM    724  CB  ILE A  78      10.052  61.235  43.795  1.00 12.34           C  
ATOM    725  CG1 ILE A  78      11.039  62.403  43.795  1.00  3.65           C  
ATOM    726  CG2 ILE A  78      10.161  60.435  45.087  1.00  4.97           C  
ATOM    727  CD1 ILE A  78      10.596  63.603  44.613  1.00  2.00           C  
ATOM    728  H   ILE A  78      12.373  60.231  43.081  1.00  0.00           H  
ATOM    729  N   TYR A  79      11.098  61.070  40.403  1.00 23.54           N  
ATOM    730  CA  TYR A  79      10.992  61.742  39.115  1.00 30.01           C  
ATOM    731  C   TYR A  79      10.703  60.750  37.981  1.00 32.67           C  
ATOM    732  O   TYR A  79      10.772  61.099  36.804  1.00 35.63           O  
ATOM    733  CB  TYR A  79      12.280  62.522  38.837  1.00 25.67           C  
ATOM    734  CG  TYR A  79      12.664  63.457  39.959  1.00 26.04           C  
ATOM    735  CD1 TYR A  79      11.896  64.584  40.242  1.00 26.31           C  
ATOM    736  CD2 TYR A  79      13.722  63.151  40.815  1.00 27.00           C  
ATOM    737  CE1 TYR A  79      12.160  65.373  41.355  1.00 23.66           C  
ATOM    738  CE2 TYR A  79      13.995  63.932  41.933  1.00 22.36           C  
ATOM    739  CZ  TYR A  79      13.206  65.037  42.202  1.00 28.80           C  
ATOM    740  OH  TYR A  79      13.425  65.777  43.341  1.00 26.46           O  
ATOM    741  H   TYR A  79      11.930  60.612  40.637  1.00  0.00           H  
ATOM    742  HH  TYR A  79      14.156  65.380  43.823  1.00  0.00           H  
ATOM    743  N   GLY A  80      10.406  59.505  38.344  0.00 33.13           N  
ATOM    744  CA  GLY A  80      10.077  58.500  37.348  0.00 34.10           C  
ATOM    745  C   GLY A  80      11.131  57.419  37.185  0.00 34.90           C  
ATOM    746  O   GLY A  80      10.812  56.230  37.185  0.00 34.69           O  
ATOM    747  H   GLY A  80      10.379  59.286  39.298  1.00  0.00           H  
ATOM    748  N   GLU A  81      12.385  57.829  37.022  0.00 35.98           N  
ATOM    749  CA  GLU A  81      13.486  56.879  36.870  0.00 37.07           C  
ATOM    750  C   GLU A  81      14.814  57.410  37.426  0.00 36.31           C  
ATOM    751  O   GLU A  81      14.970  57.532  38.642  0.00 36.67           O  
ATOM    752  CB  GLU A  81      13.636  56.480  35.397  0.00 39.07           C  
ATOM    753  CG  GLU A  81      14.101  55.044  35.184  0.00 40.42           C  
ATOM    754  CD  GLU A  81      13.145  54.022  35.775  0.00 41.88           C  
ATOM    755  OE1 GLU A  81      12.035  53.854  35.227  0.00 43.89           O  
ATOM    756  OE2 GLU A  81      13.506  53.384  36.786  0.00 39.55           O  
ATOM    757  H   GLU A  81      12.529  58.796  37.001  1.00  0.00           H  
ATOM    758  N   LYS A  82      15.743  57.778  36.546  1.00 36.19           N  
ATOM    759  CA  LYS A  82      17.083  58.183  36.972  1.00 31.71           C  
ATOM    760  C   LYS A  82      17.386  59.636  36.636  1.00 25.85           C  
ATOM    761  O   LYS A  82      17.154  60.078  35.516  1.00 32.51           O  
ATOM    762  CB  LYS A  82      18.143  57.271  36.351  1.00 29.06           C  
ATOM    763  CG  LYS A  82      18.579  56.135  37.270  1.00 39.41           C  
ATOM    764  CD  LYS A  82      18.178  54.774  36.728  1.00 42.37           C  
ATOM    765  CE  LYS A  82      18.071  53.741  37.843  1.00 43.96           C  
ATOM    766  NZ  LYS A  82      16.859  53.964  38.680  1.00 51.94           N  
ATOM    767  H   LYS A  82      15.548  57.863  35.593  1.00  0.00           H  
ATOM    768  HZ1 LYS A  82      16.022  53.935  38.062  1.00  0.00           H  
ATOM    769  HZ2 LYS A  82      16.779  53.217  39.399  1.00  0.00           H  
ATOM    770  HZ3 LYS A  82      16.910  54.894  39.142  1.00  0.00           H  
ATOM    771  N   PHE A  83      17.804  60.400  37.641  1.00 16.83           N  
ATOM    772  CA  PHE A  83      18.033  61.824  37.459  1.00  7.69           C  
ATOM    773  C   PHE A  83      19.492  62.231  37.624  1.00  7.58           C  
ATOM    774  O   PHE A  83      20.335  61.438  38.044  1.00 15.13           O  
ATOM    775  CB  PHE A  83      17.126  62.646  38.390  1.00 13.05           C  
ATOM    776  CG  PHE A  83      17.408  62.461  39.854  1.00 16.16           C  
ATOM    777  CD1 PHE A  83      17.072  61.272  40.501  1.00 15.54           C  
ATOM    778  CD2 PHE A  83      17.935  63.509  40.609  1.00 14.28           C  
ATOM    779  CE1 PHE A  83      17.254  61.126  41.882  1.00  9.88           C  
ATOM    780  CE2 PHE A  83      18.118  63.375  41.988  1.00  9.45           C  
ATOM    781  CZ  PHE A  83      17.777  62.181  42.624  1.00  6.86           C  
ATOM    782  H   PHE A  83      17.955  59.978  38.505  1.00  0.00           H  
ATOM    783  N   GLU A  84      19.787  63.465  37.245  1.00 10.96           N  
ATOM    784  CA  GLU A  84      21.161  63.913  37.052  1.00 22.02           C  
ATOM    785  C   GLU A  84      21.925  64.156  38.355  1.00 20.36           C  
ATOM    786  O   GLU A  84      21.327  64.310  39.424  1.00 23.53           O  
ATOM    787  CB  GLU A  84      21.177  65.184  36.189  1.00 22.57           C  
ATOM    788  CG  GLU A  84      20.843  66.484  36.926  1.00 39.29           C  
ATOM    789  CD  GLU A  84      19.353  66.691  37.178  1.00 44.42           C  
ATOM    790  OE1 GLU A  84      18.518  66.065  36.487  1.00 44.00           O  
ATOM    791  OE2 GLU A  84      19.019  67.519  38.054  1.00 49.98           O  
ATOM    792  H   GLU A  84      19.042  64.071  37.082  1.00  0.00           H  
ATOM    793  N   ASP A  85      23.250  64.138  38.271  1.00 13.77           N  
ATOM    794  CA  ASP A  85      24.073  64.552  39.397  1.00 13.10           C  
ATOM    795  C   ASP A  85      23.907  66.049  39.575  1.00 12.15           C  
ATOM    796  O   ASP A  85      24.361  66.827  38.742  1.00 21.19           O  
ATOM    797  CB  ASP A  85      25.544  64.214  39.148  1.00  9.05           C  
ATOM    798  CG  ASP A  85      25.805  62.723  39.129  1.00 10.65           C  
ATOM    799  OD1 ASP A  85      25.182  61.992  39.920  1.00 18.75           O  
ATOM    800  OD2 ASP A  85      26.656  62.281  38.337  1.00 15.59           O  
ATOM    801  H   ASP A  85      23.661  63.992  37.395  1.00  0.00           H  
ATOM    802  N   GLU A  86      23.194  66.440  40.626  1.00 14.42           N  
ATOM    803  CA  GLU A  86      22.800  67.836  40.825  1.00 13.19           C  
ATOM    804  C   GLU A  86      23.989  68.787  40.956  1.00 14.58           C  
ATOM    805  O   GLU A  86      24.006  69.870  40.365  1.00 22.50           O  
ATOM    806  CB  GLU A  86      21.907  67.943  42.058  1.00 11.57           C  
ATOM    807  CG  GLU A  86      21.332  69.328  42.295  1.00 10.01           C  
ATOM    808  CD  GLU A  86      20.168  69.314  43.261  1.00 14.81           C  
ATOM    809  OE1 GLU A  86      19.944  68.271  43.911  1.00 10.67           O  
ATOM    810  OE2 GLU A  86      19.458  70.338  43.356  1.00 17.61           O  
ATOM    811  H   GLU A  86      22.925  65.747  41.267  1.00  0.00           H  
ATOM    812  N   ASN A  87      24.933  68.412  41.812  1.00 14.69           N  
ATOM    813  CA  ASN A  87      26.228  69.076  41.909  1.00 13.10           C  
ATOM    814  C   ASN A  87      27.109  68.275  42.854  1.00 18.22           C  
ATOM    815  O   ASN A  87      26.632  67.368  43.542  1.00 13.44           O  
ATOM    816  CB  ASN A  87      26.083  70.513  42.427  1.00 12.99           C  
ATOM    817  CG  ASN A  87      25.514  70.579  43.835  1.00 18.94           C  
ATOM    818  OD1 ASN A  87      26.059  69.981  44.761  1.00 14.71           O  
ATOM    819  ND2 ASN A  87      24.420  71.317  44.005  1.00  9.47           N  
ATOM    820  H   ASN A  87      24.765  67.621  42.365  1.00  0.00           H  
ATOM    821 HD21 ASN A  87      23.494  70.950  44.008  1.00  0.00           H  
ATOM    822 HD22 ASN A  87      24.546  72.291  44.093  1.00  0.00           H  
ATOM    823  N   PHE A  88      28.389  68.626  42.902  1.00 19.86           N  
ATOM    824  CA  PHE A  88      29.325  67.982  43.814  1.00 20.14           C  
ATOM    825  C   PHE A  88      29.974  69.005  44.739  1.00 17.10           C  
ATOM    826  O   PHE A  88      31.158  68.914  45.052  1.00 20.63           O  
ATOM    827  CB  PHE A  88      30.392  67.228  43.024  1.00 15.00           C  
ATOM    828  CG  PHE A  88      29.835  66.160  42.130  1.00 14.71           C  
ATOM    829  CD1 PHE A  88      29.365  64.966  42.663  1.00  8.08           C  
ATOM    830  CD2 PHE A  88      29.797  66.339  40.751  1.00 14.17           C  
ATOM    831  CE1 PHE A  88      28.873  63.966  41.835  1.00 12.03           C  
ATOM    832  CE2 PHE A  88      29.306  65.344  39.917  1.00  2.86           C  
ATOM    833  CZ  PHE A  88      28.846  64.156  40.460  1.00 11.56           C  
ATOM    834  H   PHE A  88      28.701  69.307  42.275  1.00  0.00           H  
ATOM    835  N   ILE A  89      29.170  69.956  45.204  1.00 15.79           N  
ATOM    836  CA  ILE A  89      29.649  71.012  46.086  1.00 19.48           C  
ATOM    837  C   ILE A  89      30.094  70.462  47.440  1.00 19.02           C  
ATOM    838  O   ILE A  89      31.133  70.864  47.961  1.00 25.19           O  
ATOM    839  CB  ILE A  89      28.562  72.095  46.282  1.00 18.59           C  
ATOM    840  CG1 ILE A  89      28.341  72.837  44.957  1.00 20.99           C  
ATOM    841  CG2 ILE A  89      28.963  73.071  47.377  1.00 11.87           C  
ATOM    842  CD1 ILE A  89      27.152  73.778  44.952  1.00 17.02           C  
ATOM    843  H   ILE A  89      28.212  69.890  44.992  1.00  0.00           H  
ATOM    844  N   LEU A  90      29.366  69.472  47.949  1.00 19.56           N  
ATOM    845  CA  LEU A  90      29.672  68.875  49.249  1.00 16.20           C  
ATOM    846  C   LEU A  90      30.518  67.610  49.142  1.00 17.93           C  
ATOM    847  O   LEU A  90      30.380  66.823  48.204  1.00 18.31           O  
ATOM    848  CB  LEU A  90      28.385  68.571  50.021  1.00 12.16           C  
ATOM    849  CG  LEU A  90      27.402  69.728  50.231  1.00 14.75           C  
ATOM    850  CD1 LEU A  90      26.157  69.210  50.927  1.00  8.81           C  
ATOM    851  CD2 LEU A  90      28.048  70.835  51.044  1.00  7.66           C  
ATOM    852  H   LEU A  90      28.590  69.143  47.445  1.00  0.00           H  
ATOM    853  N   LYS A  91      31.373  67.404  50.138  1.00 20.17           N  
ATOM    854  CA  LYS A  91      32.357  66.334  50.097  1.00 12.13           C  
ATOM    855  C   LYS A  91      32.084  65.220  51.107  1.00 15.28           C  
ATOM    856  O   LYS A  91      31.314  65.383  52.057  1.00 10.52           O  
ATOM    857  CB  LYS A  91      33.754  66.911  50.326  1.00 18.41           C  
ATOM    858  CG  LYS A  91      34.140  68.015  49.347  1.00 18.43           C  
ATOM    859  CD  LYS A  91      35.467  68.654  49.725  1.00 33.96           C  
ATOM    860  CE  LYS A  91      35.408  69.270  51.115  1.00 47.69           C  
ATOM    861  NZ  LYS A  91      36.689  69.928  51.493  1.00 54.15           N  
ATOM    862  H   LYS A  91      31.315  68.000  50.911  1.00  0.00           H  
ATOM    863  HZ1 LYS A  91      37.466  69.239  51.447  1.00  0.00           H  
ATOM    864  HZ2 LYS A  91      36.879  70.712  50.837  1.00  0.00           H  
ATOM    865  HZ3 LYS A  91      36.613  70.301  52.462  1.00  0.00           H  
ATOM    866  N   HIS A  92      32.640  64.052  50.823  1.00 11.46           N  
ATOM    867  CA  HIS A  92      32.615  62.928  51.753  1.00 16.27           C  
ATOM    868  C   HIS A  92      33.671  63.132  52.845  1.00 21.83           C  
ATOM    869  O   HIS A  92      34.801  62.647  52.728  1.00 22.02           O  
ATOM    870  CB  HIS A  92      32.900  61.624  51.002  1.00 15.67           C  
ATOM    871  CG  HIS A  92      31.858  61.268  49.990  1.00 18.76           C  
ATOM    872  ND1 HIS A  92      31.673  61.981  48.823  1.00 13.86           N  
ATOM    873  CD2 HIS A  92      30.948  60.266  49.965  1.00 17.84           C  
ATOM    874  CE1 HIS A  92      30.696  61.433  48.124  1.00 14.72           C  
ATOM    875  NE2 HIS A  92      30.239  60.392  48.795  1.00 23.16           N  
ATOM    876  H   HIS A  92      33.127  64.016  49.992  1.00  0.00           H  
ATOM    877  HD1 HIS A  92      32.129  62.774  48.478  1.00  0.00           H  
ATOM    878  HE2 HIS A  92      29.419  59.907  48.561  1.00  0.00           H  
ATOM    879  N   THR A  93      33.306  63.883  53.881  1.00 25.07           N  
ATOM    880  CA  THR A  93      34.270  64.360  54.878  1.00 26.70           C  
ATOM    881  C   THR A  93      34.472  63.453  56.099  1.00 26.60           C  
ATOM    882  O   THR A  93      35.340  63.713  56.931  1.00 31.75           O  
ATOM    883  CB  THR A  93      33.877  65.744  55.401  1.00 23.33           C  
ATOM    884  OG1 THR A  93      32.594  65.659  56.033  1.00 21.34           O  
ATOM    885  CG2 THR A  93      33.819  66.750  54.260  1.00 20.16           C  
ATOM    886  H   THR A  93      32.370  64.173  53.959  1.00  0.00           H  
ATOM    887  HG1 THR A  93      32.342  66.533  56.354  1.00  0.00           H  
ATOM    888  N   GLY A  94      33.659  62.409  56.220  1.00 23.60           N  
ATOM    889  CA  GLY A  94      33.772  61.519  57.361  1.00 20.31           C  
ATOM    890  C   GLY A  94      32.579  60.598  57.542  1.00 17.39           C  
ATOM    891  O   GLY A  94      31.738  60.506  56.654  1.00 17.66           O  
ATOM    892  H   GLY A  94      32.955  62.295  55.556  1.00  0.00           H  
ATOM    893  N   PRO A  95      32.509  59.853  58.656  1.00 21.21           N  
ATOM    894  CA  PRO A  95      31.343  59.021  58.964  1.00 20.11           C  
ATOM    895  C   PRO A  95      30.055  59.836  59.085  1.00 24.71           C  
ATOM    896  O   PRO A  95      30.078  60.999  59.492  1.00 24.52           O  
ATOM    897  CB  PRO A  95      31.713  58.358  60.292  1.00 18.60           C  
ATOM    898  CG  PRO A  95      33.204  58.436  60.353  1.00 23.80           C  
ATOM    899  CD  PRO A  95      33.549  59.731  59.693  1.00 19.64           C  
ATOM    900  N   GLY A  96      28.941  59.230  58.688  1.00 22.61           N  
ATOM    901  CA  GLY A  96      27.656  59.891  58.811  1.00 23.25           C  
ATOM    902  C   GLY A  96      27.200  60.571  57.536  1.00 20.23           C  
ATOM    903  O   GLY A  96      26.023  60.913  57.397  1.00 21.94           O  
ATOM    904  H   GLY A  96      28.978  58.306  58.385  1.00  0.00           H  
ATOM    905  N   ILE A  97      28.136  60.797  56.620  1.00 15.44           N  
ATOM    906  CA  ILE A  97      27.822  61.389  55.321  1.00 17.32           C  
ATOM    907  C   ILE A  97      26.844  60.518  54.519  1.00 13.75           C  
ATOM    908  O   ILE A  97      27.070  59.324  54.328  1.00 16.38           O  
ATOM    909  CB  ILE A  97      29.118  61.628  54.492  1.00 13.89           C  
ATOM    910  CG1 ILE A  97      29.960  62.733  55.140  1.00 11.15           C  
ATOM    911  CG2 ILE A  97      28.781  61.996  53.054  1.00 17.20           C  
ATOM    912  CD1 ILE A  97      29.318  64.107  55.140  1.00  2.17           C  
ATOM    913  H   ILE A  97      29.063  60.594  56.846  1.00  0.00           H  
ATOM    914  N   LEU A  98      25.720  61.111  54.134  1.00 15.59           N  
ATOM    915  CA  LEU A  98      24.715  60.439  53.312  1.00 16.18           C  
ATOM    916  C   LEU A  98      24.873  60.860  51.844  1.00 17.40           C  
ATOM    917  O   LEU A  98      24.827  62.053  51.514  1.00 13.61           O  
ATOM    918  CB  LEU A  98      23.316  60.797  53.821  1.00 11.28           C  
ATOM    919  CG  LEU A  98      22.070  60.128  53.234  1.00  9.20           C  
ATOM    920  CD1 LEU A  98      22.073  58.637  53.516  1.00  7.41           C  
ATOM    921  CD2 LEU A  98      20.837  60.775  53.844  1.00  6.13           C  
ATOM    922  H   LEU A  98      25.581  62.043  54.412  1.00  0.00           H  
ATOM    923  N   SER A  99      25.077  59.880  50.969  1.00 18.46           N  
ATOM    924  CA  SER A  99      25.414  60.155  49.571  1.00 16.25           C  
ATOM    925  C   SER A  99      24.674  59.235  48.596  1.00 13.05           C  
ATOM    926  O   SER A  99      24.259  58.134  48.963  1.00 14.14           O  
ATOM    927  CB  SER A  99      26.928  60.016  49.376  1.00 16.05           C  
ATOM    928  OG  SER A  99      27.359  60.522  48.126  1.00 21.30           O  
ATOM    929  H   SER A  99      24.994  58.955  51.293  1.00  0.00           H  
ATOM    930  HG  SER A  99      26.816  61.309  47.946  1.00  0.00           H  
ATOM    931  N   MET A 100      24.499  59.692  47.358  1.00 11.09           N  
ATOM    932  CA  MET A 100      23.808  58.900  46.334  1.00 14.24           C  
ATOM    933  C   MET A 100      24.665  57.772  45.744  1.00 13.34           C  
ATOM    934  O   MET A 100      25.747  58.008  45.195  1.00 16.78           O  
ATOM    935  CB  MET A 100      23.300  59.805  45.197  1.00 13.78           C  
ATOM    936  CG  MET A 100      22.044  60.613  45.524  1.00  8.51           C  
ATOM    937  SD  MET A 100      20.692  59.608  46.192  1.00 18.96           S  
ATOM    938  CE  MET A 100      19.986  58.920  44.720  1.00 19.73           C  
ATOM    939  H   MET A 100      24.815  60.584  47.137  1.00  0.00           H  
ATOM    940  N   ALA A 101      24.160  56.546  45.839  1.00 15.61           N  
ATOM    941  CA  ALA A 101      24.814  55.392  45.233  1.00 18.10           C  
ATOM    942  C   ALA A 101      24.336  55.230  43.798  1.00 27.83           C  
ATOM    943  O   ALA A 101      23.257  54.697  43.553  1.00 43.89           O  
ATOM    944  CB  ALA A 101      24.504  54.133  46.025  1.00 10.95           C  
ATOM    945  H   ALA A 101      23.299  56.448  46.302  1.00  0.00           H  
ATOM    946  N   ASN A 102      25.106  55.754  42.857  1.00 27.61           N  
ATOM    947  CA  ASN A 102      24.760  55.648  41.446  1.00 27.34           C  
ATOM    948  C   ASN A 102      25.451  54.465  40.759  1.00 32.37           C  
ATOM    949  O   ASN A 102      26.159  53.682  41.403  1.00 29.84           O  
ATOM    950  CB  ASN A 102      25.111  56.951  40.726  1.00 27.66           C  
ATOM    951  CG  ASN A 102      26.563  57.341  40.902  1.00 18.68           C  
ATOM    952  OD1 ASN A 102      27.465  56.564  40.609  1.00 18.29           O  
ATOM    953  ND2 ASN A 102      26.793  58.523  41.443  1.00 13.87           N  
ATOM    954  H   ASN A 102      25.904  56.235  43.132  1.00  0.00           H  
ATOM    955 HD21 ASN A 102      27.726  58.809  41.421  1.00  0.00           H  
ATOM    956 HD22 ASN A 102      26.049  59.063  41.774  1.00  0.00           H  
ATOM    957  N   ALA A 103      25.159  54.291  39.474  1.00 30.77           N  
ATOM    958  CA  ALA A 103      25.869  53.331  38.638  1.00 28.93           C  
ATOM    959  C   ALA A 103      26.575  54.058  37.488  1.00 29.00           C  
ATOM    960  O   ALA A 103      26.663  53.548  36.371  1.00 33.33           O  
ATOM    961  CB  ALA A 103      24.891  52.294  38.096  1.00 24.45           C  
ATOM    962  H   ALA A 103      24.432  54.820  39.083  1.00  0.00           H  
ATOM    963  N   GLY A 104      27.072  55.258  37.776  1.00 24.77           N  
ATOM    964  CA  GLY A 104      27.696  56.081  36.756  1.00 16.35           C  
ATOM    965  C   GLY A 104      27.224  57.519  36.827  1.00 21.35           C  
ATOM    966  O   GLY A 104      26.335  57.835  37.621  1.00 15.93           O  
ATOM    967  H   GLY A 104      27.023  55.574  38.703  1.00  0.00           H  
ATOM    968  N   PRO A 105      27.790  58.420  36.008  1.00 24.55           N  
ATOM    969  CA  PRO A 105      27.292  59.799  35.915  1.00 26.58           C  
ATOM    970  C   PRO A 105      25.817  59.888  35.534  1.00 25.57           C  
ATOM    971  O   PRO A 105      25.361  59.202  34.621  1.00 23.84           O  
ATOM    972  CB  PRO A 105      28.191  60.432  34.855  1.00 24.26           C  
ATOM    973  CG  PRO A 105      29.475  59.680  34.989  1.00 26.98           C  
ATOM    974  CD  PRO A 105      29.057  58.253  35.274  1.00 27.42           C  
ATOM    975  N   ASN A 106      25.068  60.660  36.316  1.00 23.70           N  
ATOM    976  CA  ASN A 106      23.657  60.926  36.057  1.00 21.21           C  
ATOM    977  C   ASN A 106      22.793  59.666  36.046  1.00 21.36           C  
ATOM    978  O   ASN A 106      21.945  59.497  35.174  1.00 25.34           O  
ATOM    979  CB  ASN A 106      23.509  61.689  34.739  1.00 26.69           C  
ATOM    980  CG  ASN A 106      24.291  62.987  34.733  1.00 27.78           C  
ATOM    981  OD1 ASN A 106      24.525  63.585  35.780  1.00 26.87           O  
ATOM    982  ND2 ASN A 106      24.687  63.436  33.557  1.00 33.17           N  
ATOM    983  H   ASN A 106      25.492  61.039  37.102  1.00  0.00           H  
ATOM    984 HD21 ASN A 106      25.182  64.273  33.565  1.00  0.00           H  
ATOM    985 HD22 ASN A 106      24.430  62.934  32.768  1.00  0.00           H  
ATOM    986  N   THR A 107      23.021  58.781  37.016  1.00 23.66           N  
ATOM    987  CA  THR A 107      22.198  57.578  37.184  1.00 21.85           C  
ATOM    988  C   THR A 107      21.563  57.492  38.570  1.00 17.07           C  
ATOM    989  O   THR A 107      21.432  56.407  39.139  1.00 20.61           O  
ATOM    990  CB  THR A 107      23.012  56.281  36.951  1.00 23.80           C  
ATOM    991  OG1 THR A 107      24.152  56.261  37.821  1.00 27.91           O  
ATOM    992  CG2 THR A 107      23.467  56.187  35.506  1.00 17.33           C  
ATOM    993  H   THR A 107      23.809  58.928  37.573  1.00  0.00           H  
ATOM    994  HG1 THR A 107      24.674  57.065  37.688  1.00  0.00           H  
ATOM    995  N   ASN A 108      21.103  58.627  39.082  1.00 19.46           N  
ATOM    996  CA  ASN A 108      20.519  58.669  40.421  1.00 19.08           C  
ATOM    997  C   ASN A 108      19.084  58.143  40.446  1.00 16.30           C  
ATOM    998  O   ASN A 108      18.215  58.659  39.750  1.00 15.42           O  
ATOM    999  CB  ASN A 108      20.549  60.094  40.970  1.00 10.28           C  
ATOM   1000  CG  ASN A 108      21.952  60.627  41.128  1.00 14.83           C  
ATOM   1001  OD1 ASN A 108      22.821  59.974  41.699  1.00 20.13           O  
ATOM   1002  ND2 ASN A 108      22.183  61.822  40.620  1.00 15.82           N  
ATOM   1003  H   ASN A 108      21.093  59.424  38.512  1.00  0.00           H  
ATOM   1004 HD21 ASN A 108      23.056  62.215  40.769  1.00  0.00           H  
ATOM   1005 HD22 ASN A 108      21.439  62.265  40.162  1.00  0.00           H  
ATOM   1006  N   GLY A 109      18.850  57.101  41.234  1.00 14.38           N  
ATOM   1007  CA  GLY A 109      17.499  56.605  41.425  1.00  8.68           C  
ATOM   1008  C   GLY A 109      17.055  56.754  42.865  1.00  8.81           C  
ATOM   1009  O   GLY A 109      16.697  57.847  43.305  1.00 11.81           O  
ATOM   1010  H   GLY A 109      19.608  56.671  41.691  1.00  0.00           H  
ATOM   1011  N   SER A 110      17.195  55.677  43.628  1.00 14.16           N  
ATOM   1012  CA  SER A 110      16.812  55.672  45.041  1.00 14.32           C  
ATOM   1013  C   SER A 110      17.911  55.166  45.991  1.00 16.74           C  
ATOM   1014  O   SER A 110      17.826  55.364  47.207  1.00 10.52           O  
ATOM   1015  CB  SER A 110      15.567  54.818  45.236  1.00  4.27           C  
ATOM   1016  OG  SER A 110      15.786  53.506  44.748  1.00  7.69           O  
ATOM   1017  H   SER A 110      17.559  54.873  43.199  1.00  0.00           H  
ATOM   1018  HG  SER A 110      16.097  52.989  45.489  1.00  0.00           H  
ATOM   1019  N   GLN A 111      18.915  54.485  45.446  1.00 12.76           N  
ATOM   1020  CA  GLN A 111      19.971  53.903  46.269  1.00 10.89           C  
ATOM   1021  C   GLN A 111      20.934  54.937  46.841  1.00 12.70           C  
ATOM   1022  O   GLN A 111      21.340  55.886  46.163  1.00 12.52           O  
ATOM   1023  CB  GLN A 111      20.747  52.842  45.483  1.00 11.21           C  
ATOM   1024  CG  GLN A 111      20.005  51.527  45.368  1.00 12.66           C  
ATOM   1025  CD  GLN A 111      20.797  50.462  44.656  1.00 14.91           C  
ATOM   1026  OE1 GLN A 111      21.417  49.614  45.292  1.00 23.72           O  
ATOM   1027  NE2 GLN A 111      20.675  50.415  43.344  1.00 15.67           N  
ATOM   1028  H   GLN A 111      18.953  54.388  44.467  1.00  0.00           H  
ATOM   1029 HE21 GLN A 111      21.246  49.770  42.882  1.00  0.00           H  
ATOM   1030 HE22 GLN A 111      20.016  50.989  42.900  1.00  0.00           H  
ATOM   1031  N   PHE A 112      21.293  54.741  48.103  1.00 14.59           N  
ATOM   1032  CA  PHE A 112      22.119  55.693  48.840  1.00 13.39           C  
ATOM   1033  C   PHE A 112      23.111  54.913  49.696  1.00  9.54           C  
ATOM   1034  O   PHE A 112      22.917  53.719  49.949  1.00 14.16           O  
ATOM   1035  CB  PHE A 112      21.237  56.571  49.741  1.00 10.66           C  
ATOM   1036  CG  PHE A 112      20.441  55.790  50.760  1.00 14.14           C  
ATOM   1037  CD1 PHE A 112      20.993  55.460  51.993  1.00 15.52           C  
ATOM   1038  CD2 PHE A 112      19.179  55.294  50.445  1.00 19.79           C  
ATOM   1039  CE1 PHE A 112      20.312  54.639  52.889  1.00 18.15           C  
ATOM   1040  CE2 PHE A 112      18.488  54.471  51.339  1.00 16.49           C  
ATOM   1041  CZ  PHE A 112      19.060  54.142  52.560  1.00 14.33           C  
ATOM   1042  H   PHE A 112      20.988  53.919  48.545  1.00  0.00           H  
ATOM   1043  N   PHE A 113      24.132  55.601  50.193  1.00 11.81           N  
ATOM   1044  CA  PHE A 113      24.993  55.028  51.219  1.00  8.83           C  
ATOM   1045  C   PHE A 113      25.341  56.017  52.331  1.00 11.95           C  
ATOM   1046  O   PHE A 113      25.300  57.242  52.134  1.00  9.79           O  
ATOM   1047  CB  PHE A 113      26.271  54.458  50.594  1.00 10.69           C  
ATOM   1048  CG  PHE A 113      27.149  55.490  49.958  1.00 14.18           C  
ATOM   1049  CD1 PHE A 113      26.902  55.927  48.662  1.00 16.94           C  
ATOM   1050  CD2 PHE A 113      28.247  56.001  50.639  1.00  9.72           C  
ATOM   1051  CE1 PHE A 113      27.738  56.854  48.053  1.00 15.48           C  
ATOM   1052  CE2 PHE A 113      29.085  56.923  50.040  1.00 10.11           C  
ATOM   1053  CZ  PHE A 113      28.832  57.350  48.744  1.00 16.84           C  
ATOM   1054  H   PHE A 113      24.279  56.517  49.892  1.00  0.00           H  
ATOM   1055  N   ILE A 114      25.507  55.477  53.535  1.00 14.93           N  
ATOM   1056  CA  ILE A 114      26.016  56.239  54.678  1.00 16.46           C  
ATOM   1057  C   ILE A 114      27.472  55.841  54.925  1.00 12.39           C  
ATOM   1058  O   ILE A 114      27.774  54.663  55.134  1.00 10.63           O  
ATOM   1059  CB  ILE A 114      25.212  55.951  55.978  1.00 13.29           C  
ATOM   1060  CG1 ILE A 114      23.719  55.818  55.671  1.00 11.93           C  
ATOM   1061  CG2 ILE A 114      25.417  57.078  56.978  1.00 11.92           C  
ATOM   1062  CD1 ILE A 114      23.000  54.854  56.587  1.00 14.28           C  
ATOM   1063  H   ILE A 114      25.276  54.534  53.639  1.00  0.00           H  
ATOM   1064  N   CYS A 115      28.376  56.806  54.804  1.00 12.24           N  
ATOM   1065  CA  CYS A 115      29.797  56.565  55.043  1.00 16.59           C  
ATOM   1066  C   CYS A 115      30.080  56.236  56.504  1.00 16.51           C  
ATOM   1067  O   CYS A 115      29.579  56.903  57.407  1.00 13.88           O  
ATOM   1068  CB  CYS A 115      30.617  57.790  54.646  1.00 14.36           C  
ATOM   1069  SG  CYS A 115      30.386  58.326  52.949  1.00 24.05           S  
ATOM   1070  H   CYS A 115      28.050  57.686  54.513  1.00  0.00           H  
ATOM   1071  N   THR A 116      30.912  55.226  56.732  1.00 19.55           N  
ATOM   1072  CA  THR A 116      31.418  54.941  58.072  1.00 17.35           C  
ATOM   1073  C   THR A 116      32.895  55.323  58.187  1.00 20.22           C  
ATOM   1074  O   THR A 116      33.607  54.846  59.070  1.00 21.98           O  
ATOM   1075  CB  THR A 116      31.242  53.456  58.434  1.00 14.90           C  
ATOM   1076  OG1 THR A 116      31.962  52.641  57.502  1.00 22.34           O  
ATOM   1077  CG2 THR A 116      29.764  53.071  58.397  1.00 18.60           C  
ATOM   1078  H   THR A 116      31.177  54.640  55.984  1.00  0.00           H  
ATOM   1079  HG1 THR A 116      32.031  51.775  57.898  1.00  0.00           H  
ATOM   1080  N   ALA A 117      33.314  56.259  57.338  1.00 19.38           N  
ATOM   1081  CA  ALA A 117      34.701  56.718  57.268  1.00 17.01           C  
ATOM   1082  C   ALA A 117      34.817  57.877  56.281  1.00 20.72           C  
ATOM   1083  O   ALA A 117      33.833  58.265  55.649  1.00 27.17           O  
ATOM   1084  CB  ALA A 117      35.616  55.576  56.836  1.00 10.14           C  
ATOM   1085  H   ALA A 117      32.670  56.621  56.702  1.00  0.00           H  
ATOM   1086  N   LYS A 118      36.001  58.476  56.204  1.00 22.32           N  
ATOM   1087  CA  LYS A 118      36.271  59.517  55.218  1.00 21.93           C  
ATOM   1088  C   LYS A 118      36.567  58.856  53.870  1.00 26.20           C  
ATOM   1089  O   LYS A 118      37.453  58.009  53.772  1.00 26.73           O  
ATOM   1090  CB  LYS A 118      37.463  60.366  55.663  1.00 23.91           C  
ATOM   1091  CG  LYS A 118      37.427  61.813  55.200  1.00 28.52           C  
ATOM   1092  CD  LYS A 118      38.650  62.564  55.701  1.00 34.05           C  
ATOM   1093  CE  LYS A 118      38.407  64.062  55.777  1.00 42.34           C  
ATOM   1094  NZ  LYS A 118      38.676  64.766  54.494  1.00 48.00           N  
ATOM   1095  H   LYS A 118      36.717  58.167  56.796  1.00  0.00           H  
ATOM   1096  HZ1 LYS A 118      39.654  64.577  54.194  1.00  0.00           H  
ATOM   1097  HZ2 LYS A 118      38.014  64.445  53.758  1.00  0.00           H  
ATOM   1098  HZ3 LYS A 118      38.555  65.786  54.650  1.00  0.00           H  
ATOM   1099  N   THR A 119      35.748  59.160  52.867  1.00 26.09           N  
ATOM   1100  CA  THR A 119      35.845  58.502  51.560  1.00 22.35           C  
ATOM   1101  C   THR A 119      36.115  59.518  50.448  1.00 26.18           C  
ATOM   1102  O   THR A 119      35.342  59.654  49.495  1.00 29.49           O  
ATOM   1103  CB  THR A 119      34.558  57.721  51.224  1.00 20.18           C  
ATOM   1104  OG1 THR A 119      33.424  58.602  51.287  1.00 17.96           O  
ATOM   1105  CG2 THR A 119      34.369  56.570  52.197  1.00 16.01           C  
ATOM   1106  H   THR A 119      35.072  59.856  53.022  1.00  0.00           H  
ATOM   1107  HG1 THR A 119      33.053  58.538  52.173  1.00  0.00           H  
ATOM   1108  N   GLU A 120      37.284  60.140  50.518  1.00 24.97           N  
ATOM   1109  CA  GLU A 120      37.603  61.304  49.699  1.00 18.20           C  
ATOM   1110  C   GLU A 120      37.561  61.029  48.197  1.00 16.33           C  
ATOM   1111  O   GLU A 120      37.124  61.878  47.424  1.00 19.07           O  
ATOM   1112  CB  GLU A 120      38.978  61.853  50.091  1.00 26.15           C  
ATOM   1113  CG  GLU A 120      39.144  62.125  51.585  1.00 24.11           C  
ATOM   1114  CD  GLU A 120      39.932  61.046  52.309  1.00 26.12           C  
ATOM   1115  OE1 GLU A 120      39.663  59.842  52.103  1.00 24.83           O  
ATOM   1116  OE2 GLU A 120      40.817  61.411  53.111  1.00 39.52           O  
ATOM   1117  H   GLU A 120      37.915  59.766  51.158  1.00  0.00           H  
ATOM   1118  N   TRP A 121      37.901  59.806  47.803  1.00 17.26           N  
ATOM   1119  CA  TRP A 121      37.931  59.433  46.385  1.00 25.71           C  
ATOM   1120  C   TRP A 121      36.542  59.352  45.745  1.00 27.88           C  
ATOM   1121  O   TRP A 121      36.414  59.076  44.551  1.00 29.64           O  
ATOM   1122  CB  TRP A 121      38.649  58.094  46.203  1.00 20.85           C  
ATOM   1123  CG  TRP A 121      38.045  56.981  46.989  1.00 20.79           C  
ATOM   1124  CD1 TRP A 121      37.116  56.076  46.557  1.00 26.37           C  
ATOM   1125  CD2 TRP A 121      38.301  56.670  48.360  1.00 25.82           C  
ATOM   1126  NE1 TRP A 121      36.769  55.226  47.581  1.00 20.88           N  
ATOM   1127  CE2 TRP A 121      37.479  55.570  48.701  1.00 23.08           C  
ATOM   1128  CE3 TRP A 121      39.146  57.212  49.337  1.00 24.55           C  
ATOM   1129  CZ2 TRP A 121      37.474  55.009  49.975  1.00 18.50           C  
ATOM   1130  CZ3 TRP A 121      39.144  56.651  50.600  1.00 23.89           C  
ATOM   1131  CH2 TRP A 121      38.310  55.559  50.909  1.00 23.21           C  
ATOM   1132  H   TRP A 121      38.169  59.181  48.492  1.00  0.00           H  
ATOM   1133  HE1 TRP A 121      36.141  54.471  47.482  1.00  0.00           H  
ATOM   1134  N   LEU A 122      35.505  59.522  46.561  1.00 24.53           N  
ATOM   1135  CA  LEU A 122      34.134  59.508  46.073  1.00 18.11           C  
ATOM   1136  C   LEU A 122      33.654  60.895  45.670  1.00 15.50           C  
ATOM   1137  O   LEU A 122      32.594  61.040  45.058  1.00 20.88           O  
ATOM   1138  CB  LEU A 122      33.204  58.918  47.135  1.00 15.11           C  
ATOM   1139  CG  LEU A 122      33.480  57.451  47.477  1.00 14.92           C  
ATOM   1140  CD1 LEU A 122      32.426  56.928  48.441  1.00  9.67           C  
ATOM   1141  CD2 LEU A 122      33.496  56.619  46.196  1.00 12.52           C  
ATOM   1142  H   LEU A 122      35.680  59.598  47.520  1.00  0.00           H  
ATOM   1143  N   ASP A 123      34.450  61.910  45.990  1.00 14.68           N  
ATOM   1144  CA  ASP A 123      34.106  63.292  45.671  1.00 19.59           C  
ATOM   1145  C   ASP A 123      34.127  63.540  44.162  1.00 26.18           C  
ATOM   1146  O   ASP A 123      35.075  63.159  43.471  1.00 26.45           O  
ATOM   1147  CB  ASP A 123      35.074  64.255  46.367  1.00 29.21           C  
ATOM   1148  CG  ASP A 123      34.953  64.226  47.885  1.00 30.19           C  
ATOM   1149  OD1 ASP A 123      34.142  63.446  48.418  1.00 31.94           O  
ATOM   1150  OD2 ASP A 123      35.679  64.993  48.548  1.00 31.31           O  
ATOM   1151  H   ASP A 123      35.343  61.714  46.353  1.00  0.00           H  
ATOM   1152  N   GLY A 124      33.050  64.127  43.651  1.00 20.46           N  
ATOM   1153  CA  GLY A 124      32.925  64.320  42.218  1.00 18.30           C  
ATOM   1154  C   GLY A 124      32.278  63.150  41.496  1.00 17.03           C  
ATOM   1155  O   GLY A 124      31.931  63.259  40.323  1.00 25.78           O  
ATOM   1156  H   GLY A 124      32.366  64.470  44.263  1.00  0.00           H  
ATOM   1157  N   LYS A 125      32.100  62.035  42.196  1.00 12.95           N  
ATOM   1158  CA  LYS A 125      31.461  60.859  41.615  1.00 16.91           C  
ATOM   1159  C   LYS A 125      30.073  60.600  42.198  1.00 20.49           C  
ATOM   1160  O   LYS A 125      29.198  60.065  41.521  1.00 27.19           O  
ATOM   1161  CB  LYS A 125      32.333  59.622  41.827  1.00 20.01           C  
ATOM   1162  CG  LYS A 125      33.685  59.677  41.141  1.00 27.24           C  
ATOM   1163  CD  LYS A 125      34.453  58.392  41.376  1.00 36.15           C  
ATOM   1164  CE  LYS A 125      35.839  58.447  40.765  1.00 45.99           C  
ATOM   1165  NZ  LYS A 125      36.705  57.346  41.280  1.00 55.51           N  
ATOM   1166  H   LYS A 125      32.519  61.990  43.077  1.00  0.00           H  
ATOM   1167  HZ1 LYS A 125      36.262  56.428  41.070  1.00  0.00           H  
ATOM   1168  HZ2 LYS A 125      37.634  57.394  40.813  1.00  0.00           H  
ATOM   1169  HZ3 LYS A 125      36.825  57.450  42.306  1.00  0.00           H  
ATOM   1170  N   HIS A 126      29.910  60.875  43.488  1.00 23.29           N  
ATOM   1171  CA  HIS A 126      28.643  60.644  44.179  1.00 12.62           C  
ATOM   1172  C   HIS A 126      28.143  61.923  44.841  1.00 15.69           C  
ATOM   1173  O   HIS A 126      28.931  62.687  45.402  1.00 19.58           O  
ATOM   1174  CB  HIS A 126      28.808  59.553  45.238  1.00 12.69           C  
ATOM   1175  CG  HIS A 126      29.256  58.235  44.686  1.00  5.33           C  
ATOM   1176  ND1 HIS A 126      28.371  57.259  44.283  1.00 13.16           N  
ATOM   1177  CD2 HIS A 126      30.494  57.733  44.466  1.00  6.72           C  
ATOM   1178  CE1 HIS A 126      29.042  56.214  43.834  1.00 10.73           C  
ATOM   1179  NE2 HIS A 126      30.333  56.475  43.934  1.00  5.96           N  
ATOM   1180  H   HIS A 126      30.670  61.280  43.962  1.00  0.00           H  
ATOM   1181  HD1 HIS A 126      27.388  57.360  44.290  1.00  0.00           H  
ATOM   1182  HE2 HIS A 126      31.047  55.849  43.665  1.00  0.00           H  
ATOM   1183  N   VAL A 127      26.837  62.164  44.762  1.00 18.42           N  
ATOM   1184  CA  VAL A 127      26.251  63.388  45.309  1.00 19.65           C  
ATOM   1185  C   VAL A 127      25.955  63.289  46.809  1.00 18.91           C  
ATOM   1186  O   VAL A 127      25.279  62.366  47.265  1.00 17.30           O  
ATOM   1187  CB  VAL A 127      24.955  63.783  44.548  1.00 22.72           C  
ATOM   1188  CG1 VAL A 127      24.334  65.033  45.171  1.00 14.94           C  
ATOM   1189  CG2 VAL A 127      25.269  64.030  43.076  1.00 14.41           C  
ATOM   1190  H   VAL A 127      26.272  61.528  44.272  1.00  0.00           H  
ATOM   1191  N   VAL A 128      26.613  64.147  47.580  1.00 21.95           N  
ATOM   1192  CA  VAL A 128      26.366  64.276  49.013  1.00 15.78           C  
ATOM   1193  C   VAL A 128      25.173  65.200  49.245  1.00 17.00           C  
ATOM   1194  O   VAL A 128      25.151  66.336  48.761  1.00 14.50           O  
ATOM   1195  CB  VAL A 128      27.609  64.859  49.741  1.00 16.85           C  
ATOM   1196  CG1 VAL A 128      27.304  65.101  51.211  1.00  7.36           C  
ATOM   1197  CG2 VAL A 128      28.789  63.915  49.592  1.00 10.09           C  
ATOM   1198  H   VAL A 128      27.283  64.713  47.136  1.00  0.00           H  
ATOM   1199  N   PHE A 129      24.180  64.709  49.978  1.00 17.70           N  
ATOM   1200  CA  PHE A 129      22.934  65.456  50.152  1.00 21.68           C  
ATOM   1201  C   PHE A 129      22.395  65.438  51.582  1.00 21.66           C  
ATOM   1202  O   PHE A 129      21.307  65.952  51.850  1.00 22.80           O  
ATOM   1203  CB  PHE A 129      21.860  64.935  49.184  1.00 12.95           C  
ATOM   1204  CG  PHE A 129      21.421  63.530  49.465  1.00  6.36           C  
ATOM   1205  CD1 PHE A 129      22.196  62.453  49.061  1.00  3.19           C  
ATOM   1206  CD2 PHE A 129      20.258  63.284  50.176  1.00  8.45           C  
ATOM   1207  CE1 PHE A 129      21.825  61.159  49.368  1.00  2.00           C  
ATOM   1208  CE2 PHE A 129      19.884  61.988  50.488  1.00  2.51           C  
ATOM   1209  CZ  PHE A 129      20.672  60.926  50.082  1.00  2.42           C  
ATOM   1210  H   PHE A 129      24.299  63.812  50.362  1.00  0.00           H  
ATOM   1211  N   GLY A 130      23.159  64.854  52.497  1.00 21.00           N  
ATOM   1212  CA  GLY A 130      22.745  64.835  53.886  1.00 15.99           C  
ATOM   1213  C   GLY A 130      23.804  64.300  54.825  1.00 20.71           C  
ATOM   1214  O   GLY A 130      24.898  63.933  54.400  1.00 25.92           O  
ATOM   1215  H   GLY A 130      24.001  64.426  52.243  1.00  0.00           H  
ATOM   1216  N   LYS A 131      23.468  64.242  56.107  1.00 19.22           N  
ATOM   1217  CA  LYS A 131      24.338  63.639  57.111  1.00 20.51           C  
ATOM   1218  C   LYS A 131      23.507  63.126  58.286  1.00 19.12           C  
ATOM   1219  O   LYS A 131      22.426  63.657  58.576  1.00 16.86           O  
ATOM   1220  CB  LYS A 131      25.359  64.667  57.610  1.00 24.92           C  
ATOM   1221  CG  LYS A 131      24.733  65.804  58.400  1.00 34.83           C  
ATOM   1222  CD  LYS A 131      25.762  66.775  58.933  1.00 42.30           C  
ATOM   1223  CE  LYS A 131      25.073  67.917  59.661  1.00 47.25           C  
ATOM   1224  NZ  LYS A 131      25.999  69.039  59.972  1.00 56.42           N  
ATOM   1225  H   LYS A 131      22.610  64.644  56.368  1.00  0.00           H  
ATOM   1226  HZ1 LYS A 131      26.438  69.402  59.105  1.00  0.00           H  
ATOM   1227  HZ2 LYS A 131      25.465  69.795  60.446  1.00  0.00           H  
ATOM   1228  HZ3 LYS A 131      26.734  68.687  60.620  1.00  0.00           H  
ATOM   1229  N   VAL A 132      23.986  62.069  58.932  1.00 18.26           N  
ATOM   1230  CA  VAL A 132      23.343  61.551  60.138  1.00 19.95           C  
ATOM   1231  C   VAL A 132      23.281  62.627  61.223  1.00 24.69           C  
ATOM   1232  O   VAL A 132      24.283  63.276  61.528  1.00 28.91           O  
ATOM   1233  CB  VAL A 132      24.091  60.322  60.700  1.00 16.77           C  
ATOM   1234  CG1 VAL A 132      23.454  59.875  62.002  1.00 14.01           C  
ATOM   1235  CG2 VAL A 132      24.066  59.186  59.693  1.00 11.78           C  
ATOM   1236  H   VAL A 132      24.794  61.652  58.586  1.00  0.00           H  
ATOM   1237  N   LYS A 133      22.069  62.913  61.679  1.00 24.45           N  
ATOM   1238  CA  LYS A 133      21.853  63.849  62.774  1.00 25.04           C  
ATOM   1239  C   LYS A 133      22.014  63.116  64.108  1.00 28.41           C  
ATOM   1240  O   LYS A 133      22.779  63.535  64.973  1.00 33.96           O  
ATOM   1241  CB  LYS A 133      20.451  64.445  62.669  1.00 30.51           C  
ATOM   1242  CG  LYS A 133      20.310  65.827  63.261  1.00 37.98           C  
ATOM   1243  CD  LYS A 133      18.906  66.357  63.057  1.00 43.64           C  
ATOM   1244  CE  LYS A 133      18.851  67.854  63.299  1.00 54.49           C  
ATOM   1245  NZ  LYS A 133      17.580  68.449  62.804  1.00 68.56           N  
ATOM   1246  H   LYS A 133      21.321  62.531  61.188  1.00  0.00           H  
ATOM   1247  HZ1 LYS A 133      17.471  68.235  61.793  1.00  0.00           H  
ATOM   1248  HZ2 LYS A 133      16.780  68.039  63.329  1.00  0.00           H  
ATOM   1249  HZ3 LYS A 133      17.593  69.479  62.945  1.00  0.00           H  
ATOM   1250  N   GLU A 134      21.337  61.980  64.237  1.00 26.55           N  
ATOM   1251  CA  GLU A 134      21.446  61.147  65.428  1.00 26.97           C  
ATOM   1252  C   GLU A 134      21.385  59.659  65.089  1.00 23.38           C  
ATOM   1253  O   GLU A 134      20.712  59.254  64.146  1.00 25.47           O  
ATOM   1254  CB  GLU A 134      20.337  61.499  66.422  1.00 32.31           C  
ATOM   1255  CG  GLU A 134      20.648  62.710  67.284  1.00 43.46           C  
ATOM   1256  CD  GLU A 134      19.413  63.300  67.928  1.00 54.75           C  
ATOM   1257  OE1 GLU A 134      18.937  62.735  68.936  1.00 63.66           O  
ATOM   1258  OE2 GLU A 134      18.920  64.333  67.427  1.00 62.39           O  
ATOM   1259  H   GLU A 134      20.737  61.710  63.505  1.00  0.00           H  
ATOM   1260  N   GLY A 135      22.129  58.854  65.838  1.00 18.50           N  
ATOM   1261  CA  GLY A 135      22.093  57.418  65.634  1.00 11.18           C  
ATOM   1262  C   GLY A 135      23.272  56.834  64.881  1.00 11.97           C  
ATOM   1263  O   GLY A 135      23.201  55.696  64.428  1.00 21.64           O  
ATOM   1264  H   GLY A 135      22.565  59.230  66.624  1.00  0.00           H  
ATOM   1265  N   MET A 136      24.386  57.560  64.815  1.00 17.54           N  
ATOM   1266  CA  MET A 136      25.617  57.028  64.211  1.00 21.70           C  
ATOM   1267  C   MET A 136      26.031  55.701  64.853  1.00 25.61           C  
ATOM   1268  O   MET A 136      26.603  54.832  64.192  1.00 25.27           O  
ATOM   1269  CB  MET A 136      26.771  58.027  64.345  1.00 23.42           C  
ATOM   1270  CG  MET A 136      27.216  58.679  63.041  1.00 26.63           C  
ATOM   1271  SD  MET A 136      27.265  57.561  61.631  1.00 25.44           S  
ATOM   1272  CE  MET A 136      28.701  56.587  61.973  1.00 34.84           C  
ATOM   1273  H   MET A 136      24.341  58.489  65.113  1.00  0.00           H  
ATOM   1274  N   ASN A 137      25.676  55.531  66.125  1.00 25.51           N  
ATOM   1275  CA  ASN A 137      25.944  54.294  66.855  1.00 29.36           C  
ATOM   1276  C   ASN A 137      25.109  53.129  66.322  1.00 28.08           C  
ATOM   1277  O   ASN A 137      25.522  51.968  66.405  1.00 29.74           O  
ATOM   1278  CB  ASN A 137      25.669  54.492  68.347  1.00 33.76           C  
ATOM   1279  CG  ASN A 137      24.279  55.027  68.615  1.00 46.93           C  
ATOM   1280  OD1 ASN A 137      23.904  56.082  68.110  1.00 54.47           O  
ATOM   1281  ND2 ASN A 137      23.493  54.284  69.375  1.00 51.45           N  
ATOM   1282  H   ASN A 137      25.229  56.275  66.580  1.00  0.00           H  
ATOM   1283 HD21 ASN A 137      22.606  54.666  69.522  1.00  0.00           H  
ATOM   1284 HD22 ASN A 137      23.810  53.439  69.749  1.00  0.00           H  
ATOM   1285  N   ILE A 138      23.938  53.442  65.775  1.00 24.02           N  
ATOM   1286  CA  ILE A 138      23.120  52.442  65.091  1.00 22.24           C  
ATOM   1287  C   ILE A 138      23.759  52.023  63.763  1.00 22.28           C  
ATOM   1288  O   ILE A 138      23.828  50.835  63.448  1.00 20.94           O  
ATOM   1289  CB  ILE A 138      21.694  52.972  64.827  1.00 19.91           C  
ATOM   1290  CG1 ILE A 138      21.040  53.381  66.150  1.00 16.94           C  
ATOM   1291  CG2 ILE A 138      20.854  51.907  64.118  1.00 16.87           C  
ATOM   1292  CD1 ILE A 138      20.927  52.258  67.156  1.00 18.46           C  
ATOM   1293  H   ILE A 138      23.617  54.365  65.838  1.00  0.00           H  
ATOM   1294  N   VAL A 139      24.313  52.992  63.039  1.00 17.86           N  
ATOM   1295  CA  VAL A 139      25.036  52.709  61.802  1.00 19.06           C  
ATOM   1296  C   VAL A 139      26.269  51.839  62.066  1.00 22.15           C  
ATOM   1297  O   VAL A 139      26.468  50.812  61.412  1.00 21.60           O  
ATOM   1298  CB  VAL A 139      25.472  54.015  61.096  1.00 18.73           C  
ATOM   1299  CG1 VAL A 139      26.179  53.691  59.786  1.00 20.96           C  
ATOM   1300  CG2 VAL A 139      24.256  54.903  60.840  1.00  9.61           C  
ATOM   1301  H   VAL A 139      24.157  53.915  63.331  1.00  0.00           H  
ATOM   1302  N   GLU A 140      27.035  52.198  63.091  1.00 23.82           N  
ATOM   1303  CA  GLU A 140      28.143  51.360  63.560  1.00 22.61           C  
ATOM   1304  C   GLU A 140      27.680  49.953  63.948  1.00 20.95           C  
ATOM   1305  O   GLU A 140      28.372  48.972  63.688  1.00 21.28           O  
ATOM   1306  CB  GLU A 140      28.837  52.017  64.754  1.00 18.85           C  
ATOM   1307  CG  GLU A 140      29.566  53.303  64.410  1.00 26.67           C  
ATOM   1308  CD  GLU A 140      29.748  54.220  65.609  1.00 40.97           C  
ATOM   1309  OE1 GLU A 140      29.800  53.718  66.756  1.00 52.24           O  
ATOM   1310  OE2 GLU A 140      29.837  55.451  65.404  1.00 45.97           O  
ATOM   1311  H   GLU A 140      26.863  53.066  63.507  1.00  0.00           H  
ATOM   1312  N   ALA A 141      26.493  49.859  64.544  1.00 23.91           N  
ATOM   1313  CA  ALA A 141      25.877  48.564  64.839  1.00 23.54           C  
ATOM   1314  C   ALA A 141      25.541  47.794  63.566  1.00 24.14           C  
ATOM   1315  O   ALA A 141      25.767  46.586  63.484  1.00 29.93           O  
ATOM   1316  CB  ALA A 141      24.620  48.759  65.676  1.00 23.78           C  
ATOM   1317  H   ALA A 141      26.057  50.682  64.846  1.00  0.00           H  
ATOM   1318  N   MET A 142      25.034  48.503  62.561  1.00 26.59           N  
ATOM   1319  CA  MET A 142      24.687  47.895  61.275  1.00 25.60           C  
ATOM   1320  C   MET A 142      25.910  47.303  60.575  1.00 26.89           C  
ATOM   1321  O   MET A 142      25.902  46.138  60.164  1.00 21.34           O  
ATOM   1322  CB  MET A 142      24.035  48.931  60.360  1.00 19.86           C  
ATOM   1323  CG  MET A 142      22.634  49.343  60.781  1.00 18.80           C  
ATOM   1324  SD  MET A 142      22.149  50.945  60.107  1.00 23.36           S  
ATOM   1325  CE  MET A 142      22.333  50.637  58.359  1.00 13.84           C  
ATOM   1326  H   MET A 142      24.894  49.459  62.702  1.00  0.00           H  
ATOM   1327  N   GLU A 143      26.997  48.069  60.542  1.00 22.50           N  
ATOM   1328  CA  GLU A 143      28.182  47.657  59.802  1.00 30.37           C  
ATOM   1329  C   GLU A 143      28.849  46.408  60.380  1.00 29.55           C  
ATOM   1330  O   GLU A 143      29.559  45.700  59.670  1.00 29.83           O  
ATOM   1331  CB  GLU A 143      29.182  48.817  59.687  1.00 27.97           C  
ATOM   1332  CG  GLU A 143      30.051  49.060  60.902  1.00 31.21           C  
ATOM   1333  CD  GLU A 143      31.072  50.161  60.671  1.00 39.61           C  
ATOM   1334  OE1 GLU A 143      31.790  50.112  59.651  1.00 47.40           O  
ATOM   1335  OE2 GLU A 143      31.158  51.081  61.509  1.00 46.89           O  
ATOM   1336  H   GLU A 143      26.955  48.945  60.982  1.00  0.00           H  
ATOM   1337  N   ARG A 144      28.452  46.036  61.594  1.00 37.44           N  
ATOM   1338  CA  ARG A 144      28.905  44.788  62.212  1.00 40.48           C  
ATOM   1339  C   ARG A 144      28.293  43.551  61.546  1.00 40.96           C  
ATOM   1340  O   ARG A 144      28.795  42.435  61.703  1.00 41.24           O  
ATOM   1341  CB  ARG A 144      28.582  44.789  63.711  1.00 39.54           C  
ATOM   1342  CG  ARG A 144      29.481  45.698  64.536  0.00 40.28           C  
ATOM   1343  CD  ARG A 144      29.091  45.685  66.006  0.00 39.77           C  
ATOM   1344  NE  ARG A 144      30.096  46.329  66.848  0.00 39.56           N  
ATOM   1345  CZ  ARG A 144      30.103  47.622  67.161  0.00 39.03           C  
ATOM   1346  NH1 ARG A 144      29.157  48.431  66.701  0.00 39.29           N  
ATOM   1347  NH2 ARG A 144      31.062  48.109  67.937  0.00 39.14           N  
ATOM   1348  H   ARG A 144      27.871  46.640  62.102  1.00  0.00           H  
ATOM   1349  HE  ARG A 144      30.819  45.773  67.208  1.00  0.00           H  
ATOM   1350 HH11 ARG A 144      28.431  48.084  66.109  1.00  0.00           H  
ATOM   1351 HH12 ARG A 144      29.179  49.401  66.947  1.00  0.00           H  
ATOM   1352 HH21 ARG A 144      31.772  47.500  68.291  1.00  0.00           H  
ATOM   1353 HH22 ARG A 144      31.068  49.078  68.182  1.00  0.00           H  
ATOM   1354  N   PHE A 145      27.230  43.760  60.775  1.00 39.35           N  
ATOM   1355  CA  PHE A 145      26.607  42.676  60.017  1.00 34.86           C  
ATOM   1356  C   PHE A 145      27.060  42.678  58.559  1.00 33.38           C  
ATOM   1357  O   PHE A 145      26.507  41.959  57.725  1.00 26.47           O  
ATOM   1358  CB  PHE A 145      25.085  42.792  60.081  1.00 35.06           C  
ATOM   1359  CG  PHE A 145      24.542  42.814  61.477  1.00 34.71           C  
ATOM   1360  CD1 PHE A 145      24.338  41.628  62.174  1.00 35.06           C  
ATOM   1361  CD2 PHE A 145      24.249  44.022  62.105  1.00 35.41           C  
ATOM   1362  CE1 PHE A 145      23.849  41.643  63.476  1.00 31.97           C  
ATOM   1363  CE2 PHE A 145      23.761  44.047  63.408  1.00 36.62           C  
ATOM   1364  CZ  PHE A 145      23.560  42.854  64.093  1.00 32.98           C  
ATOM   1365  H   PHE A 145      26.837  44.653  60.770  1.00  0.00           H  
ATOM   1366  N   GLY A 146      28.047  43.515  58.257  1.00 34.09           N  
ATOM   1367  CA  GLY A 146      28.563  43.600  56.905  1.00 38.46           C  
ATOM   1368  C   GLY A 146      29.654  42.589  56.612  1.00 41.22           C  
ATOM   1369  O   GLY A 146      29.953  41.722  57.434  1.00 43.30           O  
ATOM   1370  H   GLY A 146      28.472  44.034  58.969  1.00  0.00           H  
ATOM   1371  N   SER A 147      30.251  42.703  55.432  1.00 40.19           N  
ATOM   1372  CA  SER A 147      31.349  41.828  55.039  1.00 39.74           C  
ATOM   1373  C   SER A 147      32.209  42.496  53.979  1.00 40.29           C  
ATOM   1374  O   SER A 147      31.846  43.545  53.443  1.00 41.92           O  
ATOM   1375  CB  SER A 147      30.816  40.502  54.496  1.00 42.00           C  
ATOM   1376  OG  SER A 147      30.370  40.641  53.161  1.00 42.54           O  
ATOM   1377  H   SER A 147      29.944  43.415  54.827  1.00  0.00           H  
ATOM   1378  HG  SER A 147      29.416  40.463  53.199  1.00  0.00           H  
ATOM   1379  N   ARG A 148      33.299  41.832  53.611  1.00 38.68           N  
ATOM   1380  CA  ARG A 148      34.300  42.416  52.723  1.00 37.02           C  
ATOM   1381  C   ARG A 148      33.760  42.774  51.341  1.00 34.43           C  
ATOM   1382  O   ARG A 148      34.196  43.748  50.731  1.00 34.01           O  
ATOM   1383  CB  ARG A 148      35.497  41.469  52.585  1.00 41.34           C  
ATOM   1384  CG  ARG A 148      36.398  41.415  53.815  0.00 43.83           C  
ATOM   1385  CD  ARG A 148      36.709  42.808  54.362  0.00 47.46           C  
ATOM   1386  NE  ARG A 148      37.312  43.684  53.359  0.00 49.44           N  
ATOM   1387  CZ  ARG A 148      37.189  45.008  53.347  0.00 51.37           C  
ATOM   1388  NH1 ARG A 148      36.475  45.625  54.280  0.00 52.39           N  
ATOM   1389  NH2 ARG A 148      37.774  45.719  52.393  0.00 53.65           N  
ATOM   1390  H   ARG A 148      33.425  40.933  53.970  1.00  0.00           H  
ATOM   1391  HE  ARG A 148      37.843  43.273  52.645  1.00  0.00           H  
ATOM   1392 HH11 ARG A 148      36.022  45.105  55.003  1.00  0.00           H  
ATOM   1393 HH12 ARG A 148      36.391  46.622  54.258  1.00  0.00           H  
ATOM   1394 HH21 ARG A 148      38.307  45.260  51.682  1.00  0.00           H  
ATOM   1395 HH22 ARG A 148      37.682  46.715  52.384  1.00  0.00           H  
ATOM   1396  N   ASN A 149      32.790  42.003  50.864  1.00 32.31           N  
ATOM   1397  CA  ASN A 149      32.176  42.277  49.571  1.00 32.90           C  
ATOM   1398  C   ASN A 149      30.841  43.016  49.694  1.00 35.71           C  
ATOM   1399  O   ASN A 149      30.263  43.439  48.691  1.00 44.06           O  
ATOM   1400  CB  ASN A 149      31.990  40.975  48.786  1.00 38.09           C  
ATOM   1401  CG  ASN A 149      31.319  39.886  49.603  1.00 44.07           C  
ATOM   1402  OD1 ASN A 149      30.439  40.153  50.413  1.00 47.02           O  
ATOM   1403  ND2 ASN A 149      31.720  38.648  49.373  1.00 54.30           N  
ATOM   1404  H   ASN A 149      32.431  41.298  51.442  1.00  0.00           H  
ATOM   1405 HD21 ASN A 149      31.246  37.972  49.895  1.00  0.00           H  
ATOM   1406 HD22 ASN A 149      32.402  38.471  48.700  1.00  0.00           H  
ATOM   1407  N   GLY A 150      30.367  43.187  50.924  1.00 31.68           N  
ATOM   1408  CA  GLY A 150      29.097  43.855  51.141  1.00 26.24           C  
ATOM   1409  C   GLY A 150      27.964  42.940  51.572  1.00 26.05           C  
ATOM   1410  O   GLY A 150      26.969  43.403  52.134  1.00 28.67           O  
ATOM   1411  H   GLY A 150      30.914  42.924  51.690  1.00  0.00           H  
ATOM   1412  N   LYS A 151      28.108  41.643  51.324  1.00 25.03           N  
ATOM   1413  CA  LYS A 151      27.079  40.679  51.705  1.00 28.67           C  
ATOM   1414  C   LYS A 151      26.830  40.700  53.215  1.00 30.88           C  
ATOM   1415  O   LYS A 151      27.729  40.431  54.013  1.00 35.24           O  
ATOM   1416  CB  LYS A 151      27.474  39.266  51.261  1.00 21.97           C  
ATOM   1417  CG  LYS A 151      26.321  38.273  51.263  0.00 25.08           C  
ATOM   1418  CD  LYS A 151      26.763  36.894  50.800  0.00 25.45           C  
ATOM   1419  CE  LYS A 151      27.626  36.204  51.844  0.00 26.86           C  
ATOM   1420  NZ  LYS A 151      27.923  34.795  51.467  0.00 27.20           N  
ATOM   1421  H   LYS A 151      28.921  41.341  50.869  1.00  0.00           H  
ATOM   1422  HZ1 LYS A 151      27.029  34.273  51.370  1.00  0.00           H  
ATOM   1423  HZ2 LYS A 151      28.434  34.776  50.562  1.00  0.00           H  
ATOM   1424  HZ3 LYS A 151      28.505  34.350  52.206  1.00  0.00           H  
ATOM   1425  N   THR A 152      25.627  41.104  53.597  1.00 36.60           N  
ATOM   1426  CA  THR A 152      25.234  41.173  55.003  1.00 36.72           C  
ATOM   1427  C   THR A 152      24.968  39.786  55.597  1.00 36.00           C  
ATOM   1428  O   THR A 152      24.321  38.949  54.971  1.00 37.41           O  
ATOM   1429  CB  THR A 152      23.965  42.034  55.176  1.00 32.19           C  
ATOM   1430  OG1 THR A 152      22.930  41.550  54.308  1.00 29.01           O  
ATOM   1431  CG2 THR A 152      24.261  43.477  54.822  1.00 26.48           C  
ATOM   1432  H   THR A 152      24.992  41.298  52.881  1.00  0.00           H  
ATOM   1433  HG1 THR A 152      22.924  40.578  54.324  1.00  0.00           H  
ATOM   1434  N   SER A 153      25.428  39.567  56.824  1.00 36.14           N  
ATOM   1435  CA  SER A 153      25.223  38.293  57.518  1.00 36.98           C  
ATOM   1436  C   SER A 153      23.821  38.163  58.112  1.00 36.65           C  
ATOM   1437  O   SER A 153      23.399  37.070  58.492  1.00 37.57           O  
ATOM   1438  CB  SER A 153      26.255  38.125  58.635  1.00 35.31           C  
ATOM   1439  OG  SER A 153      26.163  39.186  59.573  1.00 46.88           O  
ATOM   1440  H   SER A 153      25.961  40.263  57.258  1.00  0.00           H  
ATOM   1441  HG  SER A 153      26.898  39.146  60.199  1.00  0.00           H  
ATOM   1442  N   LYS A 154      23.139  39.294  58.268  1.00 36.19           N  
ATOM   1443  CA  LYS A 154      21.760  39.312  58.759  1.00 34.53           C  
ATOM   1444  C   LYS A 154      20.896  40.270  57.939  1.00 30.75           C  
ATOM   1445  O   LYS A 154      21.397  41.244  57.383  1.00 32.83           O  
ATOM   1446  CB  LYS A 154      21.723  39.731  60.232  1.00 39.73           C  
ATOM   1447  CG  LYS A 154      22.080  38.626  61.213  1.00 42.40           C  
ATOM   1448  CD  LYS A 154      21.690  39.015  62.628  1.00 48.09           C  
ATOM   1449  CE  LYS A 154      21.834  37.856  63.593  1.00 51.26           C  
ATOM   1450  NZ  LYS A 154      21.253  38.184  64.922  1.00 59.38           N  
ATOM   1451  H   LYS A 154      23.595  40.134  58.063  1.00  0.00           H  
ATOM   1452  HZ1 LYS A 154      20.243  38.406  64.816  1.00  0.00           H  
ATOM   1453  HZ2 LYS A 154      21.366  37.368  65.557  1.00  0.00           H  
ATOM   1454  HZ3 LYS A 154      21.752  39.004  65.321  1.00  0.00           H  
ATOM   1455  N   LYS A 155      19.598  39.994  57.872  1.00 25.38           N  
ATOM   1456  CA  LYS A 155      18.668  40.864  57.159  1.00 24.87           C  
ATOM   1457  C   LYS A 155      18.516  42.204  57.867  1.00 24.62           C  
ATOM   1458  O   LYS A 155      17.896  42.284  58.931  1.00 28.73           O  
ATOM   1459  CB  LYS A 155      17.296  40.194  57.036  1.00 28.22           C  
ATOM   1460  CG  LYS A 155      16.852  39.954  55.604  0.00 26.55           C  
ATOM   1461  CD  LYS A 155      17.602  38.788  54.977  0.00 27.31           C  
ATOM   1462  CE  LYS A 155      17.372  38.717  53.475  0.00 27.96           C  
ATOM   1463  NZ  LYS A 155      15.926  38.666  53.122  0.00 27.58           N  
ATOM   1464  H   LYS A 155      19.289  39.164  58.284  1.00  0.00           H  
ATOM   1465  HZ1 LYS A 155      15.470  37.867  53.605  1.00  0.00           H  
ATOM   1466  HZ2 LYS A 155      15.472  39.555  53.416  1.00  0.00           H  
ATOM   1467  HZ3 LYS A 155      15.828  38.555  52.092  1.00  0.00           H  
ATOM   1468  N   ILE A 156      19.108  43.244  57.289  1.00 25.97           N  
ATOM   1469  CA  ILE A 156      19.056  44.589  57.861  1.00 27.98           C  
ATOM   1470  C   ILE A 156      18.032  45.433  57.105  1.00 30.69           C  
ATOM   1471  O   ILE A 156      18.211  45.723  55.924  1.00 31.04           O  
ATOM   1472  CB  ILE A 156      20.444  45.291  57.786  1.00 26.88           C  
ATOM   1473  CG1 ILE A 156      21.539  44.362  58.317  1.00 18.49           C  
ATOM   1474  CG2 ILE A 156      20.429  46.590  58.591  1.00 23.88           C  
ATOM   1475  CD1 ILE A 156      21.249  43.777  59.686  1.00 16.00           C  
ATOM   1476  H   ILE A 156      19.623  43.075  56.471  1.00  0.00           H  
ATOM   1477  N   THR A 157      16.940  45.796  57.769  1.00 29.13           N  
ATOM   1478  CA  THR A 157      15.839  46.469  57.081  1.00 26.80           C  
ATOM   1479  C   THR A 157      15.474  47.821  57.680  1.00 26.85           C  
ATOM   1480  O   THR A 157      15.838  48.135  58.814  1.00 31.38           O  
ATOM   1481  CB  THR A 157      14.564  45.597  57.062  1.00 26.12           C  
ATOM   1482  OG1 THR A 157      14.166  45.296  58.406  1.00 28.85           O  
ATOM   1483  CG2 THR A 157      14.814  44.302  56.304  1.00 25.62           C  
ATOM   1484  H   THR A 157      16.903  45.678  58.743  1.00  0.00           H  
ATOM   1485  HG1 THR A 157      14.283  44.369  58.645  1.00  0.00           H  
ATOM   1486  N   ILE A 158      14.797  48.637  56.881  1.00 22.49           N  
ATOM   1487  CA  ILE A 158      14.196  49.879  57.346  1.00 23.33           C  
ATOM   1488  C   ILE A 158      12.753  49.605  57.778  1.00 24.61           C  
ATOM   1489  O   ILE A 158      11.822  49.733  56.986  1.00 26.24           O  
ATOM   1490  CB  ILE A 158      14.220  50.949  56.222  1.00 23.99           C  
ATOM   1491  CG1 ILE A 158      15.669  51.221  55.798  1.00 20.26           C  
ATOM   1492  CG2 ILE A 158      13.553  52.234  56.694  1.00 24.22           C  
ATOM   1493  CD1 ILE A 158      15.811  52.123  54.591  1.00 10.92           C  
ATOM   1494  H   ILE A 158      14.695  48.385  55.955  1.00  0.00           H  
ATOM   1495  N   ALA A 159      12.582  49.196  59.032  1.00 24.24           N  
ATOM   1496  CA  ALA A 159      11.276  48.785  59.558  1.00 24.32           C  
ATOM   1497  C   ALA A 159      10.203  49.869  59.415  1.00 20.41           C  
ATOM   1498  O   ALA A 159       9.023  49.577  59.210  1.00 20.90           O  
ATOM   1499  CB  ALA A 159      11.413  48.372  61.025  1.00 17.14           C  
ATOM   1500  H   ALA A 159      13.371  49.176  59.614  1.00  0.00           H  
ATOM   1501  N   ASP A 160      10.628  51.120  59.526  1.00 14.92           N  
ATOM   1502  CA  ASP A 160       9.745  52.264  59.353  1.00 17.79           C  
ATOM   1503  C   ASP A 160      10.595  53.508  59.099  1.00 15.76           C  
ATOM   1504  O   ASP A 160      11.773  53.541  59.447  1.00 19.95           O  
ATOM   1505  CB  ASP A 160       8.887  52.457  60.609  1.00 20.56           C  
ATOM   1506  CG  ASP A 160       7.763  53.463  60.411  1.00 25.35           C  
ATOM   1507  OD1 ASP A 160       7.301  53.646  59.263  1.00 32.59           O  
ATOM   1508  OD2 ASP A 160       7.326  54.064  61.416  1.00 32.67           O  
ATOM   1509  H   ASP A 160      11.577  51.252  59.736  1.00  0.00           H  
ATOM   1510  N   CYS A 161      10.019  54.502  58.439  1.00 13.71           N  
ATOM   1511  CA  CYS A 161      10.728  55.745  58.160  1.00  7.38           C  
ATOM   1512  C   CYS A 161       9.733  56.857  57.886  1.00 12.69           C  
ATOM   1513  O   CYS A 161       8.554  56.598  57.657  1.00 16.52           O  
ATOM   1514  CB  CYS A 161      11.668  55.582  56.959  1.00 14.50           C  
ATOM   1515  SG  CYS A 161      10.998  54.668  55.551  1.00 20.16           S  
ATOM   1516  H   CYS A 161       9.098  54.399  58.124  1.00  0.00           H  
ATOM   1517  N   GLY A 162      10.194  58.098  57.986  1.00 12.41           N  
ATOM   1518  CA  GLY A 162       9.322  59.229  57.734  1.00  5.00           C  
ATOM   1519  C   GLY A 162      10.053  60.539  57.922  1.00 11.16           C  
ATOM   1520  O   GLY A 162      11.267  60.551  58.146  1.00 10.28           O  
ATOM   1521  H   GLY A 162      11.140  58.229  58.219  1.00  0.00           H  
ATOM   1522  N   GLN A 163       9.327  61.645  57.809  1.00  8.73           N  
ATOM   1523  CA  GLN A 163       9.900  62.964  58.074  1.00 13.95           C  
ATOM   1524  C   GLN A 163       9.574  63.443  59.491  1.00 20.71           C  
ATOM   1525  O   GLN A 163       8.508  63.139  60.025  1.00 25.59           O  
ATOM   1526  CB  GLN A 163       9.384  63.974  57.054  1.00  9.21           C  
ATOM   1527  CG  GLN A 163       9.977  65.353  57.204  1.00  5.34           C  
ATOM   1528  CD  GLN A 163       9.514  66.292  56.129  1.00  7.53           C  
ATOM   1529  OE1 GLN A 163       8.882  65.880  55.158  1.00 23.11           O  
ATOM   1530  NE2 GLN A 163       9.840  67.559  56.276  1.00 10.18           N  
ATOM   1531  H   GLN A 163       8.381  61.555  57.565  1.00  0.00           H  
ATOM   1532 HE21 GLN A 163       9.503  68.154  55.585  1.00  0.00           H  
ATOM   1533 HE22 GLN A 163      10.357  67.838  57.059  1.00  0.00           H  
ATOM   1534  N   LEU A 164      10.517  64.132  60.124  1.00 29.31           N  
ATOM   1535  CA  LEU A 164      10.327  64.602  61.496  1.00 27.47           C  
ATOM   1536  C   LEU A 164       9.969  66.083  61.587  1.00 32.93           C  
ATOM   1537  O   LEU A 164      10.716  66.942  61.107  1.00 30.81           O  
ATOM   1538  CB  LEU A 164      11.583  64.344  62.333  1.00 23.07           C  
ATOM   1539  CG  LEU A 164      11.865  62.922  62.815  1.00 23.94           C  
ATOM   1540  CD1 LEU A 164      12.986  62.969  63.837  1.00 25.36           C  
ATOM   1541  CD2 LEU A 164      10.615  62.304  63.426  1.00 24.37           C  
ATOM   1542  H   LEU A 164      11.333  64.356  59.635  1.00  0.00           H  
ATOM   1543  N   GLU A 165       8.864  66.358  62.280  1.00 39.36           N  
ATOM   1544  CA  GLU A 165       8.490  67.708  62.708  1.00 48.15           C  
ATOM   1545  C   GLU A 165       8.398  68.710  61.554  1.00 55.70           C  
ATOM   1546  O   GLU A 165       7.963  68.299  60.453  1.00 65.17           O  
ATOM   1547  CB  GLU A 165       9.468  68.216  63.779  1.00 47.39           C  
ATOM   1548  CG  GLU A 165      10.051  67.124  64.671  1.00 50.34           C  
ATOM   1549  CD  GLU A 165      11.021  67.650  65.715  1.00 56.93           C  
ATOM   1550  OE1 GLU A 165      11.529  68.783  65.558  1.00 63.12           O  
ATOM   1551  OE2 GLU A 165      11.264  66.930  66.708  1.00 57.32           O  
ATOM   1552  OXT GLU A 165       8.706  69.905  61.773  1.00 63.63           O  
ATOM   1553  H   GLU A 165       8.217  65.645  62.401  1.00  0.00           H  
TER    1554      GLU A 165                                                      
ATOM   1555  N   ASN B   3      49.882  -3.972  57.959  1.00 39.55           N  
ATOM   1556  CA  ASN B   3      49.411  -2.734  57.267  1.00 32.17           C  
ATOM   1557  C   ASN B   3      50.258  -1.552  57.704  1.00 26.45           C  
ATOM   1558  O   ASN B   3      50.558  -1.412  58.884  1.00 20.19           O  
ATOM   1559  CB  ASN B   3      47.941  -2.461  57.600  1.00 32.73           C  
ATOM   1560  CG  ASN B   3      46.995  -3.258  56.731  1.00 32.88           C  
ATOM   1561  OD1 ASN B   3      47.373  -3.738  55.666  1.00 34.74           O  
ATOM   1562  ND2 ASN B   3      45.776  -3.448  57.203  1.00 36.00           N  
ATOM   1563 HD21 ASN B   3      45.195  -4.002  56.645  1.00  0.00           H  
ATOM   1564 HD22 ASN B   3      45.505  -3.056  58.054  1.00  0.00           H  
ATOM   1565  N   PRO B   4      50.733  -0.745  56.745  1.00 26.03           N  
ATOM   1566  CA  PRO B   4      51.593   0.366  57.158  1.00 22.64           C  
ATOM   1567  C   PRO B   4      50.820   1.580  57.661  1.00 23.60           C  
ATOM   1568  O   PRO B   4      49.650   1.771  57.329  1.00 26.21           O  
ATOM   1569  CB  PRO B   4      52.396   0.680  55.898  1.00 23.50           C  
ATOM   1570  CG  PRO B   4      51.497   0.275  54.786  1.00 29.42           C  
ATOM   1571  CD  PRO B   4      50.766  -0.948  55.286  1.00 29.82           C  
ATOM   1572  N   THR B   5      51.486   2.388  58.477  1.00 23.26           N  
ATOM   1573  CA  THR B   5      50.909   3.618  59.009  1.00 19.17           C  
ATOM   1574  C   THR B   5      51.760   4.796  58.551  1.00 19.19           C  
ATOM   1575  O   THR B   5      52.988   4.718  58.546  1.00 21.90           O  
ATOM   1576  CB  THR B   5      50.865   3.593  60.562  1.00 19.09           C  
ATOM   1577  OG1 THR B   5      50.037   2.509  60.998  1.00 24.44           O  
ATOM   1578  CG2 THR B   5      50.297   4.895  61.121  1.00 15.75           C  
ATOM   1579  H   THR B   5      52.398   2.117  58.725  1.00  0.00           H  
ATOM   1580  HG1 THR B   5      50.362   1.691  60.598  1.00  0.00           H  
ATOM   1581  N   VAL B   6      51.107   5.852  58.079  1.00 15.19           N  
ATOM   1582  CA  VAL B   6      51.816   7.048  57.635  1.00 15.07           C  
ATOM   1583  C   VAL B   6      51.251   8.271  58.338  1.00 14.79           C  
ATOM   1584  O   VAL B   6      50.151   8.215  58.880  1.00 16.32           O  
ATOM   1585  CB  VAL B   6      51.715   7.245  56.088  1.00 20.62           C  
ATOM   1586  CG1 VAL B   6      52.399   6.091  55.360  1.00 18.88           C  
ATOM   1587  CG2 VAL B   6      50.262   7.357  55.656  1.00 20.63           C  
ATOM   1588  H   VAL B   6      50.126   5.802  58.052  1.00  0.00           H  
ATOM   1589  N   PHE B   7      52.023   9.353  58.381  1.00 13.79           N  
ATOM   1590  CA  PHE B   7      51.561  10.589  59.004  1.00 11.76           C  
ATOM   1591  C   PHE B   7      51.706  11.800  58.089  1.00 15.04           C  
ATOM   1592  O   PHE B   7      52.581  11.834  57.219  1.00 17.86           O  
ATOM   1593  CB  PHE B   7      52.310  10.843  60.325  1.00 18.17           C  
ATOM   1594  CG  PHE B   7      53.739  11.293  60.150  1.00 12.91           C  
ATOM   1595  CD1 PHE B   7      54.767  10.362  60.037  1.00 10.23           C  
ATOM   1596  CD2 PHE B   7      54.055  12.648  60.095  1.00  7.52           C  
ATOM   1597  CE1 PHE B   7      56.088  10.773  59.870  1.00  4.16           C  
ATOM   1598  CE2 PHE B   7      55.375  13.070  59.925  1.00  8.85           C  
ATOM   1599  CZ  PHE B   7      56.390  12.129  59.812  1.00  4.04           C  
ATOM   1600  H   PHE B   7      52.900   9.314  57.945  1.00  0.00           H  
ATOM   1601  N   PHE B   8      50.838  12.786  58.295  1.00 15.08           N  
ATOM   1602  CA  PHE B   8      50.958  14.105  57.674  1.00 18.66           C  
ATOM   1603  C   PHE B   8      51.070  15.137  58.790  1.00 17.65           C  
ATOM   1604  O   PHE B   8      50.305  15.099  59.755  1.00 20.66           O  
ATOM   1605  CB  PHE B   8      49.708  14.448  56.843  1.00 21.75           C  
ATOM   1606  CG  PHE B   8      49.610  13.728  55.520  1.00 18.49           C  
ATOM   1607  CD1 PHE B   8      50.611  12.867  55.085  1.00 21.34           C  
ATOM   1608  CD2 PHE B   8      48.490  13.911  54.713  1.00 19.02           C  
ATOM   1609  CE1 PHE B   8      50.500  12.195  53.869  1.00 27.76           C  
ATOM   1610  CE2 PHE B   8      48.368  13.247  53.497  1.00 24.08           C  
ATOM   1611  CZ  PHE B   8      49.376  12.386  53.073  1.00 25.17           C  
ATOM   1612  H   PHE B   8      50.107  12.625  58.910  1.00  0.00           H  
ATOM   1613  N   ASP B   9      51.984  16.085  58.633  1.00 18.07           N  
ATOM   1614  CA  ASP B   9      52.032  17.248  59.507  1.00 17.67           C  
ATOM   1615  C   ASP B   9      51.458  18.448  58.772  1.00 15.40           C  
ATOM   1616  O   ASP B   9      52.089  19.013  57.879  1.00 20.01           O  
ATOM   1617  CB  ASP B   9      53.474  17.539  59.955  1.00 25.55           C  
ATOM   1618  CG  ASP B   9      53.968  16.567  61.016  1.00 28.30           C  
ATOM   1619  OD1 ASP B   9      53.142  16.085  61.818  1.00 29.83           O  
ATOM   1620  OD2 ASP B   9      55.184  16.280  61.042  1.00 29.78           O  
ATOM   1621  H   ASP B   9      52.606  15.985  57.899  1.00  0.00           H  
ATOM   1622  N   ILE B  10      50.231  18.802  59.121  1.00 16.95           N  
ATOM   1623  CA  ILE B  10      49.502  19.829  58.395  1.00 17.52           C  
ATOM   1624  C   ILE B  10      49.852  21.226  58.904  1.00 19.34           C  
ATOM   1625  O   ILE B  10      50.043  21.434  60.104  1.00 26.85           O  
ATOM   1626  CB  ILE B  10      47.973  19.600  58.502  1.00 15.59           C  
ATOM   1627  CG1 ILE B  10      47.622  18.172  58.062  1.00  9.92           C  
ATOM   1628  CG2 ILE B  10      47.224  20.624  57.659  1.00 18.72           C  
ATOM   1629  CD1 ILE B  10      47.877  17.887  56.591  1.00  5.27           C  
ATOM   1630  H   ILE B  10      49.824  18.353  59.894  1.00  0.00           H  
ATOM   1631  N   ALA B  11      50.010  22.158  57.972  1.00 17.20           N  
ATOM   1632  CA  ALA B  11      50.288  23.547  58.305  1.00 15.81           C  
ATOM   1633  C   ALA B  11      49.293  24.468  57.615  1.00 18.26           C  
ATOM   1634  O   ALA B  11      48.791  24.160  56.535  1.00 29.08           O  
ATOM   1635  CB  ALA B  11      51.707  23.912  57.900  1.00 10.85           C  
ATOM   1636  H   ALA B  11      49.937  21.887  57.030  1.00  0.00           H  
ATOM   1637  N   VAL B  12      48.937  25.549  58.296  1.00 21.12           N  
ATOM   1638  CA  VAL B  12      48.034  26.556  57.756  1.00 24.33           C  
ATOM   1639  C   VAL B  12      48.805  27.861  57.600  1.00 31.10           C  
ATOM   1640  O   VAL B  12      49.275  28.432  58.582  1.00 40.61           O  
ATOM   1641  CB  VAL B  12      46.838  26.790  58.700  1.00 21.88           C  
ATOM   1642  CG1 VAL B  12      45.885  27.795  58.093  1.00 25.78           C  
ATOM   1643  CG2 VAL B  12      46.119  25.476  58.978  1.00 23.19           C  
ATOM   1644  H   VAL B  12      49.279  25.655  59.203  1.00  0.00           H  
ATOM   1645  N   ASP B  13      49.033  28.269  56.356  1.00 34.37           N  
ATOM   1646  CA  ASP B  13      49.885  29.423  56.066  1.00 36.72           C  
ATOM   1647  C   ASP B  13      51.243  29.364  56.776  1.00 34.58           C  
ATOM   1648  O   ASP B  13      51.749  30.380  57.252  1.00 35.02           O  
ATOM   1649  CB  ASP B  13      49.164  30.720  56.441  1.00 41.27           C  
ATOM   1650  CG  ASP B  13      48.246  31.214  55.345  1.00 52.34           C  
ATOM   1651  OD1 ASP B  13      48.664  31.206  54.167  1.00 61.29           O  
ATOM   1652  OD2 ASP B  13      47.118  31.642  55.665  1.00 55.77           O  
ATOM   1653  H   ASP B  13      48.544  27.805  55.646  1.00  0.00           H  
ATOM   1654  N   GLY B  14      51.808  28.165  56.877  1.00 30.22           N  
ATOM   1655  CA  GLY B  14      53.083  28.005  57.554  1.00 34.49           C  
ATOM   1656  C   GLY B  14      52.978  27.646  59.026  1.00 37.01           C  
ATOM   1657  O   GLY B  14      53.825  26.925  59.552  1.00 40.51           O  
ATOM   1658  H   GLY B  14      51.390  27.385  56.460  1.00  0.00           H  
ATOM   1659  N   GLU B  15      51.967  28.179  59.705  1.00 39.83           N  
ATOM   1660  CA  GLU B  15      51.779  27.896  61.124  1.00 38.99           C  
ATOM   1661  C   GLU B  15      51.330  26.454  61.317  1.00 37.83           C  
ATOM   1662  O   GLU B  15      50.483  25.953  60.577  1.00 40.50           O  
ATOM   1663  CB  GLU B  15      50.747  28.850  61.734  1.00 40.14           C  
ATOM   1664  CG  GLU B  15      51.227  30.286  61.868  0.00 43.31           C  
ATOM   1665  CD  GLU B  15      50.180  31.198  62.479  0.00 43.73           C  
ATOM   1666  OE1 GLU B  15      49.778  30.958  63.637  0.00 44.41           O  
ATOM   1667  OE2 GLU B  15      49.771  32.167  61.806  0.00 46.47           O  
ATOM   1668  H   GLU B  15      51.331  28.763  59.243  1.00  0.00           H  
ATOM   1669  N   PRO B  16      51.971  25.733  62.245  1.00 34.69           N  
ATOM   1670  CA  PRO B  16      51.568  24.356  62.540  1.00 30.42           C  
ATOM   1671  C   PRO B  16      50.099  24.214  62.931  1.00 27.25           C  
ATOM   1672  O   PRO B  16      49.536  25.074  63.610  1.00 31.74           O  
ATOM   1673  CB  PRO B  16      52.500  23.959  63.678  1.00 26.85           C  
ATOM   1674  CG  PRO B  16      53.740  24.738  63.394  1.00 30.89           C  
ATOM   1675  CD  PRO B  16      53.259  26.068  62.880  1.00 31.47           C  
ATOM   1676  N   LEU B  17      49.484  23.124  62.492  1.00 23.46           N  
ATOM   1677  CA  LEU B  17      48.133  22.785  62.918  1.00 25.40           C  
ATOM   1678  C   LEU B  17      48.131  21.502  63.753  1.00 21.26           C  
ATOM   1679  O   LEU B  17      47.672  21.491  64.894  1.00 26.02           O  
ATOM   1680  CB  LEU B  17      47.221  22.624  61.696  1.00 29.32           C  
ATOM   1681  CG  LEU B  17      45.728  22.381  61.946  1.00 27.12           C  
ATOM   1682  CD1 LEU B  17      45.069  23.657  62.444  1.00 23.72           C  
ATOM   1683  CD2 LEU B  17      45.066  21.914  60.660  1.00 31.65           C  
ATOM   1684  H   LEU B  17      49.917  22.615  61.771  1.00  0.00           H  
ATOM   1685  N   GLY B  18      48.710  20.441  63.207  1.00 21.57           N  
ATOM   1686  CA  GLY B  18      48.737  19.174  63.914  1.00 18.80           C  
ATOM   1687  C   GLY B  18      49.120  18.013  63.021  1.00 16.98           C  
ATOM   1688  O   GLY B  18      49.500  18.211  61.870  1.00 21.27           O  
ATOM   1689  H   GLY B  18      49.084  20.513  62.300  1.00  0.00           H  
ATOM   1690  N   ARG B  19      48.975  16.798  63.535  1.00 16.16           N  
ATOM   1691  CA  ARG B  19      49.338  15.604  62.785  1.00 18.95           C  
ATOM   1692  C   ARG B  19      48.141  14.684  62.570  1.00 22.89           C  
ATOM   1693  O   ARG B  19      47.370  14.431  63.500  1.00 24.98           O  
ATOM   1694  CB  ARG B  19      50.451  14.839  63.510  1.00 13.06           C  
ATOM   1695  CG  ARG B  19      50.924  13.590  62.784  1.00 10.98           C  
ATOM   1696  CD  ARG B  19      52.118  12.938  63.476  1.00 19.48           C  
ATOM   1697  NE  ARG B  19      53.355  13.694  63.273  1.00 23.55           N  
ATOM   1698  CZ  ARG B  19      54.580  13.178  63.349  1.00 16.82           C  
ATOM   1699  NH1 ARG B  19      54.755  11.889  63.616  1.00 18.86           N  
ATOM   1700  NH2 ARG B  19      55.633  13.946  63.115  1.00  9.49           N  
ATOM   1701  H   ARG B  19      48.440  16.702  64.343  1.00  0.00           H  
ATOM   1702  HE  ARG B  19      53.284  14.657  63.171  1.00  0.00           H  
ATOM   1703 HH11 ARG B  19      53.968  11.289  63.759  1.00  0.00           H  
ATOM   1704 HH12 ARG B  19      55.681  11.517  63.680  1.00  0.00           H  
ATOM   1705 HH21 ARG B  19      55.502  14.906  62.867  1.00  0.00           H  
ATOM   1706 HH22 ARG B  19      56.555  13.564  63.178  1.00  0.00           H  
ATOM   1707  N   VAL B  20      47.969  14.233  61.329  1.00 21.32           N  
ATOM   1708  CA  VAL B  20      47.012  13.176  61.006  1.00 17.09           C  
ATOM   1709  C   VAL B  20      47.778  11.921  60.608  1.00 11.83           C  
ATOM   1710  O   VAL B  20      48.710  11.985  59.815  1.00 18.51           O  
ATOM   1711  CB  VAL B  20      46.087  13.572  59.818  1.00 21.69           C  
ATOM   1712  CG1 VAL B  20      44.884  12.629  59.757  1.00 14.23           C  
ATOM   1713  CG2 VAL B  20      45.622  15.017  59.954  1.00 18.59           C  
ATOM   1714  H   VAL B  20      48.543  14.605  60.629  1.00  0.00           H  
ATOM   1715  N   SER B  21      47.409  10.785  61.179  1.00 12.98           N  
ATOM   1716  CA  SER B  21      47.991   9.514  60.767  1.00 14.17           C  
ATOM   1717  C   SER B  21      46.955   8.611  60.111  1.00 16.10           C  
ATOM   1718  O   SER B  21      45.754   8.752  60.346  1.00 15.78           O  
ATOM   1719  CB  SER B  21      48.632   8.796  61.960  1.00 18.71           C  
ATOM   1720  OG  SER B  21      47.701   8.582  63.008  1.00 31.46           O  
ATOM   1721  H   SER B  21      46.737  10.814  61.886  1.00  0.00           H  
ATOM   1722  HG  SER B  21      48.201   8.139  63.705  1.00  0.00           H  
ATOM   1723  N   PHE B  22      47.423   7.715  59.250  1.00 15.27           N  
ATOM   1724  CA  PHE B  22      46.540   6.865  58.461  1.00 11.27           C  
ATOM   1725  C   PHE B  22      46.989   5.418  58.560  1.00 15.52           C  
ATOM   1726  O   PHE B  22      48.186   5.136  58.560  1.00 17.16           O  
ATOM   1727  CB  PHE B  22      46.567   7.279  56.980  1.00 12.35           C  
ATOM   1728  CG  PHE B  22      46.362   8.750  56.745  1.00  7.79           C  
ATOM   1729  CD1 PHE B  22      45.083   9.268  56.574  1.00  5.69           C  
ATOM   1730  CD2 PHE B  22      47.453   9.608  56.643  1.00  2.00           C  
ATOM   1731  CE1 PHE B  22      44.895  10.622  56.302  1.00  2.87           C  
ATOM   1732  CE2 PHE B  22      47.277  10.961  56.372  1.00  3.39           C  
ATOM   1733  CZ  PHE B  22      45.996  11.472  56.201  1.00  2.00           C  
ATOM   1734  H   PHE B  22      48.390   7.640  59.138  1.00  0.00           H  
ATOM   1735  N   GLU B  23      46.028   4.500  58.604  1.00 17.31           N  
ATOM   1736  CA  GLU B  23      46.322   3.095  58.354  1.00 19.94           C  
ATOM   1737  C   GLU B  23      46.030   2.766  56.894  1.00 19.44           C  
ATOM   1738  O   GLU B  23      44.995   3.161  56.363  1.00 26.74           O  
ATOM   1739  CB  GLU B  23      45.481   2.194  59.254  1.00 20.09           C  
ATOM   1740  CG  GLU B  23      45.827   0.711  59.106  1.00 30.84           C  
ATOM   1741  CD  GLU B  23      44.683  -0.219  59.487  1.00 35.34           C  
ATOM   1742  OE1 GLU B  23      43.633   0.273  59.963  1.00 39.50           O  
ATOM   1743  OE2 GLU B  23      44.836  -1.449  59.302  1.00 27.43           O  
ATOM   1744  H   GLU B  23      45.111   4.788  58.785  1.00  0.00           H  
ATOM   1745  N   LEU B  24      46.952   2.067  56.244  1.00 19.36           N  
ATOM   1746  CA  LEU B  24      46.795   1.719  54.836  1.00 13.25           C  
ATOM   1747  C   LEU B  24      46.506   0.237  54.678  1.00 16.61           C  
ATOM   1748  O   LEU B  24      47.283  -0.611  55.122  1.00 25.35           O  
ATOM   1749  CB  LEU B  24      48.054   2.083  54.047  1.00 12.87           C  
ATOM   1750  CG  LEU B  24      48.545   3.530  54.121  1.00  8.95           C  
ATOM   1751  CD1 LEU B  24      49.748   3.685  53.209  1.00  7.69           C  
ATOM   1752  CD2 LEU B  24      47.439   4.487  53.707  1.00 12.26           C  
ATOM   1753  H   LEU B  24      47.780   1.843  56.721  1.00  0.00           H  
ATOM   1754  N   PHE B  25      45.385  -0.077  54.043  1.00 19.81           N  
ATOM   1755  CA  PHE B  25      44.929  -1.458  53.943  1.00 23.14           C  
ATOM   1756  C   PHE B  25      45.640  -2.212  52.825  1.00 27.11           C  
ATOM   1757  O   PHE B  25      45.010  -2.692  51.880  1.00 32.88           O  
ATOM   1758  CB  PHE B  25      43.413  -1.498  53.736  1.00 19.27           C  
ATOM   1759  CG  PHE B  25      42.646  -0.698  54.749  1.00 19.03           C  
ATOM   1760  CD1 PHE B  25      42.832  -0.914  56.111  1.00 13.20           C  
ATOM   1761  CD2 PHE B  25      41.763   0.295  54.343  1.00 16.18           C  
ATOM   1762  CE1 PHE B  25      42.159  -0.154  57.049  1.00  7.50           C  
ATOM   1763  CE2 PHE B  25      41.080   1.062  55.277  1.00 17.95           C  
ATOM   1764  CZ  PHE B  25      41.281   0.839  56.634  1.00 18.79           C  
ATOM   1765  H   PHE B  25      44.884   0.654  53.624  1.00  0.00           H  
ATOM   1766  N   ALA B  26      46.938  -2.428  53.011  1.00 23.91           N  
ATOM   1767  CA  ALA B  26      47.741  -3.155  52.035  1.00 18.42           C  
ATOM   1768  C   ALA B  26      47.310  -4.617  51.938  1.00 17.14           C  
ATOM   1769  O   ALA B  26      47.597  -5.295  50.951  1.00 18.87           O  
ATOM   1770  CB  ALA B  26      49.210  -3.059  52.399  1.00 19.86           C  
ATOM   1771  H   ALA B  26      47.353  -2.073  53.823  1.00  0.00           H  
ATOM   1772  N   ASP B  27      46.574  -5.080  52.943  1.00 10.86           N  
ATOM   1773  CA  ASP B  27      46.009  -6.430  52.916  1.00 17.46           C  
ATOM   1774  C   ASP B  27      44.829  -6.562  51.943  1.00 18.68           C  
ATOM   1775  O   ASP B  27      44.459  -7.667  51.550  1.00 19.91           O  
ATOM   1776  CB  ASP B  27      45.591  -6.865  54.332  1.00 16.37           C  
ATOM   1777  CG  ASP B  27      44.512  -5.967  54.947  1.00 27.02           C  
ATOM   1778  OD1 ASP B  27      44.373  -4.787  54.550  1.00 23.46           O  
ATOM   1779  OD2 ASP B  27      43.822  -6.443  55.877  1.00 35.82           O  
ATOM   1780  H   ASP B  27      46.534  -4.543  53.757  1.00  0.00           H  
ATOM   1781  N   LYS B  28      44.250  -5.431  51.556  1.00 22.86           N  
ATOM   1782  CA  LYS B  28      43.125  -5.416  50.616  1.00 27.76           C  
ATOM   1783  C   LYS B  28      43.532  -4.802  49.277  1.00 27.25           C  
ATOM   1784  O   LYS B  28      43.160  -5.295  48.212  1.00 27.47           O  
ATOM   1785  CB  LYS B  28      41.953  -4.615  51.198  1.00 31.92           C  
ATOM   1786  CG  LYS B  28      41.384  -5.169  52.495  1.00 36.06           C  
ATOM   1787  CD  LYS B  28      40.591  -6.441  52.255  1.00 33.60           C  
ATOM   1788  CE  LYS B  28      40.099  -7.035  53.560  1.00 38.99           C  
ATOM   1789  NZ  LYS B  28      41.221  -7.592  54.365  1.00 47.59           N  
ATOM   1790  H   LYS B  28      44.585  -4.601  51.943  1.00  0.00           H  
ATOM   1791  HZ1 LYS B  28      41.712  -8.301  53.790  1.00  0.00           H  
ATOM   1792  HZ2 LYS B  28      41.884  -6.831  54.622  1.00  0.00           H  
ATOM   1793  HZ3 LYS B  28      40.852  -8.037  55.231  1.00  0.00           H  
ATOM   1794  N   VAL B  29      44.277  -3.703  49.347  1.00 25.33           N  
ATOM   1795  CA  VAL B  29      44.724  -2.979  48.160  1.00 17.81           C  
ATOM   1796  C   VAL B  29      46.220  -2.649  48.212  1.00 16.57           C  
ATOM   1797  O   VAL B  29      46.614  -1.485  48.356  1.00 17.29           O  
ATOM   1798  CB  VAL B  29      43.919  -1.667  47.969  1.00 16.97           C  
ATOM   1799  CG1 VAL B  29      42.559  -1.976  47.375  1.00 25.00           C  
ATOM   1800  CG2 VAL B  29      43.763  -0.948  49.293  1.00 15.72           C  
ATOM   1801  H   VAL B  29      44.483  -3.368  50.237  1.00  0.00           H  
ATOM   1802  N   PRO B  30      47.075  -3.668  48.043  1.00 14.29           N  
ATOM   1803  CA  PRO B  30      48.521  -3.494  48.212  1.00 17.20           C  
ATOM   1804  C   PRO B  30      49.149  -2.449  47.289  1.00 20.87           C  
ATOM   1805  O   PRO B  30      49.840  -1.543  47.751  1.00 27.42           O  
ATOM   1806  CB  PRO B  30      49.093  -4.898  47.964  1.00 16.26           C  
ATOM   1807  CG  PRO B  30      47.965  -5.722  47.450  1.00 12.59           C  
ATOM   1808  CD  PRO B  30      46.714  -5.092  47.968  1.00 16.18           C  
ATOM   1809  N   LYS B  31      48.835  -2.526  46.000  1.00 24.82           N  
ATOM   1810  CA  LYS B  31      49.409  -1.614  45.008  1.00 23.21           C  
ATOM   1811  C   LYS B  31      49.030  -0.147  45.250  1.00 21.08           C  
ATOM   1812  O   LYS B  31      49.836   0.756  45.036  1.00 30.74           O  
ATOM   1813  CB  LYS B  31      48.975  -2.043  43.601  1.00 26.41           C  
ATOM   1814  CG  LYS B  31      49.736  -1.366  42.479  1.00 37.02           C  
ATOM   1815  CD  LYS B  31      49.337  -1.909  41.119  1.00 44.17           C  
ATOM   1816  CE  LYS B  31      50.096  -1.204  40.004  1.00 42.13           C  
ATOM   1817  NZ  LYS B  31      49.534  -1.533  38.665  1.00 52.29           N  
ATOM   1818  H   LYS B  31      48.264  -3.266  45.719  1.00  0.00           H  
ATOM   1819  HZ1 LYS B  31      48.515  -1.337  38.666  1.00  0.00           H  
ATOM   1820  HZ2 LYS B  31      49.999  -0.956  37.935  1.00  0.00           H  
ATOM   1821  HZ3 LYS B  31      49.692  -2.541  38.462  1.00  0.00           H  
ATOM   1822  N   THR B  32      47.830   0.075  45.774  1.00 23.36           N  
ATOM   1823  CA  THR B  32      47.327   1.427  46.031  1.00 19.31           C  
ATOM   1824  C   THR B  32      47.845   1.978  47.367  1.00 18.79           C  
ATOM   1825  O   THR B  32      48.215   3.150  47.467  1.00 15.05           O  
ATOM   1826  CB  THR B  32      45.782   1.440  46.037  1.00 17.78           C  
ATOM   1827  OG1 THR B  32      45.298   0.636  44.952  1.00 13.07           O  
ATOM   1828  CG2 THR B  32      45.257   2.846  45.884  1.00  8.43           C  
ATOM   1829  H   THR B  32      47.289  -0.700  46.007  1.00  0.00           H  
ATOM   1830  HG1 THR B  32      44.762  -0.070  45.334  1.00  0.00           H  
ATOM   1831  N   ALA B  33      47.920   1.108  48.372  1.00 18.13           N  
ATOM   1832  CA  ALA B  33      48.545   1.436  49.653  1.00 14.49           C  
ATOM   1833  C   ALA B  33      50.040   1.741  49.492  1.00 15.32           C  
ATOM   1834  O   ALA B  33      50.534   2.756  49.988  1.00 16.20           O  
ATOM   1835  CB  ALA B  33      48.352   0.282  50.629  1.00 12.15           C  
ATOM   1836  H   ALA B  33      47.530   0.219  48.254  1.00  0.00           H  
ATOM   1837  N   GLU B  34      50.729   0.909  48.714  1.00 10.49           N  
ATOM   1838  CA  GLU B  34      52.146   1.100  48.420  1.00 11.19           C  
ATOM   1839  C   GLU B  34      52.449   2.431  47.734  1.00 13.78           C  
ATOM   1840  O   GLU B  34      53.351   3.163  48.157  1.00 19.09           O  
ATOM   1841  CB  GLU B  34      52.665  -0.059  47.568  1.00 14.18           C  
ATOM   1842  CG  GLU B  34      54.134   0.052  47.152  1.00 28.15           C  
ATOM   1843  CD  GLU B  34      55.112   0.172  48.325  1.00 28.16           C  
ATOM   1844  OE1 GLU B  34      54.822  -0.332  49.433  1.00 27.52           O  
ATOM   1845  OE2 GLU B  34      56.204   0.740  48.115  1.00 32.73           O  
ATOM   1846  H   GLU B  34      50.269   0.116  48.390  1.00  0.00           H  
ATOM   1847  N   ASN B  35      51.651   2.786  46.732  1.00 12.22           N  
ATOM   1848  CA  ASN B  35      51.796   4.087  46.078  1.00 13.33           C  
ATOM   1849  C   ASN B  35      51.750   5.240  47.085  1.00  9.04           C  
ATOM   1850  O   ASN B  35      52.644   6.084  47.118  1.00 18.84           O  
ATOM   1851  CB  ASN B  35      50.701   4.286  45.018  1.00  8.09           C  
ATOM   1852  CG  ASN B  35      50.883   5.569  44.233  1.00 13.39           C  
ATOM   1853  OD1 ASN B  35      51.904   5.763  43.582  1.00 13.49           O  
ATOM   1854  ND2 ASN B  35      49.922   6.473  44.334  1.00 12.20           N  
ATOM   1855  H   ASN B  35      50.986   2.140  46.413  1.00  0.00           H  
ATOM   1856 HD21 ASN B  35      50.009   7.267  43.768  1.00  0.00           H  
ATOM   1857 HD22 ASN B  35      49.165   6.285  44.925  1.00  0.00           H  
ATOM   1858  N   PHE B  36      50.728   5.241  47.934  1.00 15.36           N  
ATOM   1859  CA  PHE B  36      50.548   6.305  48.920  1.00 12.93           C  
ATOM   1860  C   PHE B  36      51.663   6.323  49.970  1.00  8.06           C  
ATOM   1861  O   PHE B  36      52.173   7.389  50.324  1.00 13.96           O  
ATOM   1862  CB  PHE B  36      49.189   6.155  49.604  1.00  7.88           C  
ATOM   1863  CG  PHE B  36      48.801   7.334  50.452  1.00 11.56           C  
ATOM   1864  CD1 PHE B  36      48.146   8.426  49.890  1.00  6.14           C  
ATOM   1865  CD2 PHE B  36      49.080   7.348  51.819  1.00 10.39           C  
ATOM   1866  CE1 PHE B  36      47.775   9.510  50.673  1.00 14.01           C  
ATOM   1867  CE2 PHE B  36      48.715   8.434  52.613  1.00  6.49           C  
ATOM   1868  CZ  PHE B  36      48.061   9.515  52.041  1.00 10.89           C  
ATOM   1869  H   PHE B  36      50.056   4.533  47.849  1.00  0.00           H  
ATOM   1870  N   ARG B  37      52.043   5.142  50.453  1.00 12.83           N  
ATOM   1871  CA  ARG B  37      53.116   5.000  51.444  1.00 18.24           C  
ATOM   1872  C   ARG B  37      54.450   5.578  50.956  1.00 21.15           C  
ATOM   1873  O   ARG B  37      55.014   6.483  51.583  1.00 24.36           O  
ATOM   1874  CB  ARG B  37      53.303   3.524  51.808  1.00 18.51           C  
ATOM   1875  CG  ARG B  37      54.293   3.277  52.940  1.00 15.52           C  
ATOM   1876  CD  ARG B  37      54.831   1.850  52.905  1.00 16.16           C  
ATOM   1877  NE  ARG B  37      55.629   1.600  51.706  1.00 22.68           N  
ATOM   1878  CZ  ARG B  37      56.840   2.109  51.492  1.00 24.47           C  
ATOM   1879  NH1 ARG B  37      57.461   2.779  52.453  1.00 22.68           N  
ATOM   1880  NH2 ARG B  37      57.454   1.905  50.334  1.00 25.52           N  
ATOM   1881  H   ARG B  37      51.554   4.353  50.146  1.00  0.00           H  
ATOM   1882  HE  ARG B  37      55.249   1.024  51.012  1.00  0.00           H  
ATOM   1883 HH11 ARG B  37      57.028   2.906  53.344  1.00  0.00           H  
ATOM   1884 HH12 ARG B  37      58.370   3.161  52.283  1.00  0.00           H  
ATOM   1885 HH21 ARG B  37      57.020   1.338  49.646  1.00  0.00           H  
ATOM   1886 HH22 ARG B  37      58.362   2.291  50.170  1.00  0.00           H  
ATOM   1887  N   ALA B  38      54.895   5.124  49.786  1.00 21.81           N  
ATOM   1888  CA  ALA B  38      56.157   5.583  49.203  1.00 15.85           C  
ATOM   1889  C   ALA B  38      56.164   7.083  48.894  1.00 18.82           C  
ATOM   1890  O   ALA B  38      57.190   7.756  49.052  1.00 21.16           O  
ATOM   1891  CB  ALA B  38      56.471   4.785  47.945  1.00 15.53           C  
ATOM   1892  H   ALA B  38      54.352   4.457  49.313  1.00  0.00           H  
ATOM   1893  N   LEU B  39      55.010   7.621  48.507  1.00 17.02           N  
ATOM   1894  CA  LEU B  39      54.884   9.059  48.258  1.00 18.76           C  
ATOM   1895  C   LEU B  39      54.879   9.878  49.554  1.00 19.12           C  
ATOM   1896  O   LEU B  39      55.143  11.084  49.544  1.00 17.98           O  
ATOM   1897  CB  LEU B  39      53.607   9.353  47.458  1.00 18.48           C  
ATOM   1898  CG  LEU B  39      53.529   8.861  46.005  1.00 21.06           C  
ATOM   1899  CD1 LEU B  39      52.141   9.135  45.451  1.00  8.90           C  
ATOM   1900  CD2 LEU B  39      54.589   9.544  45.151  1.00 13.92           C  
ATOM   1901  H   LEU B  39      54.254   7.024  48.307  1.00  0.00           H  
ATOM   1902  N   SER B  40      54.552   9.221  50.663  1.00 21.44           N  
ATOM   1903  CA  SER B  40      54.569   9.864  51.976  1.00 19.93           C  
ATOM   1904  C   SER B  40      55.965   9.885  52.585  1.00 15.93           C  
ATOM   1905  O   SER B  40      56.341  10.850  53.243  1.00 18.73           O  
ATOM   1906  CB  SER B  40      53.607   9.156  52.930  1.00 14.29           C  
ATOM   1907  OG  SER B  40      52.271   9.271  52.472  1.00 18.60           O  
ATOM   1908  H   SER B  40      54.220   8.302  50.572  1.00  0.00           H  
ATOM   1909  HG  SER B  40      52.156   8.774  51.647  1.00  0.00           H  
ATOM   1910  N   THR B  41      56.741   8.834  52.337  1.00 17.02           N  
ATOM   1911  CA  THR B  41      58.134   8.782  52.789  1.00 18.33           C  
ATOM   1912  C   THR B  41      59.095   9.551  51.882  1.00 20.57           C  
ATOM   1913  O   THR B  41      60.186   9.914  52.303  1.00 26.19           O  
ATOM   1914  CB  THR B  41      58.653   7.344  52.876  1.00 17.48           C  
ATOM   1915  OG1 THR B  41      58.801   6.812  51.553  1.00 22.58           O  
ATOM   1916  CG2 THR B  41      57.694   6.471  53.674  1.00 10.27           C  
ATOM   1917  H   THR B  41      56.346   8.068  51.864  1.00  0.00           H  
ATOM   1918  HG1 THR B  41      59.369   6.053  51.667  1.00  0.00           H  
ATOM   1919  N   GLY B  42      58.734   9.693  50.610  1.00 27.05           N  
ATOM   1920  CA  GLY B  42      59.556  10.459  49.685  1.00 23.42           C  
ATOM   1921  C   GLY B  42      60.758   9.693  49.157  1.00 28.70           C  
ATOM   1922  O   GLY B  42      61.630  10.265  48.499  1.00 32.46           O  
ATOM   1923  H   GLY B  42      57.910   9.259  50.312  1.00  0.00           H  
ATOM   1924  N   GLU B  43      60.734   8.375  49.324  1.00 25.72           N  
ATOM   1925  CA  GLU B  43      61.857   7.523  48.945  1.00 21.87           C  
ATOM   1926  C   GLU B  43      62.140   7.439  47.442  1.00 27.01           C  
ATOM   1927  O   GLU B  43      63.149   6.866  47.032  1.00 28.94           O  
ATOM   1928  CB  GLU B  43      61.659   6.117  49.513  1.00 19.29           C  
ATOM   1929  CG  GLU B  43      60.340   5.459  49.156  1.00 19.95           C  
ATOM   1930  CD  GLU B  43      60.113   4.178  49.929  1.00 19.92           C  
ATOM   1931  OE1 GLU B  43      59.823   4.256  51.139  1.00 24.36           O  
ATOM   1932  OE2 GLU B  43      60.244   3.089  49.336  1.00 27.42           O  
ATOM   1933  H   GLU B  43      59.938   8.002  49.755  1.00  0.00           H  
ATOM   1934  N   LYS B  44      61.262   8.017  46.628  1.00 25.88           N  
ATOM   1935  CA  LYS B  44      61.449   8.026  45.176  1.00 22.20           C  
ATOM   1936  C   LYS B  44      62.069   9.338  44.700  1.00 23.13           C  
ATOM   1937  O   LYS B  44      62.367   9.505  43.514  1.00 24.43           O  
ATOM   1938  CB  LYS B  44      60.109   7.812  44.460  1.00 24.21           C  
ATOM   1939  CG  LYS B  44      59.300   6.624  44.956  1.00 23.07           C  
ATOM   1940  CD  LYS B  44      59.926   5.309  44.540  1.00 23.05           C  
ATOM   1941  CE  LYS B  44      59.235   4.149  45.232  1.00 29.49           C  
ATOM   1942  NZ  LYS B  44      59.831   2.839  44.857  1.00 33.61           N  
ATOM   1943  H   LYS B  44      60.436   8.392  47.002  1.00  0.00           H  
ATOM   1944  HZ1 LYS B  44      59.766   2.702  43.830  1.00  0.00           H  
ATOM   1945  HZ2 LYS B  44      60.828   2.823  45.152  1.00  0.00           H  
ATOM   1946  HZ3 LYS B  44      59.316   2.080  45.347  1.00  0.00           H  
ATOM   1947  N   GLY B  45      62.222  10.284  45.622  1.00 20.76           N  
ATOM   1948  CA  GLY B  45      62.763  11.583  45.268  1.00 13.64           C  
ATOM   1949  C   GLY B  45      61.695  12.643  45.082  1.00 18.37           C  
ATOM   1950  O   GLY B  45      62.002  13.827  44.926  1.00 27.28           O  
ATOM   1951  H   GLY B  45      61.990  10.084  46.553  1.00  0.00           H  
ATOM   1952  N   PHE B  46      60.438  12.214  45.066  1.00 15.81           N  
ATOM   1953  CA  PHE B  46      59.301  13.125  44.953  1.00 18.37           C  
ATOM   1954  C   PHE B  46      58.137  12.605  45.806  1.00 20.18           C  
ATOM   1955  O   PHE B  46      58.142  11.446  46.229  1.00 16.07           O  
ATOM   1956  CB  PHE B  46      58.866  13.257  43.484  1.00  9.78           C  
ATOM   1957  CG  PHE B  46      58.553  11.943  42.826  1.00  6.27           C  
ATOM   1958  CD1 PHE B  46      57.295  11.370  42.953  1.00 14.96           C  
ATOM   1959  CD2 PHE B  46      59.546  11.230  42.169  1.00 16.01           C  
ATOM   1960  CE1 PHE B  46      57.032  10.103  42.449  1.00  8.15           C  
ATOM   1961  CE2 PHE B  46      59.292   9.962  41.658  1.00 13.35           C  
ATOM   1962  CZ  PHE B  46      58.032   9.397  41.803  1.00 16.78           C  
ATOM   1963  H   PHE B  46      60.273  11.255  45.136  1.00  0.00           H  
ATOM   1964  N   GLY B  47      57.164  13.465  46.089  1.00 18.20           N  
ATOM   1965  CA  GLY B  47      56.005  13.032  46.849  1.00 14.03           C  
ATOM   1966  C   GLY B  47      55.233  14.149  47.524  1.00 15.66           C  
ATOM   1967  O   GLY B  47      55.382  15.328  47.178  1.00 13.74           O  
ATOM   1968  H   GLY B  47      57.277  14.394  45.820  1.00  0.00           H  
ATOM   1969  N   TYR B  48      54.478  13.785  48.557  1.00 20.15           N  
ATOM   1970  CA  TYR B  48      53.487  14.680  49.155  1.00 16.86           C  
ATOM   1971  C   TYR B  48      54.072  15.836  49.967  1.00 18.27           C  
ATOM   1972  O   TYR B  48      53.435  16.878  50.107  1.00 19.22           O  
ATOM   1973  CB  TYR B  48      52.519  13.887  50.041  1.00 14.21           C  
ATOM   1974  CG  TYR B  48      51.706  12.838  49.314  1.00  4.74           C  
ATOM   1975  CD1 TYR B  48      51.059  13.132  48.112  1.00 11.92           C  
ATOM   1976  CD2 TYR B  48      51.549  11.561  49.851  1.00  9.24           C  
ATOM   1977  CE1 TYR B  48      50.269  12.172  47.465  1.00 12.76           C  
ATOM   1978  CE2 TYR B  48      50.774  10.598  49.219  1.00  9.33           C  
ATOM   1979  CZ  TYR B  48      50.133  10.907  48.025  1.00 15.64           C  
ATOM   1980  OH  TYR B  48      49.377   9.944  47.393  1.00 14.96           O  
ATOM   1981  H   TYR B  48      54.628  12.890  48.938  1.00  0.00           H  
ATOM   1982  HH  TYR B  48      48.817  10.374  46.736  1.00  0.00           H  
ATOM   1983  N   LYS B  49      55.258  15.643  50.538  1.00 22.55           N  
ATOM   1984  CA  LYS B  49      55.840  16.645  51.433  1.00 21.83           C  
ATOM   1985  C   LYS B  49      56.001  18.011  50.772  1.00 15.57           C  
ATOM   1986  O   LYS B  49      56.689  18.151  49.763  1.00 21.59           O  
ATOM   1987  CB  LYS B  49      57.191  16.168  51.972  1.00 28.14           C  
ATOM   1988  CG  LYS B  49      57.833  17.138  52.955  1.00 33.63           C  
ATOM   1989  CD  LYS B  49      59.141  16.592  53.493  1.00 42.55           C  
ATOM   1990  CE  LYS B  49      59.840  17.613  54.373  1.00 39.57           C  
ATOM   1991  NZ  LYS B  49      61.024  17.022  55.053  1.00 46.14           N  
ATOM   1992  H   LYS B  49      55.717  14.792  50.391  1.00  0.00           H  
ATOM   1993  HZ1 LYS B  49      61.685  16.645  54.345  1.00  0.00           H  
ATOM   1994  HZ2 LYS B  49      61.502  17.755  55.616  1.00  0.00           H  
ATOM   1995  HZ3 LYS B  49      60.713  16.255  55.684  1.00  0.00           H  
ATOM   1996  N   GLY B  50      55.349  19.012  51.346  1.00 14.62           N  
ATOM   1997  CA  GLY B  50      55.377  20.349  50.781  1.00 10.92           C  
ATOM   1998  C   GLY B  50      54.148  20.654  49.942  1.00 17.32           C  
ATOM   1999  O   GLY B  50      53.864  21.813  49.637  1.00 20.51           O  
ATOM   2000  H   GLY B  50      54.874  18.824  52.171  1.00  0.00           H  
ATOM   2001  N   SER B  51      53.416  19.612  49.560  1.00 18.92           N  
ATOM   2002  CA  SER B  51      52.223  19.778  48.731  1.00 25.05           C  
ATOM   2003  C   SER B  51      51.038  20.312  49.537  1.00 19.18           C  
ATOM   2004  O   SER B  51      51.051  20.293  50.759  1.00 19.54           O  
ATOM   2005  CB  SER B  51      51.852  18.451  48.060  1.00 18.39           C  
ATOM   2006  OG  SER B  51      51.227  17.566  48.973  1.00 27.34           O  
ATOM   2007  H   SER B  51      53.717  18.732  49.846  1.00  0.00           H  
ATOM   2008  HG  SER B  51      51.774  17.465  49.765  1.00  0.00           H  
ATOM   2009  N   CYS B  52      50.037  20.844  48.847  1.00 25.31           N  
ATOM   2010  CA  CYS B  52      48.898  21.470  49.517  1.00 23.77           C  
ATOM   2011  C   CYS B  52      47.578  20.734  49.281  1.00 20.51           C  
ATOM   2012  O   CYS B  52      47.471  19.898  48.379  1.00 22.03           O  
ATOM   2013  CB  CYS B  52      48.757  22.926  49.059  1.00 25.55           C  
ATOM   2014  SG  CYS B  52      48.148  23.133  47.356  1.00 47.27           S  
ATOM   2015  H   CYS B  52      50.141  20.910  47.875  1.00  0.00           H  
ATOM   2016  N   PHE B  53      46.609  20.980  50.154  1.00 19.53           N  
ATOM   2017  CA  PHE B  53      45.227  20.577  49.918  1.00 18.55           C  
ATOM   2018  C   PHE B  53      44.517  21.666  49.123  1.00 19.37           C  
ATOM   2019  O   PHE B  53      44.229  22.742  49.646  1.00 20.56           O  
ATOM   2020  CB  PHE B  53      44.504  20.336  51.249  1.00 17.37           C  
ATOM   2021  CG  PHE B  53      44.821  19.009  51.876  1.00  8.61           C  
ATOM   2022  CD1 PHE B  53      45.999  18.828  52.590  1.00 10.56           C  
ATOM   2023  CD2 PHE B  53      43.978  17.919  51.690  1.00  9.06           C  
ATOM   2024  CE1 PHE B  53      46.336  17.577  53.105  1.00  3.04           C  
ATOM   2025  CE2 PHE B  53      44.306  16.662  52.198  1.00 10.99           C  
ATOM   2026  CZ  PHE B  53      45.491  16.492  52.908  1.00 12.79           C  
ATOM   2027  H   PHE B  53      46.835  21.373  51.015  1.00  0.00           H  
ATOM   2028  N   HIS B  54      44.332  21.415  47.831  1.00 20.43           N  
ATOM   2029  CA  HIS B  54      43.867  22.447  46.902  1.00 19.74           C  
ATOM   2030  C   HIS B  54      42.339  22.520  46.806  1.00 19.08           C  
ATOM   2031  O   HIS B  54      41.787  23.500  46.314  1.00 16.38           O  
ATOM   2032  CB  HIS B  54      44.464  22.212  45.507  1.00 15.10           C  
ATOM   2033  CG  HIS B  54      43.929  20.996  44.819  1.00  9.05           C  
ATOM   2034  ND1 HIS B  54      44.397  19.726  45.082  1.00  6.12           N  
ATOM   2035  CD2 HIS B  54      42.892  20.844  43.960  1.00  7.96           C  
ATOM   2036  CE1 HIS B  54      43.662  18.844  44.428  1.00  9.04           C  
ATOM   2037  NE2 HIS B  54      42.743  19.498  43.739  1.00  6.30           N  
ATOM   2038  H   HIS B  54      44.518  20.495  47.561  1.00  0.00           H  
ATOM   2039  HD1 HIS B  54      45.193  19.463  45.595  1.00  0.00           H  
ATOM   2040  HE2 HIS B  54      42.083  19.082  43.133  1.00  0.00           H  
ATOM   2041  N   ARG B  55      41.671  21.454  47.235  1.00 19.44           N  
ATOM   2042  CA  ARG B  55      40.219  21.360  47.131  1.00 24.73           C  
ATOM   2043  C   ARG B  55      39.626  20.774  48.414  1.00 26.11           C  
ATOM   2044  O   ARG B  55      39.858  19.608  48.738  1.00 25.67           O  
ATOM   2045  CB  ARG B  55      39.838  20.489  45.926  1.00 23.19           C  
ATOM   2046  CG  ARG B  55      38.347  20.258  45.751  1.00 24.51           C  
ATOM   2047  CD  ARG B  55      38.070  19.364  44.551  1.00 27.51           C  
ATOM   2048  NE  ARG B  55      36.639  19.205  44.296  1.00 13.30           N  
ATOM   2049  CZ  ARG B  55      36.025  18.029  44.203  1.00 18.77           C  
ATOM   2050  NH1 ARG B  55      36.701  16.907  44.403  1.00 24.22           N  
ATOM   2051  NH2 ARG B  55      34.725  17.975  43.951  1.00 17.32           N  
ATOM   2052  H   ARG B  55      42.156  20.735  47.686  1.00  0.00           H  
ATOM   2053  HE  ARG B  55      36.094  20.012  44.193  1.00  0.00           H  
ATOM   2054 HH11 ARG B  55      37.675  16.940  44.615  1.00  0.00           H  
ATOM   2055 HH12 ARG B  55      36.240  16.023  44.321  1.00  0.00           H  
ATOM   2056 HH21 ARG B  55      34.205  18.822  43.842  1.00  0.00           H  
ATOM   2057 HH22 ARG B  55      34.257  17.096  43.891  1.00  0.00           H  
ATOM   2058  N   ILE B  56      38.983  21.628  49.205  1.00 27.28           N  
ATOM   2059  CA  ILE B  56      38.345  21.204  50.452  1.00 26.57           C  
ATOM   2060  C   ILE B  56      36.879  21.637  50.502  1.00 21.62           C  
ATOM   2061  O   ILE B  56      36.574  22.832  50.497  1.00 18.39           O  
ATOM   2062  CB  ILE B  56      39.082  21.789  51.688  1.00 25.27           C  
ATOM   2063  CG1 ILE B  56      40.492  21.202  51.787  1.00 13.62           C  
ATOM   2064  CG2 ILE B  56      38.296  21.489  52.962  1.00 22.17           C  
ATOM   2065  CD1 ILE B  56      41.368  21.908  52.784  1.00  9.08           C  
ATOM   2066  H   ILE B  56      38.974  22.572  48.945  1.00  0.00           H  
ATOM   2067  N   ILE B  57      35.977  20.664  50.548  1.00 22.50           N  
ATOM   2068  CA  ILE B  57      34.545  20.957  50.590  1.00 23.95           C  
ATOM   2069  C   ILE B  57      33.912  20.506  51.910  1.00 21.04           C  
ATOM   2070  O   ILE B  57      33.838  19.307  52.206  1.00 22.84           O  
ATOM   2071  CB  ILE B  57      33.794  20.297  49.402  1.00 23.17           C  
ATOM   2072  CG1 ILE B  57      34.390  20.782  48.076  1.00 27.47           C  
ATOM   2073  CG2 ILE B  57      32.312  20.649  49.457  1.00 20.02           C  
ATOM   2074  CD1 ILE B  57      33.841  20.085  46.843  1.00 20.69           C  
ATOM   2075  H   ILE B  57      36.299  19.736  50.574  1.00  0.00           H  
ATOM   2076  N   PRO B  58      33.522  21.474  52.757  1.00 18.21           N  
ATOM   2077  CA  PRO B  58      32.918  21.205  54.067  1.00 23.25           C  
ATOM   2078  C   PRO B  58      31.738  20.233  54.007  1.00 26.32           C  
ATOM   2079  O   PRO B  58      30.821  20.401  53.205  1.00 34.80           O  
ATOM   2080  CB  PRO B  58      32.494  22.592  54.545  1.00 17.96           C  
ATOM   2081  CG  PRO B  58      33.486  23.504  53.908  1.00 10.96           C  
ATOM   2082  CD  PRO B  58      33.732  22.918  52.545  1.00 18.16           C  
ATOM   2083  N   GLY B  59      31.826  19.163  54.787  1.00 26.55           N  
ATOM   2084  CA  GLY B  59      30.777  18.158  54.800  1.00 23.29           C  
ATOM   2085  C   GLY B  59      30.963  17.068  53.762  1.00 27.03           C  
ATOM   2086  O   GLY B  59      30.221  16.087  53.743  1.00 33.95           O  
ATOM   2087  H   GLY B  59      32.597  19.079  55.368  1.00  0.00           H  
ATOM   2088  N   PHE B  60      31.961  17.232  52.900  1.00 23.82           N  
ATOM   2089  CA  PHE B  60      32.207  16.277  51.824  1.00 18.09           C  
ATOM   2090  C   PHE B  60      33.565  15.583  52.003  1.00 16.40           C  
ATOM   2091  O   PHE B  60      33.633  14.448  52.480  1.00 12.14           O  
ATOM   2092  CB  PHE B  60      32.126  17.006  50.468  1.00 16.99           C  
ATOM   2093  CG  PHE B  60      32.248  16.102  49.270  1.00  8.44           C  
ATOM   2094  CD1 PHE B  60      31.847  14.769  49.332  1.00 11.01           C  
ATOM   2095  CD2 PHE B  60      32.821  16.574  48.094  1.00  9.43           C  
ATOM   2096  CE1 PHE B  60      32.023  13.919  48.242  1.00 15.61           C  
ATOM   2097  CE2 PHE B  60      33.002  15.734  46.999  1.00  8.91           C  
ATOM   2098  CZ  PHE B  60      32.604  14.402  47.074  1.00  6.86           C  
ATOM   2099  H   PHE B  60      32.509  18.035  52.964  1.00  0.00           H  
ATOM   2100  N   MET B  61      34.646  16.279  51.661  1.00 18.89           N  
ATOM   2101  CA  MET B  61      35.990  15.711  51.785  1.00 15.69           C  
ATOM   2102  C   MET B  61      37.109  16.748  51.672  1.00 11.68           C  
ATOM   2103  O   MET B  61      36.879  17.895  51.279  1.00 14.67           O  
ATOM   2104  CB  MET B  61      36.198  14.606  50.740  1.00 14.88           C  
ATOM   2105  CG  MET B  61      35.947  15.040  49.301  1.00 19.26           C  
ATOM   2106  SD  MET B  61      37.377  15.793  48.514  1.00 22.60           S  
ATOM   2107  CE  MET B  61      36.738  17.384  48.023  1.00  4.48           C  
ATOM   2108  H   MET B  61      34.542  17.214  51.382  1.00  0.00           H  
ATOM   2109  N   CYS B  62      38.304  16.353  52.101  1.00 17.31           N  
ATOM   2110  CA  CYS B  62      39.526  17.131  51.879  1.00 13.24           C  
ATOM   2111  C   CYS B  62      40.397  16.446  50.825  1.00 15.77           C  
ATOM   2112  O   CYS B  62      40.702  15.255  50.947  1.00  7.56           O  
ATOM   2113  CB  CYS B  62      40.318  17.252  53.181  1.00 17.32           C  
ATOM   2114  SG  CYS B  62      39.503  18.240  54.452  1.00 27.93           S  
ATOM   2115  H   CYS B  62      38.342  15.504  52.587  1.00  0.00           H  
ATOM   2116  N   GLN B  63      40.796  17.194  49.797  1.00 16.53           N  
ATOM   2117  CA  GLN B  63      41.554  16.620  48.684  1.00 20.74           C  
ATOM   2118  C   GLN B  63      42.950  17.214  48.500  1.00 17.71           C  
ATOM   2119  O   GLN B  63      43.118  18.434  48.385  1.00 13.80           O  
ATOM   2120  CB  GLN B  63      40.771  16.753  47.371  1.00 21.91           C  
ATOM   2121  CG  GLN B  63      41.352  15.929  46.219  1.00 20.47           C  
ATOM   2122  CD  GLN B  63      40.693  16.219  44.881  1.00 23.12           C  
ATOM   2123  OE1 GLN B  63      39.496  16.456  44.803  1.00 15.94           O  
ATOM   2124  NE2 GLN B  63      41.479  16.190  43.819  1.00 22.78           N  
ATOM   2125  H   GLN B  63      40.514  18.131  49.756  1.00  0.00           H  
ATOM   2126 HE21 GLN B  63      40.988  16.348  42.990  1.00  0.00           H  
ATOM   2127 HE22 GLN B  63      42.434  16.001  43.888  1.00  0.00           H  
ATOM   2128  N   GLY B  64      43.929  16.327  48.351  1.00 12.52           N  
ATOM   2129  CA  GLY B  64      45.295  16.754  48.106  1.00 13.72           C  
ATOM   2130  C   GLY B  64      46.045  15.768  47.232  1.00 16.24           C  
ATOM   2131  O   GLY B  64      45.430  14.932  46.564  1.00 13.87           O  
ATOM   2132  H   GLY B  64      43.695  15.370  48.372  1.00  0.00           H  
ATOM   2133  N   GLY B  65      47.369  15.885  47.204  1.00 18.89           N  
ATOM   2134  CA  GLY B  65      48.193  14.899  46.518  1.00 15.78           C  
ATOM   2135  C   GLY B  65      48.736  15.331  45.167  1.00 16.82           C  
ATOM   2136  O   GLY B  65      49.516  14.614  44.548  1.00 17.18           O  
ATOM   2137  H   GLY B  65      47.767  16.592  47.737  1.00  0.00           H  
ATOM   2138  N   ASP B  66      48.321  16.500  44.694  1.00 19.64           N  
ATOM   2139  CA  ASP B  66      48.798  17.007  43.410  1.00 25.35           C  
ATOM   2140  C   ASP B  66      50.100  17.789  43.591  1.00 24.29           C  
ATOM   2141  O   ASP B  66      50.106  19.024  43.598  1.00 21.78           O  
ATOM   2142  CB  ASP B  66      47.721  17.887  42.750  1.00 27.47           C  
ATOM   2143  CG  ASP B  66      48.103  18.354  41.347  1.00 31.05           C  
ATOM   2144  OD1 ASP B  66      49.172  17.958  40.828  1.00 30.42           O  
ATOM   2145  OD2 ASP B  66      47.342  19.157  40.772  1.00 22.09           O  
ATOM   2146  H   ASP B  66      47.645  16.975  45.220  1.00  0.00           H  
ATOM   2147  N   PHE B  67      51.210  17.065  43.665  1.00 23.90           N  
ATOM   2148  CA  PHE B  67      52.500  17.692  43.933  1.00 23.78           C  
ATOM   2149  C   PHE B  67      53.194  18.293  42.701  1.00 26.42           C  
ATOM   2150  O   PHE B  67      54.059  19.159  42.835  1.00 29.03           O  
ATOM   2151  CB  PHE B  67      53.436  16.712  44.662  1.00 16.90           C  
ATOM   2152  CG  PHE B  67      53.550  15.356  44.011  1.00 11.95           C  
ATOM   2153  CD1 PHE B  67      54.500  15.121  43.026  1.00  9.03           C  
ATOM   2154  CD2 PHE B  67      52.804  14.285  44.480  1.00 11.24           C  
ATOM   2155  CE1 PHE B  67      54.711  13.844  42.529  1.00  2.00           C  
ATOM   2156  CE2 PHE B  67      53.011  13.004  43.988  1.00  9.20           C  
ATOM   2157  CZ  PHE B  67      53.967  12.782  43.011  1.00  8.59           C  
ATOM   2158  H   PHE B  67      51.119  16.086  43.639  1.00  0.00           H  
ATOM   2159  N   THR B  68      52.699  17.969  41.510  1.00 25.98           N  
ATOM   2160  CA  THR B  68      53.278  18.505  40.273  1.00 18.47           C  
ATOM   2161  C   THR B  68      52.595  19.784  39.788  1.00 19.84           C  
ATOM   2162  O   THR B  68      53.257  20.751  39.419  1.00 18.91           O  
ATOM   2163  CB  THR B  68      53.212  17.477  39.139  1.00 18.56           C  
ATOM   2164  OG1 THR B  68      51.843  17.264  38.774  1.00 23.89           O  
ATOM   2165  CG2 THR B  68      53.823  16.152  39.584  1.00 17.21           C  
ATOM   2166  H   THR B  68      52.029  17.261  41.465  1.00  0.00           H  
ATOM   2167  HG1 THR B  68      51.835  17.439  37.812  1.00  0.00           H  
ATOM   2168  N   ARG B  69      51.267  19.799  39.836  1.00 24.19           N  
ATOM   2169  CA  ARG B  69      50.485  20.909  39.281  1.00 27.03           C  
ATOM   2170  C   ARG B  69      49.789  21.763  40.341  1.00 27.40           C  
ATOM   2171  O   ARG B  69      49.419  22.903  40.079  1.00 27.22           O  
ATOM   2172  CB  ARG B  69      49.441  20.372  38.300  1.00 28.37           C  
ATOM   2173  CG  ARG B  69      49.986  19.992  36.933  1.00 25.50           C  
ATOM   2174  CD  ARG B  69      49.669  21.074  35.934  1.00 27.50           C  
ATOM   2175  NE  ARG B  69      49.340  20.547  34.615  1.00 30.07           N  
ATOM   2176  CZ  ARG B  69      48.571  21.179  33.734  1.00 34.58           C  
ATOM   2177  NH1 ARG B  69      47.917  22.281  34.083  1.00 34.05           N  
ATOM   2178  NH2 ARG B  69      48.404  20.677  32.520  1.00 45.96           N  
ATOM   2179  H   ARG B  69      50.860  18.958  40.095  1.00  0.00           H  
ATOM   2180  HE  ARG B  69      49.708  19.677  34.357  1.00  0.00           H  
ATOM   2181 HH11 ARG B  69      47.988  22.636  35.016  1.00  0.00           H  
ATOM   2182 HH12 ARG B  69      47.334  22.747  33.418  1.00  0.00           H  
ATOM   2183 HH21 ARG B  69      48.852  19.821  32.263  1.00  0.00           H  
ATOM   2184 HH22 ARG B  69      47.820  21.156  31.864  1.00  0.00           H  
ATOM   2185  N   HIS B  70      49.487  21.151  41.485  1.00 30.85           N  
ATOM   2186  CA  HIS B  70      48.999  21.862  42.676  1.00 34.33           C  
ATOM   2187  C   HIS B  70      47.588  22.465  42.600  1.00 29.84           C  
ATOM   2188  O   HIS B  70      47.161  23.148  43.527  1.00 29.34           O  
ATOM   2189  CB  HIS B  70      49.993  22.961  43.092  1.00 36.98           C  
ATOM   2190  CG  HIS B  70      51.421  22.508  43.120  1.00 44.95           C  
ATOM   2191  ND1 HIS B  70      52.295  22.744  42.080  1.00 47.08           N  
ATOM   2192  CD2 HIS B  70      52.112  21.787  44.035  1.00 44.17           C  
ATOM   2193  CE1 HIS B  70      53.460  22.185  42.348  1.00 46.59           C  
ATOM   2194  NE2 HIS B  70      53.375  21.595  43.527  1.00 47.90           N  
ATOM   2195  H   HIS B  70      49.683  20.199  41.544  1.00  0.00           H  
ATOM   2196  HD1 HIS B  70      52.107  23.296  41.286  1.00  0.00           H  
ATOM   2197  HE2 HIS B  70      54.067  20.989  43.875  1.00  0.00           H  
ATOM   2198  N   ASN B  71      46.843  22.164  41.541  1.00 27.71           N  
ATOM   2199  CA  ASN B  71      45.490  22.714  41.390  1.00 25.73           C  
ATOM   2200  C   ASN B  71      44.417  21.668  41.070  1.00 27.25           C  
ATOM   2201  O   ASN B  71      43.237  21.992  40.955  1.00 31.30           O  
ATOM   2202  CB  ASN B  71      45.475  23.804  40.312  1.00 18.85           C  
ATOM   2203  CG  ASN B  71      45.928  23.296  38.958  1.00 13.43           C  
ATOM   2204  OD1 ASN B  71      45.974  22.089  38.716  1.00 16.04           O  
ATOM   2205  ND2 ASN B  71      46.295  24.208  38.080  1.00 24.29           N  
ATOM   2206  H   ASN B  71      47.289  21.757  40.775  1.00  0.00           H  
ATOM   2207 HD21 ASN B  71      46.575  23.839  37.213  1.00  0.00           H  
ATOM   2208 HD22 ASN B  71      46.320  25.143  38.358  1.00  0.00           H  
ATOM   2209  N   GLY B  72      44.843  20.422  40.890  1.00 26.46           N  
ATOM   2210  CA  GLY B  72      43.916  19.345  40.584  1.00 22.21           C  
ATOM   2211  C   GLY B  72      44.173  18.675  39.245  1.00 22.83           C  
ATOM   2212  O   GLY B  72      43.653  17.592  38.979  1.00 17.82           O  
ATOM   2213  H   GLY B  72      45.787  20.288  41.016  1.00  0.00           H  
ATOM   2214  N   THR B  73      45.014  19.297  38.422  1.00 22.21           N  
ATOM   2215  CA  THR B  73      45.262  18.821  37.059  1.00 19.88           C  
ATOM   2216  C   THR B  73      46.454  17.877  36.913  1.00 20.79           C  
ATOM   2217  O   THR B  73      46.799  17.485  35.801  1.00 26.25           O  
ATOM   2218  CB  THR B  73      45.489  19.993  36.083  1.00 15.36           C  
ATOM   2219  OG1 THR B  73      46.606  20.775  36.522  1.00 26.10           O  
ATOM   2220  CG2 THR B  73      44.261  20.874  36.005  1.00  5.42           C  
ATOM   2221  H   THR B  73      45.407  20.143  38.712  1.00  0.00           H  
ATOM   2222  HG1 THR B  73      46.569  21.011  37.440  1.00  0.00           H  
ATOM   2223  N   GLY B  74      47.083  17.506  38.024  1.00 22.12           N  
ATOM   2224  CA  GLY B  74      48.294  16.707  37.930  1.00 18.39           C  
ATOM   2225  C   GLY B  74      48.502  15.617  38.966  1.00 17.57           C  
ATOM   2226  O   GLY B  74      47.554  15.014  39.471  1.00 20.80           O  
ATOM   2227  H   GLY B  74      46.655  17.681  38.877  1.00  0.00           H  
ATOM   2228  N   GLY B  75      49.754  15.457  39.375  1.00 20.84           N  
ATOM   2229  CA  GLY B  75      50.118  14.357  40.245  1.00 15.25           C  
ATOM   2230  C   GLY B  75      50.600  13.162  39.448  1.00 18.43           C  
ATOM   2231  O   GLY B  75      50.341  13.071  38.248  1.00 27.36           O  
ATOM   2232  H   GLY B  75      50.444  16.030  38.997  1.00  0.00           H  
ATOM   2233  N   LYS B  76      51.346  12.273  40.093  1.00 16.47           N  
ATOM   2234  CA  LYS B  76      51.776  11.041  39.449  1.00 13.99           C  
ATOM   2235  C   LYS B  76      52.123   9.966  40.466  1.00 16.25           C  
ATOM   2236  O   LYS B  76      52.462  10.266  41.610  1.00 19.00           O  
ATOM   2237  CB  LYS B  76      52.974  11.302  38.521  1.00 27.44           C  
ATOM   2238  CG  LYS B  76      54.249  11.780  39.213  1.00 26.90           C  
ATOM   2239  CD  LYS B  76      55.426  11.756  38.244  1.00 34.20           C  
ATOM   2240  CE  LYS B  76      56.757  12.009  38.942  1.00 35.09           C  
ATOM   2241  NZ  LYS B  76      56.906  13.419  39.393  1.00 42.75           N  
ATOM   2242  H   LYS B  76      51.570  12.413  41.037  1.00  0.00           H  
ATOM   2243  HZ1 LYS B  76      56.804  14.051  38.573  1.00  0.00           H  
ATOM   2244  HZ2 LYS B  76      56.173  13.643  40.096  1.00  0.00           H  
ATOM   2245  HZ3 LYS B  76      57.846  13.553  39.818  1.00  0.00           H  
ATOM   2246  N   SER B  77      51.934   8.714  40.068  1.00 15.51           N  
ATOM   2247  CA  SER B  77      52.186   7.575  40.941  1.00 16.73           C  
ATOM   2248  C   SER B  77      53.667   7.189  40.997  1.00 15.72           C  
ATOM   2249  O   SER B  77      54.517   7.828  40.374  1.00 17.69           O  
ATOM   2250  CB  SER B  77      51.363   6.373  40.473  1.00 17.33           C  
ATOM   2251  OG  SER B  77      51.775   5.938  39.186  1.00 25.13           O  
ATOM   2252  H   SER B  77      51.695   8.591  39.124  1.00  0.00           H  
ATOM   2253  HG  SER B  77      51.599   6.668  38.572  1.00  0.00           H  
ATOM   2254  N   ILE B  78      53.968   6.138  41.751  1.00 14.01           N  
ATOM   2255  CA  ILE B  78      55.317   5.579  41.790  1.00 18.45           C  
ATOM   2256  C   ILE B  78      55.503   4.534  40.688  1.00 24.64           C  
ATOM   2257  O   ILE B  78      56.566   3.930  40.564  1.00 28.71           O  
ATOM   2258  CB  ILE B  78      55.628   4.922  43.161  1.00 10.84           C  
ATOM   2259  CG1 ILE B  78      54.692   3.744  43.419  1.00 12.17           C  
ATOM   2260  CG2 ILE B  78      55.508   5.946  44.274  1.00 16.08           C  
ATOM   2261  CD1 ILE B  78      55.109   2.889  44.598  1.00 13.09           C  
ATOM   2262  H   ILE B  78      53.281   5.813  42.363  1.00  0.00           H  
ATOM   2263  N   TYR B  79      54.423   4.240  39.973  1.00 24.26           N  
ATOM   2264  CA  TYR B  79      54.476   3.334  38.830  1.00 26.45           C  
ATOM   2265  C   TYR B  79      54.583   4.125  37.527  1.00 31.61           C  
ATOM   2266  O   TYR B  79      54.948   3.584  36.486  1.00 39.27           O  
ATOM   2267  CB  TYR B  79      53.227   2.451  38.806  1.00 23.89           C  
ATOM   2268  CG  TYR B  79      52.933   1.799  40.134  1.00 23.31           C  
ATOM   2269  CD1 TYR B  79      53.776   0.815  40.647  1.00 24.79           C  
ATOM   2270  CD2 TYR B  79      51.869   2.231  40.923  1.00 19.32           C  
ATOM   2271  CE1 TYR B  79      53.573   0.280  41.916  1.00 26.67           C  
ATOM   2272  CE2 TYR B  79      51.657   1.708  42.197  1.00 20.45           C  
ATOM   2273  CZ  TYR B  79      52.513   0.732  42.687  1.00 28.49           C  
ATOM   2274  OH  TYR B  79      52.304   0.196  43.940  1.00 30.00           O  
ATOM   2275  H   TYR B  79      53.569   4.641  40.229  1.00  0.00           H  
ATOM   2276  HH  TYR B  79      51.549   0.642  44.336  1.00  0.00           H  
ATOM   2277  N   GLY B  80      54.303   5.421  37.608  0.00 33.31           N  
ATOM   2278  CA  GLY B  80      54.349   6.278  36.437  0.00 33.27           C  
ATOM   2279  C   GLY B  80      53.307   7.374  36.532  0.00 33.04           C  
ATOM   2280  O   GLY B  80      53.062   7.910  37.612  0.00 33.18           O  
ATOM   2281  H   GLY B  80      54.033   5.799  38.469  1.00  0.00           H  
ATOM   2282  N   GLU B  81      52.637   7.661  35.422  0.00 32.07           N  
ATOM   2283  CA  GLU B  81      51.532   8.614  35.434  0.00 30.67           C  
ATOM   2284  C   GLU B  81      50.330   8.064  36.205  0.00 27.59           C  
ATOM   2285  O   GLU B  81      50.084   8.455  37.346  0.00 28.29           O  
ATOM   2286  CB  GLU B  81      51.118   8.967  34.001  0.00 33.18           C  
ATOM   2287  CG  GLU B  81      51.914  10.108  33.383  0.00 37.00           C  
ATOM   2288  CD  GLU B  81      51.542  11.463  33.958  0.00 38.58           C  
ATOM   2289  OE1 GLU B  81      50.535  12.046  33.505  0.00 39.02           O  
ATOM   2290  OE2 GLU B  81      52.260  11.948  34.858  0.00 40.59           O  
ATOM   2291  H   GLU B  81      52.915   7.219  34.594  1.00  0.00           H  
ATOM   2292  N   LYS B  82      49.675   7.061  35.628  1.00 25.38           N  
ATOM   2293  CA  LYS B  82      48.434   6.519  36.174  1.00 14.11           C  
ATOM   2294  C   LYS B  82      48.489   4.999  36.259  1.00 15.86           C  
ATOM   2295  O   LYS B  82      49.222   4.355  35.511  1.00 21.36           O  
ATOM   2296  CB  LYS B  82      47.247   6.936  35.302  1.00 14.81           C  
ATOM   2297  CG  LYS B  82      47.133   8.435  35.079  1.00 14.11           C  
ATOM   2298  CD  LYS B  82      46.944   9.172  36.397  1.00 28.15           C  
ATOM   2299  CE  LYS B  82      47.217  10.661  36.255  1.00 36.00           C  
ATOM   2300  NZ  LYS B  82      46.842  11.410  37.483  1.00 47.91           N  
ATOM   2301  H   LYS B  82      50.048   6.626  34.836  1.00  0.00           H  
ATOM   2302  HZ1 LYS B  82      45.842  11.232  37.705  1.00  0.00           H  
ATOM   2303  HZ2 LYS B  82      47.434  11.092  38.277  1.00  0.00           H  
ATOM   2304  HZ3 LYS B  82      46.987  12.429  37.332  1.00  0.00           H  
ATOM   2305  N   PHE B  83      47.754   4.428  37.204  1.00 12.64           N  
ATOM   2306  CA  PHE B  83      47.589   2.983  37.239  1.00  9.07           C  
ATOM   2307  C   PHE B  83      46.135   2.546  37.433  1.00 13.54           C  
ATOM   2308  O   PHE B  83      45.250   3.367  37.701  1.00  9.54           O  
ATOM   2309  CB  PHE B  83      48.502   2.347  38.308  1.00 14.71           C  
ATOM   2310  CG  PHE B  83      48.152   2.715  39.731  1.00  5.34           C  
ATOM   2311  CD1 PHE B  83      48.530   3.942  40.260  1.00  5.79           C  
ATOM   2312  CD2 PHE B  83      47.528   1.795  40.563  1.00  7.27           C  
ATOM   2313  CE1 PHE B  83      48.298   4.247  41.601  1.00  8.49           C  
ATOM   2314  CE2 PHE B  83      47.291   2.089  41.900  1.00 11.42           C  
ATOM   2315  CZ  PHE B  83      47.680   3.320  42.420  1.00  8.16           C  
ATOM   2316  H   PHE B  83      47.365   5.004  37.891  1.00  0.00           H  
ATOM   2317  N   GLU B  84      45.905   1.248  37.269  1.00 13.08           N  
ATOM   2318  CA  GLU B  84      44.570   0.663  37.289  1.00 25.11           C  
ATOM   2319  C   GLU B  84      43.814   0.953  38.574  1.00 24.66           C  
ATOM   2320  O   GLU B  84      44.408   1.288  39.598  1.00 30.32           O  
ATOM   2321  CB  GLU B  84      44.656  -0.857  37.123  1.00 31.70           C  
ATOM   2322  CG  GLU B  84      44.742  -1.356  35.694  1.00 44.32           C  
ATOM   2323  CD  GLU B  84      44.742  -2.878  35.610  1.00 57.69           C  
ATOM   2324  OE1 GLU B  84      43.882  -3.517  36.259  1.00 65.41           O  
ATOM   2325  OE2 GLU B  84      45.602  -3.437  34.894  1.00 64.63           O  
ATOM   2326  H   GLU B  84      46.682   0.674  37.123  1.00  0.00           H  
ATOM   2327  N   ASP B  85      42.502   0.765  38.525  1.00 17.51           N  
ATOM   2328  CA  ASP B  85      41.711   0.604  39.735  1.00 17.73           C  
ATOM   2329  C   ASP B  85      41.904  -0.819  40.242  1.00 21.34           C  
ATOM   2330  O   ASP B  85      41.456  -1.776  39.610  1.00 23.42           O  
ATOM   2331  CB  ASP B  85      40.234   0.856  39.447  1.00 15.10           C  
ATOM   2332  CG  ASP B  85      39.946   2.300  39.104  1.00 14.17           C  
ATOM   2333  OD1 ASP B  85      40.571   3.194  39.703  1.00 14.61           O  
ATOM   2334  OD2 ASP B  85      39.059   2.542  38.263  1.00 22.06           O  
ATOM   2335  H   ASP B  85      42.079   0.695  37.651  1.00  0.00           H  
ATOM   2336  N   GLU B  86      42.641  -0.954  41.341  1.00 23.18           N  
ATOM   2337  CA  GLU B  86      43.075  -2.263  41.829  1.00 18.95           C  
ATOM   2338  C   GLU B  86      41.904  -3.172  42.196  1.00 18.29           C  
ATOM   2339  O   GLU B  86      41.897  -4.361  41.871  1.00 22.60           O  
ATOM   2340  CB  GLU B  86      43.993  -2.079  43.035  1.00 20.09           C  
ATOM   2341  CG  GLU B  86      44.590  -3.371  43.566  1.00 17.09           C  
ATOM   2342  CD  GLU B  86      45.756  -3.130  44.503  1.00 18.85           C  
ATOM   2343  OE1 GLU B  86      45.966  -1.966  44.911  1.00 13.03           O  
ATOM   2344  OE2 GLU B  86      46.481  -4.102  44.803  1.00 16.60           O  
ATOM   2345  H   GLU B  86      42.912  -0.132  41.799  1.00  0.00           H  
ATOM   2346  N   ASN B  87      40.969  -2.625  42.963  1.00 16.12           N  
ATOM   2347  CA  ASN B  87      39.691  -3.274  43.230  1.00 15.23           C  
ATOM   2348  C   ASN B  87      38.811  -2.286  43.983  1.00 16.25           C  
ATOM   2349  O   ASN B  87      39.283  -1.241  44.441  1.00 15.52           O  
ATOM   2350  CB  ASN B  87      39.880  -4.558  44.056  1.00 18.51           C  
ATOM   2351  CG  ASN B  87      40.475  -4.295  45.431  1.00 20.78           C  
ATOM   2352  OD1 ASN B  87      39.925  -3.531  46.225  1.00 22.02           O  
ATOM   2353  ND2 ASN B  87      41.578  -4.965  45.732  1.00 15.38           N  
ATOM   2354  H   ASN B  87      41.132  -1.731  43.327  1.00  0.00           H  
ATOM   2355 HD21 ASN B  87      42.497  -4.592  45.629  1.00  0.00           H  
ATOM   2356 HD22 ASN B  87      41.469  -5.894  46.039  1.00  0.00           H  
ATOM   2357  N   PHE B  88      37.542  -2.640  44.148  1.00 19.52           N  
ATOM   2358  CA  PHE B  88      36.612  -1.820  44.919  1.00 21.07           C  
ATOM   2359  C   PHE B  88      36.001  -2.622  46.065  1.00 19.42           C  
ATOM   2360  O   PHE B  88      34.819  -2.480  46.379  1.00 24.92           O  
ATOM   2361  CB  PHE B  88      35.510  -1.271  44.008  1.00 12.19           C  
ATOM   2362  CG  PHE B  88      36.023  -0.424  42.883  1.00 11.07           C  
ATOM   2363  CD1 PHE B  88      36.469   0.867  43.120  1.00  6.07           C  
ATOM   2364  CD2 PHE B  88      36.062  -0.920  41.583  1.00 16.41           C  
ATOM   2365  CE1 PHE B  88      36.946   1.659  42.082  1.00 12.84           C  
ATOM   2366  CE2 PHE B  88      36.537  -0.140  40.536  1.00  5.03           C  
ATOM   2367  CZ  PHE B  88      36.979   1.154  40.785  1.00 14.54           C  
ATOM   2368  H   PHE B  88      37.226  -3.449  43.703  1.00  0.00           H  
ATOM   2369  N   ILE B  89      36.833  -3.433  46.711  1.00 16.79           N  
ATOM   2370  CA  ILE B  89      36.389  -4.264  47.825  1.00 16.73           C  
ATOM   2371  C   ILE B  89      35.958  -3.430  49.031  1.00 15.46           C  
ATOM   2372  O   ILE B  89      34.954  -3.735  49.669  1.00 28.65           O  
ATOM   2373  CB  ILE B  89      37.498  -5.265  48.235  1.00 19.22           C  
ATOM   2374  CG1 ILE B  89      37.719  -6.269  47.103  1.00 17.05           C  
ATOM   2375  CG2 ILE B  89      37.122  -6.001  49.525  1.00 13.97           C  
ATOM   2376  CD1 ILE B  89      38.911  -7.180  47.297  1.00 21.58           C  
ATOM   2377  H   ILE B  89      37.781  -3.400  46.473  1.00  0.00           H  
ATOM   2378  N   LEU B  90      36.670  -2.335  49.290  1.00 11.35           N  
ATOM   2379  CA  LEU B  90      36.364  -1.468  50.428  1.00  5.50           C  
ATOM   2380  C   LEU B  90      35.498  -0.263  50.043  1.00 16.34           C  
ATOM   2381  O   LEU B  90      35.613   0.259  48.932  1.00 21.78           O  
ATOM   2382  CB  LEU B  90      37.661  -0.985  51.084  1.00 14.06           C  
ATOM   2383  CG  LEU B  90      38.675  -2.052  51.520  1.00 16.39           C  
ATOM   2384  CD1 LEU B  90      39.927  -1.379  52.049  1.00 11.37           C  
ATOM   2385  CD2 LEU B  90      38.067  -2.958  52.577  1.00  5.95           C  
ATOM   2386  H   LEU B  90      37.429  -2.126  48.703  1.00  0.00           H  
ATOM   2387  N   LYS B  91      34.752   0.273  51.010  1.00 13.01           N  
ATOM   2388  CA  LYS B  91      33.734   1.290  50.731  1.00 16.06           C  
ATOM   2389  C   LYS B  91      33.901   2.601  51.511  1.00 21.64           C  
ATOM   2390  O   LYS B  91      34.580   2.641  52.538  1.00 25.27           O  
ATOM   2391  CB  LYS B  91      32.339   0.715  51.009  1.00 20.82           C  
ATOM   2392  CG  LYS B  91      31.999  -0.526  50.198  0.00 16.54           C  
ATOM   2393  CD  LYS B  91      30.685  -1.138  50.655  0.00 16.75           C  
ATOM   2394  CE  LYS B  91      30.400  -2.444  49.931  0.00 15.32           C  
ATOM   2395  NZ  LYS B  91      31.421  -3.489  50.230  0.00 14.98           N  
ATOM   2396  H   LYS B  91      34.908  -0.034  51.924  1.00  0.00           H  
ATOM   2397  HZ1 LYS B  91      31.474  -3.639  51.258  1.00  0.00           H  
ATOM   2398  HZ2 LYS B  91      31.153  -4.380  49.765  1.00  0.00           H  
ATOM   2399  HZ3 LYS B  91      32.348  -3.179  49.876  1.00  0.00           H  
ATOM   2400  N   HIS B  92      33.182   3.639  51.077  1.00 16.33           N  
ATOM   2401  CA  HIS B  92      33.196   4.945  51.739  1.00 16.72           C  
ATOM   2402  C   HIS B  92      32.158   4.982  52.865  1.00 25.23           C  
ATOM   2403  O   HIS B  92      31.033   5.449  52.668  1.00 28.76           O  
ATOM   2404  CB  HIS B  92      32.896   6.060  50.727  1.00 17.72           C  
ATOM   2405  CG  HIS B  92      33.936   6.210  49.655  1.00 24.73           C  
ATOM   2406  ND1 HIS B  92      34.113   5.283  48.648  1.00 22.32           N  
ATOM   2407  CD2 HIS B  92      34.843   7.189  49.425  1.00 19.43           C  
ATOM   2408  CE1 HIS B  92      35.083   5.684  47.846  1.00 12.11           C  
ATOM   2409  NE2 HIS B  92      35.544   6.837  48.297  1.00 14.84           N  
ATOM   2410  H   HIS B  92      32.528   3.437  50.390  1.00  0.00           H  
ATOM   2411  HD1 HIS B  92      33.638   4.443  48.510  1.00  0.00           H  
ATOM   2412  HE2 HIS B  92      36.364   7.266  47.968  1.00  0.00           H  
ATOM   2413  N   THR B  93      32.539   4.484  54.040  1.00 26.66           N  
ATOM   2414  CA  THR B  93      31.588   4.232  55.130  1.00 25.68           C  
ATOM   2415  C   THR B  93      31.401   5.375  56.133  1.00 25.76           C  
ATOM   2416  O   THR B  93      30.541   5.299  57.010  1.00 32.12           O  
ATOM   2417  CB  THR B  93      31.985   2.985  55.931  1.00 22.35           C  
ATOM   2418  OG1 THR B  93      33.275   3.190  56.517  1.00 28.44           O  
ATOM   2419  CG2 THR B  93      32.027   1.762  55.031  1.00 16.75           C  
ATOM   2420  H   THR B  93      33.476   4.217  54.166  1.00  0.00           H  
ATOM   2421  HG1 THR B  93      33.537   2.411  57.012  1.00  0.00           H  
ATOM   2422  N   GLY B  94      32.213   6.419  56.022  1.00 22.86           N  
ATOM   2423  CA  GLY B  94      32.112   7.530  56.954  1.00 17.50           C  
ATOM   2424  C   GLY B  94      33.308   8.466  56.916  1.00 18.27           C  
ATOM   2425  O   GLY B  94      34.146   8.362  56.020  1.00 14.82           O  
ATOM   2426  H   GLY B  94      32.906   6.398  55.337  1.00  0.00           H  
ATOM   2427  N   PRO B  95      33.389   9.428  57.849  1.00 19.63           N  
ATOM   2428  CA  PRO B  95      34.558  10.310  57.957  1.00 21.94           C  
ATOM   2429  C   PRO B  95      35.846   9.541  58.229  1.00 24.87           C  
ATOM   2430  O   PRO B  95      35.830   8.489  58.869  1.00 28.57           O  
ATOM   2431  CB  PRO B  95      34.201  11.234  59.124  1.00 19.75           C  
ATOM   2432  CG  PRO B  95      32.715  11.174  59.208  1.00 22.96           C  
ATOM   2433  CD  PRO B  95      32.365   9.765  58.846  1.00 15.43           C  
ATOM   2434  N   GLY B  96      36.954  10.049  57.700  1.00 23.93           N  
ATOM   2435  CA  GLY B  96      38.243   9.429  57.942  1.00 23.46           C  
ATOM   2436  C   GLY B  96      38.685   8.496  56.836  1.00 23.59           C  
ATOM   2437  O   GLY B  96      39.860   8.132  56.764  1.00 25.99           O  
ATOM   2438  H   GLY B  96      36.910  10.885  57.204  1.00  0.00           H  
ATOM   2439  N   ILE B  97      37.740   8.081  55.995  1.00 20.75           N  
ATOM   2440  CA  ILE B  97      38.037   7.222  54.851  1.00 16.10           C  
ATOM   2441  C   ILE B  97      38.996   7.903  53.870  1.00 17.39           C  
ATOM   2442  O   ILE B  97      38.760   9.033  53.434  1.00 17.55           O  
ATOM   2443  CB  ILE B  97      36.736   6.813  54.110  1.00 17.03           C  
ATOM   2444  CG1 ILE B  97      35.900   5.880  54.992  1.00 10.78           C  
ATOM   2445  CG2 ILE B  97      37.062   6.139  52.783  1.00 19.88           C  
ATOM   2446  CD1 ILE B  97      36.540   4.538  55.275  1.00  5.03           C  
ATOM   2447  H   ILE B  97      36.813   8.324  56.187  1.00  0.00           H  
ATOM   2448  N   LEU B  98      40.118   7.238  53.602  1.00 19.44           N  
ATOM   2449  CA  LEU B  98      41.115   7.721  52.645  1.00 17.97           C  
ATOM   2450  C   LEU B  98      40.945   7.001  51.297  1.00 17.88           C  
ATOM   2451  O   LEU B  98      40.991   5.765  51.221  1.00  8.78           O  
ATOM   2452  CB  LEU B  98      42.524   7.481  53.205  1.00 14.95           C  
ATOM   2453  CG  LEU B  98      43.762   8.007  52.478  1.00  9.86           C  
ATOM   2454  CD1 LEU B  98      43.762   9.519  52.449  1.00 12.01           C  
ATOM   2455  CD2 LEU B  98      45.002   7.498  53.189  1.00 14.63           C  
ATOM   2456  H   LEU B  98      40.264   6.389  54.071  1.00  0.00           H  
ATOM   2457  N   SER B  99      40.725   7.777  50.241  1.00 16.11           N  
ATOM   2458  CA  SER B  99      40.372   7.210  48.937  1.00 18.22           C  
ATOM   2459  C   SER B  99      41.091   7.902  47.779  1.00 12.81           C  
ATOM   2460  O   SER B  99      41.509   9.054  47.898  1.00 12.99           O  
ATOM   2461  CB  SER B  99      38.857   7.302  48.738  1.00 19.22           C  
ATOM   2462  OG  SER B  99      38.422   6.540  47.629  1.00 27.93           O  
ATOM   2463  H   SER B  99      40.807   8.748  50.362  1.00  0.00           H  
ATOM   2464  HG  SER B  99      38.953   5.731  47.613  1.00  0.00           H  
ATOM   2465  N   MET B 100      41.250   7.193  46.665  1.00 14.57           N  
ATOM   2466  CA  MET B 100      41.929   7.746  45.488  1.00 15.41           C  
ATOM   2467  C   MET B 100      41.067   8.724  44.683  1.00 13.95           C  
ATOM   2468  O   MET B 100      39.978   8.377  44.216  1.00 19.45           O  
ATOM   2469  CB  MET B 100      42.422   6.619  44.567  1.00 14.82           C  
ATOM   2470  CG  MET B 100      43.684   5.900  45.051  1.00 14.82           C  
ATOM   2471  SD  MET B 100      45.045   7.018  45.496  1.00 17.06           S  
ATOM   2472  CE  MET B 100      45.751   7.377  43.892  1.00 24.82           C  
ATOM   2473  H   MET B 100      40.936   6.272  46.643  1.00  0.00           H  
ATOM   2474  N   ALA B 101      41.567   9.943  44.515  1.00 15.69           N  
ATOM   2475  CA  ALA B 101      40.905  10.944  43.685  1.00 20.33           C  
ATOM   2476  C   ALA B 101      41.365  10.797  42.242  1.00 29.49           C  
ATOM   2477  O   ALA B 101      42.443  11.265  41.876  1.00 45.61           O  
ATOM   2478  CB  ALA B 101      41.220  12.347  44.190  1.00  6.60           C  
ATOM   2479  H   ALA B 101      42.436  10.136  44.930  1.00  0.00           H  
ATOM   2480  N   ASN B 102      40.578  10.092  41.439  1.00 30.26           N  
ATOM   2481  CA  ASN B 102      40.912   9.894  40.033  1.00 23.62           C  
ATOM   2482  C   ASN B 102      40.211  10.902  39.123  1.00 28.44           C  
ATOM   2483  O   ASN B 102      39.508  11.801  39.596  1.00 28.50           O  
ATOM   2484  CB  ASN B 102      40.556   8.467  39.608  1.00 25.51           C  
ATOM   2485  CG  ASN B 102      39.108   8.123  39.880  1.00 26.62           C  
ATOM   2486  OD1 ASN B 102      38.196   8.837  39.461  1.00 25.85           O  
ATOM   2487  ND2 ASN B 102      38.889   7.081  40.660  1.00 26.74           N  
ATOM   2488  H   ASN B 102      39.791   9.674  41.821  1.00  0.00           H  
ATOM   2489 HD21 ASN B 102      37.953   6.797  40.716  1.00  0.00           H  
ATOM   2490 HD22 ASN B 102      39.634   6.622  41.093  1.00  0.00           H  
ATOM   2491  N   ALA B 103      40.481  10.798  37.825  1.00 26.65           N  
ATOM   2492  CA  ALA B 103      39.754  11.562  36.815  1.00 26.39           C  
ATOM   2493  C   ALA B 103      39.033  10.607  35.854  1.00 29.24           C  
ATOM   2494  O   ALA B 103      38.924  10.867  34.655  1.00 30.15           O  
ATOM   2495  CB  ALA B 103      40.717  12.464  36.050  1.00 21.77           C  
ATOM   2496  H   ALA B 103      41.208  10.200  37.548  1.00  0.00           H  
ATOM   2497  N   GLY B 104      38.543   9.497  36.398  1.00 25.94           N  
ATOM   2498  CA  GLY B 104      37.909   8.475  35.586  1.00 16.51           C  
ATOM   2499  C   GLY B 104      38.388   7.083  35.953  1.00 19.01           C  
ATOM   2500  O   GLY B 104      39.285   6.942  36.781  1.00 15.41           O  
ATOM   2501  H   GLY B 104      38.614   9.384  37.369  1.00  0.00           H  
ATOM   2502  N   PRO B 105      37.817   6.028  35.354  1.00 21.90           N  
ATOM   2503  CA  PRO B 105      38.317   4.662  35.546  1.00 24.19           C  
ATOM   2504  C   PRO B 105      39.788   4.493  35.176  1.00 27.03           C  
ATOM   2505  O   PRO B 105      40.234   4.967  34.133  1.00 26.24           O  
ATOM   2506  CB  PRO B 105      37.409   3.822  34.650  1.00 22.67           C  
ATOM   2507  CG  PRO B 105      36.129   4.581  34.641  1.00 25.17           C  
ATOM   2508  CD  PRO B 105      36.542   6.035  34.616  1.00 25.66           C  
ATOM   2509  N   ASN B 106      40.550   3.905  36.094  1.00 24.40           N  
ATOM   2510  CA  ASN B 106      41.958   3.589  35.874  1.00 20.10           C  
ATOM   2511  C   ASN B 106      42.816   4.821  35.581  1.00 21.58           C  
ATOM   2512  O   ASN B 106      43.660   4.802  34.685  1.00 22.31           O  
ATOM   2513  CB  ASN B 106      42.091   2.564  34.740  1.00 25.36           C  
ATOM   2514  CG  ASN B 106      41.314   1.290  35.012  1.00 27.18           C  
ATOM   2515  OD1 ASN B 106      41.068   0.932  36.160  1.00 37.06           O  
ATOM   2516  ND2 ASN B 106      40.921   0.604  33.961  1.00 31.19           N  
ATOM   2517  H   ASN B 106      40.136   3.699  36.944  1.00  0.00           H  
ATOM   2518 HD21 ASN B 106      40.412  -0.204  34.161  1.00  0.00           H  
ATOM   2519 HD22 ASN B 106      41.146   0.940  33.077  1.00  0.00           H  
ATOM   2520  N   THR B 107      42.593   5.890  36.344  1.00 23.23           N  
ATOM   2521  CA  THR B 107      43.417   7.100  36.246  1.00 24.13           C  
ATOM   2522  C   THR B 107      44.072   7.479  37.580  1.00 18.48           C  
ATOM   2523  O   THR B 107      44.202   8.659  37.909  1.00 18.59           O  
ATOM   2524  CB  THR B 107      42.597   8.324  35.751  1.00 23.72           C  
ATOM   2525  OG1 THR B 107      41.462   8.522  36.604  1.00 24.24           O  
ATOM   2526  CG2 THR B 107      42.135   8.124  34.321  1.00 15.63           C  
ATOM   2527  H   THR B 107      41.818   5.863  36.938  1.00  0.00           H  
ATOM   2528  HG1 THR B 107      40.952   7.707  36.664  1.00  0.00           H  
ATOM   2529  N   ASN B 108      44.542   6.479  38.315  1.00 22.00           N  
ATOM   2530  CA  ASN B 108      45.142   6.720  39.625  1.00 18.82           C  
ATOM   2531  C   ASN B 108      46.579   7.235  39.522  1.00 16.63           C  
ATOM   2532  O   ASN B 108      47.444   6.574  38.948  1.00 15.82           O  
ATOM   2533  CB  ASN B 108      45.123   5.442  40.460  1.00 15.02           C  
ATOM   2534  CG  ASN B 108      43.724   4.955  40.750  1.00 16.64           C  
ATOM   2535  OD1 ASN B 108      42.869   5.708  41.208  1.00 22.51           O  
ATOM   2536  ND2 ASN B 108      43.485   3.681  40.498  1.00 20.11           N  
ATOM   2537  H   ASN B 108      44.548   5.579  37.923  1.00  0.00           H  
ATOM   2538 HD21 ASN B 108      42.617   3.326  40.742  1.00  0.00           H  
ATOM   2539 HD22 ASN B 108      44.226   3.152  40.136  1.00  0.00           H  
ATOM   2540  N   GLY B 109      46.822   8.420  40.065  1.00  8.29           N  
ATOM   2541  CA  GLY B 109      48.175   8.936  40.122  1.00  5.89           C  
ATOM   2542  C   GLY B 109      48.633   9.103  41.557  1.00  9.58           C  
ATOM   2543  O   GLY B 109      48.973   8.125  42.223  1.00 10.77           O  
ATOM   2544  H   GLY B 109      46.067   8.937  40.426  1.00  0.00           H  
ATOM   2545  N   SER B 110      48.499  10.320  42.075  1.00 11.87           N  
ATOM   2546  CA  SER B 110      48.899  10.626  43.448  1.00 11.58           C  
ATOM   2547  C   SER B 110      47.816  11.322  44.277  1.00 17.40           C  
ATOM   2548  O   SER B 110      47.918  11.389  45.505  1.00 19.43           O  
ATOM   2549  CB  SER B 110      50.147  11.499  43.437  1.00  8.10           C  
ATOM   2550  OG  SER B 110      49.921  12.675  42.687  1.00  9.69           O  
ATOM   2551  H   SER B 110      48.129  11.010  41.489  1.00  0.00           H  
ATOM   2552  HG  SER B 110      49.615  13.334  43.315  1.00  0.00           H  
ATOM   2553  N   GLN B 111      46.806  11.877  43.613  1.00 12.20           N  
ATOM   2554  CA  GLN B 111      45.758  12.616  44.315  1.00  9.27           C  
ATOM   2555  C   GLN B 111      44.807  11.725  45.107  1.00  8.40           C  
ATOM   2556  O   GLN B 111      44.411  10.648  44.659  1.00 13.26           O  
ATOM   2557  CB  GLN B 111      44.971  13.492  43.338  1.00 11.92           C  
ATOM   2558  CG  GLN B 111      45.711  14.754  42.939  1.00 17.30           C  
ATOM   2559  CD  GLN B 111      44.907  15.653  42.019  1.00 18.57           C  
ATOM   2560  OE1 GLN B 111      44.279  16.612  42.462  1.00 14.37           O  
ATOM   2561  NE2 GLN B 111      45.021  15.420  40.724  1.00 18.42           N  
ATOM   2562  H   GLN B 111      46.749  11.754  42.643  1.00  0.00           H  
ATOM   2563 HE21 GLN B 111      44.434  15.944  40.146  1.00  0.00           H  
ATOM   2564 HE22 GLN B 111      45.664  14.751  40.409  1.00  0.00           H  
ATOM   2565  N   PHE B 112      44.460  12.184  46.302  1.00 10.51           N  
ATOM   2566  CA  PHE B 112      43.647  11.414  47.236  1.00  7.79           C  
ATOM   2567  C   PHE B 112      42.665  12.358  47.926  1.00  6.46           C  
ATOM   2568  O   PHE B 112      42.854  13.577  47.922  1.00  8.94           O  
ATOM   2569  CB  PHE B 112      44.542  10.737  48.289  1.00 11.29           C  
ATOM   2570  CG  PHE B 112      45.352  11.709  49.122  1.00 14.81           C  
ATOM   2571  CD1 PHE B 112      44.807  12.298  50.260  1.00 14.51           C  
ATOM   2572  CD2 PHE B 112      46.613  12.124  48.699  1.00 20.29           C  
ATOM   2573  CE1 PHE B 112      45.496  13.294  50.951  1.00 16.16           C  
ATOM   2574  CE2 PHE B 112      47.310  13.117  49.387  1.00  9.07           C  
ATOM   2575  CZ  PHE B 112      46.749  13.703  50.509  1.00 13.15           C  
ATOM   2576  H   PHE B 112      44.769  13.080  46.558  1.00  0.00           H  
ATOM   2577  N   PHE B 113      41.655  11.792  48.570  1.00  8.15           N  
ATOM   2578  CA  PHE B 113      40.803  12.572  49.458  1.00 10.03           C  
ATOM   2579  C   PHE B 113      40.468  11.835  50.761  1.00 12.74           C  
ATOM   2580  O   PHE B 113      40.510  10.595  50.831  1.00  6.77           O  
ATOM   2581  CB  PHE B 113      39.515  13.005  48.734  1.00 10.98           C  
ATOM   2582  CG  PHE B 113      38.619  11.862  48.339  1.00  9.87           C  
ATOM   2583  CD1 PHE B 113      38.856  11.149  47.172  1.00  9.19           C  
ATOM   2584  CD2 PHE B 113      37.531  11.511  49.127  1.00  4.66           C  
ATOM   2585  CE1 PHE B 113      38.028  10.108  46.796  1.00  8.14           C  
ATOM   2586  CE2 PHE B 113      36.699  10.471  48.758  1.00 10.04           C  
ATOM   2587  CZ  PHE B 113      36.947   9.768  47.590  1.00 14.22           C  
ATOM   2588  H   PHE B 113      41.501  10.833  48.468  1.00  0.00           H  
ATOM   2589  N   ILE B 114      40.306  12.619  51.823  1.00 15.18           N  
ATOM   2590  CA  ILE B 114      39.821  12.112  53.104  1.00 15.39           C  
ATOM   2591  C   ILE B 114      38.373  12.555  53.273  1.00 13.22           C  
ATOM   2592  O   ILE B 114      38.074  13.751  53.249  1.00 15.24           O  
ATOM   2593  CB  ILE B 114      40.636  12.673  54.303  1.00 11.66           C  
ATOM   2594  CG1 ILE B 114      42.127  12.734  53.972  1.00 13.31           C  
ATOM   2595  CG2 ILE B 114      40.441  11.787  55.515  1.00 19.36           C  
ATOM   2596  CD1 ILE B 114      42.847  13.881  54.654  1.00  8.18           C  
ATOM   2597  H   ILE B 114      40.545  13.561  51.722  1.00  0.00           H  
ATOM   2598  N   CYS B 115      37.467  11.589  53.369  1.00 16.71           N  
ATOM   2599  CA  CYS B 115      36.047  11.882  53.577  1.00 18.09           C  
ATOM   2600  C   CYS B 115      35.773  12.510  54.944  1.00 18.24           C  
ATOM   2601  O   CYS B 115      36.270  12.043  55.967  1.00 19.75           O  
ATOM   2602  CB  CYS B 115      35.219  10.604  53.452  1.00 19.06           C  
ATOM   2603  SG  CYS B 115      35.448   9.708  51.904  1.00 27.40           S  
ATOM   2604  H   CYS B 115      37.790  10.668  53.277  1.00  0.00           H  
ATOM   2605  N   THR B 116      34.952  13.550  54.962  1.00 18.52           N  
ATOM   2606  CA  THR B 116      34.464  14.108  56.217  1.00 18.47           C  
ATOM   2607  C   THR B 116      32.987  13.758  56.434  1.00 20.72           C  
ATOM   2608  O   THR B 116      32.277  14.419  57.195  1.00 21.88           O  
ATOM   2609  CB  THR B 116      34.643  15.639  56.252  1.00 21.10           C  
ATOM   2610  OG1 THR B 116      33.913  16.237  55.175  1.00 21.06           O  
ATOM   2611  CG2 THR B 116      36.119  16.005  56.121  1.00 19.49           C  
ATOM   2612  H   THR B 116      34.676  13.961  54.111  1.00  0.00           H  
ATOM   2613  HG1 THR B 116      33.840  17.167  55.384  1.00  0.00           H  
ATOM   2614  N   ALA B 117      32.560  12.666  55.806  1.00 18.76           N  
ATOM   2615  CA  ALA B 117      31.172  12.207  55.850  1.00 19.39           C  
ATOM   2616  C   ALA B 117      31.044  10.865  55.132  1.00 22.72           C  
ATOM   2617  O   ALA B 117      32.019  10.350  54.578  1.00 27.18           O  
ATOM   2618  CB  ALA B 117      30.248  13.232  55.199  1.00 10.96           C  
ATOM   2619  H   ALA B 117      33.195  12.178  55.250  1.00  0.00           H  
ATOM   2620  N   LYS B 118      29.861  10.265  55.205  1.00 26.04           N  
ATOM   2621  CA  LYS B 118      29.581   9.039  54.462  1.00 25.30           C  
ATOM   2622  C   LYS B 118      29.269   9.401  53.006  1.00 24.65           C  
ATOM   2623  O   LYS B 118      28.375  10.202  52.743  1.00 26.43           O  
ATOM   2624  CB  LYS B 118      28.396   8.304  55.092  1.00 24.51           C  
ATOM   2625  CG  LYS B 118      28.430   6.790  54.935  1.00 27.43           C  
ATOM   2626  CD  LYS B 118      27.211   6.164  55.592  1.00 39.09           C  
ATOM   2627  CE  LYS B 118      27.461   4.718  55.986  1.00 49.21           C  
ATOM   2628  NZ  LYS B 118      27.176   3.762  54.884  1.00 49.51           N  
ATOM   2629  H   LYS B 118      29.151  10.693  55.722  1.00  0.00           H  
ATOM   2630  HZ1 LYS B 118      26.193   3.880  54.569  1.00  0.00           H  
ATOM   2631  HZ2 LYS B 118      27.831   3.914  54.094  1.00  0.00           H  
ATOM   2632  HZ3 LYS B 118      27.300   2.797  55.258  1.00  0.00           H  
ATOM   2633  N   THR B 119      30.077   8.894  52.079  1.00 25.44           N  
ATOM   2634  CA  THR B 119      29.960   9.259  50.663  1.00 19.86           C  
ATOM   2635  C   THR B 119      29.676   8.030  49.796  1.00 24.91           C  
ATOM   2636  O   THR B 119      30.439   7.691  48.887  1.00 28.02           O  
ATOM   2637  CB  THR B 119      31.242   9.949  50.150  1.00 18.36           C  
ATOM   2638  OG1 THR B 119      32.374   9.098  50.383  1.00 20.93           O  
ATOM   2639  CG2 THR B 119      31.454  11.276  50.854  1.00 14.05           C  
ATOM   2640  H   THR B 119      30.750   8.244  52.369  1.00  0.00           H  
ATOM   2641  HG1 THR B 119      32.753   9.348  51.236  1.00  0.00           H  
ATOM   2642  N   GLU B 120      28.507   7.440  50.010  1.00 22.55           N  
ATOM   2643  CA  GLU B 120      28.182   6.129  49.462  1.00 19.41           C  
ATOM   2644  C   GLU B 120      28.209   6.073  47.932  1.00 19.97           C  
ATOM   2645  O   GLU B 120      28.634   5.074  47.350  1.00 21.36           O  
ATOM   2646  CB  GLU B 120      26.811   5.678  49.976  1.00 29.10           C  
ATOM   2647  CG  GLU B 120      26.661   5.735  51.493  1.00 29.85           C  
ATOM   2648  CD  GLU B 120      25.871   6.947  51.977  1.00 30.57           C  
ATOM   2649  OE1 GLU B 120      26.143   8.080  51.520  1.00 27.33           O  
ATOM   2650  OE2 GLU B 120      24.993   6.769  52.850  1.00 37.12           O  
ATOM   2651  H   GLU B 120      27.884   7.938  50.565  1.00  0.00           H  
ATOM   2652  N   TRP B 121      27.868   7.187  47.290  1.00 21.12           N  
ATOM   2653  CA  TRP B 121      27.813   7.248  45.827  1.00 23.63           C  
ATOM   2654  C   TRP B 121      29.193   7.190  45.170  1.00 28.74           C  
ATOM   2655  O   TRP B 121      29.308   7.208  43.942  1.00 29.26           O  
ATOM   2656  CB  TRP B 121      27.092   8.519  45.372  1.00 17.40           C  
ATOM   2657  CG  TRP B 121      27.701   9.773  45.898  1.00 20.39           C  
ATOM   2658  CD1 TRP B 121      28.625  10.565  45.273  1.00 20.33           C  
ATOM   2659  CD2 TRP B 121      27.463  10.366  47.177  1.00 20.14           C  
ATOM   2660  NE1 TRP B 121      28.986  11.607  46.090  1.00 13.50           N  
ATOM   2661  CE2 TRP B 121      28.289  11.509  47.267  1.00 20.80           C  
ATOM   2662  CE3 TRP B 121      26.632  10.042  48.257  1.00 22.09           C  
ATOM   2663  CZ2 TRP B 121      28.309  12.330  48.397  1.00 19.74           C  
ATOM   2664  CZ3 TRP B 121      26.648  10.861  49.379  1.00 22.65           C  
ATOM   2665  CH2 TRP B 121      27.482  11.993  49.439  1.00 21.96           C  
ATOM   2666  H   TRP B 121      27.600   7.942  47.837  1.00  0.00           H  
ATOM   2667  HE1 TRP B 121      29.605  12.330  45.827  1.00  0.00           H  
ATOM   2668  N   LEU B 122      30.238   7.197  45.993  1.00 23.20           N  
ATOM   2669  CA  LEU B 122      31.601   7.107  45.490  1.00 19.55           C  
ATOM   2670  C   LEU B 122      32.076   5.664  45.385  1.00 14.44           C  
ATOM   2671  O   LEU B 122      33.129   5.392  44.806  1.00 21.47           O  
ATOM   2672  CB  LEU B 122      32.549   7.909  46.385  1.00 19.06           C  
ATOM   2673  CG  LEU B 122      32.277   9.414  46.412  1.00 18.56           C  
ATOM   2674  CD1 LEU B 122      33.340  10.119  47.233  1.00 16.19           C  
ATOM   2675  CD2 LEU B 122      32.255   9.957  44.990  1.00 17.36           C  
ATOM   2676  H   LEU B 122      30.075   7.328  46.946  1.00  0.00           H  
ATOM   2677  N   ASP B 123      31.287   4.741  45.923  1.00 11.19           N  
ATOM   2678  CA  ASP B 123      31.634   3.322  45.901  1.00 19.95           C  
ATOM   2679  C   ASP B 123      31.594   2.759  44.486  1.00 24.38           C  
ATOM   2680  O   ASP B 123      30.632   2.980  43.748  1.00 27.75           O  
ATOM   2681  CB  ASP B 123      30.682   2.524  46.796  1.00 26.59           C  
ATOM   2682  CG  ASP B 123      30.822   2.875  48.269  1.00 30.12           C  
ATOM   2683  OD1 ASP B 123      31.641   3.754  48.615  1.00 28.58           O  
ATOM   2684  OD2 ASP B 123      30.091   2.279  49.084  1.00 32.87           O  
ATOM   2685  H   ASP B 123      30.400   5.012  46.250  1.00  0.00           H  
ATOM   2686  N   GLY B 124      32.667   2.078  44.096  1.00 21.56           N  
ATOM   2687  CA  GLY B 124      32.774   1.584  42.732  1.00 20.48           C  
ATOM   2688  C   GLY B 124      33.403   2.573  41.767  1.00 16.37           C  
ATOM   2689  O   GLY B 124      33.747   2.217  40.647  1.00 25.75           O  
ATOM   2690  H   GLY B 124      33.359   1.869  44.752  1.00  0.00           H  
ATOM   2691  N   LYS B 125      33.585   3.810  42.211  1.00 17.83           N  
ATOM   2692  CA  LYS B 125      34.218   4.837  41.388  1.00 21.08           C  
ATOM   2693  C   LYS B 125      35.617   5.210  41.884  1.00 21.37           C  
ATOM   2694  O   LYS B 125      36.479   5.592  41.098  1.00 29.02           O  
ATOM   2695  CB  LYS B 125      33.344   6.092  41.350  1.00 22.26           C  
ATOM   2696  CG  LYS B 125      31.979   5.891  40.714  1.00 23.88           C  
ATOM   2697  CD  LYS B 125      31.225   7.202  40.664  1.00 33.58           C  
ATOM   2698  CE  LYS B 125      29.831   7.022  40.095  1.00 46.91           C  
ATOM   2699  NZ  LYS B 125      28.967   8.208  40.378  1.00 50.93           N  
ATOM   2700  H   LYS B 125      33.184   4.045  43.070  1.00  0.00           H  
ATOM   2701  HZ1 LYS B 125      29.407   9.061  39.977  1.00  0.00           H  
ATOM   2702  HZ2 LYS B 125      28.032   8.063  39.947  1.00  0.00           H  
ATOM   2703  HZ3 LYS B 125      28.861   8.322  41.407  1.00  0.00           H  
ATOM   2704  N   HIS B 126      35.794   5.223  43.201  1.00 23.87           N  
ATOM   2705  CA  HIS B 126      37.073   5.590  43.811  1.00 15.58           C  
ATOM   2706  C   HIS B 126      37.583   4.479  44.726  1.00 18.59           C  
ATOM   2707  O   HIS B 126      36.801   3.856  45.454  1.00 20.76           O  
ATOM   2708  CB  HIS B 126      36.916   6.879  44.611  1.00 10.56           C  
ATOM   2709  CG  HIS B 126      36.464   8.043  43.790  1.00  9.05           C  
ATOM   2710  ND1 HIS B 126      37.344   8.905  43.173  1.00 16.64           N  
ATOM   2711  CD2 HIS B 126      35.223   8.498  43.494  1.00 14.62           C  
ATOM   2712  CE1 HIS B 126      36.668   9.845  42.537  1.00  9.61           C  
ATOM   2713  NE2 HIS B 126      35.379   9.621  42.718  1.00 14.72           N  
ATOM   2714  H   HIS B 126      35.044   4.925  43.759  1.00  0.00           H  
ATOM   2715  HD1 HIS B 126      38.326   8.820  43.209  1.00  0.00           H  
ATOM   2716  HE2 HIS B 126      34.655  10.169  42.323  1.00  0.00           H  
ATOM   2717  N   VAL B 127      38.887   4.222  44.675  1.00 19.92           N  
ATOM   2718  CA  VAL B 127      39.482   3.144  45.466  1.00 22.68           C  
ATOM   2719  C   VAL B 127      39.795   3.561  46.910  1.00 22.10           C  
ATOM   2720  O   VAL B 127      40.484   4.557  47.154  1.00 22.57           O  
ATOM   2721  CB  VAL B 127      40.768   2.594  44.789  1.00 24.98           C  
ATOM   2722  CG1 VAL B 127      41.404   1.503  45.651  1.00 21.21           C  
ATOM   2723  CG2 VAL B 127      40.428   2.029  43.417  1.00 15.59           C  
ATOM   2724  H   VAL B 127      39.446   4.742  44.059  1.00  0.00           H  
ATOM   2725  N   VAL B 128      39.136   2.894  47.852  1.00 23.08           N  
ATOM   2726  CA  VAL B 128      39.412   3.065  49.277  1.00 17.56           C  
ATOM   2727  C   VAL B 128      40.615   2.208  49.683  1.00 19.22           C  
ATOM   2728  O   VAL B 128      40.640   0.993  49.441  1.00 15.05           O  
ATOM   2729  CB  VAL B 128      38.189   2.656  50.126  1.00 14.30           C  
ATOM   2730  CG1 VAL B 128      38.523   2.736  51.614  1.00 16.90           C  
ATOM   2731  CG2 VAL B 128      37.014   3.553  49.801  1.00  7.98           C  
ATOM   2732  H   VAL B 128      38.473   2.234  47.548  1.00  0.00           H  
ATOM   2733  N   PHE B 129      41.621   2.847  50.276  1.00 19.65           N  
ATOM   2734  CA  PHE B 129      42.868   2.151  50.596  1.00 21.17           C  
ATOM   2735  C   PHE B 129      43.421   2.473  51.983  1.00 20.30           C  
ATOM   2736  O   PHE B 129      44.504   2.022  52.345  1.00 24.40           O  
ATOM   2737  CB  PHE B 129      43.928   2.450  49.529  1.00 13.98           C  
ATOM   2738  CG  PHE B 129      44.366   3.881  49.496  1.00 11.74           C  
ATOM   2739  CD1 PHE B 129      43.577   4.847  48.885  1.00  7.87           C  
ATOM   2740  CD2 PHE B 129      45.541   4.273  50.126  1.00  9.58           C  
ATOM   2741  CE1 PHE B 129      43.946   6.187  48.907  1.00  6.01           C  
ATOM   2742  CE2 PHE B 129      45.914   5.604  50.155  1.00  9.32           C  
ATOM   2743  CZ  PHE B 129      45.114   6.568  49.544  1.00  8.87           C  
ATOM   2744  H   PHE B 129      41.499   3.802  50.471  1.00  0.00           H  
ATOM   2745  N   GLY B 130      42.672   3.239  52.763  1.00 20.50           N  
ATOM   2746  CA  GLY B 130      43.105   3.551  54.111  1.00 17.89           C  
ATOM   2747  C   GLY B 130      42.057   4.271  54.933  1.00 23.99           C  
ATOM   2748  O   GLY B 130      40.952   4.547  54.459  1.00 27.32           O  
ATOM   2749  H   GLY B 130      41.822   3.599  52.436  1.00  0.00           H  
ATOM   2750  N   LYS B 131      42.417   4.601  56.166  1.00 21.00           N  
ATOM   2751  CA  LYS B 131      41.556   5.399  57.030  1.00 22.31           C  
ATOM   2752  C   LYS B 131      42.388   6.152  58.069  1.00 22.32           C  
ATOM   2753  O   LYS B 131      43.475   5.703  58.451  1.00 26.68           O  
ATOM   2754  CB  LYS B 131      40.536   4.499  57.734  1.00 24.93           C  
ATOM   2755  CG  LYS B 131      39.262   5.224  58.127  1.00 35.60           C  
ATOM   2756  CD  LYS B 131      38.362   4.368  58.995  1.00 35.09           C  
ATOM   2757  CE  LYS B 131      37.325   5.229  59.694  1.00 32.74           C  
ATOM   2758  NZ  LYS B 131      36.629   4.473  60.770  1.00 52.03           N  
ATOM   2759  H   LYS B 131      43.285   4.273  56.491  1.00  0.00           H  
ATOM   2760  HZ1 LYS B 131      37.320   4.137  61.470  1.00  0.00           H  
ATOM   2761  HZ2 LYS B 131      35.920   5.074  61.234  1.00  0.00           H  
ATOM   2762  HZ3 LYS B 131      36.154   3.652  60.341  1.00  0.00           H  
ATOM   2763  N   VAL B 132      41.907   7.321  58.481  1.00 20.28           N  
ATOM   2764  CA  VAL B 132      42.562   8.083  59.539  1.00 21.90           C  
ATOM   2765  C   VAL B 132      42.645   7.261  60.824  1.00 27.71           C  
ATOM   2766  O   VAL B 132      41.648   6.698  61.277  1.00 32.99           O  
ATOM   2767  CB  VAL B 132      41.814   9.397  59.841  1.00 16.45           C  
ATOM   2768  CG1 VAL B 132      42.463  10.112  61.020  1.00 18.84           C  
ATOM   2769  CG2 VAL B 132      41.817  10.294  58.620  1.00 18.49           C  
ATOM   2770  H   VAL B 132      41.085   7.654  58.073  1.00  0.00           H  
ATOM   2771  N   LYS B 133      43.866   7.077  61.314  1.00 30.26           N  
ATOM   2772  CA  LYS B 133      44.104   6.399  62.583  1.00 27.89           C  
ATOM   2773  C   LYS B 133      43.961   7.395  63.731  1.00 29.03           C  
ATOM   2774  O   LYS B 133      43.206   7.171  64.675  1.00 33.72           O  
ATOM   2775  CB  LYS B 133      45.506   5.795  62.590  1.00 29.15           C  
ATOM   2776  CG  LYS B 133      45.657   4.581  63.474  1.00 34.58           C  
ATOM   2777  CD  LYS B 133      47.051   4.001  63.355  1.00 42.35           C  
ATOM   2778  CE  LYS B 133      47.107   2.587  63.901  1.00 51.33           C  
ATOM   2779  NZ  LYS B 133      48.373   1.899  63.523  1.00 66.27           N  
ATOM   2780  H   LYS B 133      44.602   7.348  60.741  1.00  0.00           H  
ATOM   2781  HZ1 LYS B 133      48.466   1.892  62.487  1.00  0.00           H  
ATOM   2782  HZ2 LYS B 133      49.181   2.409  63.935  1.00  0.00           H  
ATOM   2783  HZ3 LYS B 133      48.363   0.923  63.880  1.00  0.00           H  
ATOM   2784  N   GLU B 134      44.636   8.532  63.602  1.00 27.51           N  
ATOM   2785  CA  GLU B 134      44.543   9.600  64.590  1.00 27.96           C  
ATOM   2786  C   GLU B 134      44.601  10.981  63.947  1.00 21.60           C  
ATOM   2787  O   GLU B 134      45.256  11.172  62.929  1.00 29.10           O  
ATOM   2788  CB  GLU B 134      45.664   9.465  65.624  1.00 36.29           C  
ATOM   2789  CG  GLU B 134      45.365   8.468  66.734  1.00 42.40           C  
ATOM   2790  CD  GLU B 134      46.611   8.027  67.465  1.00 53.60           C  
ATOM   2791  OE1 GLU B 134      47.101   8.789  68.325  1.00 62.00           O  
ATOM   2792  OE2 GLU B 134      47.108   6.919  67.172  1.00 64.58           O  
ATOM   2793  H   GLU B 134      45.222   8.640  62.821  1.00  0.00           H  
ATOM   2794  N   GLY B 135      43.873  11.931  64.519  1.00 20.05           N  
ATOM   2795  CA  GLY B 135      43.899  13.288  64.009  1.00 14.38           C  
ATOM   2796  C   GLY B 135      42.703  13.702  63.167  1.00 21.16           C  
ATOM   2797  O   GLY B 135      42.771  14.721  62.480  1.00 29.35           O  
ATOM   2798  H   GLY B 135      43.454  11.739  65.370  1.00  0.00           H  
ATOM   2799  N   MET B 136      41.587  12.979  63.271  1.00 20.49           N  
ATOM   2800  CA  MET B 136      40.345  13.377  62.592  1.00 19.18           C  
ATOM   2801  C   MET B 136      39.940  14.807  62.943  1.00 22.65           C  
ATOM   2802  O   MET B 136      39.352  15.515  62.127  1.00 24.55           O  
ATOM   2803  CB  MET B 136      39.195  12.434  62.955  1.00 23.96           C  
ATOM   2804  CG  MET B 136      38.735  11.510  61.826  1.00 34.73           C  
ATOM   2805  SD  MET B 136      38.647  12.290  60.190  1.00 33.99           S  
ATOM   2806  CE  MET B 136      37.216  13.330  60.360  1.00 32.01           C  
ATOM   2807  H   MET B 136      41.642  12.140  63.763  1.00  0.00           H  
ATOM   2808  N   ASN B 137      40.317  15.243  64.140  1.00 21.12           N  
ATOM   2809  CA  ASN B 137      40.057  16.608  64.590  1.00 24.74           C  
ATOM   2810  C   ASN B 137      40.880  17.630  63.807  1.00 22.44           C  
ATOM   2811  O   ASN B 137      40.475  18.781  63.656  1.00 24.51           O  
ATOM   2812  CB  ASN B 137      40.358  16.733  66.085  1.00 36.87           C  
ATOM   2813  CG  ASN B 137      41.766  16.270  66.439  1.00 49.80           C  
ATOM   2814  OD1 ASN B 137      42.143  15.133  66.158  1.00 55.17           O  
ATOM   2815  ND2 ASN B 137      42.562  17.163  67.011  1.00 47.15           N  
ATOM   2816  H   ASN B 137      40.776  14.617  64.739  1.00  0.00           H  
ATOM   2817 HD21 ASN B 137      43.446  16.807  67.225  1.00  0.00           H  
ATOM   2818 HD22 ASN B 137      42.246  18.066  67.195  1.00  0.00           H  
ATOM   2819  N   ILE B 138      42.045  17.207  63.327  1.00 20.80           N  
ATOM   2820  CA  ILE B 138      42.855  18.036  62.433  1.00 21.80           C  
ATOM   2821  C   ILE B 138      42.201  18.167  61.056  1.00 20.86           C  
ATOM   2822  O   ILE B 138      42.138  19.261  60.498  1.00 21.26           O  
ATOM   2823  CB  ILE B 138      44.280  17.453  62.259  1.00 23.50           C  
ATOM   2824  CG1 ILE B 138      44.970  17.333  63.624  1.00 23.30           C  
ATOM   2825  CG2 ILE B 138      45.108  18.339  61.320  1.00 17.17           C  
ATOM   2826  CD1 ILE B 138      45.112  18.653  64.367  1.00 23.79           C  
ATOM   2827  H   ILE B 138      42.371  16.320  63.579  1.00  0.00           H  
ATOM   2828  N   VAL B 139      41.643  17.067  60.555  1.00 19.30           N  
ATOM   2829  CA  VAL B 139      40.888  17.083  59.302  1.00 17.24           C  
ATOM   2830  C   VAL B 139      39.658  17.991  59.399  1.00 17.98           C  
ATOM   2831  O   VAL B 139      39.447  18.857  58.549  1.00 19.04           O  
ATOM   2832  CB  VAL B 139      40.443  15.658  58.897  1.00 24.35           C  
ATOM   2833  CG1 VAL B 139      39.704  15.695  57.558  1.00 23.14           C  
ATOM   2834  CG2 VAL B 139      41.657  14.735  58.811  1.00 16.81           C  
ATOM   2835  H   VAL B 139      41.791  16.227  61.041  1.00  0.00           H  
ATOM   2836  N   GLU B 140      38.914  17.865  60.494  1.00 18.59           N  
ATOM   2837  CA  GLU B 140      37.811  18.778  60.786  1.00 17.95           C  
ATOM   2838  C   GLU B 140      38.274  20.230  60.856  1.00 19.97           C  
ATOM   2839  O   GLU B 140      37.572  21.134  60.410  1.00 30.64           O  
ATOM   2840  CB  GLU B 140      37.139  18.392  62.101  1.00 15.98           C  
ATOM   2841  CG  GLU B 140      36.403  17.064  62.057  1.00 29.14           C  
ATOM   2842  CD  GLU B 140      36.229  16.432  63.430  1.00 36.67           C  
ATOM   2843  OE1 GLU B 140      36.195  17.169  64.440  1.00 42.66           O  
ATOM   2844  OE2 GLU B 140      36.134  15.189  63.501  1.00 43.70           O  
ATOM   2845  H   GLU B 140      39.088  17.100  61.079  1.00  0.00           H  
ATOM   2846  N   ALA B 141      39.466  20.450  61.399  1.00 25.74           N  
ATOM   2847  CA  ALA B 141      40.082  21.779  61.403  1.00 26.20           C  
ATOM   2848  C   ALA B 141      40.398  22.264  59.986  1.00 25.94           C  
ATOM   2849  O   ALA B 141      40.170  23.425  59.653  1.00 27.39           O  
ATOM   2850  CB  ALA B 141      41.355  21.765  62.245  1.00 23.33           C  
ATOM   2851  H   ALA B 141      39.912  19.713  61.865  1.00  0.00           H  
ATOM   2852  N   MET B 142      40.897  21.359  59.149  1.00 28.61           N  
ATOM   2853  CA  MET B 142      41.224  21.679  57.760  1.00 25.56           C  
ATOM   2854  C   MET B 142      39.989  22.106  56.971  1.00 26.68           C  
ATOM   2855  O   MET B 142      39.987  23.157  56.326  1.00 21.44           O  
ATOM   2856  CB  MET B 142      41.864  20.469  57.076  1.00 24.43           C  
ATOM   2857  CG  MET B 142      43.268  20.155  57.547  1.00 19.10           C  
ATOM   2858  SD  MET B 142      43.722  18.450  57.215  1.00 27.63           S  
ATOM   2859  CE  MET B 142      43.505  18.368  55.450  1.00 14.44           C  
ATOM   2860  H   MET B 142      41.039  20.452  59.489  1.00  0.00           H  
ATOM   2861  N   GLU B 143      38.906  21.345  57.111  1.00 29.02           N  
ATOM   2862  CA  GLU B 143      37.700  21.594  56.325  1.00 33.64           C  
ATOM   2863  C   GLU B 143      37.038  22.933  56.644  1.00 32.66           C  
ATOM   2864  O   GLU B 143      36.321  23.489  55.813  1.00 39.76           O  
ATOM   2865  CB  GLU B 143      36.701  20.439  56.484  1.00 30.21           C  
ATOM   2866  CG  GLU B 143      35.850  20.472  57.732  1.00 33.21           C  
ATOM   2867  CD  GLU B 143      34.827  19.353  57.763  1.00 43.43           C  
ATOM   2868  OE1 GLU B 143      34.098  19.181  56.764  1.00 51.22           O  
ATOM   2869  OE2 GLU B 143      34.750  18.641  58.787  1.00 51.60           O  
ATOM   2870  H   GLU B 143      38.949  20.587  57.734  1.00  0.00           H  
ATOM   2871  N   ARG B 144      37.413  23.517  57.776  1.00 32.15           N  
ATOM   2872  CA  ARG B 144      36.933  24.839  58.157  1.00 31.88           C  
ATOM   2873  C   ARG B 144      37.539  25.961  57.309  1.00 32.82           C  
ATOM   2874  O   ARG B 144      37.088  27.104  57.366  1.00 36.49           O  
ATOM   2875  CB  ARG B 144      37.220  25.091  59.641  1.00 36.37           C  
ATOM   2876  CG  ARG B 144      36.309  24.330  60.590  0.00 35.21           C  
ATOM   2877  CD  ARG B 144      36.730  24.531  62.038  0.00 37.26           C  
ATOM   2878  NE  ARG B 144      35.707  24.077  62.978  0.00 38.05           N  
ATOM   2879  CZ  ARG B 144      35.616  22.838  63.454  0.00 38.40           C  
ATOM   2880  NH1 ARG B 144      36.474  21.904  63.067  0.00 38.11           N  
ATOM   2881  NH2 ARG B 144      34.655  22.530  64.313  0.00 38.21           N  
ATOM   2882  H   ARG B 144      38.002  23.028  58.387  1.00  0.00           H  
ATOM   2883  HE  ARG B 144      35.038  24.728  63.279  1.00  0.00           H  
ATOM   2884 HH11 ARG B 144      37.192  22.115  62.403  1.00  0.00           H  
ATOM   2885 HH12 ARG B 144      36.390  20.976  63.430  1.00  0.00           H  
ATOM   2886 HH21 ARG B 144      34.002  23.230  64.602  1.00  0.00           H  
ATOM   2887 HH22 ARG B 144      34.586  21.601  64.676  1.00  0.00           H  
ATOM   2888  N   PHE B 145      38.577  25.638  56.545  1.00 36.69           N  
ATOM   2889  CA  PHE B 145      39.145  26.582  55.581  1.00 33.76           C  
ATOM   2890  C   PHE B 145      38.682  26.283  54.154  1.00 31.25           C  
ATOM   2891  O   PHE B 145      39.198  26.854  53.186  1.00 29.05           O  
ATOM   2892  CB  PHE B 145      40.673  26.547  55.641  1.00 34.56           C  
ATOM   2893  CG  PHE B 145      41.229  26.824  57.002  1.00 33.03           C  
ATOM   2894  CD1 PHE B 145      41.394  28.130  57.447  1.00 29.81           C  
ATOM   2895  CD2 PHE B 145      41.569  25.778  57.851  1.00 37.12           C  
ATOM   2896  CE1 PHE B 145      41.888  28.390  58.719  1.00 32.47           C  
ATOM   2897  CE2 PHE B 145      42.064  26.028  59.126  1.00 39.57           C  
ATOM   2898  CZ  PHE B 145      42.224  27.338  59.561  1.00 33.20           C  
ATOM   2899  H   PHE B 145      39.012  24.780  56.699  1.00  0.00           H  
ATOM   2900  N   GLY B 146      37.732  25.363  54.032  1.00 34.31           N  
ATOM   2901  CA  GLY B 146      37.215  24.996  52.727  1.00 38.81           C  
ATOM   2902  C   GLY B 146      36.075  25.882  52.266  1.00 41.82           C  
ATOM   2903  O   GLY B 146      35.749  26.878  52.914  1.00 41.28           O  
ATOM   2904  H   GLY B 146      37.336  24.977  54.838  1.00  0.00           H  
ATOM   2905  N   SER B 147      35.470  25.518  51.139  1.00 43.40           N  
ATOM   2906  CA  SER B 147      34.330  26.256  50.597  1.00 40.19           C  
ATOM   2907  C   SER B 147      33.496  25.359  49.695  1.00 41.11           C  
ATOM   2908  O   SER B 147      33.912  24.251  49.363  1.00 45.02           O  
ATOM   2909  CB  SER B 147      34.803  27.475  49.803  1.00 42.32           C  
ATOM   2910  OG  SER B 147      35.267  27.100  48.518  1.00 44.72           O  
ATOM   2911  H   SER B 147      35.809  24.719  50.677  1.00  0.00           H  
ATOM   2912  HG  SER B 147      36.208  27.319  48.508  1.00  0.00           H  
ATOM   2913  N   ARG B 148      32.358  25.873  49.232  1.00 45.32           N  
ATOM   2914  CA  ARG B 148      31.405  25.081  48.447  1.00 43.46           C  
ATOM   2915  C   ARG B 148      31.997  24.464  47.180  1.00 34.48           C  
ATOM   2916  O   ARG B 148      31.721  23.311  46.854  1.00 30.41           O  
ATOM   2917  CB  ARG B 148      30.188  25.933  48.071  1.00 52.00           C  
ATOM   2918  CG  ARG B 148      29.109  25.168  47.313  1.00 62.90           C  
ATOM   2919  CD  ARG B 148      28.014  26.095  46.813  1.00 71.18           C  
ATOM   2920  NE  ARG B 148      27.079  25.404  45.930  1.00 73.48           N  
ATOM   2921  CZ  ARG B 148      27.087  25.502  44.604  1.00 74.09           C  
ATOM   2922  NH1 ARG B 148      27.986  26.263  43.993  1.00 77.21           N  
ATOM   2923  NH2 ARG B 148      26.198  24.832  43.885  1.00 79.32           N  
ATOM   2924  H   ARG B 148      32.167  26.807  49.443  1.00  0.00           H  
ATOM   2925  HE  ARG B 148      26.407  24.818  46.339  1.00  0.00           H  
ATOM   2926 HH11 ARG B 148      28.664  26.772  44.522  1.00  0.00           H  
ATOM   2927 HH12 ARG B 148      27.967  26.340  42.997  1.00  0.00           H  
ATOM   2928 HH21 ARG B 148      25.533  24.242  44.345  1.00  0.00           H  
ATOM   2929 HH22 ARG B 148      26.196  24.903  42.888  1.00  0.00           H  
ATOM   2930  N   ASN B 149      32.774  25.247  46.442  1.00 31.94           N  
ATOM   2931  CA  ASN B 149      33.391  24.746  45.218  1.00 37.51           C  
ATOM   2932  C   ASN B 149      34.709  24.022  45.477  1.00 33.43           C  
ATOM   2933  O   ASN B 149      35.266  23.395  44.576  1.00 39.38           O  
ATOM   2934  CB  ASN B 149      33.606  25.887  44.215  1.00 43.56           C  
ATOM   2935  CG  ASN B 149      34.337  27.072  44.817  1.00 46.35           C  
ATOM   2936  OD1 ASN B 149      34.905  26.983  45.900  1.00 45.78           O  
ATOM   2937  ND2 ASN B 149      34.317  28.193  44.118  1.00 47.13           N  
ATOM   2938  H   ASN B 149      33.001  26.137  46.783  1.00  0.00           H  
ATOM   2939 HD21 ASN B 149      34.809  28.928  44.531  1.00  0.00           H  
ATOM   2940 HD22 ASN B 149      33.856  28.230  43.261  1.00  0.00           H  
ATOM   2941  N   GLY B 150      35.202  24.115  46.709  1.00 30.85           N  
ATOM   2942  CA  GLY B 150      36.447  23.457  47.066  1.00 24.95           C  
ATOM   2943  C   GLY B 150      37.629  24.385  47.282  1.00 21.52           C  
ATOM   2944  O   GLY B 150      38.689  23.945  47.713  1.00 24.96           O  
ATOM   2945  H   GLY B 150      34.699  24.606  47.388  1.00  0.00           H  
ATOM   2946  N   LYS B 151      37.442  25.674  47.032  1.00 27.64           N  
ATOM   2947  CA  LYS B 151      38.528  26.643  47.165  1.00 29.88           C  
ATOM   2948  C   LYS B 151      38.840  26.942  48.627  1.00 31.95           C  
ATOM   2949  O   LYS B 151      37.933  27.196  49.422  1.00 32.61           O  
ATOM   2950  CB  LYS B 151      38.173  27.942  46.439  1.00 33.38           C  
ATOM   2951  CG  LYS B 151      39.308  28.950  46.374  1.00 34.89           C  
ATOM   2952  CD  LYS B 151      38.837  30.276  45.794  1.00 41.89           C  
ATOM   2953  CE  LYS B 151      39.900  31.351  45.948  1.00 49.37           C  
ATOM   2954  NZ  LYS B 151      39.396  32.693  45.552  1.00 47.05           N  
ATOM   2955  H   LYS B 151      36.543  25.970  46.769  1.00  0.00           H  
ATOM   2956  HZ1 LYS B 151      39.091  32.671  44.558  1.00  0.00           H  
ATOM   2957  HZ2 LYS B 151      38.594  32.956  46.159  1.00  0.00           H  
ATOM   2958  HZ3 LYS B 151      40.159  33.391  45.664  1.00  0.00           H  
ATOM   2959  N   THR B 152      40.130  26.966  48.957  1.00 35.77           N  
ATOM   2960  CA  THR B 152      40.592  27.164  50.333  1.00 26.43           C  
ATOM   2961  C   THR B 152      40.930  28.626  50.622  1.00 23.58           C  
ATOM   2962  O   THR B 152      41.538  29.304  49.798  1.00 19.56           O  
ATOM   2963  CB  THR B 152      41.844  26.307  50.634  1.00 21.50           C  
ATOM   2964  OG1 THR B 152      42.906  26.677  49.748  1.00 24.28           O  
ATOM   2965  CG2 THR B 152      41.539  24.839  50.441  1.00 10.12           C  
ATOM   2966  H   THR B 152      40.804  26.853  48.257  1.00  0.00           H  
ATOM   2967  HG1 THR B 152      43.762  26.520  50.174  1.00  0.00           H  
ATOM   2968  N   SER B 153      40.498  29.119  51.780  1.00 20.47           N  
ATOM   2969  CA  SER B 153      40.769  30.505  52.167  1.00 21.11           C  
ATOM   2970  C   SER B 153      42.137  30.688  52.830  1.00 21.77           C  
ATOM   2971  O   SER B 153      42.585  31.813  53.052  1.00 25.82           O  
ATOM   2972  CB  SER B 153      39.676  31.020  53.105  1.00 20.38           C  
ATOM   2973  OG  SER B 153      39.588  30.219  54.268  1.00 39.20           O  
ATOM   2974  H   SER B 153      39.960  28.532  52.359  1.00  0.00           H  
ATOM   2975  HG  SER B 153      38.690  30.250  54.618  1.00  0.00           H  
ATOM   2976  N   LYS B 154      42.793  29.579  53.152  1.00 22.22           N  
ATOM   2977  CA  LYS B 154      44.153  29.611  53.677  1.00 18.10           C  
ATOM   2978  C   LYS B 154      44.979  28.469  53.093  1.00 17.54           C  
ATOM   2979  O   LYS B 154      44.484  27.354  52.937  1.00 14.88           O  
ATOM   2980  CB  LYS B 154      44.138  29.505  55.207  1.00 25.92           C  
ATOM   2981  CG  LYS B 154      43.984  30.840  55.929  1.00 34.02           C  
ATOM   2982  CD  LYS B 154      44.181  30.680  57.430  1.00 47.62           C  
ATOM   2983  CE  LYS B 154      44.363  32.019  58.133  1.00 52.84           C  
ATOM   2984  NZ  LYS B 154      43.124  32.846  58.124  1.00 60.32           N  
ATOM   2985  H   LYS B 154      42.334  28.726  53.031  1.00  0.00           H  
ATOM   2986  HZ1 LYS B 154      42.345  32.344  58.593  1.00  0.00           H  
ATOM   2987  HZ2 LYS B 154      43.312  33.743  58.617  1.00  0.00           H  
ATOM   2988  HZ3 LYS B 154      42.866  33.049  57.137  1.00  0.00           H  
ATOM   2989  N   LYS B 155      46.248  28.746  52.804  1.00 18.54           N  
ATOM   2990  CA  LYS B 155      47.149  27.743  52.243  1.00 21.03           C  
ATOM   2991  C   LYS B 155      47.405  26.574  53.190  1.00 23.80           C  
ATOM   2992  O   LYS B 155      48.204  26.677  54.121  1.00 28.66           O  
ATOM   2993  CB  LYS B 155      48.478  28.387  51.851  1.00 19.86           C  
ATOM   2994  CG  LYS B 155      49.304  27.548  50.895  1.00 26.23           C  
ATOM   2995  CD  LYS B 155      50.248  28.419  50.087  1.00 36.04           C  
ATOM   2996  CE  LYS B 155      50.645  27.743  48.784  1.00 47.01           C  
ATOM   2997  NZ  LYS B 155      51.801  26.818  48.938  1.00 55.55           N  
ATOM   2998  H   LYS B 155      46.548  29.666  52.940  1.00  0.00           H  
ATOM   2999  HZ1 LYS B 155      51.616  26.116  49.680  1.00  0.00           H  
ATOM   3000  HZ2 LYS B 155      51.961  26.339  48.028  1.00  0.00           H  
ATOM   3001  HZ3 LYS B 155      52.640  27.383  49.180  1.00  0.00           H  
ATOM   3002  N   ILE B 156      46.748  25.452  52.922  1.00 25.66           N  
ATOM   3003  CA  ILE B 156      46.878  24.263  53.755  1.00 25.05           C  
ATOM   3004  C   ILE B 156      47.826  23.237  53.140  1.00 31.19           C  
ATOM   3005  O   ILE B 156      47.509  22.616  52.127  1.00 30.79           O  
ATOM   3006  CB  ILE B 156      45.506  23.607  53.982  1.00 28.97           C  
ATOM   3007  CG1 ILE B 156      44.550  24.633  54.599  1.00 27.46           C  
ATOM   3008  CG2 ILE B 156      45.654  22.364  54.868  1.00 18.02           C  
ATOM   3009  CD1 ILE B 156      43.096  24.347  54.356  1.00 36.18           C  
ATOM   3010  H   ILE B 156      46.101  25.476  52.179  1.00  0.00           H  
ATOM   3011  N   THR B 157      48.956  23.008  53.802  1.00 31.59           N  
ATOM   3012  CA  THR B 157      50.026  22.184  53.241  1.00 27.76           C  
ATOM   3013  C   THR B 157      50.405  20.994  54.115  1.00 26.97           C  
ATOM   3014  O   THR B 157      50.080  20.943  55.299  1.00 29.77           O  
ATOM   3015  CB  THR B 157      51.309  23.012  52.992  1.00 28.95           C  
ATOM   3016  OG1 THR B 157      51.755  23.591  54.226  1.00 36.68           O  
ATOM   3017  CG2 THR B 157      51.043  24.120  51.979  1.00 29.62           C  
ATOM   3018  H   THR B 157      49.030  23.338  54.725  1.00  0.00           H  
ATOM   3019  HG1 THR B 157      51.649  24.554  54.255  1.00  0.00           H  
ATOM   3020  N   ILE B 158      51.049  20.014  53.495  1.00 24.70           N  
ATOM   3021  CA  ILE B 158      51.658  18.897  54.204  1.00 25.32           C  
ATOM   3022  C   ILE B 158      53.121  19.242  54.516  1.00 29.65           C  
ATOM   3023  O   ILE B 158      54.027  18.928  53.738  1.00 29.86           O  
ATOM   3024  CB  ILE B 158      51.589  17.606  53.347  1.00 25.28           C  
ATOM   3025  CG1 ILE B 158      50.125  17.267  53.042  1.00 17.81           C  
ATOM   3026  CG2 ILE B 158      52.276  16.446  54.068  1.00 21.06           C  
ATOM   3027  CD1 ILE B 158      49.944  16.134  52.064  1.00 14.31           C  
ATOM   3028  H   ILE B 158      51.122  20.055  52.531  1.00  0.00           H  
ATOM   3029  N   ALA B 159      53.338  19.916  55.643  1.00 25.92           N  
ATOM   3030  CA  ALA B 159      54.662  20.417  56.019  1.00 19.07           C  
ATOM   3031  C   ALA B 159      55.718  19.313  56.086  1.00 17.72           C  
ATOM   3032  O   ALA B 159      56.888  19.532  55.773  1.00 22.90           O  
ATOM   3033  CB  ALA B 159      54.579  21.144  57.355  1.00 16.49           C  
ATOM   3034  H   ALA B 159      52.569  20.073  56.232  1.00  0.00           H  
ATOM   3035  N   ASP B 160      55.286  18.122  56.478  1.00 15.12           N  
ATOM   3036  CA  ASP B 160      56.161  16.957  56.535  1.00 17.64           C  
ATOM   3037  C   ASP B 160      55.294  15.702  56.593  1.00  9.74           C  
ATOM   3038  O   ASP B 160      54.135  15.764  56.983  1.00 14.96           O  
ATOM   3039  CB  ASP B 160      57.067  17.036  57.776  1.00 22.90           C  
ATOM   3040  CG  ASP B 160      58.183  15.995  57.766  1.00 30.67           C  
ATOM   3041  OD1 ASP B 160      58.605  15.558  56.670  1.00 36.60           O  
ATOM   3042  OD2 ASP B 160      58.653  15.627  58.864  1.00 33.46           O  
ATOM   3043  H   ASP B 160      54.350  18.052  56.750  1.00  0.00           H  
ATOM   3044  N   CYS B 161      55.843  14.576  56.155  1.00 11.07           N  
ATOM   3045  CA  CYS B 161      55.119  13.311  56.179  1.00  8.96           C  
ATOM   3046  C   CYS B 161      56.100  12.152  56.127  1.00  8.85           C  
ATOM   3047  O   CYS B 161      57.271  12.337  55.801  1.00 12.75           O  
ATOM   3048  CB  CYS B 161      54.142  13.219  54.993  1.00 16.68           C  
ATOM   3049  SG  CYS B 161      54.797  13.791  53.392  1.00 12.20           S  
ATOM   3050  H   CYS B 161      56.755  14.595  55.793  1.00  0.00           H  
ATOM   3051  N   GLY B 162      55.635  10.973  56.517  1.00  6.65           N  
ATOM   3052  CA  GLY B 162      56.489   9.804  56.491  1.00  3.05           C  
ATOM   3053  C   GLY B 162      55.763   8.576  56.996  1.00  8.13           C  
ATOM   3054  O   GLY B 162      54.567   8.633  57.270  1.00 10.23           O  
ATOM   3055  H   GLY B 162      54.697  10.907  56.798  1.00  0.00           H  
ATOM   3056  N   GLN B 163      56.475   7.459  57.092  1.00  6.91           N  
ATOM   3057  CA  GLN B 163      55.911   6.242  57.654  1.00 12.60           C  
ATOM   3058  C   GLN B 163      56.268   6.080  59.132  1.00 22.09           C  
ATOM   3059  O   GLN B 163      57.351   6.480  59.563  1.00 24.84           O  
ATOM   3060  CB  GLN B 163      56.401   5.027  56.870  1.00  4.49           C  
ATOM   3061  CG  GLN B 163      55.805   3.722  57.340  1.00  3.11           C  
ATOM   3062  CD  GLN B 163      56.210   2.564  56.475  1.00 13.43           C  
ATOM   3063  OE1 GLN B 163      56.815   2.745  55.421  1.00 21.32           O  
ATOM   3064  NE2 GLN B 163      55.866   1.360  56.901  1.00 16.33           N  
ATOM   3065  H   GLN B 163      57.411   7.480  56.803  1.00  0.00           H  
ATOM   3066 HE21 GLN B 163      56.185   0.621  56.362  1.00  0.00           H  
ATOM   3067 HE22 GLN B 163      55.389   1.259  57.758  1.00  0.00           H  
ATOM   3068  N   LEU B 164      55.334   5.518  59.897  1.00 28.39           N  
ATOM   3069  CA  LEU B 164      55.505   5.296  61.333  1.00 33.33           C  
ATOM   3070  C   LEU B 164      55.694   3.817  61.680  1.00 38.13           C  
ATOM   3071  O   LEU B 164      56.563   3.463  62.477  1.00 42.64           O  
ATOM   3072  CB  LEU B 164      54.293   5.832  62.091  1.00 26.28           C  
ATOM   3073  CG  LEU B 164      53.967   7.311  61.923  1.00 31.51           C  
ATOM   3074  CD1 LEU B 164      52.583   7.580  62.481  1.00 35.95           C  
ATOM   3075  CD2 LEU B 164      55.009   8.157  62.635  1.00 29.83           C  
ATOM   3076  H   LEU B 164      54.512   5.245  59.452  1.00  0.00           H  
ATOM   3077  N   GLU B 165      54.797   2.980  61.168  0.00 41.22           N  
ATOM   3078  CA  GLU B 165      54.855   1.541  61.406  0.00 42.95           C  
ATOM   3079  C   GLU B 165      54.595   0.776  60.109  0.00 43.23           C  
ATOM   3080  O   GLU B 165      53.442   0.790  59.635  0.00 43.00           O  
ATOM   3081  CB  GLU B 165      53.823   1.134  62.466  0.00 44.15           C  
ATOM   3082  CG  GLU B 165      54.265   1.374  63.904  0.00 45.08           C  
ATOM   3083  CD  GLU B 165      55.406   0.466  64.326  0.00 46.52           C  
ATOM   3084  OE1 GLU B 165      55.177  -0.753  64.473  0.00 44.87           O  
ATOM   3085  OE2 GLU B 165      56.532   0.973  64.517  0.00 45.48           O  
ATOM   3086  OXT GLU B 165      55.565   0.241  59.535  0.00 44.72           O  
ATOM   3087  H   GLU B 165      54.101   3.297  60.569  1.00  0.00           H  
TER    3088      GLU B 165                                                      
ATOM   3089  N   PRO C 401      14.541  24.747  24.637  1.00 30.25           N  
ATOM   3090  CA  PRO C 401      15.374  25.756  25.334  1.00 35.32           C  
ATOM   3091  C   PRO C 401      15.221  25.661  26.852  1.00 33.71           C  
ATOM   3092  O   PRO C 401      14.601  24.726  27.352  1.00 38.04           O  
ATOM   3093  CB  PRO C 401      14.940  27.127  24.837  1.00 31.52           C  
ATOM   3094  CG  PRO C 401      14.294  26.799  23.507  1.00 33.65           C  
ATOM   3095  CD  PRO C 401      13.697  25.392  23.616  1.00 33.83           C  
ATOM   3096  H2  PRO C 401      15.053  23.975  24.203  1.00  0.00           H  
ATOM   3097  H3  PRO C 401      13.879  24.345  25.344  1.00  0.00           H  
ATOM   3098  N   ILE C 402      15.858  26.574  27.577  1.00 33.59           N  
ATOM   3099  CA  ILE C 402      15.683  26.674  29.023  1.00 25.20           C  
ATOM   3100  C   ILE C 402      15.030  28.011  29.366  1.00 22.09           C  
ATOM   3101  O   ILE C 402      15.473  29.059  28.899  1.00 24.75           O  
ATOM   3102  CB  ILE C 402      17.051  26.505  29.764  1.00 27.86           C  
ATOM   3103  CG1 ILE C 402      17.351  25.008  29.925  1.00 28.54           C  
ATOM   3104  CG2 ILE C 402      17.040  27.219  31.127  1.00 14.62           C  
ATOM   3105  CD1 ILE C 402      18.404  24.675  30.958  1.00 38.49           C  
ATOM   3106  H   ILE C 402      16.473  27.220  27.164  1.00  0.00           H  
ATOM   3107  N   VAL C 403      13.903  27.953  30.072  1.00 20.84           N  
ATOM   3108  CA  VAL C 403      13.085  29.141  30.320  1.00 23.24           C  
ATOM   3109  C   VAL C 403      12.832  29.385  31.805  1.00 31.91           C  
ATOM   3110  O   VAL C 403      13.054  28.501  32.635  1.00 35.19           O  
ATOM   3111  CB  VAL C 403      11.719  29.030  29.616  1.00 18.05           C  
ATOM   3112  CG1 VAL C 403      11.918  28.936  28.110  1.00 21.31           C  
ATOM   3113  CG2 VAL C 403      10.961  27.813  30.131  1.00  9.05           C  
ATOM   3114  H   VAL C 403      13.650  27.102  30.478  1.00  0.00           H  
ATOM   3115  N   GLN C 404      12.301  30.564  32.120  1.00 36.95           N  
ATOM   3116  CA  GLN C 404      11.922  30.923  33.489  1.00 42.65           C  
ATOM   3117  C   GLN C 404      10.461  30.555  33.759  1.00 43.07           C  
ATOM   3118  O   GLN C 404       9.559  30.990  33.040  1.00 40.59           O  
ATOM   3119  CB  GLN C 404      12.114  32.427  33.721  1.00 45.79           C  
ATOM   3120  CG  GLN C 404      13.426  33.003  33.195  0.00 39.31           C  
ATOM   3121  CD  GLN C 404      13.414  33.248  31.693  0.00 39.00           C  
ATOM   3122  OE1 GLN C 404      12.389  33.108  31.033  0.00 37.74           O  
ATOM   3123  NE2 GLN C 404      14.570  33.571  31.141  0.00 36.88           N  
ATOM   3124  H   GLN C 404      12.069  31.178  31.390  1.00  0.00           H  
ATOM   3125 HE21 GLN C 404      14.482  33.714  30.178  1.00  0.00           H  
ATOM   3126 HE22 GLN C 404      15.388  33.644  31.654  1.00  0.00           H  
ATOM   3127  N   ASN C 405      10.228  29.755  34.794  1.00 45.66           N  
ATOM   3128  CA  ASN C 405       8.893  29.220  35.050  1.00 49.77           C  
ATOM   3129  C   ASN C 405       8.049  30.083  35.993  1.00 50.79           C  
ATOM   3130  O   ASN C 405       8.545  31.040  36.590  1.00 50.26           O  
ATOM   3131  CB  ASN C 405       8.997  27.793  35.599  1.00 53.14           C  
ATOM   3132  CG  ASN C 405       9.751  27.723  36.910  1.00 56.84           C  
ATOM   3133  OD1 ASN C 405      10.074  28.744  37.509  1.00 63.63           O  
ATOM   3134  ND2 ASN C 405      10.000  26.514  37.383  1.00 66.84           N  
ATOM   3135  H   ASN C 405      10.982  29.555  35.391  1.00  0.00           H  
ATOM   3136 HD21 ASN C 405      10.384  26.511  38.289  1.00  0.00           H  
ATOM   3137 HD22 ASN C 405       9.790  25.711  36.872  1.00  0.00           H  
ATOM   3138  N   LEU C 406       6.772  29.732  36.126  0.00 50.12           N  
ATOM   3139  CA  LEU C 406       5.889  30.364  37.107  0.00 49.78           C  
ATOM   3140  C   LEU C 406       6.300  29.978  38.532  0.00 49.44           C  
ATOM   3141  O   LEU C 406       5.642  29.169  39.190  0.00 49.44           O  
ATOM   3142  CB  LEU C 406       4.433  29.958  36.849  0.00 49.69           C  
ATOM   3143  CG  LEU C 406       3.355  30.652  37.689  0.00 49.34           C  
ATOM   3144  CD1 LEU C 406       3.257  32.118  37.298  0.00 49.48           C  
ATOM   3145  CD2 LEU C 406       2.020  29.955  37.491  0.00 48.92           C  
ATOM   3146  H   LEU C 406       6.408  29.092  35.487  1.00  0.00           H  
ATOM   3147  N   GLN C 407       7.427  30.529  38.970  0.00 49.27           N  
ATOM   3148  CA  GLN C 407       8.041  30.192  40.253  0.00 49.46           C  
ATOM   3149  C   GLN C 407       9.362  30.948  40.399  0.00 49.47           C  
ATOM   3150  O   GLN C 407       9.746  31.345  41.499  0.00 50.73           O  
ATOM   3151  CB  GLN C 407       8.309  28.686  40.343  0.00 49.43           C  
ATOM   3152  CG  GLN C 407       8.754  28.212  41.718  0.00 49.55           C  
ATOM   3153  CD  GLN C 407       9.591  26.948  41.664  0.00 49.79           C  
ATOM   3154  OE1 GLN C 407       9.937  26.459  40.591  0.00 50.71           O  
ATOM   3155  NE2 GLN C 407       9.930  26.419  42.826  0.00 49.57           N  
ATOM   3156  H   GLN C 407       7.828  31.209  38.390  1.00  0.00           H  
ATOM   3157 HE21 GLN C 407      10.501  25.638  42.753  1.00  0.00           H  
ATOM   3158 HE22 GLN C 407       9.613  26.829  43.651  1.00  0.00           H  
ATOM   3159  N   GLY C 408      10.066  31.110  39.282  0.00 49.04           N  
ATOM   3160  CA  GLY C 408      11.330  31.823  39.294  0.00 48.77           C  
ATOM   3161  C   GLY C 408      12.500  31.016  38.760  0.00 48.99           C  
ATOM   3162  O   GLY C 408      13.458  31.582  38.239  0.00 49.48           O  
ATOM   3163  H   GLY C 408       9.728  30.733  38.439  1.00  0.00           H  
ATOM   3164  N   GLN C 409      12.394  29.691  38.825  1.00 49.93           N  
ATOM   3165  CA  GLN C 409      13.494  28.805  38.449  1.00 48.25           C  
ATOM   3166  C   GLN C 409      13.638  28.568  36.939  1.00 45.27           C  
ATOM   3167  O   GLN C 409      12.670  28.657  36.179  1.00 33.98           O  
ATOM   3168  CB  GLN C 409      13.354  27.455  39.162  1.00 53.03           C  
ATOM   3169  CG  GLN C 409      14.669  26.696  39.280  1.00 61.74           C  
ATOM   3170  CD  GLN C 409      14.498  25.265  39.746  1.00 62.85           C  
ATOM   3171  OE1 GLN C 409      13.585  24.948  40.503  1.00 63.42           O  
ATOM   3172  NE2 GLN C 409      15.435  24.414  39.370  1.00 65.94           N  
ATOM   3173  H   GLN C 409      11.511  29.315  39.023  1.00  0.00           H  
ATOM   3174 HE21 GLN C 409      15.299  23.469  39.556  1.00  0.00           H  
ATOM   3175 HE22 GLN C 409      16.200  24.776  38.884  1.00  0.00           H  
ATOM   3176  N   MET C 410      14.859  28.249  36.520  1.00 45.62           N  
ATOM   3177  CA  MET C 410      15.138  27.902  35.131  1.00 44.26           C  
ATOM   3178  C   MET C 410      14.852  26.430  34.868  1.00 38.69           C  
ATOM   3179  O   MET C 410      15.459  25.548  35.472  1.00 41.00           O  
ATOM   3180  CB  MET C 410      16.593  28.216  34.780  1.00 47.21           C  
ATOM   3181  CG  MET C 410      16.871  29.692  34.579  1.00 48.40           C  
ATOM   3182  SD  MET C 410      15.812  30.425  33.319  1.00 58.33           S  
ATOM   3183  CE  MET C 410      16.898  31.669  32.647  1.00 58.23           C  
ATOM   3184  H   MET C 410      15.580  28.207  37.176  1.00  0.00           H  
ATOM   3185  N   VAL C 411      13.862  26.177  34.024  1.00 35.40           N  
ATOM   3186  CA  VAL C 411      13.457  24.817  33.704  1.00 29.45           C  
ATOM   3187  C   VAL C 411      13.606  24.530  32.212  1.00 28.25           C  
ATOM   3188  O   VAL C 411      13.647  25.448  31.387  1.00 27.01           O  
ATOM   3189  CB  VAL C 411      11.992  24.556  34.139  1.00 27.26           C  
ATOM   3190  CG1 VAL C 411      11.890  24.568  35.657  1.00 20.08           C  
ATOM   3191  CG2 VAL C 411      11.069  25.606  33.545  1.00 19.74           C  
ATOM   3192  H   VAL C 411      13.417  26.938  33.601  1.00  0.00           H  
ATOM   3193  N   HIS C 412      13.723  23.253  31.871  1.00 25.79           N  
ATOM   3194  CA  HIS C 412      13.806  22.846  30.476  1.00 22.54           C  
ATOM   3195  C   HIS C 412      12.458  22.857  29.758  1.00 24.35           C  
ATOM   3196  O   HIS C 412      11.463  22.355  30.272  1.00 21.64           O  
ATOM   3197  CB  HIS C 412      14.411  21.452  30.357  1.00 18.93           C  
ATOM   3198  CG  HIS C 412      14.379  20.905  28.966  1.00 14.63           C  
ATOM   3199  ND1 HIS C 412      13.602  19.824  28.610  1.00 22.88           N  
ATOM   3200  CD2 HIS C 412      14.977  21.329  27.826  1.00 20.45           C  
ATOM   3201  CE1 HIS C 412      13.724  19.601  27.314  1.00 22.83           C  
ATOM   3202  NE2 HIS C 412      14.551  20.501  26.815  1.00 21.50           N  
ATOM   3203  H   HIS C 412      13.695  22.601  32.600  1.00  0.00           H  
ATOM   3204  HD1 HIS C 412      12.957  19.352  29.180  1.00  0.00           H  
ATOM   3205  HE2 HIS C 412      14.932  20.427  25.924  1.00  0.00           H  
ATOM   3206  N   GLN C 413      12.514  23.208  28.479  1.00 27.02           N  
ATOM   3207  CA  GLN C 413      11.369  23.134  27.580  1.00 23.04           C  
ATOM   3208  C   GLN C 413      11.826  22.638  26.196  1.00 21.62           C  
ATOM   3209  O   GLN C 413      12.913  22.995  25.728  1.00 23.73           O  
ATOM   3210  CB  GLN C 413      10.749  24.518  27.468  1.00 15.61           C  
ATOM   3211  CG  GLN C 413       9.415  24.559  26.793  1.00 17.98           C  
ATOM   3212  CD  GLN C 413       8.954  25.978  26.566  1.00 20.27           C  
ATOM   3213  OE1 GLN C 413       9.610  26.747  25.869  1.00 22.78           O  
ATOM   3214  NE2 GLN C 413       7.843  26.346  27.182  1.00 31.03           N  
ATOM   3215  H   GLN C 413      13.328  23.662  28.197  1.00  0.00           H  
ATOM   3216 HE21 GLN C 413       7.592  27.272  27.016  1.00  0.00           H  
ATOM   3217 HE22 GLN C 413       7.354  25.695  27.719  1.00  0.00           H  
ATOM   3218  N   ALA C 414      11.056  21.738  25.592  1.00 20.20           N  
ATOM   3219  CA  ALA C 414      11.389  21.210  24.265  1.00 14.76           C  
ATOM   3220  C   ALA C 414      11.351  22.313  23.204  1.00 16.42           C  
ATOM   3221  O   ALA C 414      10.703  23.339  23.411  1.00 18.83           O  
ATOM   3222  CB  ALA C 414      10.426  20.091  23.901  1.00 12.99           C  
ATOM   3223  H   ALA C 414      10.204  21.496  26.010  1.00  0.00           H  
ATOM   3224  N   ILE C 415      12.150  22.175  22.143  1.00 27.45           N  
ATOM   3225  CA  ILE C 415      12.169  23.182  21.077  1.00 29.10           C  
ATOM   3226  C   ILE C 415      10.838  23.188  20.305  1.00 26.18           C  
ATOM   3227  O   ILE C 415      10.250  22.134  20.066  1.00 21.14           O  
ATOM   3228  CB  ILE C 415      13.366  22.929  20.119  1.00 22.09           C  
ATOM   3229  CG1 ILE C 415      13.425  24.006  19.044  1.00 18.09           C  
ATOM   3230  CG2 ILE C 415      13.280  21.543  19.506  1.00 18.27           C  
ATOM   3231  CD1 ILE C 415      14.747  24.030  18.316  1.00 35.54           C  
ATOM   3232  H   ILE C 415      12.615  21.324  22.022  1.00  0.00           H  
ATOM   3233  N   SER C 416      10.297  24.379  20.065  1.00 25.74           N  
ATOM   3234  CA  SER C 416       9.033  24.515  19.344  1.00 27.41           C  
ATOM   3235  C   SER C 416       9.167  24.032  17.907  1.00 28.77           C  
ATOM   3236  O   SER C 416      10.076  24.454  17.181  1.00 30.43           O  
ATOM   3237  CB  SER C 416       8.571  25.969  19.332  1.00 20.20           C  
ATOM   3238  OG  SER C 416       7.415  26.117  18.526  1.00 30.62           O  
ATOM   3239  H   SER C 416      10.749  25.165  20.429  1.00  0.00           H  
ATOM   3240  HG  SER C 416       7.074  27.009  18.674  1.00  0.00           H  
ATOM   3241  N   PRO C 417       8.251  23.156  17.465  1.00 28.92           N  
ATOM   3242  CA  PRO C 417       8.296  22.624  16.099  1.00 24.82           C  
ATOM   3243  C   PRO C 417       8.123  23.710  15.034  1.00 25.31           C  
ATOM   3244  O   PRO C 417       8.730  23.641  13.970  1.00 22.66           O  
ATOM   3245  CB  PRO C 417       7.161  21.601  16.073  1.00 21.98           C  
ATOM   3246  CG  PRO C 417       6.937  21.249  17.512  1.00 33.91           C  
ATOM   3247  CD  PRO C 417       7.174  22.531  18.252  1.00 28.96           C  
ATOM   3248  N   ARG C 418       7.389  24.768  15.365  1.00 28.40           N  
ATOM   3249  CA  ARG C 418       7.223  25.889  14.444  1.00 36.29           C  
ATOM   3250  C   ARG C 418       8.499  26.723  14.288  1.00 37.75           C  
ATOM   3251  O   ARG C 418       8.823  27.174  13.189  1.00 38.73           O  
ATOM   3252  CB  ARG C 418       6.054  26.774  14.888  1.00 38.53           C  
ATOM   3253  CG  ARG C 418       4.778  26.523  14.097  0.00 36.68           C  
ATOM   3254  CD  ARG C 418       3.714  27.570  14.381  0.00 36.50           C  
ATOM   3255  NE  ARG C 418       2.653  27.547  13.375  0.00 35.23           N  
ATOM   3256  CZ  ARG C 418       1.454  28.102  13.530  0.00 35.13           C  
ATOM   3257  NH1 ARG C 418       1.137  28.710  14.666  0.00 35.66           N  
ATOM   3258  NH2 ARG C 418       0.565  28.041  12.549  0.00 35.50           N  
ATOM   3259  H   ARG C 418       6.925  24.756  16.231  1.00  0.00           H  
ATOM   3260  HE  ARG C 418       2.833  27.097  12.522  1.00  0.00           H  
ATOM   3261 HH11 ARG C 418       1.793  28.757  15.418  1.00  0.00           H  
ATOM   3262 HH12 ARG C 418       0.232  29.124  14.765  1.00  0.00           H  
ATOM   3263 HH21 ARG C 418       0.798  27.584  11.690  1.00  0.00           H  
ATOM   3264 HH22 ARG C 418      -0.334  28.465  12.662  1.00  0.00           H  
ATOM   3265  N   THR C 419       9.263  26.845  15.371  1.00 38.35           N  
ATOM   3266  CA  THR C 419      10.582  27.481  15.327  1.00 35.74           C  
ATOM   3267  C   THR C 419      11.571  26.631  14.531  1.00 28.07           C  
ATOM   3268  O   THR C 419      12.386  27.153  13.776  1.00 23.64           O  
ATOM   3269  CB  THR C 419      11.150  27.705  16.751  1.00 36.74           C  
ATOM   3270  OG1 THR C 419      10.255  28.539  17.498  1.00 39.25           O  
ATOM   3271  CG2 THR C 419      12.515  28.373  16.689  1.00 36.03           C  
ATOM   3272  H   THR C 419       8.905  26.536  16.226  1.00  0.00           H  
ATOM   3273  HG1 THR C 419      10.422  29.461  17.266  1.00  0.00           H  
ATOM   3274  N   LEU C 420      11.466  25.315  14.675  1.00 26.79           N  
ATOM   3275  CA  LEU C 420      12.248  24.393  13.855  1.00 29.73           C  
ATOM   3276  C   LEU C 420      11.885  24.539  12.383  1.00 30.41           C  
ATOM   3277  O   LEU C 420      12.756  24.736  11.539  1.00 30.64           O  
ATOM   3278  CB  LEU C 420      12.002  22.951  14.295  1.00 30.56           C  
ATOM   3279  CG  LEU C 420      12.923  22.377  15.370  1.00 29.25           C  
ATOM   3280  CD1 LEU C 420      12.375  21.042  15.842  1.00 29.09           C  
ATOM   3281  CD2 LEU C 420      14.325  22.216  14.811  1.00 31.93           C  
ATOM   3282  H   LEU C 420      10.909  24.971  15.402  1.00  0.00           H  
ATOM   3283  N   ASN C 421      10.586  24.555  12.103  1.00 28.34           N  
ATOM   3284  CA  ASN C 421      10.093  24.723  10.742  1.00 31.35           C  
ATOM   3285  C   ASN C 421      10.477  26.076  10.142  1.00 32.60           C  
ATOM   3286  O   ASN C 421      10.841  26.158   8.969  1.00 35.14           O  
ATOM   3287  CB  ASN C 421       8.579  24.526  10.705  1.00 24.66           C  
ATOM   3288  CG  ASN C 421       8.186  23.062  10.727  1.00 23.88           C  
ATOM   3289  OD1 ASN C 421       8.559  22.296   9.847  1.00 25.60           O  
ATOM   3290  ND2 ASN C 421       7.481  22.654  11.764  1.00 29.60           N  
ATOM   3291  H   ASN C 421       9.969  24.413  12.839  1.00  0.00           H  
ATOM   3292 HD21 ASN C 421       7.213  21.719  11.726  1.00  0.00           H  
ATOM   3293 HD22 ASN C 421       7.279  23.283  12.477  1.00  0.00           H  
ATOM   3294  N   ALA C 422      10.520  27.104  10.985  1.00 33.94           N  
ATOM   3295  CA  ALA C 422      10.994  28.428  10.586  1.00 33.45           C  
ATOM   3296  C   ALA C 422      12.464  28.395  10.162  1.00 32.68           C  
ATOM   3297  O   ALA C 422      12.832  28.947   9.125  1.00 37.63           O  
ATOM   3298  CB  ALA C 422      10.796  29.421  11.732  1.00 28.30           C  
ATOM   3299  H   ALA C 422      10.183  26.969  11.888  1.00  0.00           H  
ATOM   3300  N   TRP C 423      13.289  27.710  10.947  1.00 28.83           N  
ATOM   3301  CA  TRP C 423      14.691  27.495  10.601  1.00 27.60           C  
ATOM   3302  C   TRP C 423      14.839  26.751   9.269  1.00 24.29           C  
ATOM   3303  O   TRP C 423      15.512  27.229   8.355  1.00 23.95           O  
ATOM   3304  CB  TRP C 423      15.393  26.717  11.722  1.00 22.10           C  
ATOM   3305  CG  TRP C 423      16.790  26.286  11.390  1.00 15.38           C  
ATOM   3306  CD1 TRP C 423      17.271  25.009  11.383  1.00 17.26           C  
ATOM   3307  CD2 TRP C 423      17.887  27.132  11.021  1.00  4.66           C  
ATOM   3308  NE1 TRP C 423      18.601  25.005  11.037  1.00 19.41           N  
ATOM   3309  CE2 TRP C 423      19.006  26.294  10.810  1.00 13.14           C  
ATOM   3310  CE3 TRP C 423      18.033  28.515  10.845  1.00  8.51           C  
ATOM   3311  CZ2 TRP C 423      20.258  26.795  10.437  1.00  8.34           C  
ATOM   3312  CZ3 TRP C 423      19.280  29.014  10.470  1.00 10.41           C  
ATOM   3313  CH2 TRP C 423      20.374  28.153  10.272  1.00  9.23           C  
ATOM   3314  H   TRP C 423      12.944  27.370  11.799  1.00  0.00           H  
ATOM   3315  HE1 TRP C 423      19.153  24.188  11.015  1.00  0.00           H  
ATOM   3316  N   VAL C 424      14.161  25.614   9.149  1.00 26.35           N  
ATOM   3317  CA  VAL C 424      14.150  24.835   7.911  1.00 31.96           C  
ATOM   3318  C   VAL C 424      13.780  25.697   6.702  1.00 31.86           C  
ATOM   3319  O   VAL C 424      14.480  25.691   5.689  1.00 33.18           O  
ATOM   3320  CB  VAL C 424      13.158  23.647   8.006  1.00 31.96           C  
ATOM   3321  CG1 VAL C 424      13.136  22.866   6.701  1.00 37.32           C  
ATOM   3322  CG2 VAL C 424      13.556  22.728   9.145  1.00 29.87           C  
ATOM   3323  H   VAL C 424      13.676  25.298   9.937  1.00  0.00           H  
ATOM   3324  N   LYS C 425      12.749  26.520   6.865  1.00 32.34           N  
ATOM   3325  CA  LYS C 425      12.322  27.444   5.820  1.00 34.37           C  
ATOM   3326  C   LYS C 425      13.404  28.455   5.431  1.00 34.41           C  
ATOM   3327  O   LYS C 425      13.686  28.638   4.248  1.00 34.94           O  
ATOM   3328  CB  LYS C 425      11.055  28.184   6.253  1.00 38.93           C  
ATOM   3329  CG  LYS C 425       9.786  27.704   5.569  0.00 37.79           C  
ATOM   3330  CD  LYS C 425       9.776  28.091   4.100  0.00 39.26           C  
ATOM   3331  CE  LYS C 425       8.408  27.878   3.479  0.00 38.45           C  
ATOM   3332  NZ  LYS C 425       8.322  28.490   2.125  0.00 40.18           N  
ATOM   3333  H   LYS C 425      12.250  26.479   7.707  1.00  0.00           H  
ATOM   3334  HZ1 LYS C 425       8.542  29.504   2.200  1.00  0.00           H  
ATOM   3335  HZ2 LYS C 425       9.008  28.033   1.491  1.00  0.00           H  
ATOM   3336  HZ3 LYS C 425       7.361  28.372   1.745  1.00  0.00           H  
ATOM   3337  N   VAL C 426      14.043  29.066   6.426  1.00 35.19           N  
ATOM   3338  CA  VAL C 426      15.125  30.025   6.183  1.00 34.33           C  
ATOM   3339  C   VAL C 426      16.249  29.410   5.337  1.00 33.82           C  
ATOM   3340  O   VAL C 426      16.650  29.974   4.321  1.00 32.68           O  
ATOM   3341  CB  VAL C 426      15.717  30.554   7.522  1.00 33.10           C  
ATOM   3342  CG1 VAL C 426      16.946  31.418   7.267  1.00 30.81           C  
ATOM   3343  CG2 VAL C 426      14.672  31.358   8.270  1.00 25.75           C  
ATOM   3344  H   VAL C 426      13.764  28.869   7.346  1.00  0.00           H  
ATOM   3345  N   VAL C 427      16.670  28.203   5.701  1.00 38.16           N  
ATOM   3346  CA  VAL C 427      17.728  27.503   4.973  1.00 37.81           C  
ATOM   3347  C   VAL C 427      17.247  26.988   3.612  1.00 41.05           C  
ATOM   3348  O   VAL C 427      18.036  26.875   2.671  1.00 48.08           O  
ATOM   3349  CB  VAL C 427      18.292  26.325   5.807  1.00 32.66           C  
ATOM   3350  CG1 VAL C 427      19.402  25.613   5.046  1.00 29.02           C  
ATOM   3351  CG2 VAL C 427      18.821  26.842   7.133  1.00 27.73           C  
ATOM   3352  H   VAL C 427      16.267  27.802   6.503  1.00  0.00           H  
ATOM   3353  N   GLU C 428      15.946  26.725   3.501  1.00 35.74           N  
ATOM   3354  CA  GLU C 428      15.337  26.360   2.224  1.00 31.06           C  
ATOM   3355  C   GLU C 428      15.337  27.524   1.237  1.00 34.06           C  
ATOM   3356  O   GLU C 428      15.689  27.361   0.073  1.00 38.64           O  
ATOM   3357  CB  GLU C 428      13.900  25.893   2.435  1.00 30.08           C  
ATOM   3358  CG  GLU C 428      13.724  24.388   2.479  1.00 31.60           C  
ATOM   3359  CD  GLU C 428      12.297  23.978   2.790  1.00 34.52           C  
ATOM   3360  OE1 GLU C 428      11.370  24.759   2.479  1.00 41.02           O  
ATOM   3361  OE2 GLU C 428      12.100  22.868   3.332  1.00 27.16           O  
ATOM   3362  H   GLU C 428      15.393  26.750   4.309  1.00  0.00           H  
ATOM   3363  N   GLU C 429      14.937  28.698   1.714  1.00 35.07           N  
ATOM   3364  CA  GLU C 429      14.779  29.864   0.848  1.00 39.31           C  
ATOM   3365  C   GLU C 429      16.088  30.620   0.653  1.00 39.22           C  
ATOM   3366  O   GLU C 429      16.485  30.906  -0.470  1.00 43.81           O  
ATOM   3367  CB  GLU C 429      13.727  30.817   1.426  1.00 46.13           C  
ATOM   3368  CG  GLU C 429      12.344  30.213   1.597  1.00 57.16           C  
ATOM   3369  CD  GLU C 429      11.378  31.164   2.277  1.00 68.34           C  
ATOM   3370  OE1 GLU C 429      10.742  31.968   1.567  1.00 75.90           O  
ATOM   3371  OE2 GLU C 429      11.287  31.139   3.524  1.00 73.33           O  
ATOM   3372  H   GLU C 429      14.729  28.755   2.665  1.00  0.00           H  
ATOM   3373  N   LYS C 430      16.734  30.973   1.759  1.00 41.16           N  
ATOM   3374  CA  LYS C 430      17.947  31.782   1.711  1.00 43.96           C  
ATOM   3375  C   LYS C 430      19.207  30.961   1.416  1.00 44.61           C  
ATOM   3376  O   LYS C 430      20.217  31.509   0.983  1.00 44.54           O  
ATOM   3377  CB  LYS C 430      18.137  32.534   3.034  1.00 44.14           C  
ATOM   3378  CG  LYS C 430      17.331  33.808   3.145  0.00 50.41           C  
ATOM   3379  CD  LYS C 430      15.941  33.545   3.706  0.00 52.80           C  
ATOM   3380  CE  LYS C 430      15.086  34.796   3.664  0.00 54.41           C  
ATOM   3381  NZ  LYS C 430      15.735  35.940   4.359  0.00 55.01           N  
ATOM   3382  H   LYS C 430      16.346  30.711   2.615  1.00  0.00           H  
ATOM   3383  HZ1 LYS C 430      15.901  35.681   5.352  1.00  0.00           H  
ATOM   3384  HZ2 LYS C 430      16.646  36.159   3.903  1.00  0.00           H  
ATOM   3385  HZ3 LYS C 430      15.108  36.766   4.299  1.00  0.00           H  
ATOM   3386  N   ALA C 431      19.150  29.655   1.679  1.00 48.18           N  
ATOM   3387  CA  ALA C 431      20.359  28.838   1.758  1.00 54.96           C  
ATOM   3388  C   ALA C 431      21.328  29.456   2.772  1.00 55.78           C  
ATOM   3389  O   ALA C 431      20.970  30.377   3.502  1.00 60.88           O  
ATOM   3390  CB  ALA C 431      21.013  28.720   0.390  1.00 53.96           C  
ATOM   3391  H   ALA C 431      18.267  29.245   1.853  1.00  0.00           H  
ATOM   3392  N   PHE C 432      22.554  28.950   2.825  1.00 52.82           N  
ATOM   3393  CA  PHE C 432      23.497  29.396   3.844  1.00 51.29           C  
ATOM   3394  C   PHE C 432      24.192  30.712   3.458  1.00 48.79           C  
ATOM   3395  O   PHE C 432      25.395  30.751   3.238  1.00 52.18           O  
ATOM   3396  CB  PHE C 432      24.533  28.305   4.141  1.00 49.39           C  
ATOM   3397  CG  PHE C 432      24.015  27.188   4.979  1.00 49.69           C  
ATOM   3398  CD1 PHE C 432      23.597  27.423   6.281  1.00 43.81           C  
ATOM   3399  CD2 PHE C 432      23.937  25.900   4.467  1.00 47.29           C  
ATOM   3400  CE1 PHE C 432      23.097  26.383   7.072  1.00 43.15           C  
ATOM   3401  CE2 PHE C 432      23.438  24.845   5.251  1.00 44.15           C  
ATOM   3402  CZ  PHE C 432      23.018  25.090   6.555  1.00 45.29           C  
ATOM   3403  H   PHE C 432      22.925  28.381   2.122  1.00  0.00           H  
ATOM   3404  N   SER C 433      23.421  31.792   3.458  1.00 46.58           N  
ATOM   3405  CA  SER C 433      23.928  33.127   3.150  1.00 47.93           C  
ATOM   3406  C   SER C 433      24.107  33.933   4.450  1.00 49.14           C  
ATOM   3407  O   SER C 433      23.640  33.512   5.511  1.00 49.94           O  
ATOM   3408  CB  SER C 433      22.947  33.850   2.221  1.00 46.98           C  
ATOM   3409  OG  SER C 433      21.900  34.468   2.953  1.00 47.50           O  
ATOM   3410  H   SER C 433      22.499  31.683   3.775  1.00  0.00           H  
ATOM   3411  HG  SER C 433      21.086  34.204   2.501  1.00  0.00           H  
ATOM   3412  N   PRO C 434      24.728  35.126   4.375  1.00 48.63           N  
ATOM   3413  CA  PRO C 434      24.971  35.920   5.585  1.00 45.52           C  
ATOM   3414  C   PRO C 434      23.742  36.137   6.469  1.00 42.53           C  
ATOM   3415  O   PRO C 434      23.862  36.259   7.684  1.00 44.28           O  
ATOM   3416  CB  PRO C 434      25.505  37.234   5.034  1.00 46.88           C  
ATOM   3417  CG  PRO C 434      26.217  36.833   3.793  1.00 46.17           C  
ATOM   3418  CD  PRO C 434      25.390  35.723   3.198  1.00 47.47           C  
ATOM   3419  N   GLU C 435      22.562  36.114   5.859  1.00 42.25           N  
ATOM   3420  CA  GLU C 435      21.309  36.366   6.569  1.00 42.19           C  
ATOM   3421  C   GLU C 435      20.931  35.210   7.495  1.00 37.98           C  
ATOM   3422  O   GLU C 435      20.249  35.400   8.506  1.00 37.31           O  
ATOM   3423  CB  GLU C 435      20.186  36.619   5.563  1.00 46.72           C  
ATOM   3424  CG  GLU C 435      20.509  37.706   4.546  0.00 50.85           C  
ATOM   3425  CD  GLU C 435      19.376  37.972   3.568  0.00 52.93           C  
ATOM   3426  OE1 GLU C 435      18.211  37.649   3.884  0.00 54.75           O  
ATOM   3427  OE2 GLU C 435      19.650  38.543   2.492  0.00 55.51           O  
ATOM   3428  H   GLU C 435      22.540  35.895   4.904  1.00  0.00           H  
ATOM   3429  N   VAL C 436      21.530  34.057   7.235  1.00 30.40           N  
ATOM   3430  CA  VAL C 436      21.240  32.855   7.998  1.00 30.80           C  
ATOM   3431  C   VAL C 436      21.813  32.876   9.421  1.00 26.25           C  
ATOM   3432  O   VAL C 436      21.279  32.228  10.324  1.00 24.03           O  
ATOM   3433  CB  VAL C 436      21.735  31.611   7.229  1.00 32.73           C  
ATOM   3434  CG1 VAL C 436      21.832  30.398   8.136  1.00 40.69           C  
ATOM   3435  CG2 VAL C 436      20.783  31.327   6.103  1.00 37.79           C  
ATOM   3436  H   VAL C 436      22.117  34.006   6.460  1.00  0.00           H  
ATOM   3437  N   ILE C 437      22.825  33.704   9.650  1.00 22.53           N  
ATOM   3438  CA  ILE C 437      23.458  33.753  10.965  1.00 23.12           C  
ATOM   3439  C   ILE C 437      22.635  34.495  12.025  1.00 18.54           C  
ATOM   3440  O   ILE C 437      22.266  33.905  13.046  1.00 22.68           O  
ATOM   3441  CB  ILE C 437      24.886  34.342  10.888  1.00 24.98           C  
ATOM   3442  CG1 ILE C 437      25.746  33.498   9.940  1.00 23.74           C  
ATOM   3443  CG2 ILE C 437      25.514  34.373  12.273  1.00 22.05           C  
ATOM   3444  CD1 ILE C 437      27.121  34.074   9.680  1.00 23.32           C  
ATOM   3445  H   ILE C 437      23.156  34.254   8.908  1.00  0.00           H  
ATOM   3446  N   PRO C 438      22.242  35.755  11.756  1.00 13.54           N  
ATOM   3447  CA  PRO C 438      21.369  36.455  12.707  1.00 18.56           C  
ATOM   3448  C   PRO C 438      20.074  35.690  12.988  1.00 24.31           C  
ATOM   3449  O   PRO C 438      19.591  35.663  14.121  1.00 29.21           O  
ATOM   3450  CB  PRO C 438      21.090  37.796  12.021  1.00 16.01           C  
ATOM   3451  CG  PRO C 438      22.181  37.956  11.035  1.00 10.17           C  
ATOM   3452  CD  PRO C 438      22.485  36.573  10.557  1.00 11.36           C  
ATOM   3453  N   MET C 439      19.560  35.017  11.961  1.00 26.66           N  
ATOM   3454  CA  MET C 439      18.372  34.179  12.093  1.00 30.54           C  
ATOM   3455  C   MET C 439      18.576  33.012  13.063  1.00 27.37           C  
ATOM   3456  O   MET C 439      17.793  32.830  13.996  1.00 31.49           O  
ATOM   3457  CB  MET C 439      17.956  33.641  10.722  1.00 41.27           C  
ATOM   3458  CG  MET C 439      16.596  34.126  10.256  1.00 50.62           C  
ATOM   3459  SD  MET C 439      15.342  33.964  11.542  1.00 61.48           S  
ATOM   3460  CE  MET C 439      14.697  35.624  11.574  1.00 58.80           C  
ATOM   3461  H   MET C 439      19.956  35.143  11.074  1.00  0.00           H  
ATOM   3462  N   PHE C 440      19.657  32.261  12.870  1.00 26.00           N  
ATOM   3463  CA  PHE C 440      19.966  31.119  13.728  1.00 19.07           C  
ATOM   3464  C   PHE C 440      20.068  31.537  15.187  1.00 17.57           C  
ATOM   3465  O   PHE C 440      19.469  30.911  16.057  1.00 17.05           O  
ATOM   3466  CB  PHE C 440      21.276  30.449  13.295  1.00 20.25           C  
ATOM   3467  CG  PHE C 440      21.621  29.216  14.093  1.00 17.03           C  
ATOM   3468  CD1 PHE C 440      21.075  27.980  13.759  1.00 15.29           C  
ATOM   3469  CD2 PHE C 440      22.460  29.298  15.201  1.00 18.11           C  
ATOM   3470  CE1 PHE C 440      21.354  26.846  14.515  1.00  9.62           C  
ATOM   3471  CE2 PHE C 440      22.745  28.172  15.966  1.00 10.93           C  
ATOM   3472  CZ  PHE C 440      22.190  26.944  15.622  1.00 16.17           C  
ATOM   3473  H   PHE C 440      20.233  32.454  12.098  1.00  0.00           H  
ATOM   3474  N   SER C 441      20.803  32.616  15.441  1.00 17.47           N  
ATOM   3475  CA  SER C 441      20.968  33.126  16.801  1.00 21.17           C  
ATOM   3476  C   SER C 441      19.624  33.522  17.399  1.00 20.82           C  
ATOM   3477  O   SER C 441      19.290  33.113  18.514  1.00 23.09           O  
ATOM   3478  CB  SER C 441      21.911  34.330  16.811  1.00 18.89           C  
ATOM   3479  OG  SER C 441      23.131  34.021  16.158  1.00 36.82           O  
ATOM   3480  H   SER C 441      21.250  33.041  14.679  1.00  0.00           H  
ATOM   3481  HG  SER C 441      23.009  33.880  15.213  1.00  0.00           H  
ATOM   3482  N   ALA C 442      18.798  34.177  16.584  1.00 22.50           N  
ATOM   3483  CA  ALA C 442      17.482  34.647  17.006  1.00 19.71           C  
ATOM   3484  C   ALA C 442      16.518  33.500  17.317  1.00 22.66           C  
ATOM   3485  O   ALA C 442      15.718  33.589  18.250  1.00 23.65           O  
ATOM   3486  CB  ALA C 442      16.898  35.556  15.938  1.00 16.72           C  
ATOM   3487  H   ALA C 442      19.097  34.380  15.672  1.00  0.00           H  
ATOM   3488  N   LEU C 443      16.661  32.395  16.591  1.00 21.30           N  
ATOM   3489  CA  LEU C 443      15.780  31.244  16.758  1.00 18.02           C  
ATOM   3490  C   LEU C 443      16.326  30.195  17.727  1.00 23.20           C  
ATOM   3491  O   LEU C 443      15.717  29.141  17.916  1.00 28.27           O  
ATOM   3492  CB  LEU C 443      15.510  30.589  15.399  1.00 21.53           C  
ATOM   3493  CG  LEU C 443      14.894  31.455  14.295  1.00 24.47           C  
ATOM   3494  CD1 LEU C 443      14.735  30.631  13.025  1.00 26.40           C  
ATOM   3495  CD2 LEU C 443      13.549  31.998  14.742  1.00 19.65           C  
ATOM   3496  H   LEU C 443      17.343  32.390  15.888  1.00  0.00           H  
ATOM   3497  N   SER C 444      17.484  30.466  18.322  1.00 24.48           N  
ATOM   3498  CA  SER C 444      18.129  29.491  19.203  1.00 23.99           C  
ATOM   3499  C   SER C 444      18.398  30.029  20.608  1.00 22.09           C  
ATOM   3500  O   SER C 444      19.091  29.393  21.407  1.00 19.29           O  
ATOM   3501  CB  SER C 444      19.443  28.997  18.582  1.00 17.47           C  
ATOM   3502  OG  SER C 444      20.377  30.054  18.439  1.00 19.31           O  
ATOM   3503  H   SER C 444      17.941  31.308  18.117  1.00  0.00           H  
ATOM   3504  HG  SER C 444      20.365  30.345  17.529  1.00  0.00           H  
ATOM   3505  N   GLU C 445      17.789  31.161  20.941  1.00 23.73           N  
ATOM   3506  CA  GLU C 445      17.967  31.741  22.266  1.00 21.91           C  
ATOM   3507  C   GLU C 445      17.491  30.826  23.389  1.00 23.94           C  
ATOM   3508  O   GLU C 445      16.408  30.246  23.328  1.00 33.04           O  
ATOM   3509  CB  GLU C 445      17.287  33.103  22.358  1.00 26.73           C  
ATOM   3510  CG  GLU C 445      18.232  34.239  22.003  1.00 44.65           C  
ATOM   3511  CD  GLU C 445      17.569  35.601  22.014  1.00 54.16           C  
ATOM   3512  OE1 GLU C 445      16.706  35.841  22.889  1.00 56.23           O  
ATOM   3513  OE2 GLU C 445      17.943  36.443  21.167  1.00 56.76           O  
ATOM   3514  H   GLU C 445      17.213  31.592  20.277  1.00  0.00           H  
ATOM   3515  N   GLY C 446      18.405  30.543  24.307  1.00 25.27           N  
ATOM   3516  CA  GLY C 446      18.105  29.653  25.414  1.00 16.10           C  
ATOM   3517  C   GLY C 446      18.240  28.180  25.075  1.00 18.33           C  
ATOM   3518  O   GLY C 446      17.905  27.320  25.893  1.00 18.61           O  
ATOM   3519  H   GLY C 446      19.291  30.937  24.189  1.00  0.00           H  
ATOM   3520  N   ALA C 447      18.721  27.873  23.874  1.00 15.32           N  
ATOM   3521  CA  ALA C 447      18.772  26.489  23.419  1.00 17.85           C  
ATOM   3522  C   ALA C 447      19.863  25.670  24.104  1.00 19.63           C  
ATOM   3523  O   ALA C 447      20.928  26.186  24.437  1.00 17.69           O  
ATOM   3524  CB  ALA C 447      18.953  26.439  21.911  1.00 19.46           C  
ATOM   3525  H   ALA C 447      19.045  28.585  23.277  1.00  0.00           H  
ATOM   3526  N   THR C 448      19.536  24.419  24.410  1.00 22.55           N  
ATOM   3527  CA  THR C 448      20.522  23.448  24.880  1.00 21.35           C  
ATOM   3528  C   THR C 448      21.348  22.945  23.693  1.00 26.24           C  
ATOM   3529  O   THR C 448      20.894  23.004  22.550  1.00 29.23           O  
ATOM   3530  CB  THR C 448      19.840  22.228  25.539  1.00 19.07           C  
ATOM   3531  OG1 THR C 448      19.172  21.451  24.539  1.00 18.36           O  
ATOM   3532  CG2 THR C 448      18.825  22.679  26.579  1.00 24.42           C  
ATOM   3533  H   THR C 448      18.610  24.175  24.275  1.00  0.00           H  
ATOM   3534  HG1 THR C 448      18.312  21.836  24.444  1.00  0.00           H  
ATOM   3535  N   PRO C 449      22.513  22.333  23.958  1.00 24.24           N  
ATOM   3536  CA  PRO C 449      23.241  21.611  22.910  1.00 18.75           C  
ATOM   3537  C   PRO C 449      22.371  20.647  22.102  1.00 19.24           C  
ATOM   3538  O   PRO C 449      22.451  20.618  20.873  1.00 21.35           O  
ATOM   3539  CB  PRO C 449      24.337  20.888  23.683  1.00 18.64           C  
ATOM   3540  CG  PRO C 449      24.635  21.817  24.814  1.00 15.64           C  
ATOM   3541  CD  PRO C 449      23.316  22.455  25.190  1.00 22.69           C  
ATOM   3542  N   GLN C 450      21.485  19.920  22.780  1.00 18.42           N  
ATOM   3543  CA  GLN C 450      20.527  19.043  22.100  1.00 18.60           C  
ATOM   3544  C   GLN C 450      19.606  19.818  21.148  1.00 16.70           C  
ATOM   3545  O   GLN C 450      19.437  19.433  19.994  1.00 20.21           O  
ATOM   3546  CB  GLN C 450      19.684  18.274  23.122  1.00 20.30           C  
ATOM   3547  CG  GLN C 450      18.590  17.382  22.515  1.00 20.98           C  
ATOM   3548  CD  GLN C 450      17.607  16.861  23.561  1.00 28.09           C  
ATOM   3549  OE1 GLN C 450      17.640  15.694  23.938  1.00 25.30           O  
ATOM   3550  NE2 GLN C 450      16.747  17.737  24.051  1.00 25.20           N  
ATOM   3551  H   GLN C 450      21.545  19.905  23.763  1.00  0.00           H  
ATOM   3552 HE21 GLN C 450      16.161  17.365  24.729  1.00  0.00           H  
ATOM   3553 HE22 GLN C 450      16.771  18.635  23.711  1.00  0.00           H  
ATOM   3554  N   ASP C 451      19.094  20.956  21.602  1.00 14.25           N  
ATOM   3555  CA  ASP C 451      18.243  21.797  20.762  1.00 15.95           C  
ATOM   3556  C   ASP C 451      18.993  22.332  19.553  1.00 20.43           C  
ATOM   3557  O   ASP C 451      18.469  22.330  18.442  1.00 31.39           O  
ATOM   3558  CB  ASP C 451      17.680  22.970  21.567  1.00 13.98           C  
ATOM   3559  CG  ASP C 451      16.682  22.531  22.616  1.00 25.55           C  
ATOM   3560  OD1 ASP C 451      15.949  21.551  22.368  1.00 28.09           O  
ATOM   3561  OD2 ASP C 451      16.627  23.166  23.691  1.00 28.52           O  
ATOM   3562  H   ASP C 451      19.374  21.234  22.499  1.00  0.00           H  
ATOM   3563  N   LEU C 452      20.240  22.740  19.769  1.00 23.87           N  
ATOM   3564  CA  LEU C 452      21.097  23.233  18.693  1.00 19.32           C  
ATOM   3565  C   LEU C 452      21.398  22.141  17.663  1.00 15.58           C  
ATOM   3566  O   LEU C 452      21.320  22.375  16.460  1.00 15.91           O  
ATOM   3567  CB  LEU C 452      22.400  23.788  19.276  1.00 15.86           C  
ATOM   3568  CG  LEU C 452      22.235  25.015  20.179  1.00 15.02           C  
ATOM   3569  CD1 LEU C 452      23.518  25.282  20.950  1.00 13.50           C  
ATOM   3570  CD2 LEU C 452      21.860  26.218  19.344  1.00  9.34           C  
ATOM   3571  H   LEU C 452      20.585  22.723  20.684  1.00  0.00           H  
ATOM   3572  N   ASN C 453      21.597  20.918  18.142  1.00 16.45           N  
ATOM   3573  CA  ASN C 453      21.807  19.775  17.259  1.00 24.75           C  
ATOM   3574  C   ASN C 453      20.537  19.381  16.498  1.00 27.66           C  
ATOM   3575  O   ASN C 453      20.605  18.955  15.348  1.00 28.08           O  
ATOM   3576  CB  ASN C 453      22.335  18.575  18.054  1.00 23.09           C  
ATOM   3577  CG  ASN C 453      23.788  18.743  18.464  1.00 27.20           C  
ATOM   3578  OD1 ASN C 453      24.554  19.418  17.790  1.00 24.48           O  
ATOM   3579  ND2 ASN C 453      24.156  18.170  19.596  1.00 18.19           N  
ATOM   3580  H   ASN C 453      21.690  20.818  19.111  1.00  0.00           H  
ATOM   3581 HD21 ASN C 453      25.100  18.306  19.816  1.00  0.00           H  
ATOM   3582 HD22 ASN C 453      23.503  17.686  20.129  1.00  0.00           H  
ATOM   3583  N   THR C 454      19.382  19.549  17.134  1.00 27.74           N  
ATOM   3584  CA  THR C 454      18.097  19.338  16.468  1.00 25.22           C  
ATOM   3585  C   THR C 454      17.920  20.326  15.310  1.00 24.28           C  
ATOM   3586  O   THR C 454      17.551  19.932  14.205  1.00 21.86           O  
ATOM   3587  CB  THR C 454      16.909  19.502  17.453  1.00 26.63           C  
ATOM   3588  OG1 THR C 454      17.045  18.577  18.542  1.00 25.84           O  
ATOM   3589  CG2 THR C 454      15.593  19.225  16.753  1.00 29.28           C  
ATOM   3590  H   THR C 454      19.416  19.824  18.072  1.00  0.00           H  
ATOM   3591  HG1 THR C 454      17.972  18.502  18.833  1.00  0.00           H  
ATOM   3592  N   MET C 455      18.299  21.583  15.535  1.00 21.38           N  
ATOM   3593  CA  MET C 455      18.282  22.600  14.481  1.00 23.63           C  
ATOM   3594  C   MET C 455      19.214  22.280  13.307  1.00 26.46           C  
ATOM   3595  O   MET C 455      18.881  22.539  12.148  1.00 25.09           O  
ATOM   3596  CB  MET C 455      18.653  23.968  15.052  1.00 19.68           C  
ATOM   3597  CG  MET C 455      17.623  24.552  15.997  1.00 20.79           C  
ATOM   3598  SD  MET C 455      18.045  26.238  16.482  1.00 25.78           S  
ATOM   3599  CE  MET C 455      17.416  27.170  15.078  1.00 16.09           C  
ATOM   3600  H   MET C 455      18.559  21.836  16.448  1.00  0.00           H  
ATOM   3601  N   LEU C 456      20.393  21.746  13.609  1.00 25.69           N  
ATOM   3602  CA  LEU C 456      21.358  21.394  12.568  1.00 26.08           C  
ATOM   3603  C   LEU C 456      20.955  20.151  11.774  1.00 23.32           C  
ATOM   3604  O   LEU C 456      21.005  20.149  10.548  1.00 27.28           O  
ATOM   3605  CB  LEU C 456      22.747  21.185  13.178  1.00 21.46           C  
ATOM   3606  CG  LEU C 456      23.333  22.380  13.928  1.00 11.77           C  
ATOM   3607  CD1 LEU C 456      24.729  22.021  14.402  1.00 17.23           C  
ATOM   3608  CD2 LEU C 456      23.354  23.609  13.027  1.00  4.40           C  
ATOM   3609  H   LEU C 456      20.644  21.675  14.557  1.00  0.00           H  
ATOM   3610  N   ASN C 457      20.494  19.122  12.474  1.00 19.65           N  
ATOM   3611  CA  ASN C 457      20.158  17.852  11.839  1.00 27.42           C  
ATOM   3612  C   ASN C 457      18.834  17.893  11.084  1.00 32.83           C  
ATOM   3613  O   ASN C 457      18.476  16.940  10.392  1.00 38.55           O  
ATOM   3614  CB  ASN C 457      20.117  16.734  12.881  1.00 29.67           C  
ATOM   3615  CG  ASN C 457      21.427  16.583  13.621  1.00 41.96           C  
ATOM   3616  OD1 ASN C 457      22.463  17.080  13.185  1.00 48.69           O  
ATOM   3617  ND2 ASN C 457      21.387  15.913  14.761  1.00 52.39           N  
ATOM   3618  H   ASN C 457      20.471  19.208  13.448  1.00  0.00           H  
ATOM   3619 HD21 ASN C 457      22.266  15.836  15.174  1.00  0.00           H  
ATOM   3620 HD22 ASN C 457      20.548  15.549  15.089  1.00  0.00           H  
ATOM   3621  N   THR C 458      18.084  18.977  11.252  1.00 30.66           N  
ATOM   3622  CA  THR C 458      16.848  19.162  10.500  1.00 34.77           C  
ATOM   3623  C   THR C 458      17.108  19.767   9.116  1.00 35.15           C  
ATOM   3624  O   THR C 458      16.219  19.786   8.259  1.00 33.30           O  
ATOM   3625  CB  THR C 458      15.838  20.045  11.278  1.00 32.56           C  
ATOM   3626  OG1 THR C 458      14.532  19.891  10.712  1.00 45.76           O  
ATOM   3627  CG2 THR C 458      16.231  21.507  11.211  1.00 37.16           C  
ATOM   3628  H   THR C 458      18.343  19.608  11.954  1.00  0.00           H  
ATOM   3629  HG1 THR C 458      14.606  20.095   9.784  1.00  0.00           H  
ATOM   3630  N   VAL C 459      18.337  20.224   8.890  1.00 36.50           N  
ATOM   3631  CA  VAL C 459      18.737  20.768   7.594  1.00 37.47           C  
ATOM   3632  C   VAL C 459      18.926  19.666   6.551  1.00 37.44           C  
ATOM   3633  O   VAL C 459      19.913  18.933   6.577  1.00 37.15           O  
ATOM   3634  CB  VAL C 459      20.050  21.587   7.703  1.00 35.36           C  
ATOM   3635  CG1 VAL C 459      20.487  22.075   6.328  1.00 33.85           C  
ATOM   3636  CG2 VAL C 459      19.850  22.772   8.637  1.00 41.26           C  
ATOM   3637  H   VAL C 459      19.013  20.180   9.603  1.00  0.00           H  
ATOM   3638  N   GLY C 460      18.054  19.675   5.547  1.00 36.47           N  
ATOM   3639  CA  GLY C 460      18.166  18.732   4.446  1.00 36.71           C  
ATOM   3640  C   GLY C 460      19.090  19.192   3.327  1.00 34.20           C  
ATOM   3641  O   GLY C 460      19.088  20.366   2.948  1.00 32.08           O  
ATOM   3642  H   GLY C 460      17.384  20.389   5.561  1.00  0.00           H  
ATOM   3643  N   GLY C 461      19.844  18.254   2.762  1.00 31.80           N  
ATOM   3644  CA  GLY C 461      20.808  18.599   1.730  1.00 30.68           C  
ATOM   3645  C   GLY C 461      22.024  19.335   2.269  1.00 33.46           C  
ATOM   3646  O   GLY C 461      22.386  19.161   3.436  1.00 40.51           O  
ATOM   3647  H   GLY C 461      19.803  17.346   3.123  1.00  0.00           H  
ATOM   3648  N   HIS C 462      22.658  20.144   1.425  1.00 28.16           N  
ATOM   3649  CA  HIS C 462      23.830  20.919   1.815  1.00 20.64           C  
ATOM   3650  C   HIS C 462      24.887  20.123   2.591  1.00 18.71           C  
ATOM   3651  O   HIS C 462      25.539  20.651   3.492  1.00 20.24           O  
ATOM   3652  CB  HIS C 462      23.411  22.134   2.644  1.00 17.00           C  
ATOM   3653  CG  HIS C 462      22.555  23.102   1.896  1.00 18.87           C  
ATOM   3654  ND1 HIS C 462      23.081  24.099   1.103  1.00 14.20           N  
ATOM   3655  CD2 HIS C 462      21.220  23.330   1.944  1.00 14.83           C  
ATOM   3656  CE1 HIS C 462      22.116  24.908   0.707  1.00 15.80           C  
ATOM   3657  NE2 HIS C 462      20.977  24.463   1.206  1.00 16.22           N  
ATOM   3658  H   HIS C 462      22.295  20.227   0.521  1.00  0.00           H  
ATOM   3659  HD1 HIS C 462      24.020  24.190   0.819  1.00  0.00           H  
ATOM   3660  HE2 HIS C 462      20.093  24.876   1.068  1.00  0.00           H  
ATOM   3661  N   GLN C 463      25.087  18.875   2.186  1.00 15.19           N  
ATOM   3662  CA  GLN C 463      26.021  17.962   2.844  1.00 23.46           C  
ATOM   3663  C   GLN C 463      27.429  18.537   3.034  1.00 25.75           C  
ATOM   3664  O   GLN C 463      28.001  18.447   4.126  1.00 30.99           O  
ATOM   3665  CB  GLN C 463      26.100  16.650   2.058  1.00 17.05           C  
ATOM   3666  CG  GLN C 463      26.786  15.508   2.799  0.00 16.96           C  
ATOM   3667  CD  GLN C 463      26.809  14.221   1.995  0.00 14.89           C  
ATOM   3668  OE1 GLN C 463      26.191  14.122   0.937  0.00 14.36           O  
ATOM   3669  NE2 GLN C 463      27.519  13.227   2.497  0.00 14.64           N  
ATOM   3670  H   GLN C 463      24.512  18.524   1.476  1.00  0.00           H  
ATOM   3671 HE21 GLN C 463      27.504  12.427   1.936  1.00  0.00           H  
ATOM   3672 HE22 GLN C 463      27.987  13.321   3.345  1.00  0.00           H  
ATOM   3673  N   ALA C 464      27.974  19.147   1.984  1.00 26.71           N  
ATOM   3674  CA  ALA C 464      29.341  19.664   2.022  1.00 26.15           C  
ATOM   3675  C   ALA C 464      29.507  20.750   3.087  1.00 27.11           C  
ATOM   3676  O   ALA C 464      30.452  20.720   3.876  1.00 30.09           O  
ATOM   3677  CB  ALA C 464      29.741  20.205   0.650  1.00 22.30           C  
ATOM   3678  H   ALA C 464      27.440  19.230   1.162  1.00  0.00           H  
ATOM   3679  N   ALA C 465      28.532  21.651   3.163  1.00 24.54           N  
ATOM   3680  CA  ALA C 465      28.548  22.731   4.143  1.00 24.73           C  
ATOM   3681  C   ALA C 465      28.406  22.215   5.573  1.00 25.00           C  
ATOM   3682  O   ALA C 465      29.129  22.648   6.466  1.00 30.83           O  
ATOM   3683  CB  ALA C 465      27.450  23.733   3.840  1.00 17.92           C  
ATOM   3684  H   ALA C 465      27.792  21.594   2.525  1.00  0.00           H  
ATOM   3685  N   MET C 466      27.529  21.238   5.773  1.00 21.89           N  
ATOM   3686  CA  MET C 466      27.312  20.665   7.097  1.00 23.43           C  
ATOM   3687  C   MET C 466      28.540  19.909   7.613  1.00 25.73           C  
ATOM   3688  O   MET C 466      28.841  19.936   8.807  1.00 26.13           O  
ATOM   3689  CB  MET C 466      26.090  19.741   7.080  1.00 19.93           C  
ATOM   3690  CG  MET C 466      24.769  20.455   6.819  1.00 17.14           C  
ATOM   3691  SD  MET C 466      24.558  21.985   7.761  1.00 23.55           S  
ATOM   3692  CE  MET C 466      23.990  21.340   9.320  1.00 18.39           C  
ATOM   3693  H   MET C 466      26.995  20.940   5.003  1.00  0.00           H  
ATOM   3694  N   GLN C 467      29.283  19.299   6.695  1.00 29.41           N  
ATOM   3695  CA  GLN C 467      30.562  18.661   7.013  1.00 29.50           C  
ATOM   3696  C   GLN C 467      31.622  19.699   7.410  1.00 27.40           C  
ATOM   3697  O   GLN C 467      32.406  19.482   8.335  1.00 21.87           O  
ATOM   3698  CB  GLN C 467      31.044  17.857   5.804  1.00 34.27           C  
ATOM   3699  CG  GLN C 467      32.031  16.756   6.130  1.00 49.96           C  
ATOM   3700  CD  GLN C 467      32.415  15.941   4.907  1.00 60.75           C  
ATOM   3701  OE1 GLN C 467      33.593  15.727   4.634  1.00 66.80           O  
ATOM   3702  NE2 GLN C 467      31.419  15.477   4.166  1.00 63.68           N  
ATOM   3703  H   GLN C 467      28.916  19.245   5.782  1.00  0.00           H  
ATOM   3704 HE21 GLN C 467      31.739  14.964   3.401  1.00  0.00           H  
ATOM   3705 HE22 GLN C 467      30.495  15.661   4.400  1.00  0.00           H  
ATOM   3706  N   MET C 468      31.582  20.853   6.750  1.00 22.32           N  
ATOM   3707  CA  MET C 468      32.467  21.972   7.054  1.00 22.70           C  
ATOM   3708  C   MET C 468      32.180  22.571   8.436  1.00 23.60           C  
ATOM   3709  O   MET C 468      33.098  22.843   9.209  1.00 26.04           O  
ATOM   3710  CB  MET C 468      32.303  23.047   5.985  1.00 24.67           C  
ATOM   3711  CG  MET C 468      33.597  23.669   5.503  1.00 40.90           C  
ATOM   3712  SD  MET C 468      33.297  24.924   4.240  1.00 45.45           S  
ATOM   3713  CE  MET C 468      32.746  23.889   2.868  1.00 50.16           C  
ATOM   3714  H   MET C 468      30.965  20.911   5.986  1.00  0.00           H  
ATOM   3715  N   LEU C 469      30.900  22.775   8.733  1.00 21.73           N  
ATOM   3716  CA  LEU C 469      30.457  23.267  10.038  1.00 21.34           C  
ATOM   3717  C   LEU C 469      30.834  22.296  11.164  1.00 21.21           C  
ATOM   3718  O   LEU C 469      31.360  22.703  12.199  1.00 22.28           O  
ATOM   3719  CB  LEU C 469      28.939  23.484  10.014  1.00 23.22           C  
ATOM   3720  CG  LEU C 469      28.183  23.765  11.316  1.00 23.56           C  
ATOM   3721  CD1 LEU C 469      28.495  25.163  11.808  1.00 25.76           C  
ATOM   3722  CD2 LEU C 469      26.694  23.611  11.078  1.00 18.85           C  
ATOM   3723  H   LEU C 469      30.248  22.637   8.016  1.00  0.00           H  
ATOM   3724  N   LYS C 470      30.634  21.008  10.916  1.00 14.44           N  
ATOM   3725  CA  LYS C 470      30.974  19.953  11.868  1.00 19.92           C  
ATOM   3726  C   LYS C 470      32.465  19.950  12.235  1.00 21.44           C  
ATOM   3727  O   LYS C 470      32.822  19.936  13.414  1.00 24.21           O  
ATOM   3728  CB  LYS C 470      30.571  18.597  11.283  1.00 23.59           C  
ATOM   3729  CG  LYS C 470      30.868  17.398  12.161  1.00 38.25           C  
ATOM   3730  CD  LYS C 470      31.135  16.167  11.304  1.00 42.23           C  
ATOM   3731  CE  LYS C 470      30.077  15.097  11.504  1.00 53.40           C  
ATOM   3732  NZ  LYS C 470      30.223  13.993  10.510  1.00 62.02           N  
ATOM   3733  H   LYS C 470      30.190  20.766  10.074  1.00  0.00           H  
ATOM   3734  HZ1 LYS C 470      31.194  13.619  10.525  1.00  0.00           H  
ATOM   3735  HZ2 LYS C 470      29.555  13.227  10.732  1.00  0.00           H  
ATOM   3736  HZ3 LYS C 470      30.016  14.369   9.563  1.00  0.00           H  
ATOM   3737  N   GLU C 471      33.325  20.039  11.226  1.00 20.49           N  
ATOM   3738  CA  GLU C 471      34.764  20.162  11.446  1.00 16.55           C  
ATOM   3739  C   GLU C 471      35.137  21.373  12.296  1.00 18.52           C  
ATOM   3740  O   GLU C 471      35.905  21.256  13.245  1.00 19.13           O  
ATOM   3741  CB  GLU C 471      35.502  20.243  10.114  1.00 12.67           C  
ATOM   3742  CG  GLU C 471      36.507  19.124   9.903  1.00 32.83           C  
ATOM   3743  CD  GLU C 471      37.397  18.890  11.116  1.00 33.59           C  
ATOM   3744  OE1 GLU C 471      38.352  19.676  11.326  1.00 27.10           O  
ATOM   3745  OE2 GLU C 471      37.138  17.913  11.855  1.00 32.05           O  
ATOM   3746  H   GLU C 471      32.976  19.972  10.308  1.00  0.00           H  
ATOM   3747  N   THR C 472      34.555  22.525  11.983  1.00 19.28           N  
ATOM   3748  CA  THR C 472      34.772  23.735  12.773  1.00 21.95           C  
ATOM   3749  C   THR C 472      34.364  23.567  14.242  1.00 25.27           C  
ATOM   3750  O   THR C 472      35.098  23.964  15.151  1.00 25.45           O  
ATOM   3751  CB  THR C 472      34.007  24.928  12.175  1.00 17.89           C  
ATOM   3752  OG1 THR C 472      34.557  25.238  10.891  1.00 17.55           O  
ATOM   3753  CG2 THR C 472      34.130  26.161  13.069  1.00 20.24           C  
ATOM   3754  H   THR C 472      33.972  22.554  11.191  1.00  0.00           H  
ATOM   3755  HG1 THR C 472      34.812  24.427  10.439  1.00  0.00           H  
ATOM   3756  N   ILE C 473      33.222  22.928  14.473  1.00 25.49           N  
ATOM   3757  CA  ILE C 473      32.776  22.621  15.827  1.00 20.53           C  
ATOM   3758  C   ILE C 473      33.774  21.690  16.522  1.00 23.71           C  
ATOM   3759  O   ILE C 473      34.184  21.948  17.652  1.00 26.43           O  
ATOM   3760  CB  ILE C 473      31.372  21.963  15.818  1.00 15.21           C  
ATOM   3761  CG1 ILE C 473      30.321  22.981  15.366  1.00 13.34           C  
ATOM   3762  CG2 ILE C 473      31.026  21.440  17.198  1.00 12.92           C  
ATOM   3763  CD1 ILE C 473      28.969  22.366  15.043  1.00 16.53           C  
ATOM   3764  H   ILE C 473      32.653  22.697  13.704  1.00  0.00           H  
ATOM   3765  N   ASN C 474      34.226  20.661  15.810  1.00 21.38           N  
ATOM   3766  CA  ASN C 474      35.177  19.695  16.361  1.00 20.31           C  
ATOM   3767  C   ASN C 474      36.535  20.316  16.691  1.00 26.88           C  
ATOM   3768  O   ASN C 474      37.189  19.918  17.655  1.00 24.88           O  
ATOM   3769  CB  ASN C 474      35.373  18.535  15.391  1.00 13.03           C  
ATOM   3770  CG  ASN C 474      34.168  17.626  15.316  1.00 17.27           C  
ATOM   3771  OD1 ASN C 474      34.195  16.614  14.627  1.00 28.56           O  
ATOM   3772  ND2 ASN C 474      33.095  17.987  16.005  1.00 25.73           N  
ATOM   3773  H   ASN C 474      33.902  20.552  14.892  1.00  0.00           H  
ATOM   3774 HD21 ASN C 474      32.412  17.295  15.927  1.00  0.00           H  
ATOM   3775 HD22 ASN C 474      32.987  18.801  16.522  1.00  0.00           H  
ATOM   3776  N   GLU C 475      36.941  21.304  15.900  1.00 25.01           N  
ATOM   3777  CA  GLU C 475      38.139  22.084  16.190  1.00 24.94           C  
ATOM   3778  C   GLU C 475      37.967  22.894  17.472  1.00 24.72           C  
ATOM   3779  O   GLU C 475      38.826  22.864  18.353  1.00 26.48           O  
ATOM   3780  CB  GLU C 475      38.450  23.032  15.032  1.00 17.34           C  
ATOM   3781  CG  GLU C 475      38.892  22.331  13.761  1.00 23.19           C  
ATOM   3782  CD  GLU C 475      38.979  23.268  12.565  1.00 29.89           C  
ATOM   3783  OE1 GLU C 475      38.736  24.485  12.720  1.00 30.01           O  
ATOM   3784  OE2 GLU C 475      39.283  22.779  11.460  1.00 40.84           O  
ATOM   3785  H   GLU C 475      36.449  21.466  15.070  1.00  0.00           H  
ATOM   3786  N   GLU C 476      36.827  23.567  17.594  1.00 23.32           N  
ATOM   3787  CA  GLU C 476      36.518  24.364  18.779  1.00 20.21           C  
ATOM   3788  C   GLU C 476      36.398  23.499  20.026  1.00 14.41           C  
ATOM   3789  O   GLU C 476      36.826  23.892  21.109  1.00 22.36           O  
ATOM   3790  CB  GLU C 476      35.218  25.136  18.568  1.00 27.37           C  
ATOM   3791  CG  GLU C 476      35.296  26.223  17.502  1.00 32.15           C  
ATOM   3792  CD  GLU C 476      36.297  27.318  17.836  1.00 31.53           C  
ATOM   3793  OE1 GLU C 476      36.350  27.756  19.003  1.00 40.45           O  
ATOM   3794  OE2 GLU C 476      37.011  27.765  16.918  1.00 39.88           O  
ATOM   3795  H   GLU C 476      36.206  23.564  16.833  1.00  0.00           H  
ATOM   3796  N   ALA C 477      35.857  22.301  19.854  1.00 10.07           N  
ATOM   3797  CA  ALA C 477      35.760  21.323  20.930  1.00 16.15           C  
ATOM   3798  C   ALA C 477      37.143  20.836  21.380  1.00 22.93           C  
ATOM   3799  O   ALA C 477      37.400  20.684  22.580  1.00 26.09           O  
ATOM   3800  CB  ALA C 477      34.901  20.143  20.480  1.00  6.30           C  
ATOM   3801  H   ALA C 477      35.471  22.103  18.982  1.00  0.00           H  
ATOM   3802  N   ALA C 478      38.042  20.642  20.418  1.00 18.75           N  
ATOM   3803  CA  ALA C 478      39.421  20.247  20.706  1.00 16.10           C  
ATOM   3804  C   ALA C 478      40.207  21.372  21.377  1.00 16.36           C  
ATOM   3805  O   ALA C 478      40.992  21.130  22.294  1.00 20.60           O  
ATOM   3806  CB  ALA C 478      40.123  19.812  19.424  1.00 10.51           C  
ATOM   3807  H   ALA C 478      37.756  20.724  19.483  1.00  0.00           H  
ATOM   3808  N   GLU C 479      39.967  22.604  20.940  1.00 19.74           N  
ATOM   3809  CA  GLU C 479      40.547  23.785  21.580  1.00 25.56           C  
ATOM   3810  C   GLU C 479      40.098  23.944  23.030  1.00 30.10           C  
ATOM   3811  O   GLU C 479      40.898  24.304  23.892  1.00 35.58           O  
ATOM   3812  CB  GLU C 479      40.181  25.053  20.804  1.00 23.98           C  
ATOM   3813  CG  GLU C 479      41.265  25.536  19.855  1.00 41.31           C  
ATOM   3814  CD  GLU C 479      42.575  25.846  20.563  1.00 41.94           C  
ATOM   3815  OE1 GLU C 479      42.704  26.958  21.121  1.00 41.58           O  
ATOM   3816  OE2 GLU C 479      43.479  24.984  20.543  1.00 38.62           O  
ATOM   3817  H   GLU C 479      39.410  22.701  20.142  1.00  0.00           H  
ATOM   3818  N   TRP C 480      38.818  23.682  23.292  1.00 27.98           N  
ATOM   3819  CA  TRP C 480      38.278  23.737  24.651  1.00 26.47           C  
ATOM   3820  C   TRP C 480      39.030  22.794  25.590  1.00 24.45           C  
ATOM   3821  O   TRP C 480      39.505  23.209  26.646  1.00 24.00           O  
ATOM   3822  CB  TRP C 480      36.785  23.379  24.652  1.00 23.19           C  
ATOM   3823  CG  TRP C 480      36.154  23.415  26.019  1.00 13.49           C  
ATOM   3824  CD1 TRP C 480      36.089  22.389  26.927  1.00  4.35           C  
ATOM   3825  CD2 TRP C 480      35.546  24.549  26.653  1.00  2.00           C  
ATOM   3826  NE1 TRP C 480      35.488  22.821  28.084  1.00  3.12           N  
ATOM   3827  CE2 TRP C 480      35.146  24.141  27.944  1.00  2.00           C  
ATOM   3828  CE3 TRP C 480      35.304  25.869  26.254  1.00  2.00           C  
ATOM   3829  CZ2 TRP C 480      34.516  25.007  28.839  1.00  4.71           C  
ATOM   3830  CZ3 TRP C 480      34.682  26.732  27.147  1.00  2.19           C  
ATOM   3831  CH2 TRP C 480      34.294  26.297  28.424  1.00  2.00           C  
ATOM   3832  H   TRP C 480      38.224  23.509  22.531  1.00  0.00           H  
ATOM   3833  HE1 TRP C 480      35.291  22.255  28.869  1.00  0.00           H  
ATOM   3834  N   ASP C 481      39.124  21.528  25.198  1.00 20.58           N  
ATOM   3835  CA  ASP C 481      39.871  20.530  25.953  1.00 20.43           C  
ATOM   3836  C   ASP C 481      41.310  20.972  26.234  1.00 25.74           C  
ATOM   3837  O   ASP C 481      41.755  20.964  27.381  1.00 29.82           O  
ATOM   3838  CB  ASP C 481      39.879  19.203  25.191  1.00 19.94           C  
ATOM   3839  CG  ASP C 481      38.537  18.500  25.220  1.00 23.84           C  
ATOM   3840  OD1 ASP C 481      37.642  18.934  25.972  1.00 25.78           O  
ATOM   3841  OD2 ASP C 481      38.383  17.494  24.505  1.00 29.75           O  
ATOM   3842  H   ASP C 481      38.675  21.272  24.360  1.00  0.00           H  
ATOM   3843  N   ARG C 482      41.997  21.448  25.199  1.00 24.92           N  
ATOM   3844  CA  ARG C 482      43.375  21.916  25.333  1.00 20.21           C  
ATOM   3845  C   ARG C 482      43.495  23.087  26.308  1.00 21.64           C  
ATOM   3846  O   ARG C 482      44.500  23.224  27.005  1.00 26.77           O  
ATOM   3847  CB  ARG C 482      43.935  22.337  23.972  1.00 19.71           C  
ATOM   3848  CG  ARG C 482      45.455  22.455  23.937  1.00 22.22           C  
ATOM   3849  CD  ARG C 482      45.950  23.079  22.640  1.00 11.56           C  
ATOM   3850  NE  ARG C 482      45.514  24.463  22.506  1.00  4.92           N  
ATOM   3851  CZ  ARG C 482      46.257  25.514  22.830  1.00 17.85           C  
ATOM   3852  NH1 ARG C 482      47.485  25.347  23.305  1.00 17.35           N  
ATOM   3853  NH2 ARG C 482      45.769  26.735  22.682  1.00 23.07           N  
ATOM   3854  H   ARG C 482      41.576  21.428  24.311  1.00  0.00           H  
ATOM   3855  HE  ARG C 482      44.595  24.627  22.222  1.00  0.00           H  
ATOM   3856 HH11 ARG C 482      47.844  24.427  23.437  1.00  0.00           H  
ATOM   3857 HH12 ARG C 482      48.039  26.142  23.551  1.00  0.00           H  
ATOM   3858 HH21 ARG C 482      44.841  26.860  22.329  1.00  0.00           H  
ATOM   3859 HH22 ARG C 482      46.323  27.530  22.929  1.00  0.00           H  
ATOM   3860  N   LEU C 483      42.473  23.937  26.347  1.00 18.02           N  
ATOM   3861  CA  LEU C 483      42.469  25.078  27.257  1.00 14.74           C  
ATOM   3862  C   LEU C 483      41.800  24.771  28.597  1.00 15.21           C  
ATOM   3863  O   LEU C 483      41.684  25.648  29.448  1.00 22.18           O  
ATOM   3864  CB  LEU C 483      41.772  26.273  26.611  1.00 17.77           C  
ATOM   3865  CG  LEU C 483      42.330  26.793  25.284  1.00 24.74           C  
ATOM   3866  CD1 LEU C 483      41.393  27.847  24.734  1.00 32.10           C  
ATOM   3867  CD2 LEU C 483      43.716  27.375  25.476  1.00 25.46           C  
ATOM   3868  H   LEU C 483      41.748  23.812  25.697  1.00  0.00           H  
ATOM   3869  N   HIS C 484      41.306  23.548  28.762  1.00 15.93           N  
ATOM   3870  CA  HIS C 484      40.596  23.169  29.982  1.00 18.55           C  
ATOM   3871  C   HIS C 484      40.996  21.791  30.496  1.00 18.76           C  
ATOM   3872  O   HIS C 484      40.215  20.846  30.423  1.00 25.26           O  
ATOM   3873  CB  HIS C 484      39.079  23.212  29.756  1.00 13.80           C  
ATOM   3874  CG  HIS C 484      38.549  24.590  29.510  1.00  8.18           C  
ATOM   3875  ND1 HIS C 484      38.588  25.192  28.271  1.00 14.79           N  
ATOM   3876  CD2 HIS C 484      38.053  25.518  30.362  1.00 13.78           C  
ATOM   3877  CE1 HIS C 484      38.149  26.433  28.370  1.00 13.03           C  
ATOM   3878  NE2 HIS C 484      37.818  26.656  29.629  1.00 17.19           N  
ATOM   3879  H   HIS C 484      41.447  22.882  28.055  1.00  0.00           H  
ATOM   3880  HD1 HIS C 484      38.854  24.758  27.434  1.00  0.00           H  
ATOM   3881  HE2 HIS C 484      37.467  27.499  29.981  1.00  0.00           H  
ATOM   3882  N   PRO C 485      42.165  21.694  31.148  1.00 18.47           N  
ATOM   3883  CA  PRO C 485      42.599  20.428  31.749  1.00 17.94           C  
ATOM   3884  C   PRO C 485      41.668  19.908  32.849  1.00 18.23           C  
ATOM   3885  O   PRO C 485      41.139  20.675  33.662  1.00 17.83           O  
ATOM   3886  CB  PRO C 485      43.999  20.743  32.278  1.00 17.14           C  
ATOM   3887  CG  PRO C 485      43.990  22.221  32.491  1.00 21.39           C  
ATOM   3888  CD  PRO C 485      43.144  22.771  31.382  1.00 21.70           C  
ATOM   3889  N   VAL C 486      41.472  18.595  32.849  1.00 14.78           N  
ATOM   3890  CA  VAL C 486      40.581  17.917  33.782  1.00 17.13           C  
ATOM   3891  C   VAL C 486      41.130  17.907  35.207  1.00 20.34           C  
ATOM   3892  O   VAL C 486      42.157  17.294  35.483  1.00 24.54           O  
ATOM   3893  CB  VAL C 486      40.344  16.447  33.349  1.00 19.50           C  
ATOM   3894  CG1 VAL C 486      39.322  15.777  34.258  1.00 16.72           C  
ATOM   3895  CG2 VAL C 486      39.875  16.399  31.913  1.00 28.32           C  
ATOM   3896  H   VAL C 486      41.969  18.069  32.190  1.00  0.00           H  
ATOM   3897  N   HIS C 487      40.409  18.547  36.118  1.00 21.46           N  
ATOM   3898  CA  HIS C 487      40.703  18.424  37.540  1.00  8.74           C  
ATOM   3899  C   HIS C 487      40.169  17.100  38.061  1.00  9.30           C  
ATOM   3900  O   HIS C 487      39.008  16.773  37.851  1.00 17.43           O  
ATOM   3901  CB  HIS C 487      40.057  19.564  38.313  1.00  4.21           C  
ATOM   3902  CG  HIS C 487      40.577  20.915  37.943  1.00  3.34           C  
ATOM   3903  ND1 HIS C 487      40.113  21.618  36.852  1.00 11.85           N  
ATOM   3904  CD2 HIS C 487      41.434  21.743  38.583  1.00  7.18           C  
ATOM   3905  CE1 HIS C 487      40.647  22.825  36.844  1.00 11.40           C  
ATOM   3906  NE2 HIS C 487      41.454  22.926  37.884  1.00 19.01           N  
ATOM   3907  H   HIS C 487      39.611  18.993  35.789  1.00  0.00           H  
ATOM   3908  HD1 HIS C 487      39.547  21.284  36.127  1.00  0.00           H  
ATOM   3909  HE2 HIS C 487      41.945  23.733  38.152  1.00  0.00           H  
ATOM   3910  N   ALA C 488      41.027  16.326  38.710  1.00 18.42           N  
ATOM   3911  CA  ALA C 488      40.606  15.072  39.329  1.00 16.28           C  
ATOM   3912  C   ALA C 488      39.756  15.322  40.574  1.00 17.03           C  
ATOM   3913  O   ALA C 488      39.758  16.421  41.135  1.00 16.95           O  
ATOM   3914  CB  ALA C 488      41.832  14.242  39.692  1.00 25.54           C  
ATOM   3915  H   ALA C 488      41.975  16.572  38.703  1.00  0.00           H  
ATOM   3916  N   GLY C 489      39.042  14.297  41.018  1.00 20.29           N  
ATOM   3917  CA  GLY C 489      38.353  14.403  42.291  1.00 28.04           C  
ATOM   3918  C   GLY C 489      36.946  13.843  42.320  1.00 31.77           C  
ATOM   3919  O   GLY C 489      36.272  13.782  41.289  1.00 35.08           O  
ATOM   3920  H   GLY C 489      38.923  13.526  40.423  1.00  0.00           H  
ATOM   3921  N   PRO C 490      36.481  13.394  43.496  1.00 30.70           N  
ATOM   3922  CA  PRO C 490      35.094  12.962  43.674  1.00 28.22           C  
ATOM   3923  C   PRO C 490      34.105  14.093  43.419  1.00 29.32           C  
ATOM   3924  O   PRO C 490      34.347  15.242  43.783  1.00 28.97           O  
ATOM   3925  CB  PRO C 490      35.057  12.489  45.124  1.00 30.22           C  
ATOM   3926  CG  PRO C 490      36.098  13.316  45.794  1.00 29.61           C  
ATOM   3927  CD  PRO C 490      37.205  13.421  44.779  1.00 32.09           C  
ATOM   3928  N   ILE C 491      33.006  13.767  42.754  1.00 32.82           N  
ATOM   3929  CA  ILE C 491      31.970  14.756  42.487  1.00 32.15           C  
ATOM   3930  C   ILE C 491      31.064  14.940  43.710  1.00 30.32           C  
ATOM   3931  O   ILE C 491      30.515  13.969  44.243  1.00 28.50           O  
ATOM   3932  CB  ILE C 491      31.122  14.351  41.256  1.00 30.79           C  
ATOM   3933  CG1 ILE C 491      32.039  13.869  40.128  1.00 27.78           C  
ATOM   3934  CG2 ILE C 491      30.314  15.540  40.764  1.00 25.91           C  
ATOM   3935  CD1 ILE C 491      31.358  12.976  39.123  1.00 32.68           C  
ATOM   3936  H   ILE C 491      32.945  12.865  42.390  1.00  0.00           H  
ATOM   3937  N   ALA C 492      31.026  16.165  44.229  1.00 31.97           N  
ATOM   3938  CA  ALA C 492      30.151  16.505  45.349  1.00 33.44           C  
ATOM   3939  C   ALA C 492      28.682  16.395  44.953  1.00 42.47           C  
ATOM   3940  O   ALA C 492      28.310  16.691  43.813  1.00 43.46           O  
ATOM   3941  CB  ALA C 492      30.450  17.912  45.841  1.00 29.12           C  
ATOM   3942  H   ALA C 492      31.625  16.838  43.844  1.00  0.00           H  
ATOM   3943  N   PRO C 493      27.821  15.989  45.900  1.00 43.60           N  
ATOM   3944  CA  PRO C 493      26.372  16.030  45.678  1.00 43.51           C  
ATOM   3945  C   PRO C 493      25.894  17.442  45.328  1.00 40.64           C  
ATOM   3946  O   PRO C 493      26.372  18.428  45.898  1.00 34.99           O  
ATOM   3947  CB  PRO C 493      25.799  15.539  47.007  1.00 44.33           C  
ATOM   3948  CG  PRO C 493      26.850  15.894  48.006  1.00 47.14           C  
ATOM   3949  CD  PRO C 493      28.147  15.651  47.295  1.00 45.38           C  
ATOM   3950  N   GLY C 494      25.082  17.536  44.279  1.00 38.39           N  
ATOM   3951  CA  GLY C 494      24.643  18.833  43.790  1.00 35.94           C  
ATOM   3952  C   GLY C 494      25.611  19.483  42.814  1.00 34.12           C  
ATOM   3953  O   GLY C 494      25.356  20.569  42.288  1.00 35.00           O  
ATOM   3954  H   GLY C 494      24.775  16.708  43.857  1.00  0.00           H  
ATOM   3955  N   GLN C 495      26.765  18.859  42.629  1.00 35.57           N  
ATOM   3956  CA  GLN C 495      27.739  19.340  41.665  1.00 37.51           C  
ATOM   3957  C   GLN C 495      27.788  18.391  40.478  1.00 35.25           C  
ATOM   3958  O   GLN C 495      27.306  17.262  40.552  1.00 33.44           O  
ATOM   3959  CB  GLN C 495      29.126  19.434  42.305  1.00 41.00           C  
ATOM   3960  CG  GLN C 495      29.328  20.624  43.235  0.00 42.43           C  
ATOM   3961  CD  GLN C 495      30.767  20.752  43.710  0.00 44.42           C  
ATOM   3962  OE1 GLN C 495      31.661  20.076  43.210  0.00 45.00           O  
ATOM   3963  NE2 GLN C 495      30.993  21.612  44.688  0.00 45.50           N  
ATOM   3964  H   GLN C 495      26.964  18.041  43.130  1.00  0.00           H  
ATOM   3965 HE21 GLN C 495      31.937  21.667  44.940  1.00  0.00           H  
ATOM   3966 HE22 GLN C 495      30.286  22.119  45.121  1.00  0.00           H  
ATOM   3967  N   MET C 496      28.350  18.863  39.375  1.00 40.33           N  
ATOM   3968  CA  MET C 496      28.509  18.025  38.195  1.00 43.29           C  
ATOM   3969  C   MET C 496      29.947  18.007  37.700  1.00 38.12           C  
ATOM   3970  O   MET C 496      30.691  18.972  37.878  1.00 39.43           O  
ATOM   3971  CB  MET C 496      27.585  18.504  37.074  1.00 50.67           C  
ATOM   3972  CG  MET C 496      26.167  17.952  37.157  1.00 53.82           C  
ATOM   3973  SD  MET C 496      25.183  18.345  35.707  1.00 45.61           S  
ATOM   3974  CE  MET C 496      26.083  17.487  34.456  1.00 46.13           C  
ATOM   3975  H   MET C 496      28.708  19.770  39.367  1.00  0.00           H  
ATOM   3976  N   ARG C 497      30.349  16.872  37.142  1.00 32.93           N  
ATOM   3977  CA  ARG C 497      31.600  16.771  36.399  1.00 30.96           C  
ATOM   3978  C   ARG C 497      31.734  17.927  35.401  1.00 32.17           C  
ATOM   3979  O   ARG C 497      30.743  18.372  34.816  1.00 30.44           O  
ATOM   3980  CB  ARG C 497      31.644  15.424  35.671  1.00 36.61           C  
ATOM   3981  CG  ARG C 497      32.418  15.413  34.365  1.00 48.12           C  
ATOM   3982  CD  ARG C 497      32.038  14.210  33.515  1.00 51.22           C  
ATOM   3983  NE  ARG C 497      30.692  14.312  32.949  1.00 46.54           N  
ATOM   3984  CZ  ARG C 497      30.402  14.085  31.670  1.00 46.58           C  
ATOM   3985  NH1 ARG C 497      31.368  13.830  30.797  1.00 53.98           N  
ATOM   3986  NH2 ARG C 497      29.145  14.122  31.256  1.00 41.08           N  
ATOM   3987  H   ARG C 497      29.764  16.097  37.238  1.00  0.00           H  
ATOM   3988  HE  ARG C 497      29.956  14.570  33.542  1.00  0.00           H  
ATOM   3989 HH11 ARG C 497      32.320  13.779  31.099  1.00  0.00           H  
ATOM   3990 HH12 ARG C 497      31.142  13.651  29.840  1.00  0.00           H  
ATOM   3991 HH21 ARG C 497      28.407  14.311  31.902  1.00  0.00           H  
ATOM   3992 HH22 ARG C 497      28.938  13.947  30.293  1.00  0.00           H  
ATOM   3993  N   GLU C 498      32.938  18.479  35.295  1.00 29.34           N  
ATOM   3994  CA  GLU C 498      33.201  19.567  34.360  1.00 26.98           C  
ATOM   3995  C   GLU C 498      33.133  19.057  32.914  1.00 25.31           C  
ATOM   3996  O   GLU C 498      33.509  17.917  32.632  1.00 28.72           O  
ATOM   3997  CB  GLU C 498      34.572  20.191  34.655  1.00 24.42           C  
ATOM   3998  CG  GLU C 498      35.760  19.262  34.390  1.00 43.64           C  
ATOM   3999  CD  GLU C 498      36.950  19.517  35.308  1.00 43.49           C  
ATOM   4000  OE1 GLU C 498      37.386  20.683  35.440  1.00 35.93           O  
ATOM   4001  OE2 GLU C 498      37.468  18.534  35.878  1.00 47.33           O  
ATOM   4002  H   GLU C 498      33.643  18.139  35.878  1.00  0.00           H  
ATOM   4003  N   PRO C 499      32.553  19.858  32.005  1.00 27.85           N  
ATOM   4004  CA  PRO C 499      32.281  19.459  30.618  1.00 26.62           C  
ATOM   4005  C   PRO C 499      33.513  19.480  29.704  1.00 24.60           C  
ATOM   4006  O   PRO C 499      34.336  20.397  29.760  1.00 23.71           O  
ATOM   4007  CB  PRO C 499      31.231  20.472  30.166  1.00 27.19           C  
ATOM   4008  CG  PRO C 499      31.572  21.696  30.943  1.00 22.37           C  
ATOM   4009  CD  PRO C 499      31.983  21.184  32.303  1.00 26.82           C  
ATOM   4010  N   ARG C 500      33.661  18.430  28.907  1.00 21.05           N  
ATOM   4011  CA  ARG C 500      34.622  18.418  27.809  1.00 22.80           C  
ATOM   4012  C   ARG C 500      33.980  19.006  26.546  1.00 21.60           C  
ATOM   4013  O   ARG C 500      32.770  19.225  26.509  1.00 21.19           O  
ATOM   4014  CB  ARG C 500      35.081  16.985  27.542  1.00 17.62           C  
ATOM   4015  CG  ARG C 500      35.316  16.162  28.801  1.00 20.79           C  
ATOM   4016  CD  ARG C 500      36.749  16.283  29.303  1.00 23.59           C  
ATOM   4017  NE  ARG C 500      37.184  17.672  29.387  1.00 24.32           N  
ATOM   4018  CZ  ARG C 500      38.400  18.086  29.057  1.00 30.93           C  
ATOM   4019  NH1 ARG C 500      39.354  17.213  28.850  1.00 42.73           N  
ATOM   4020  NH2 ARG C 500      38.697  19.368  29.040  1.00 27.94           N  
ATOM   4021  H   ARG C 500      33.145  17.642  29.136  1.00  0.00           H  
ATOM   4022  HE  ARG C 500      36.559  18.350  29.643  1.00  0.00           H  
ATOM   4023 HH11 ARG C 500      39.811  16.939  29.640  1.00  0.00           H  
ATOM   4024 HH12 ARG C 500      39.478  16.937  27.913  1.00  0.00           H  
ATOM   4025 HH21 ARG C 500      37.955  19.979  29.261  1.00  0.00           H  
ATOM   4026 HH22 ARG C 500      39.616  19.711  28.813  1.00  0.00           H  
ATOM   4027  N   GLY C 501      34.780  19.237  25.508  1.00 20.78           N  
ATOM   4028  CA  GLY C 501      34.253  19.774  24.262  1.00 18.93           C  
ATOM   4029  C   GLY C 501      33.144  18.923  23.658  1.00 19.43           C  
ATOM   4030  O   GLY C 501      32.114  19.442  23.232  1.00 21.12           O  
ATOM   4031  H   GLY C 501      35.729  19.092  25.600  1.00  0.00           H  
ATOM   4032  N   SER C 502      33.294  17.606  23.756  1.00 11.72           N  
ATOM   4033  CA  SER C 502      32.294  16.665  23.259  1.00 12.30           C  
ATOM   4034  C   SER C 502      30.995  16.709  24.077  1.00 22.81           C  
ATOM   4035  O   SER C 502      29.928  16.287  23.611  1.00 12.88           O  
ATOM   4036  CB  SER C 502      32.869  15.249  23.271  1.00  4.38           C  
ATOM   4037  OG  SER C 502      33.187  14.828  24.588  1.00  6.29           O  
ATOM   4038  H   SER C 502      34.117  17.264  24.154  1.00  0.00           H  
ATOM   4039  HG  SER C 502      32.415  14.339  24.901  1.00  0.00           H  
ATOM   4040  N   ASP C 503      31.104  17.189  25.313  1.00 23.30           N  
ATOM   4041  CA  ASP C 503      29.943  17.388  26.174  1.00 16.37           C  
ATOM   4042  C   ASP C 503      29.214  18.671  25.799  1.00 15.32           C  
ATOM   4043  O   ASP C 503      27.987  18.710  25.760  1.00 24.67           O  
ATOM   4044  CB  ASP C 503      30.368  17.469  27.643  1.00 22.06           C  
ATOM   4045  CG  ASP C 503      30.831  16.138  28.200  1.00 20.62           C  
ATOM   4046  OD1 ASP C 503      30.217  15.102  27.880  1.00 16.19           O  
ATOM   4047  OD2 ASP C 503      31.778  16.138  29.012  1.00 29.55           O  
ATOM   4048  H   ASP C 503      32.001  17.420  25.635  1.00  0.00           H  
ATOM   4049  N   ILE C 504      29.972  19.739  25.595  1.00 13.62           N  
ATOM   4050  CA  ILE C 504      29.407  21.013  25.171  1.00 12.55           C  
ATOM   4051  C   ILE C 504      28.718  20.873  23.811  1.00 18.27           C  
ATOM   4052  O   ILE C 504      27.673  21.475  23.565  1.00 16.99           O  
ATOM   4053  CB  ILE C 504      30.506  22.093  25.087  1.00 13.85           C  
ATOM   4054  CG1 ILE C 504      31.133  22.294  26.469  1.00 13.53           C  
ATOM   4055  CG2 ILE C 504      29.928  23.406  24.568  1.00 11.11           C  
ATOM   4056  CD1 ILE C 504      32.161  23.388  26.516  1.00 13.67           C  
ATOM   4057  H   ILE C 504      30.934  19.674  25.780  1.00  0.00           H  
ATOM   4058  N   ALA C 505      29.273  20.010  22.967  1.00 18.41           N  
ATOM   4059  CA  ALA C 505      28.699  19.712  21.659  1.00 20.03           C  
ATOM   4060  C   ALA C 505      27.516  18.739  21.740  1.00 19.06           C  
ATOM   4061  O   ALA C 505      26.852  18.475  20.742  1.00 25.62           O  
ATOM   4062  CB  ALA C 505      29.779  19.150  20.738  1.00 13.05           C  
ATOM   4063  H   ALA C 505      30.152  19.646  23.207  1.00  0.00           H  
ATOM   4064  N   GLY C 506      27.288  18.172  22.920  1.00 22.79           N  
ATOM   4065  CA  GLY C 506      26.174  17.258  23.109  1.00 15.03           C  
ATOM   4066  C   GLY C 506      26.418  15.844  22.610  1.00 19.67           C  
ATOM   4067  O   GLY C 506      25.507  15.018  22.606  1.00 23.20           O  
ATOM   4068  H   GLY C 506      27.831  18.451  23.684  1.00  0.00           H  
ATOM   4069  N   THR C 507      27.645  15.569  22.182  1.00 19.23           N  
ATOM   4070  CA  THR C 507      28.023  14.257  21.647  1.00 12.91           C  
ATOM   4071  C   THR C 507      27.931  13.215  22.741  1.00 17.64           C  
ATOM   4072  O   THR C 507      27.484  12.095  22.517  1.00 21.72           O  
ATOM   4073  CB  THR C 507      29.490  14.261  21.127  1.00 18.65           C  
ATOM   4074  OG1 THR C 507      29.640  15.262  20.114  1.00 22.62           O  
ATOM   4075  CG2 THR C 507      29.886  12.895  20.556  1.00 18.37           C  
ATOM   4076  H   THR C 507      28.321  16.278  22.200  1.00  0.00           H  
ATOM   4077  HG1 THR C 507      29.041  15.124  19.375  1.00  0.00           H  
ATOM   4078  N   THR C 508      28.468  13.568  23.902  1.00 23.55           N  
ATOM   4079  CA  THR C 508      28.659  12.617  24.992  1.00 22.49           C  
ATOM   4080  C   THR C 508      27.927  13.026  26.272  1.00 23.17           C  
ATOM   4081  O   THR C 508      28.090  12.396  27.315  1.00 30.81           O  
ATOM   4082  CB  THR C 508      30.162  12.455  25.314  1.00 24.54           C  
ATOM   4083  OG1 THR C 508      30.765  13.751  25.427  1.00 17.43           O  
ATOM   4084  CG2 THR C 508      30.871  11.661  24.217  1.00 22.68           C  
ATOM   4085  H   THR C 508      28.832  14.476  23.966  1.00  0.00           H  
ATOM   4086  HG1 THR C 508      30.597  14.000  26.334  1.00  0.00           H  
ATOM   4087  N   SER C 509      27.175  14.121  26.209  1.00 16.39           N  
ATOM   4088  CA  SER C 509      26.354  14.546  27.337  1.00 16.25           C  
ATOM   4089  C   SER C 509      24.879  14.249  27.103  1.00 23.95           C  
ATOM   4090  O   SER C 509      24.388  14.329  25.975  1.00 29.21           O  
ATOM   4091  CB  SER C 509      26.530  16.040  27.605  1.00  9.57           C  
ATOM   4092  OG  SER C 509      26.299  16.793  26.432  1.00 12.35           O  
ATOM   4093  H   SER C 509      27.094  14.599  25.361  1.00  0.00           H  
ATOM   4094  HG  SER C 509      26.619  17.700  26.556  1.00  0.00           H  
ATOM   4095  N   THR C 510      24.190  13.850  28.167  1.00 23.99           N  
ATOM   4096  CA  THR C 510      22.738  13.672  28.131  1.00 14.53           C  
ATOM   4097  C   THR C 510      22.027  15.008  28.318  1.00 14.18           C  
ATOM   4098  O   THR C 510      22.623  15.972  28.805  1.00 19.62           O  
ATOM   4099  CB  THR C 510      22.258  12.730  29.244  1.00 15.95           C  
ATOM   4100  OG1 THR C 510      22.479  13.349  30.520  1.00 22.00           O  
ATOM   4101  CG2 THR C 510      22.995  11.399  29.178  1.00  2.00           C  
ATOM   4102  H   THR C 510      24.697  13.634  28.966  1.00  0.00           H  
ATOM   4103  HG1 THR C 510      23.379  13.157  30.807  1.00  0.00           H  
ATOM   4104  N   LEU C 511      20.736  15.047  28.003  1.00 13.16           N  
ATOM   4105  CA  LEU C 511      19.962  16.279  28.142  1.00 11.50           C  
ATOM   4106  C   LEU C 511      19.874  16.732  29.602  1.00  5.89           C  
ATOM   4107  O   LEU C 511      20.012  17.922  29.898  1.00 11.13           O  
ATOM   4108  CB  LEU C 511      18.557  16.097  27.551  1.00 12.57           C  
ATOM   4109  CG  LEU C 511      17.498  17.168  27.835  1.00  8.44           C  
ATOM   4110  CD1 LEU C 511      17.953  18.524  27.344  1.00  4.63           C  
ATOM   4111  CD2 LEU C 511      16.197  16.779  27.177  1.00 14.39           C  
ATOM   4112  H   LEU C 511      20.322  14.238  27.630  1.00  0.00           H  
ATOM   4113  N   GLN C 512      19.730  15.776  30.517  1.00 10.59           N  
ATOM   4114  CA  GLN C 512      19.647  16.096  31.946  1.00 14.04           C  
ATOM   4115  C   GLN C 512      20.936  16.739  32.451  1.00 10.40           C  
ATOM   4116  O   GLN C 512      20.900  17.761  33.142  1.00 11.96           O  
ATOM   4117  CB  GLN C 512      19.334  14.842  32.772  1.00  9.75           C  
ATOM   4118  CG  GLN C 512      17.976  14.202  32.484  0.00 14.43           C  
ATOM   4119  CD  GLN C 512      16.832  15.201  32.463  0.00 14.13           C  
ATOM   4120  OE1 GLN C 512      16.452  15.755  33.491  0.00 15.61           O  
ATOM   4121  NE2 GLN C 512      16.251  15.404  31.293  0.00 18.15           N  
ATOM   4122  H   GLN C 512      19.642  14.851  30.196  1.00  0.00           H  
ATOM   4123 HE21 GLN C 512      15.513  16.034  31.338  1.00  0.00           H  
ATOM   4124 HE22 GLN C 512      16.568  14.933  30.501  1.00  0.00           H  
ATOM   4125  N   GLU C 513      22.064  16.239  31.949  1.00 16.17           N  
ATOM   4126  CA  GLU C 513      23.373  16.834  32.226  1.00 19.50           C  
ATOM   4127  C   GLU C 513      23.479  18.263  31.710  1.00 23.12           C  
ATOM   4128  O   GLU C 513      23.978  19.152  32.412  1.00 26.10           O  
ATOM   4129  CB  GLU C 513      24.485  16.003  31.591  1.00 13.92           C  
ATOM   4130  CG  GLU C 513      24.832  14.746  32.350  1.00 19.94           C  
ATOM   4131  CD  GLU C 513      25.863  13.899  31.633  1.00 29.11           C  
ATOM   4132  OE1 GLU C 513      26.099  14.128  30.427  1.00 30.04           O  
ATOM   4133  OE2 GLU C 513      26.439  12.997  32.276  1.00 31.69           O  
ATOM   4134  H   GLU C 513      21.994  15.440  31.386  1.00  0.00           H  
ATOM   4135  N   GLN C 514      23.064  18.464  30.460  1.00 18.27           N  
ATOM   4136  CA  GLN C 514      23.124  19.782  29.834  1.00 13.41           C  
ATOM   4137  C   GLN C 514      22.301  20.784  30.636  1.00  9.49           C  
ATOM   4138  O   GLN C 514      22.764  21.885  30.929  1.00 10.75           O  
ATOM   4139  CB  GLN C 514      22.624  19.710  28.385  1.00  9.67           C  
ATOM   4140  CG  GLN C 514      23.495  18.847  27.461  1.00 12.82           C  
ATOM   4141  CD  GLN C 514      22.827  18.534  26.120  1.00 10.30           C  
ATOM   4142  OE1 GLN C 514      21.924  19.240  25.679  1.00 13.03           O  
ATOM   4143  NE2 GLN C 514      23.282  17.480  25.466  1.00  3.80           N  
ATOM   4144  H   GLN C 514      22.726  17.694  29.952  1.00  0.00           H  
ATOM   4145 HE21 GLN C 514      22.852  17.352  24.597  1.00  0.00           H  
ATOM   4146 HE22 GLN C 514      23.990  16.914  25.834  1.00  0.00           H  
ATOM   4147  N   ILE C 515      21.129  20.353  31.094  1.00 19.76           N  
ATOM   4148  CA  ILE C 515      20.301  21.182  31.968  1.00 19.86           C  
ATOM   4149  C   ILE C 515      21.050  21.489  33.269  1.00 14.46           C  
ATOM   4150  O   ILE C 515      21.154  22.648  33.676  1.00 11.56           O  
ATOM   4151  CB  ILE C 515      18.953  20.486  32.300  1.00 20.72           C  
ATOM   4152  CG1 ILE C 515      18.207  20.135  31.012  1.00 23.13           C  
ATOM   4153  CG2 ILE C 515      18.070  21.412  33.129  1.00 23.07           C  
ATOM   4154  CD1 ILE C 515      16.975  19.277  31.236  1.00 20.53           C  
ATOM   4155  H   ILE C 515      20.820  19.467  30.808  1.00  0.00           H  
ATOM   4156  N   GLY C 516      21.674  20.460  33.839  1.00 14.25           N  
ATOM   4157  CA  GLY C 516      22.442  20.621  35.064  1.00 17.46           C  
ATOM   4158  C   GLY C 516      23.503  21.705  35.016  1.00 16.09           C  
ATOM   4159  O   GLY C 516      23.572  22.560  35.902  1.00 19.54           O  
ATOM   4160  H   GLY C 516      21.589  19.572  33.432  1.00  0.00           H  
ATOM   4161  N   TRP C 517      24.287  21.717  33.945  1.00 22.13           N  
ATOM   4162  CA  TRP C 517      25.297  22.751  33.745  1.00 20.30           C  
ATOM   4163  C   TRP C 517      24.679  24.135  33.535  1.00 25.92           C  
ATOM   4164  O   TRP C 517      25.037  25.100  34.217  1.00 29.03           O  
ATOM   4165  CB  TRP C 517      26.182  22.390  32.550  1.00 18.50           C  
ATOM   4166  CG  TRP C 517      27.121  21.260  32.825  1.00 18.98           C  
ATOM   4167  CD1 TRP C 517      27.933  21.122  33.911  1.00 21.85           C  
ATOM   4168  CD2 TRP C 517      27.375  20.125  31.985  1.00 22.22           C  
ATOM   4169  NE1 TRP C 517      28.682  19.976  33.797  1.00 28.73           N  
ATOM   4170  CE2 TRP C 517      28.359  19.344  32.627  1.00 21.57           C  
ATOM   4171  CE3 TRP C 517      26.871  19.695  30.751  1.00 23.00           C  
ATOM   4172  CZ2 TRP C 517      28.847  18.153  32.079  1.00 21.75           C  
ATOM   4173  CZ3 TRP C 517      27.358  18.511  30.205  1.00 19.26           C  
ATOM   4174  CH2 TRP C 517      28.336  17.754  30.872  1.00 19.96           C  
ATOM   4175  H   TRP C 517      24.199  20.976  33.305  1.00  0.00           H  
ATOM   4176  HE1 TRP C 517      29.352  19.656  34.446  1.00  0.00           H  
ATOM   4177  N   MET C 518      23.686  24.203  32.654  1.00 28.49           N  
ATOM   4178  CA  MET C 518      23.050  25.467  32.295  1.00 25.89           C  
ATOM   4179  C   MET C 518      22.250  26.094  33.438  1.00 29.81           C  
ATOM   4180  O   MET C 518      22.100  27.313  33.497  1.00 29.69           O  
ATOM   4181  CB  MET C 518      22.128  25.264  31.093  1.00 25.37           C  
ATOM   4182  CG  MET C 518      22.841  25.091  29.766  1.00 22.01           C  
ATOM   4183  SD  MET C 518      21.675  24.839  28.413  1.00 19.27           S  
ATOM   4184  CE  MET C 518      21.623  23.124  28.393  1.00  7.88           C  
ATOM   4185  H   MET C 518      23.381  23.364  32.241  1.00  0.00           H  
ATOM   4186  N   THR C 519      21.702  25.256  34.314  1.00 34.03           N  
ATOM   4187  CA  THR C 519      20.847  25.732  35.403  1.00 38.88           C  
ATOM   4188  C   THR C 519      21.571  25.915  36.745  1.00 36.00           C  
ATOM   4189  O   THR C 519      21.014  26.473  37.690  1.00 38.51           O  
ATOM   4190  CB  THR C 519      19.631  24.795  35.611  1.00 39.76           C  
ATOM   4191  OG1 THR C 519      18.608  25.499  36.325  1.00 57.84           O  
ATOM   4192  CG2 THR C 519      20.024  23.552  36.403  1.00 35.50           C  
ATOM   4193  H   THR C 519      21.873  24.303  34.188  1.00  0.00           H  
ATOM   4194  HG1 THR C 519      19.047  26.094  36.950  1.00  0.00           H  
ATOM   4195  N   HIS C 520      22.815  25.451  36.813  1.00 34.32           N  
ATOM   4196  CA  HIS C 520      23.620  25.498  38.032  1.00 30.00           C  
ATOM   4197  C   HIS C 520      23.881  26.926  38.508  1.00 33.12           C  
ATOM   4198  O   HIS C 520      23.800  27.872  37.735  1.00 39.29           O  
ATOM   4199  CB  HIS C 520      24.955  24.792  37.777  1.00 34.78           C  
ATOM   4200  CG  HIS C 520      25.803  24.621  38.999  1.00 38.34           C  
ATOM   4201  ND1 HIS C 520      26.936  25.372  39.230  1.00 37.12           N  
ATOM   4202  CD2 HIS C 520      25.720  23.742  40.026  1.00 42.82           C  
ATOM   4203  CE1 HIS C 520      27.517  24.961  40.342  1.00 37.39           C  
ATOM   4204  NE2 HIS C 520      26.798  23.974  40.845  1.00 43.99           N  
ATOM   4205  H   HIS C 520      23.182  25.069  35.988  1.00  0.00           H  
ATOM   4206  HD1 HIS C 520      27.301  26.085  38.656  1.00  0.00           H  
ATOM   4207  HE2 HIS C 520      26.982  23.503  41.688  1.00  0.00           H  
ATOM   4208  N   ASN C 521      24.212  27.078  39.785  1.00 38.62           N  
ATOM   4209  CA  ASN C 521      24.680  28.363  40.299  1.00 41.81           C  
ATOM   4210  C   ASN C 521      26.136  28.261  40.743  1.00 40.46           C  
ATOM   4211  O   ASN C 521      26.489  27.362  41.505  1.00 43.61           O  
ATOM   4212  CB  ASN C 521      23.814  28.822  41.473  1.00 49.03           C  
ATOM   4213  CG  ASN C 521      23.976  30.298  41.772  0.00 45.94           C  
ATOM   4214  OD1 ASN C 521      24.721  30.681  42.667  0.00 48.25           O  
ATOM   4215  ND2 ASN C 521      23.322  31.136  40.987  0.00 46.61           N  
ATOM   4216  H   ASN C 521      24.028  26.349  40.410  1.00  0.00           H  
ATOM   4217 HD21 ASN C 521      23.472  32.072  41.224  1.00  0.00           H  
ATOM   4218 HD22 ASN C 521      22.758  30.819  40.257  1.00  0.00           H  
ATOM   4219  N   PRO C 522      27.025  29.042  40.110  1.00 37.62           N  
ATOM   4220  CA  PRO C 522      26.787  29.744  38.842  1.00 39.44           C  
ATOM   4221  C   PRO C 522      26.765  28.793  37.634  1.00 41.88           C  
ATOM   4222  O   PRO C 522      27.322  27.690  37.694  1.00 46.02           O  
ATOM   4223  CB  PRO C 522      27.949  30.728  38.769  1.00 35.07           C  
ATOM   4224  CG  PRO C 522      29.052  30.014  39.473  1.00 37.56           C  
ATOM   4225  CD  PRO C 522      28.396  29.264  40.603  1.00 33.82           C  
ATOM   4226  N   PRO C 523      26.014  29.155  36.576  1.00 39.46           N  
ATOM   4227  CA  PRO C 523      25.793  28.250  35.441  1.00 32.60           C  
ATOM   4228  C   PRO C 523      27.001  28.081  34.524  1.00 26.38           C  
ATOM   4229  O   PRO C 523      27.731  29.034  34.243  1.00 22.35           O  
ATOM   4230  CB  PRO C 523      24.612  28.881  34.705  1.00 33.55           C  
ATOM   4231  CG  PRO C 523      24.702  30.325  35.045  1.00 40.62           C  
ATOM   4232  CD  PRO C 523      25.173  30.361  36.474  1.00 40.71           C  
ATOM   4233  N   ILE C 524      27.229  26.845  34.098  1.00 21.69           N  
ATOM   4234  CA  ILE C 524      28.213  26.563  33.060  1.00 24.50           C  
ATOM   4235  C   ILE C 524      27.520  26.519  31.693  1.00 16.26           C  
ATOM   4236  O   ILE C 524      26.836  25.548  31.363  1.00 16.26           O  
ATOM   4237  CB  ILE C 524      28.919  25.209  33.304  1.00 25.62           C  
ATOM   4238  CG1 ILE C 524      29.352  25.093  34.768  1.00 32.10           C  
ATOM   4239  CG2 ILE C 524      30.135  25.094  32.402  1.00 28.91           C  
ATOM   4240  CD1 ILE C 524      28.522  24.123  35.585  1.00 34.50           C  
ATOM   4241  H   ILE C 524      26.663  26.132  34.454  1.00  0.00           H  
ATOM   4242  N   PRO C 525      27.656  27.596  30.900  1.00 13.20           N  
ATOM   4243  CA  PRO C 525      26.682  27.888  29.844  1.00 15.34           C  
ATOM   4244  C   PRO C 525      26.961  27.116  28.557  1.00 16.12           C  
ATOM   4245  O   PRO C 525      27.221  27.707  27.508  1.00 20.27           O  
ATOM   4246  CB  PRO C 525      26.823  29.402  29.636  1.00 18.74           C  
ATOM   4247  CG  PRO C 525      27.987  29.846  30.519  1.00 12.67           C  
ATOM   4248  CD  PRO C 525      28.712  28.614  30.946  1.00 14.98           C  
ATOM   4249  N   VAL C 526      26.848  25.793  28.631  1.00 15.93           N  
ATOM   4250  CA  VAL C 526      27.188  24.919  27.513  1.00 17.09           C  
ATOM   4251  C   VAL C 526      26.369  25.193  26.246  1.00 20.51           C  
ATOM   4252  O   VAL C 526      26.872  25.036  25.132  1.00 19.73           O  
ATOM   4253  CB  VAL C 526      27.042  23.432  27.910  1.00 22.88           C  
ATOM   4254  CG1 VAL C 526      28.069  23.086  28.978  1.00 19.72           C  
ATOM   4255  CG2 VAL C 526      25.626  23.143  28.409  1.00 13.09           C  
ATOM   4256  H   VAL C 526      26.541  25.410  29.478  1.00  0.00           H  
ATOM   4257  N   GLY C 527      25.152  25.703  26.423  1.00 17.99           N  
ATOM   4258  CA  GLY C 527      24.333  26.074  25.283  1.00 12.20           C  
ATOM   4259  C   GLY C 527      24.889  27.288  24.559  1.00 18.18           C  
ATOM   4260  O   GLY C 527      25.063  27.278  23.340  1.00 18.22           O  
ATOM   4261  H   GLY C 527      24.822  25.854  27.332  1.00  0.00           H  
ATOM   4262  N   GLU C 528      25.294  28.286  25.338  1.00 18.56           N  
ATOM   4263  CA  GLU C 528      25.836  29.532  24.802  1.00 17.89           C  
ATOM   4264  C   GLU C 528      27.218  29.329  24.175  1.00 18.85           C  
ATOM   4265  O   GLU C 528      27.549  29.943  23.157  1.00 19.55           O  
ATOM   4266  CB  GLU C 528      25.923  30.574  25.925  1.00 14.63           C  
ATOM   4267  CG  GLU C 528      26.292  31.978  25.457  0.00 20.00           C  
ATOM   4268  CD  GLU C 528      26.685  32.905  26.598  0.00 21.73           C  
ATOM   4269  OE1 GLU C 528      26.274  32.659  27.753  0.00 22.94           O  
ATOM   4270  OE2 GLU C 528      27.402  33.893  26.334  0.00 23.62           O  
ATOM   4271  H   GLU C 528      25.230  28.153  26.308  1.00  0.00           H  
ATOM   4272  N   ILE C 529      28.019  28.467  24.796  1.00 16.87           N  
ATOM   4273  CA  ILE C 529      29.357  28.153  24.301  1.00 18.82           C  
ATOM   4274  C   ILE C 529      29.283  27.402  22.970  1.00 13.69           C  
ATOM   4275  O   ILE C 529      29.863  27.836  21.978  1.00 14.62           O  
ATOM   4276  CB  ILE C 529      30.151  27.302  25.331  1.00 21.82           C  
ATOM   4277  CG1 ILE C 529      30.385  28.110  26.609  1.00 25.02           C  
ATOM   4278  CG2 ILE C 529      31.494  26.871  24.748  1.00 18.44           C  
ATOM   4279  CD1 ILE C 529      30.817  27.262  27.794  1.00  8.89           C  
ATOM   4280  H   ILE C 529      27.693  28.070  25.629  1.00  0.00           H  
ATOM   4281  N   TYR C 530      28.501  26.326  22.935  1.00 14.80           N  
ATOM   4282  CA  TYR C 530      28.289  25.562  21.707  1.00 11.14           C  
ATOM   4283  C   TYR C 530      27.724  26.417  20.573  1.00 14.78           C  
ATOM   4284  O   TYR C 530      28.201  26.346  19.440  1.00 20.16           O  
ATOM   4285  CB  TYR C 530      27.351  24.387  21.968  1.00 14.62           C  
ATOM   4286  CG  TYR C 530      27.235  23.411  20.812  1.00 17.78           C  
ATOM   4287  CD1 TYR C 530      28.266  23.275  19.879  1.00 16.08           C  
ATOM   4288  CD2 TYR C 530      26.108  22.594  20.673  1.00 10.91           C  
ATOM   4289  CE1 TYR C 530      28.178  22.356  18.841  1.00 15.55           C  
ATOM   4290  CE2 TYR C 530      26.012  21.668  19.637  1.00 10.13           C  
ATOM   4291  CZ  TYR C 530      27.050  21.557  18.725  1.00 18.45           C  
ATOM   4292  OH  TYR C 530      26.977  20.650  17.696  1.00 21.48           O  
ATOM   4293  H   TYR C 530      28.061  26.028  23.762  1.00  0.00           H  
ATOM   4294  HH  TYR C 530      26.205  20.097  17.803  1.00  0.00           H  
ATOM   4295  N   LYS C 531      26.755  27.272  20.889  1.00 16.22           N  
ATOM   4296  CA  LYS C 531      26.174  28.161  19.885  1.00 16.91           C  
ATOM   4297  C   LYS C 531      27.233  29.047  19.226  1.00 22.23           C  
ATOM   4298  O   LYS C 531      27.234  29.209  18.003  1.00 21.94           O  
ATOM   4299  CB  LYS C 531      25.077  29.031  20.501  1.00 17.20           C  
ATOM   4300  CG  LYS C 531      24.286  29.831  19.476  1.00 22.96           C  
ATOM   4301  CD  LYS C 531      23.529  30.991  20.105  1.00 19.00           C  
ATOM   4302  CE  LYS C 531      22.289  30.520  20.838  1.00 22.16           C  
ATOM   4303  NZ  LYS C 531      21.403  31.668  21.176  1.00 33.49           N  
ATOM   4304  H   LYS C 531      26.388  27.254  21.802  1.00  0.00           H  
ATOM   4305  HZ1 LYS C 531      21.172  32.206  20.316  1.00  0.00           H  
ATOM   4306  HZ2 LYS C 531      20.525  31.315  21.610  1.00  0.00           H  
ATOM   4307  HZ3 LYS C 531      21.894  32.288  21.851  1.00  0.00           H  
ATOM   4308  N   ARG C 532      28.193  29.522  20.022  1.00 24.95           N  
ATOM   4309  CA  ARG C 532      29.319  30.308  19.507  1.00 20.61           C  
ATOM   4310  C   ARG C 532      30.177  29.524  18.515  1.00 13.60           C  
ATOM   4311  O   ARG C 532      30.584  30.053  17.484  1.00 19.74           O  
ATOM   4312  CB  ARG C 532      30.200  30.799  20.659  1.00 27.13           C  
ATOM   4313  CG  ARG C 532      29.603  31.943  21.459  1.00 33.15           C  
ATOM   4314  CD  ARG C 532      30.680  32.734  22.193  1.00 36.57           C  
ATOM   4315  NE  ARG C 532      31.390  31.921  23.176  1.00 38.42           N  
ATOM   4316  CZ  ARG C 532      31.183  31.978  24.489  1.00 38.53           C  
ATOM   4317  NH1 ARG C 532      30.283  32.814  24.993  1.00 27.73           N  
ATOM   4318  NH2 ARG C 532      31.883  31.194  25.300  1.00 38.36           N  
ATOM   4319  H   ARG C 532      28.123  29.368  20.990  1.00  0.00           H  
ATOM   4320  HE  ARG C 532      32.070  31.296  22.846  1.00  0.00           H  
ATOM   4321 HH11 ARG C 532      29.747  33.406  24.391  1.00  0.00           H  
ATOM   4322 HH12 ARG C 532      30.138  32.843  25.981  1.00  0.00           H  
ATOM   4323 HH21 ARG C 532      32.566  30.573  24.916  1.00  0.00           H  
ATOM   4324 HH22 ARG C 532      31.738  31.234  26.287  1.00  0.00           H  
ATOM   4325  N   TRP C 533      30.408  28.251  18.808  1.00 10.34           N  
ATOM   4326  CA  TRP C 533      31.138  27.370  17.895  1.00 17.53           C  
ATOM   4327  C   TRP C 533      30.374  27.174  16.586  1.00 24.77           C  
ATOM   4328  O   TRP C 533      30.979  27.109  15.511  1.00 25.59           O  
ATOM   4329  CB  TRP C 533      31.376  26.005  18.548  1.00 11.07           C  
ATOM   4330  CG  TRP C 533      32.132  26.062  19.842  1.00 12.66           C  
ATOM   4331  CD1 TRP C 533      32.755  27.152  20.386  1.00  7.55           C  
ATOM   4332  CD2 TRP C 533      32.385  24.969  20.733  1.00  3.43           C  
ATOM   4333  NE1 TRP C 533      33.380  26.802  21.555  1.00 14.77           N  
ATOM   4334  CE2 TRP C 533      33.177  25.466  21.788  1.00  6.62           C  
ATOM   4335  CE3 TRP C 533      32.031  23.614  20.734  1.00  6.93           C  
ATOM   4336  CZ2 TRP C 533      33.622  24.658  22.836  1.00  5.55           C  
ATOM   4337  CZ3 TRP C 533      32.475  22.808  21.771  1.00  6.87           C  
ATOM   4338  CH2 TRP C 533      33.264  23.335  22.810  1.00 11.77           C  
ATOM   4339  H   TRP C 533      30.102  27.922  19.681  1.00  0.00           H  
ATOM   4340  HE1 TRP C 533      33.782  27.428  22.197  1.00  0.00           H  
ATOM   4341  N   ILE C 534      29.045  27.083  16.686  1.00 21.33           N  
ATOM   4342  CA  ILE C 534      28.176  26.952  15.514  1.00 18.14           C  
ATOM   4343  C   ILE C 534      28.140  28.238  14.684  1.00 15.05           C  
ATOM   4344  O   ILE C 534      28.207  28.190  13.460  1.00 21.26           O  
ATOM   4345  CB  ILE C 534      26.727  26.558  15.922  1.00 16.05           C  
ATOM   4346  CG1 ILE C 534      26.721  25.165  16.549  1.00  9.50           C  
ATOM   4347  CG2 ILE C 534      25.816  26.541  14.709  1.00 10.81           C  
ATOM   4348  CD1 ILE C 534      25.380  24.746  17.097  1.00 16.40           C  
ATOM   4349  H   ILE C 534      28.659  27.056  17.588  1.00  0.00           H  
ATOM   4350  N   ILE C 535      28.117  29.384  15.354  1.00 14.41           N  
ATOM   4351  CA  ILE C 535      28.117  30.680  14.673  1.00 16.60           C  
ATOM   4352  C   ILE C 535      29.423  30.934  13.905  1.00 22.11           C  
ATOM   4353  O   ILE C 535      29.409  31.518  12.816  1.00 21.55           O  
ATOM   4354  CB  ILE C 535      27.869  31.840  15.678  1.00 12.55           C  
ATOM   4355  CG1 ILE C 535      26.473  31.714  16.300  1.00 17.85           C  
ATOM   4356  CG2 ILE C 535      28.005  33.189  14.991  1.00  3.38           C  
ATOM   4357  CD1 ILE C 535      25.332  31.850  15.316  1.00 18.21           C  
ATOM   4358  H   ILE C 535      28.080  29.341  16.330  1.00  0.00           H  
ATOM   4359  N   LEU C 536      30.536  30.439  14.441  1.00 19.13           N  
ATOM   4360  CA  LEU C 536      31.827  30.534  13.762  1.00 20.48           C  
ATOM   4361  C   LEU C 536      31.890  29.639  12.525  1.00 16.45           C  
ATOM   4362  O   LEU C 536      32.368  30.056  11.471  1.00 26.78           O  
ATOM   4363  CB  LEU C 536      32.964  30.163  14.720  1.00 18.45           C  
ATOM   4364  CG  LEU C 536      33.359  31.199  15.778  1.00 16.53           C  
ATOM   4365  CD1 LEU C 536      34.307  30.558  16.772  1.00 21.79           C  
ATOM   4366  CD2 LEU C 536      34.008  32.408  15.130  1.00 12.55           C  
ATOM   4367  H   LEU C 536      30.488  30.087  15.357  1.00  0.00           H  
ATOM   4368  N   GLY C 537      31.396  28.414  12.657  1.00 16.32           N  
ATOM   4369  CA  GLY C 537      31.273  27.531  11.508  1.00 18.85           C  
ATOM   4370  C   GLY C 537      30.339  28.060  10.431  1.00 20.08           C  
ATOM   4371  O   GLY C 537      30.622  27.925   9.239  1.00 19.31           O  
ATOM   4372  H   GLY C 537      31.184  28.078  13.555  1.00  0.00           H  
ATOM   4373  N   LEU C 538      29.232  28.674  10.852  1.00 19.33           N  
ATOM   4374  CA  LEU C 538      28.303  29.331   9.935  1.00 17.47           C  
ATOM   4375  C   LEU C 538      28.995  30.439   9.145  1.00 17.80           C  
ATOM   4376  O   LEU C 538      28.898  30.479   7.926  1.00 22.75           O  
ATOM   4377  CB  LEU C 538      27.106  29.918  10.694  1.00 13.94           C  
ATOM   4378  CG  LEU C 538      26.034  28.973  11.250  1.00 15.55           C  
ATOM   4379  CD1 LEU C 538      24.869  29.797  11.773  1.00  7.83           C  
ATOM   4380  CD2 LEU C 538      25.558  28.007  10.178  1.00 13.19           C  
ATOM   4381  H   LEU C 538      29.024  28.617  11.806  1.00  0.00           H  
ATOM   4382  N   ASN C 539      29.777  31.267   9.832  1.00 19.64           N  
ATOM   4383  CA  ASN C 539      30.598  32.291   9.176  1.00 16.76           C  
ATOM   4384  C   ASN C 539      31.530  31.721   8.106  1.00 17.82           C  
ATOM   4385  O   ASN C 539      31.791  32.367   7.094  1.00 20.99           O  
ATOM   4386  CB  ASN C 539      31.436  33.046  10.209  1.00 16.98           C  
ATOM   4387  CG  ASN C 539      30.712  34.242  10.787  1.00 15.24           C  
ATOM   4388  OD1 ASN C 539      30.770  35.337  10.238  1.00 22.30           O  
ATOM   4389  ND2 ASN C 539      30.046  34.044  11.913  1.00 14.23           N  
ATOM   4390  H   ASN C 539      29.771  31.200  10.811  1.00  0.00           H  
ATOM   4391 HD21 ASN C 539      29.520  34.798  12.228  1.00  0.00           H  
ATOM   4392 HD22 ASN C 539      30.087  33.182  12.351  1.00  0.00           H  
ATOM   4393  N   LYS C 540      32.033  30.514   8.333  1.00 17.37           N  
ATOM   4394  CA  LYS C 540      32.899  29.864   7.360  1.00 22.43           C  
ATOM   4395  C   LYS C 540      32.132  29.349   6.142  1.00 25.83           C  
ATOM   4396  O   LYS C 540      32.548  29.567   5.007  1.00 25.60           O  
ATOM   4397  CB  LYS C 540      33.658  28.708   8.010  1.00 25.71           C  
ATOM   4398  CG  LYS C 540      34.670  28.047   7.087  1.00 26.32           C  
ATOM   4399  CD  LYS C 540      35.519  27.036   7.828  1.00 30.94           C  
ATOM   4400  CE  LYS C 540      36.481  26.338   6.891  1.00 34.27           C  
ATOM   4401  NZ  LYS C 540      37.235  25.276   7.600  1.00 51.41           N  
ATOM   4402  H   LYS C 540      31.890  30.101   9.211  1.00  0.00           H  
ATOM   4403  HZ1 LYS C 540      37.770  25.700   8.386  1.00  0.00           H  
ATOM   4404  HZ2 LYS C 540      36.574  24.567   7.975  1.00  0.00           H  
ATOM   4405  HZ3 LYS C 540      37.896  24.821   6.939  1.00  0.00           H  
ATOM   4406  N   ILE C 541      31.014  28.667   6.374  1.00 28.61           N  
ATOM   4407  CA  ILE C 541      30.254  28.078   5.273  1.00 24.01           C  
ATOM   4408  C   ILE C 541      29.481  29.087   4.417  1.00 25.21           C  
ATOM   4409  O   ILE C 541      29.416  28.932   3.200  1.00 26.69           O  
ATOM   4410  CB  ILE C 541      29.291  26.968   5.758  1.00 21.20           C  
ATOM   4411  CG1 ILE C 541      28.258  27.532   6.735  1.00 22.54           C  
ATOM   4412  CG2 ILE C 541      30.086  25.838   6.379  1.00 16.15           C  
ATOM   4413  CD1 ILE C 541      27.286  26.492   7.258  1.00 18.46           C  
ATOM   4414  H   ILE C 541      30.751  28.519   7.308  1.00  0.00           H  
ATOM   4415  N   VAL C 542      29.018  30.183   5.019  1.00 23.07           N  
ATOM   4416  CA  VAL C 542      28.437  31.273   4.232  1.00 21.60           C  
ATOM   4417  C   VAL C 542      29.480  31.905   3.312  1.00 29.57           C  
ATOM   4418  O   VAL C 542      29.150  32.704   2.441  1.00 34.11           O  
ATOM   4419  CB  VAL C 542      27.805  32.387   5.117  1.00 13.18           C  
ATOM   4420  CG1 VAL C 542      26.838  31.783   6.119  1.00 15.80           C  
ATOM   4421  CG2 VAL C 542      28.871  33.192   5.814  1.00 17.12           C  
ATOM   4422  H   VAL C 542      29.036  30.230   5.997  1.00  0.00           H  
ATOM   4423  N   ARG C 543      30.735  31.499   3.484  1.00 34.10           N  
ATOM   4424  CA  ARG C 543      31.818  31.902   2.592  1.00 41.56           C  
ATOM   4425  C   ARG C 543      31.885  31.019   1.340  1.00 44.48           C  
ATOM   4426  O   ARG C 543      32.911  30.963   0.664  1.00 46.28           O  
ATOM   4427  CB  ARG C 543      33.150  31.845   3.340  1.00 41.61           C  
ATOM   4428  CG  ARG C 543      33.967  33.117   3.276  1.00 53.16           C  
ATOM   4429  CD  ARG C 543      35.048  33.121   4.346  1.00 54.82           C  
ATOM   4430  NE  ARG C 543      34.533  33.563   5.640  1.00 58.82           N  
ATOM   4431  CZ  ARG C 543      35.146  33.361   6.803  1.00 62.06           C  
ATOM   4432  NH1 ARG C 543      36.252  32.629   6.861  1.00 61.83           N  
ATOM   4433  NH2 ARG C 543      34.640  33.872   7.916  1.00 56.54           N  
ATOM   4434  H   ARG C 543      30.968  30.962   4.265  1.00  0.00           H  
ATOM   4435  HE  ARG C 543      33.673  34.033   5.662  1.00  0.00           H  
ATOM   4436 HH11 ARG C 543      36.639  32.226   6.032  1.00  0.00           H  
ATOM   4437 HH12 ARG C 543      36.706  32.488   7.740  1.00  0.00           H  
ATOM   4438 HH21 ARG C 543      33.800  34.414   7.899  1.00  0.00           H  
ATOM   4439 HH22 ARG C 543      35.132  33.734   8.772  1.00  0.00           H  
ATOM   4440  N   MET C 544      30.814  30.273   1.083  1.00 48.16           N  
ATOM   4441  CA  MET C 544      30.649  29.560  -0.183  1.00 48.68           C  
ATOM   4442  C   MET C 544      29.225  29.735  -0.733  1.00 48.13           C  
ATOM   4443  O   MET C 544      28.731  28.906  -1.501  1.00 47.51           O  
ATOM   4444  CB  MET C 544      30.989  28.068  -0.004  1.00 52.04           C  
ATOM   4445  CG  MET C 544      29.957  27.251   0.766  1.00 53.53           C  
ATOM   4446  SD  MET C 544      30.544  25.638   1.344  1.00 55.87           S  
ATOM   4447  CE  MET C 544      30.365  24.646  -0.128  1.00 58.57           C  
ATOM   4448  H   MET C 544      30.141  30.159   1.781  1.00  0.00           H  
ATOM   4449  N   TYR C 545      28.574  30.821  -0.327  1.00 46.86           N  
ATOM   4450  CA  TYR C 545      27.210  31.124  -0.750  1.00 49.45           C  
ATOM   4451  C   TYR C 545      27.051  32.612  -1.079  1.00 52.12           C  
ATOM   4452  O   TYR C 545      25.911  33.032  -1.375  0.00 51.49           O  
ATOM   4453  CB  TYR C 545      26.211  30.732   0.348  1.00 47.02           C  
ATOM   4454  CG  TYR C 545      26.038  29.240   0.529  1.00 39.47           C  
ATOM   4455  CD1 TYR C 545      26.881  28.520   1.369  1.00 34.91           C  
ATOM   4456  CD2 TYR C 545      25.058  28.542  -0.176  1.00 41.15           C  
ATOM   4457  CE1 TYR C 545      26.763  27.140   1.499  1.00 35.98           C  
ATOM   4458  CE2 TYR C 545      24.930  27.159  -0.051  1.00 40.72           C  
ATOM   4459  CZ  TYR C 545      25.789  26.466   0.786  1.00 35.30           C  
ATOM   4460  OH  TYR C 545      25.682  25.099   0.905  1.00 32.41           O  
ATOM   4461  OXT TYR C 545      28.068  33.339  -1.057  0.00 51.17           O  
ATOM   4462  H   TYR C 545      29.015  31.534   0.176  1.00  0.00           H  
ATOM   4463  HH  TYR C 545      26.423  24.788   1.449  1.00  0.00           H  
TER    4464      TYR C 545                                                      
ATOM   4465  N   PRO D 401      51.122  40.354  27.185  0.00 42.33           N  
ATOM   4466  CA  PRO D 401      50.431  39.344  28.022  0.00 42.25           C  
ATOM   4467  C   PRO D 401      50.674  39.576  29.513  0.00 41.99           C  
ATOM   4468  O   PRO D 401      51.312  40.558  29.893  0.00 42.13           O  
ATOM   4469  CB  PRO D 401      50.940  37.972  27.605  0.00 42.74           C  
ATOM   4470  CG  PRO D 401      51.518  38.236  26.222  0.00 42.24           C  
ATOM   4471  CD  PRO D 401      51.970  39.701  26.172  0.00 42.55           C  
ATOM   4472  H2  PRO D 401      50.428  40.963  26.721  1.00  0.00           H  
ATOM   4473  H3  PRO D 401      51.754  40.932  27.796  1.00  0.00           H  
ATOM   4474  N   ILE D 402      50.077  38.734  30.351  0.00 41.57           N  
ATOM   4475  CA  ILE D 402      50.365  38.747  31.783  0.00 41.35           C  
ATOM   4476  C   ILE D 402      51.193  37.518  32.162  0.00 41.02           C  
ATOM   4477  O   ILE D 402      50.682  36.400  32.212  0.00 41.04           O  
ATOM   4478  CB  ILE D 402      49.065  38.774  32.623  0.00 41.16           C  
ATOM   4479  CG1 ILE D 402      48.224  39.995  32.240  0.00 42.17           C  
ATOM   4480  CG2 ILE D 402      49.400  38.822  34.110  0.00 41.24           C  
ATOM   4481  CD1 ILE D 402      46.882  40.059  32.931  0.00 39.49           C  
ATOM   4482  H   ILE D 402      49.407  38.092  30.029  1.00  0.00           H  
ATOM   4483  N   VAL D 403      52.491  37.726  32.349  0.00 40.73           N  
ATOM   4484  CA  VAL D 403      53.424  36.619  32.546  0.00 40.43           C  
ATOM   4485  C   VAL D 403      54.071  36.632  33.929  0.00 40.49           C  
ATOM   4486  O   VAL D 403      53.993  37.622  34.655  0.00 41.23           O  
ATOM   4487  CB  VAL D 403      54.552  36.633  31.479  0.00 39.91           C  
ATOM   4488  CG1 VAL D 403      53.956  36.644  30.079  0.00 38.97           C  
ATOM   4489  CG2 VAL D 403      55.462  37.836  31.686  0.00 40.20           C  
ATOM   4490  H   VAL D 403      52.786  38.650  32.481  1.00  0.00           H  
ATOM   4491  N   GLN D 404      54.694  35.517  34.294  0.00 40.41           N  
ATOM   4492  CA  GLN D 404      55.592  35.486  35.443  0.00 40.56           C  
ATOM   4493  C   GLN D 404      56.892  36.208  35.099  0.00 40.45           C  
ATOM   4494  O   GLN D 404      57.557  35.866  34.119  0.00 41.11           O  
ATOM   4495  CB  GLN D 404      55.908  34.043  35.835  0.00 40.64           C  
ATOM   4496  CG  GLN D 404      54.885  33.396  36.748  0.00 39.71           C  
ATOM   4497  CD  GLN D 404      55.331  32.030  37.232  0.00 38.85           C  
ATOM   4498  OE1 GLN D 404      56.502  31.812  37.525  0.00 38.27           O  
ATOM   4499  NE2 GLN D 404      54.407  31.090  37.268  0.00 39.44           N  
ATOM   4500  H   GLN D 404      54.543  34.704  33.784  1.00  0.00           H  
ATOM   4501 HE21 GLN D 404      54.742  30.238  37.582  1.00  0.00           H  
ATOM   4502 HE22 GLN D 404      53.489  31.315  37.025  1.00  0.00           H  
ATOM   4503  N   ASN D 405      57.206  37.259  35.848  0.00 40.53           N  
ATOM   4504  CA  ASN D 405      58.470  37.964  35.659  0.00 40.80           C  
ATOM   4505  C   ASN D 405      59.644  37.201  36.281  0.00 40.56           C  
ATOM   4506  O   ASN D 405      59.471  36.104  36.811  0.00 40.67           O  
ATOM   4507  CB  ASN D 405      58.386  39.386  36.238  0.00 41.27           C  
ATOM   4508  CG  ASN D 405      58.117  39.406  37.737  0.00 40.40           C  
ATOM   4509  OD1 ASN D 405      58.068  38.369  38.393  0.00 38.71           O  
ATOM   4510  ND2 ASN D 405      57.996  40.599  38.292  0.00 39.29           N  
ATOM   4511  H   ASN D 405      56.552  37.525  36.531  1.00  0.00           H  
ATOM   4512 HD21 ASN D 405      57.824  40.580  39.252  1.00  0.00           H  
ATOM   4513 HD22 ASN D 405      58.070  41.409  37.750  1.00  0.00           H  
ATOM   4514  N   LEU D 406      60.814  37.832  36.306  0.00 40.08           N  
ATOM   4515  CA  LEU D 406      62.008  37.227  36.898  0.00 39.63           C  
ATOM   4516  C   LEU D 406      61.853  36.913  38.391  0.00 39.85           C  
ATOM   4517  O   LEU D 406      62.678  36.212  38.974  0.00 39.49           O  
ATOM   4518  CB  LEU D 406      63.216  38.145  36.692  0.00 38.36           C  
ATOM   4519  CG  LEU D 406      63.558  38.537  35.251  0.00 37.61           C  
ATOM   4520  CD1 LEU D 406      64.627  39.616  35.259  0.00 37.01           C  
ATOM   4521  CD2 LEU D 406      64.029  37.317  34.473  0.00 35.06           C  
ATOM   4522  H   LEU D 406      60.887  38.674  35.818  1.00  0.00           H  
ATOM   4523  N   GLN D 407      60.793  37.436  39.002  0.00 40.23           N  
ATOM   4524  CA  GLN D 407      60.544  37.236  40.427  0.00 40.80           C  
ATOM   4525  C   GLN D 407      59.295  36.389  40.699  0.00 41.35           C  
ATOM   4526  O   GLN D 407      58.813  36.325  41.831  0.00 41.14           O  
ATOM   4527  CB  GLN D 407      60.418  38.593  41.123  0.00 40.02           C  
ATOM   4528  CG  GLN D 407      60.972  38.623  42.540  0.00 41.05           C  
ATOM   4529  CD  GLN D 407      61.243  40.032  43.030  0.00 40.99           C  
ATOM   4530  OE1 GLN D 407      60.773  41.005  42.447  0.00 39.38           O  
ATOM   4531  NE2 GLN D 407      62.046  40.150  44.073  0.00 38.57           N  
ATOM   4532  H   GLN D 407      60.140  37.933  38.481  1.00  0.00           H  
ATOM   4533 HE21 GLN D 407      62.171  41.067  44.384  1.00  0.00           H  
ATOM   4534 HE22 GLN D 407      62.444  39.352  44.466  1.00  0.00           H  
ATOM   4535  N   GLY D 408      58.724  35.819  39.642  0.00 42.54           N  
ATOM   4536  CA  GLY D 408      57.660  34.841  39.804  0.00 43.68           C  
ATOM   4537  C   GLY D 408      56.235  35.368  39.861  0.00 44.68           C  
ATOM   4538  O   GLY D 408      55.285  34.597  39.732  0.00 44.47           O  
ATOM   4539  H   GLY D 408      59.034  36.042  38.741  1.00  0.00           H  
ATOM   4540  N   GLN D 409      56.069  36.673  40.054  0.00 45.80           N  
ATOM   4541  CA  GLN D 409      54.730  37.244  40.189  0.00 47.04           C  
ATOM   4542  C   GLN D 409      54.103  37.632  38.846  0.00 47.03           C  
ATOM   4543  O   GLN D 409      54.807  37.951  37.885  0.00 46.37           O  
ATOM   4544  CB  GLN D 409      54.755  38.446  41.147  0.00 48.19           C  
ATOM   4545  CG  GLN D 409      54.821  39.816  40.486  0.00 49.75           C  
ATOM   4546  CD  GLN D 409      53.824  40.794  41.081  0.00 50.20           C  
ATOM   4547  OE1 GLN D 409      53.907  41.145  42.253  0.00 51.59           O  
ATOM   4548  NE2 GLN D 409      52.868  41.226  40.278  0.00 51.95           N  
ATOM   4549  H   GLN D 409      56.869  37.234  40.062  1.00  0.00           H  
ATOM   4550 HE21 GLN D 409      52.253  41.839  40.721  1.00  0.00           H  
ATOM   4551 HE22 GLN D 409      52.796  40.942  39.347  1.00  0.00           H  
ATOM   4552  N   MET D 410      52.774  37.608  38.796  0.00 47.70           N  
ATOM   4553  CA  MET D 410      52.027  37.920  37.577  0.00 48.60           C  
ATOM   4554  C   MET D 410      52.117  39.401  37.207  0.00 49.11           C  
ATOM   4555  O   MET D 410      51.661  40.268  37.954  0.00 49.35           O  
ATOM   4556  CB  MET D 410      50.558  37.522  37.745  0.00 48.60           C  
ATOM   4557  CG  MET D 410      50.333  36.031  37.933  0.00 47.48           C  
ATOM   4558  SD  MET D 410      50.730  35.079  36.456  0.00 47.40           S  
ATOM   4559  CE  MET D 410      49.158  35.126  35.598  0.00 48.43           C  
ATOM   4560  H   MET D 410      52.296  37.366  39.612  1.00  0.00           H  
ATOM   4561  N   VAL D 411      52.732  39.686  36.064  0.00 49.56           N  
ATOM   4562  CA  VAL D 411      52.982  41.062  35.643  0.00 50.04           C  
ATOM   4563  C   VAL D 411      52.545  41.325  34.203  0.00 51.09           C  
ATOM   4564  O   VAL D 411      52.447  40.403  33.390  0.00 51.94           O  
ATOM   4565  CB  VAL D 411      54.484  41.426  35.766  0.00 49.45           C  
ATOM   4566  CG1 VAL D 411      54.984  41.111  37.158  0.00 48.75           C  
ATOM   4567  CG2 VAL D 411      55.304  40.672  34.725  0.00 46.98           C  
ATOM   4568  H   VAL D 411      53.019  38.942  35.501  1.00  0.00           H  
ATOM   4569  N   HIS D 412      52.344  42.596  33.873  1.00 50.90           N  
ATOM   4570  CA  HIS D 412      52.126  42.982  32.483  1.00 52.80           C  
ATOM   4571  C   HIS D 412      53.422  43.018  31.688  1.00 54.04           C  
ATOM   4572  O   HIS D 412      54.118  44.036  31.657  1.00 54.06           O  
ATOM   4573  CB  HIS D 412      51.452  44.352  32.374  1.00 51.21           C  
ATOM   4574  CG  HIS D 412      51.406  44.885  30.973  1.00 51.41           C  
ATOM   4575  ND1 HIS D 412      52.241  45.890  30.533  1.00 50.67           N  
ATOM   4576  CD2 HIS D 412      50.699  44.485  29.888  1.00 50.93           C  
ATOM   4577  CE1 HIS D 412      52.054  46.085  29.240  1.00 48.67           C  
ATOM   4578  NE2 HIS D 412      51.122  45.245  28.825  1.00 48.94           N  
ATOM   4579  H   HIS D 412      52.356  43.253  34.596  1.00  0.00           H  
ATOM   4580  HD1 HIS D 412      52.913  46.363  31.072  1.00  0.00           H  
ATOM   4581  HE2 HIS D 412      50.717  45.283  27.936  1.00  0.00           H  
ATOM   4582  N   GLN D 413      53.681  41.943  30.958  1.00 55.74           N  
ATOM   4583  CA  GLN D 413      54.647  42.002  29.875  1.00 56.77           C  
ATOM   4584  C   GLN D 413      53.962  42.620  28.664  1.00 58.98           C  
ATOM   4585  O   GLN D 413      52.848  42.222  28.293  1.00 62.93           O  
ATOM   4586  CB  GLN D 413      55.156  40.606  29.523  1.00 55.93           C  
ATOM   4587  CG  GLN D 413      56.335  40.611  28.569  1.00 50.99           C  
ATOM   4588  CD  GLN D 413      57.256  39.437  28.791  1.00 58.18           C  
ATOM   4589  OE1 GLN D 413      56.967  38.318  28.377  1.00 62.31           O  
ATOM   4590  NE2 GLN D 413      58.361  39.677  29.476  1.00 61.71           N  
ATOM   4591  H   GLN D 413      53.196  41.114  31.163  1.00  0.00           H  
ATOM   4592 HE21 GLN D 413      58.902  38.875  29.600  1.00  0.00           H  
ATOM   4593 HE22 GLN D 413      58.569  40.572  29.800  1.00  0.00           H  
ATOM   4594  N   ALA D 414      54.562  43.682  28.138  1.00 57.76           N  
ATOM   4595  CA  ALA D 414      54.110  44.271  26.885  1.00 49.84           C  
ATOM   4596  C   ALA D 414      54.102  43.220  25.774  1.00 49.00           C  
ATOM   4597  O   ALA D 414      54.341  42.032  26.011  1.00 48.59           O  
ATOM   4598  CB  ALA D 414      55.014  45.441  26.500  1.00 45.21           C  
ATOM   4599  H   ALA D 414      55.357  44.023  28.599  1.00  0.00           H  
ATOM   4600  N   ILE D 415      53.724  43.639  24.579  1.00 46.11           N  
ATOM   4601  CA  ILE D 415      53.792  42.743  23.426  1.00 38.98           C  
ATOM   4602  C   ILE D 415      55.091  42.919  22.664  1.00 31.60           C  
ATOM   4603  O   ILE D 415      55.645  44.021  22.590  1.00 28.64           O  
ATOM   4604  CB  ILE D 415      52.615  42.917  22.419  1.00 44.89           C  
ATOM   4605  CG1 ILE D 415      52.099  44.355  22.422  1.00 44.99           C  
ATOM   4606  CG2 ILE D 415      51.511  41.908  22.720  1.00 39.13           C  
ATOM   4607  CD1 ILE D 415      51.043  44.602  21.378  1.00 53.06           C  
ATOM   4608  H   ILE D 415      53.510  44.583  24.450  1.00  0.00           H  
ATOM   4609  N   SER D 416      55.619  41.800  22.186  1.00 29.34           N  
ATOM   4610  CA  SER D 416      56.870  41.798  21.440  1.00 30.47           C  
ATOM   4611  C   SER D 416      56.714  42.526  20.105  1.00 34.90           C  
ATOM   4612  O   SER D 416      55.773  42.267  19.347  1.00 41.09           O  
ATOM   4613  CB  SER D 416      57.343  40.358  21.220  1.00 28.39           C  
ATOM   4614  OG  SER D 416      57.437  40.037  19.845  1.00 42.20           O  
ATOM   4615  H   SER D 416      55.140  40.965  22.352  1.00  0.00           H  
ATOM   4616  HG  SER D 416      57.039  39.155  19.723  1.00  0.00           H  
ATOM   4617  N   PRO D 417      57.611  43.485  19.825  1.00 36.64           N  
ATOM   4618  CA  PRO D 417      57.581  44.260  18.580  1.00 34.14           C  
ATOM   4619  C   PRO D 417      57.668  43.388  17.331  1.00 36.12           C  
ATOM   4620  O   PRO D 417      57.033  43.676  16.318  1.00 33.47           O  
ATOM   4621  CB  PRO D 417      58.793  45.177  18.713  1.00 35.84           C  
ATOM   4622  CG  PRO D 417      58.898  45.405  20.174  1.00 36.22           C  
ATOM   4623  CD  PRO D 417      58.545  44.074  20.800  1.00 37.47           C  
ATOM   4624  N   ARG D 418      58.405  42.287  17.424  1.00 37.67           N  
ATOM   4625  CA  ARG D 418      58.521  41.363  16.297  1.00 43.77           C  
ATOM   4626  C   ARG D 418      57.223  40.596  16.031  1.00 42.10           C  
ATOM   4627  O   ARG D 418      56.851  40.377  14.881  1.00 45.67           O  
ATOM   4628  CB  ARG D 418      59.689  40.387  16.507  1.00 45.94           C  
ATOM   4629  CG  ARG D 418      59.792  39.787  17.901  0.00 46.35           C  
ATOM   4630  CD  ARG D 418      61.239  39.495  18.272  0.00 48.71           C  
ATOM   4631  NE  ARG D 418      62.023  40.719  18.429  0.00 49.59           N  
ATOM   4632  CZ  ARG D 418      63.325  40.818  18.174  0.00 49.39           C  
ATOM   4633  NH1 ARG D 418      64.009  39.765  17.745  0.00 49.51           N  
ATOM   4634  NH2 ARG D 418      63.947  41.976  18.347  0.00 48.45           N  
ATOM   4635  H   ARG D 418      58.867  42.110  18.267  1.00  0.00           H  
ATOM   4636  HE  ARG D 418      61.561  41.523  18.747  1.00  0.00           H  
ATOM   4637 HH11 ARG D 418      63.554  38.886  17.605  1.00  0.00           H  
ATOM   4638 HH12 ARG D 418      64.988  39.855  17.557  1.00  0.00           H  
ATOM   4639 HH21 ARG D 418      63.438  42.773  18.673  1.00  0.00           H  
ATOM   4640 HH22 ARG D 418      64.926  42.052  18.157  1.00  0.00           H  
ATOM   4641  N   THR D 419      56.492  40.277  17.094  1.00 38.70           N  
ATOM   4642  CA  THR D 419      55.166  39.672  16.970  1.00 39.07           C  
ATOM   4643  C   THR D 419      54.167  40.667  16.374  1.00 35.46           C  
ATOM   4644  O   THR D 419      53.320  40.301  15.560  1.00 31.98           O  
ATOM   4645  CB  THR D 419      54.635  39.192  18.347  1.00 43.67           C  
ATOM   4646  OG1 THR D 419      55.539  38.222  18.899  1.00 45.75           O  
ATOM   4647  CG2 THR D 419      53.254  38.565  18.206  1.00 43.63           C  
ATOM   4648  H   THR D 419      56.877  40.424  17.986  1.00  0.00           H  
ATOM   4649  HG1 THR D 419      55.349  37.364  18.497  1.00  0.00           H  
ATOM   4650  N   LEU D 420      54.290  41.932  16.764  1.00 34.97           N  
ATOM   4651  CA  LEU D 420      53.503  43.001  16.158  1.00 33.22           C  
ATOM   4652  C   LEU D 420      53.828  43.133  14.670  1.00 37.18           C  
ATOM   4653  O   LEU D 420      52.932  43.120  13.827  1.00 37.04           O  
ATOM   4654  CB  LEU D 420      53.789  44.327  16.863  1.00 34.91           C  
ATOM   4655  CG  LEU D 420      52.907  44.698  18.052  1.00 36.03           C  
ATOM   4656  CD1 LEU D 420      53.496  45.910  18.757  1.00 33.12           C  
ATOM   4657  CD2 LEU D 420      51.492  44.990  17.572  1.00 38.34           C  
ATOM   4658  H   LEU D 420      54.874  42.130  17.530  1.00  0.00           H  
ATOM   4659  N   ASN D 421      55.120  43.146  14.356  1.00 39.42           N  
ATOM   4660  CA  ASN D 421      55.598  43.238  12.978  1.00 41.26           C  
ATOM   4661  C   ASN D 421      55.133  42.040  12.149  1.00 43.56           C  
ATOM   4662  O   ASN D 421      54.744  42.187  10.987  1.00 43.63           O  
ATOM   4663  CB  ASN D 421      57.130  43.313  12.963  1.00 43.89           C  
ATOM   4664  CG  ASN D 421      57.685  43.647  11.593  0.00 43.90           C  
ATOM   4665  OD1 ASN D 421      57.962  42.762  10.789  0.00 44.10           O  
ATOM   4666  ND2 ASN D 421      57.860  44.928  11.324  0.00 44.13           N  
ATOM   4667  H   ASN D 421      55.762  43.118  15.088  1.00  0.00           H  
ATOM   4668 HD21 ASN D 421      58.215  45.073  10.429  1.00  0.00           H  
ATOM   4669 HD22 ASN D 421      57.650  45.609  11.988  1.00  0.00           H  
ATOM   4670  N   ALA D 422      55.116  40.869  12.780  1.00 38.93           N  
ATOM   4671  CA  ALA D 422      54.620  39.648  12.151  1.00 37.89           C  
ATOM   4672  C   ALA D 422      53.142  39.775  11.777  1.00 36.09           C  
ATOM   4673  O   ALA D 422      52.742  39.436  10.663  1.00 39.58           O  
ATOM   4674  CB  ALA D 422      54.826  38.459  13.086  1.00 36.19           C  
ATOM   4675  H   ALA D 422      55.489  40.833  13.682  1.00  0.00           H  
ATOM   4676  N   TRP D 423      52.346  40.307  12.700  1.00 31.83           N  
ATOM   4677  CA  TRP D 423      50.939  40.599  12.439  1.00 27.74           C  
ATOM   4678  C   TRP D 423      50.768  41.583  11.276  1.00 27.72           C  
ATOM   4679  O   TRP D 423      50.070  41.292  10.301  1.00 27.04           O  
ATOM   4680  CB  TRP D 423      50.283  41.157  13.706  1.00 24.28           C  
ATOM   4681  CG  TRP D 423      48.881  41.655  13.508  1.00 23.51           C  
ATOM   4682  CD1 TRP D 423      48.414  42.914  13.764  1.00 24.32           C  
ATOM   4683  CD2 TRP D 423      47.762  40.903  13.018  1.00 18.81           C  
ATOM   4684  NE1 TRP D 423      47.074  42.995  13.462  1.00 26.55           N  
ATOM   4685  CE2 TRP D 423      46.647  41.775  13.002  1.00 21.38           C  
ATOM   4686  CE3 TRP D 423      47.592  39.579  12.591  1.00 16.91           C  
ATOM   4687  CZ2 TRP D 423      45.379  41.365  12.575  1.00 21.17           C  
ATOM   4688  CZ3 TRP D 423      46.330  39.171  12.166  1.00 20.42           C  
ATOM   4689  CH2 TRP D 423      45.240  40.064  12.161  1.00 18.91           C  
ATOM   4690  H   TRP D 423      52.722  40.480  13.593  1.00  0.00           H  
ATOM   4691  HE1 TRP D 423      46.539  43.808  13.597  1.00  0.00           H  
ATOM   4692  N   VAL D 424      51.458  42.718  11.359  1.00 30.93           N  
ATOM   4693  CA  VAL D 424      51.449  43.720  10.289  1.00 33.95           C  
ATOM   4694  C   VAL D 424      51.781  43.096   8.930  1.00 33.97           C  
ATOM   4695  O   VAL D 424      51.062  43.299   7.954  1.00 37.03           O  
ATOM   4696  CB  VAL D 424      52.459  44.856  10.581  1.00 34.94           C  
ATOM   4697  CG1 VAL D 424      52.453  45.875   9.453  1.00 39.59           C  
ATOM   4698  CG2 VAL D 424      52.111  45.534  11.890  1.00 37.31           C  
ATOM   4699  H   VAL D 424      51.971  42.875  12.180  1.00  0.00           H  
ATOM   4700  N   LYS D 425      52.792  42.235   8.915  1.00 36.59           N  
ATOM   4701  CA  LYS D 425      53.202  41.522   7.710  1.00 38.42           C  
ATOM   4702  C   LYS D 425      52.078  40.643   7.154  1.00 38.99           C  
ATOM   4703  O   LYS D 425      51.765  40.702   5.963  1.00 44.16           O  
ATOM   4704  CB  LYS D 425      54.428  40.655   8.022  1.00 44.03           C  
ATOM   4705  CG  LYS D 425      55.193  40.183   6.799  1.00 48.56           C  
ATOM   4706  CD  LYS D 425      56.389  41.073   6.523  1.00 57.06           C  
ATOM   4707  CE  LYS D 425      56.877  40.898   5.094  1.00 67.97           C  
ATOM   4708  NZ  LYS D 425      58.361  40.767   5.010  1.00 66.48           N  
ATOM   4709  H   LYS D 425      53.289  42.090   9.746  1.00  0.00           H  
ATOM   4710  HZ1 LYS D 425      58.828  41.594   5.429  1.00  0.00           H  
ATOM   4711  HZ2 LYS D 425      58.651  39.903   5.511  1.00  0.00           H  
ATOM   4712  HZ3 LYS D 425      58.620  40.682   4.005  1.00  0.00           H  
ATOM   4713  N   VAL D 426      51.460  39.851   8.027  1.00 35.96           N  
ATOM   4714  CA  VAL D 426      50.361  38.966   7.634  1.00 37.65           C  
ATOM   4715  C   VAL D 426      49.225  39.736   6.952  1.00 35.80           C  
ATOM   4716  O   VAL D 426      48.794  39.384   5.853  1.00 35.41           O  
ATOM   4717  CB  VAL D 426      49.794  38.198   8.863  1.00 37.88           C  
ATOM   4718  CG1 VAL D 426      48.558  37.401   8.474  1.00 27.56           C  
ATOM   4719  CG2 VAL D 426      50.854  37.265   9.424  1.00 37.71           C  
ATOM   4720  H   VAL D 426      51.772  39.863   8.960  1.00  0.00           H  
ATOM   4721  N   VAL D 427      48.830  40.853   7.551  1.00 38.53           N  
ATOM   4722  CA  VAL D 427      47.766  41.688   6.997  1.00 40.65           C  
ATOM   4723  C   VAL D 427      48.217  42.459   5.748  1.00 45.47           C  
ATOM   4724  O   VAL D 427      47.408  42.753   4.864  1.00 49.54           O  
ATOM   4725  CB  VAL D 427      47.242  42.685   8.058  1.00 33.72           C  
ATOM   4726  CG1 VAL D 427      46.122  43.535   7.484  1.00 33.38           C  
ATOM   4727  CG2 VAL D 427      46.744  41.926   9.274  1.00 33.05           C  
ATOM   4728  H   VAL D 427      49.264  41.092   8.403  1.00  0.00           H  
ATOM   4729  N   GLU D 428      49.501  42.800   5.689  1.00 52.60           N  
ATOM   4730  CA  GLU D 428      50.054  43.535   4.553  1.00 54.47           C  
ATOM   4731  C   GLU D 428      50.108  42.669   3.293  1.00 56.16           C  
ATOM   4732  O   GLU D 428      49.754  43.124   2.205  1.00 57.21           O  
ATOM   4733  CB  GLU D 428      51.457  44.048   4.891  1.00 54.26           C  
ATOM   4734  CG  GLU D 428      52.139  44.820   3.772  0.00 52.31           C  
ATOM   4735  CD  GLU D 428      53.647  44.863   3.930  0.00 51.41           C  
ATOM   4736  OE1 GLU D 428      54.133  45.558   4.848  0.00 50.14           O  
ATOM   4737  OE2 GLU D 428      54.347  44.198   3.138  0.00 48.72           O  
ATOM   4738  H   GLU D 428      50.081  42.563   6.444  1.00  0.00           H  
ATOM   4739  N   GLU D 429      50.511  41.413   3.452  1.00 54.53           N  
ATOM   4740  CA  GLU D 429      50.633  40.506   2.316  1.00 58.91           C  
ATOM   4741  C   GLU D 429      49.331  39.752   2.007  1.00 59.87           C  
ATOM   4742  O   GLU D 429      48.830  39.796   0.883  1.00 60.39           O  
ATOM   4743  CB  GLU D 429      51.770  39.507   2.554  1.00 57.51           C  
ATOM   4744  CG  GLU D 429      52.282  38.854   1.273  0.00 61.99           C  
ATOM   4745  CD  GLU D 429      53.446  37.908   1.509  0.00 63.33           C  
ATOM   4746  OE1 GLU D 429      54.394  38.286   2.231  0.00 63.14           O  
ATOM   4747  OE2 GLU D 429      53.426  36.795   0.943  0.00 63.23           O  
ATOM   4748  H   GLU D 429      50.776  41.124   4.349  1.00  0.00           H  
ATOM   4749  N   LYS D 430      48.775  39.089   3.017  1.00 59.93           N  
ATOM   4750  CA  LYS D 430      47.580  38.257   2.846  1.00 60.34           C  
ATOM   4751  C   LYS D 430      46.281  39.072   2.750  1.00 63.23           C  
ATOM   4752  O   LYS D 430      45.328  38.658   2.084  1.00 68.48           O  
ATOM   4753  CB  LYS D 430      47.465  37.266   4.009  1.00 55.92           C  
ATOM   4754  CG  LYS D 430      47.982  35.879   3.704  0.00 57.90           C  
ATOM   4755  CD  LYS D 430      46.968  35.083   2.902  0.00 57.50           C  
ATOM   4756  CE  LYS D 430      47.527  34.675   1.558  0.00 56.03           C  
ATOM   4757  NZ  LYS D 430      46.811  33.495   1.010  0.00 56.52           N  
ATOM   4758  H   LYS D 430      49.184  39.151   3.902  1.00  0.00           H  
ATOM   4759  HZ1 LYS D 430      46.868  32.734   1.717  1.00  0.00           H  
ATOM   4760  HZ2 LYS D 430      45.814  33.736   0.840  1.00  0.00           H  
ATOM   4761  HZ3 LYS D 430      47.265  33.183   0.130  1.00  0.00           H  
ATOM   4762  N   ALA D 431      46.272  40.242   3.384  0.00 57.69           N  
ATOM   4763  CA  ALA D 431      45.048  40.998   3.657  0.00 56.36           C  
ATOM   4764  C   ALA D 431      44.099  40.213   4.572  0.00 55.90           C  
ATOM   4765  O   ALA D 431      44.478  39.176   5.126  0.00 58.13           O  
ATOM   4766  CB  ALA D 431      44.352  41.384   2.353  0.00 55.29           C  
ATOM   4767  H   ALA D 431      47.147  40.593   3.618  1.00  0.00           H  
ATOM   4768  N   PHE D 432      42.875  40.710   4.743  1.00 55.20           N  
ATOM   4769  CA  PHE D 432      41.947  40.089   5.681  1.00 52.32           C  
ATOM   4770  C   PHE D 432      41.232  38.878   5.082  1.00 53.72           C  
ATOM   4771  O   PHE D 432      40.025  38.902   4.883  1.00 59.69           O  
ATOM   4772  CB  PHE D 432      40.939  41.116   6.193  1.00 49.51           C  
ATOM   4773  CG  PHE D 432      41.503  42.055   7.225  1.00 49.59           C  
ATOM   4774  CD1 PHE D 432      41.952  41.571   8.450  1.00 50.34           C  
ATOM   4775  CD2 PHE D 432      41.584  43.422   6.975  1.00 49.85           C  
ATOM   4776  CE1 PHE D 432      42.483  42.432   9.413  1.00 47.04           C  
ATOM   4777  CE2 PHE D 432      42.109  44.299   7.926  1.00 48.01           C  
ATOM   4778  CZ  PHE D 432      42.564  43.803   9.153  1.00 47.36           C  
ATOM   4779  H   PHE D 432      42.502  41.377   4.137  1.00  0.00           H  
ATOM   4780  N   SER D 433      41.989  37.811   4.845  1.00 53.28           N  
ATOM   4781  CA  SER D 433      41.457  36.562   4.308  1.00 52.10           C  
ATOM   4782  C   SER D 433      41.300  35.528   5.432  1.00 53.23           C  
ATOM   4783  O   SER D 433      41.799  35.735   6.541  1.00 56.67           O  
ATOM   4784  CB  SER D 433      42.403  36.026   3.233  1.00 50.72           C  
ATOM   4785  OG  SER D 433      43.464  35.277   3.805  1.00 51.49           O  
ATOM   4786  H   SER D 433      42.920  37.856   5.158  1.00  0.00           H  
ATOM   4787  HG  SER D 433      44.267  35.594   3.376  1.00  0.00           H  
ATOM   4788  N   PRO D 434      40.669  34.372   5.147  1.00 49.86           N  
ATOM   4789  CA  PRO D 434      40.445  33.361   6.190  1.00 47.48           C  
ATOM   4790  C   PRO D 434      41.690  32.976   6.986  1.00 45.14           C  
ATOM   4791  O   PRO D 434      41.599  32.628   8.161  1.00 51.12           O  
ATOM   4792  CB  PRO D 434      39.884  32.178   5.415  1.00 48.74           C  
ATOM   4793  CG  PRO D 434      39.146  32.812   4.293  1.00 52.43           C  
ATOM   4794  CD  PRO D 434      39.981  34.010   3.893  1.00 52.62           C  
ATOM   4795  N   GLU D 435      42.855  33.129   6.367  1.00 44.63           N  
ATOM   4796  CA  GLU D 435      44.126  32.750   6.988  1.00 44.20           C  
ATOM   4797  C   GLU D 435      44.577  33.707   8.106  1.00 40.10           C  
ATOM   4798  O   GLU D 435      45.248  33.296   9.055  1.00 36.46           O  
ATOM   4799  CB  GLU D 435      45.216  32.659   5.915  1.00 47.58           C  
ATOM   4800  CG  GLU D 435      44.849  31.773   4.725  0.00 51.30           C  
ATOM   4801  CD  GLU D 435      45.950  31.682   3.681  0.00 53.03           C  
ATOM   4802  OE1 GLU D 435      47.127  31.933   4.016  0.00 54.50           O  
ATOM   4803  OE2 GLU D 435      45.639  31.334   2.522  0.00 55.75           O  
ATOM   4804  H   GLU D 435      42.849  33.505   5.465  1.00  0.00           H  
ATOM   4805  N   VAL D 436      44.191  34.976   8.000  1.00 36.84           N  
ATOM   4806  CA  VAL D 436      44.546  36.006   8.980  1.00 34.27           C  
ATOM   4807  C   VAL D 436      43.950  35.771  10.381  1.00 28.10           C  
ATOM   4808  O   VAL D 436      44.472  36.265  11.383  1.00 26.29           O  
ATOM   4809  CB  VAL D 436      44.120  37.412   8.459  1.00 38.56           C  
ATOM   4810  CG1 VAL D 436      42.676  37.717   8.838  1.00 42.60           C  
ATOM   4811  CG2 VAL D 436      45.054  38.481   8.990  1.00 43.21           C  
ATOM   4812  H   VAL D 436      43.636  35.225   7.231  1.00  0.00           H  
ATOM   4813  N   ILE D 437      42.897  34.966  10.458  1.00 24.02           N  
ATOM   4814  CA  ILE D 437      42.234  34.724  11.733  1.00 24.08           C  
ATOM   4815  C   ILE D 437      43.012  33.786  12.663  1.00 21.15           C  
ATOM   4816  O   ILE D 437      43.375  34.182  13.774  1.00 28.06           O  
ATOM   4817  CB  ILE D 437      40.786  34.204  11.533  1.00 29.89           C  
ATOM   4818  CG1 ILE D 437      39.973  35.226  10.727  1.00 28.02           C  
ATOM   4819  CG2 ILE D 437      40.116  33.965  12.890  1.00 23.65           C  
ATOM   4820  CD1 ILE D 437      38.578  34.766  10.376  1.00 23.50           C  
ATOM   4821  H   ILE D 437      42.562  34.564   9.630  1.00  0.00           H  
ATOM   4822  N   PRO D 438      43.370  32.573  12.194  1.00 16.36           N  
ATOM   4823  CA  PRO D 438      44.192  31.690  13.035  1.00 19.20           C  
ATOM   4824  C   PRO D 438      45.508  32.344  13.460  1.00 24.02           C  
ATOM   4825  O   PRO D 438      45.970  32.161  14.588  1.00 29.98           O  
ATOM   4826  CB  PRO D 438      44.438  30.466  12.146  1.00 15.52           C  
ATOM   4827  CG  PRO D 438      43.373  30.518  11.113  1.00 13.73           C  
ATOM   4828  CD  PRO D 438      43.128  31.976  10.871  1.00 15.91           C  
ATOM   4829  N   MET D 439      46.064  33.168  12.575  1.00 26.09           N  
ATOM   4830  CA  MET D 439      47.280  33.924  12.871  1.00 25.48           C  
ATOM   4831  C   MET D 439      47.084  34.912  14.018  1.00 20.64           C  
ATOM   4832  O   MET D 439      47.846  34.905  14.979  1.00 29.33           O  
ATOM   4833  CB  MET D 439      47.754  34.675  11.624  1.00 24.78           C  
ATOM   4834  CG  MET D 439      49.205  35.115  11.687  1.00 26.74           C  
ATOM   4835  SD  MET D 439      50.324  33.711  11.857  1.00 36.75           S  
ATOM   4836  CE  MET D 439      50.239  33.018  10.193  1.00 40.71           C  
ATOM   4837  H   MET D 439      45.673  33.213  11.677  1.00  0.00           H  
ATOM   4838  N   PHE D 440      46.033  35.726  13.937  1.00 24.42           N  
ATOM   4839  CA  PHE D 440      45.743  36.716  14.974  1.00 18.61           C  
ATOM   4840  C   PHE D 440      45.595  36.056  16.338  1.00 18.84           C  
ATOM   4841  O   PHE D 440      46.198  36.498  17.313  1.00 16.69           O  
ATOM   4842  CB  PHE D 440      44.461  37.491  14.645  1.00 20.32           C  
ATOM   4843  CG  PHE D 440      44.136  38.583  15.636  1.00 15.23           C  
ATOM   4844  CD1 PHE D 440      44.726  39.838  15.527  1.00 11.65           C  
ATOM   4845  CD2 PHE D 440      43.264  38.345  16.693  1.00 11.12           C  
ATOM   4846  CE1 PHE D 440      44.457  40.840  16.453  1.00  2.48           C  
ATOM   4847  CE2 PHE D 440      42.991  39.339  17.626  1.00  8.06           C  
ATOM   4848  CZ  PHE D 440      43.592  40.590  17.502  1.00 13.64           C  
ATOM   4849  H   PHE D 440      45.468  35.690  13.134  1.00  0.00           H  
ATOM   4850  N   SER D 441      44.799  34.991  16.393  1.00 15.65           N  
ATOM   4851  CA  SER D 441      44.593  34.229  17.628  1.00 21.37           C  
ATOM   4852  C   SER D 441      45.917  33.710  18.182  1.00 24.11           C  
ATOM   4853  O   SER D 441      46.238  33.915  19.355  1.00 27.16           O  
ATOM   4854  CB  SER D 441      43.655  33.041  17.369  1.00 12.05           C  
ATOM   4855  OG  SER D 441      43.540  32.214  18.514  0.00 15.91           O  
ATOM   4856  H   SER D 441      44.325  34.747  15.567  1.00  0.00           H  
ATOM   4857  HG  SER D 441      43.149  31.369  18.280  1.00  0.00           H  
ATOM   4858  N   ALA D 442      46.739  33.170  17.286  1.00 25.91           N  
ATOM   4859  CA  ALA D 442      48.032  32.598  17.648  1.00 23.02           C  
ATOM   4860  C   ALA D 442      49.019  33.644  18.170  1.00 26.48           C  
ATOM   4861  O   ALA D 442      49.807  33.369  19.077  1.00 29.46           O  
ATOM   4862  CB  ALA D 442      48.627  31.871  16.447  1.00 26.64           C  
ATOM   4863  H   ALA D 442      46.452  33.145  16.349  1.00  0.00           H  
ATOM   4864  N   LEU D 443      48.929  34.859  17.638  1.00 22.25           N  
ATOM   4865  CA  LEU D 443      49.845  35.932  18.011  1.00 20.46           C  
ATOM   4866  C   LEU D 443      49.309  36.823  19.130  1.00 22.27           C  
ATOM   4867  O   LEU D 443      49.945  37.811  19.495  1.00 26.72           O  
ATOM   4868  CB  LEU D 443      50.170  36.797  16.789  1.00 21.88           C  
ATOM   4869  CG  LEU D 443      50.775  36.107  15.564  1.00 23.41           C  
ATOM   4870  CD1 LEU D 443      50.997  37.123  14.462  1.00 27.39           C  
ATOM   4871  CD2 LEU D 443      52.080  35.442  15.932  1.00 21.36           C  
ATOM   4872  H   LEU D 443      48.264  35.005  16.933  1.00  0.00           H  
ATOM   4873  N   SER D 444      48.129  36.499  19.651  1.00 21.33           N  
ATOM   4874  CA  SER D 444      47.497  37.335  20.674  1.00 21.36           C  
ATOM   4875  C   SER D 444      47.174  36.573  21.958  1.00 22.85           C  
ATOM   4876  O   SER D 444      46.482  37.086  22.841  1.00 21.20           O  
ATOM   4877  CB  SER D 444      46.219  37.976  20.126  1.00 16.86           C  
ATOM   4878  OG  SER D 444      45.254  36.988  19.798  1.00 24.13           O  
ATOM   4879  H   SER D 444      47.650  35.718  19.301  1.00  0.00           H  
ATOM   4880  HG  SER D 444      45.274  36.855  18.848  1.00  0.00           H  
ATOM   4881  N   GLU D 445      47.740  35.380  22.096  1.00 24.86           N  
ATOM   4882  CA  GLU D 445      47.541  34.572  23.293  1.00 23.38           C  
ATOM   4883  C   GLU D 445      47.994  35.295  24.565  1.00 24.32           C  
ATOM   4884  O   GLU D 445      49.099  35.839  24.627  1.00 22.50           O  
ATOM   4885  CB  GLU D 445      48.279  33.242  23.147  1.00 22.84           C  
ATOM   4886  CG  GLU D 445      47.660  32.308  22.115  0.00 23.51           C  
ATOM   4887  CD  GLU D 445      48.483  31.055  21.882  0.00 22.77           C  
ATOM   4888  OE1 GLU D 445      48.549  30.204  22.795  0.00 24.20           O  
ATOM   4889  OE2 GLU D 445      49.049  30.912  20.778  0.00 23.35           O  
ATOM   4890  H   GLU D 445      48.287  35.046  21.357  1.00  0.00           H  
ATOM   4891  N   GLY D 446      47.065  35.437  25.507  1.00 24.97           N  
ATOM   4892  CA  GLY D 446      47.358  36.115  26.758  1.00 22.19           C  
ATOM   4893  C   GLY D 446      47.285  37.629  26.678  1.00 20.66           C  
ATOM   4894  O   GLY D 446      47.625  38.322  27.637  1.00 21.04           O  
ATOM   4895  H   GLY D 446      46.166  35.104  25.318  1.00  0.00           H  
ATOM   4896  N   ALA D 447      46.848  38.155  25.540  1.00 20.07           N  
ATOM   4897  CA  ALA D 447      46.860  39.597  25.330  1.00 16.06           C  
ATOM   4898  C   ALA D 447      45.777  40.325  26.124  1.00 18.78           C  
ATOM   4899  O   ALA D 447      44.699  39.787  26.367  1.00 18.32           O  
ATOM   4900  CB  ALA D 447      46.733  39.911  23.850  1.00 17.57           C  
ATOM   4901  H   ALA D 447      46.512  37.568  24.826  1.00  0.00           H  
ATOM   4902  N   THR D 448      46.134  41.497  26.640  1.00 19.41           N  
ATOM   4903  CA  THR D 448      45.169  42.406  27.254  1.00 22.70           C  
ATOM   4904  C   THR D 448      44.395  43.139  26.157  1.00 25.92           C  
ATOM   4905  O   THR D 448      44.878  43.257  25.028  1.00 32.19           O  
ATOM   4906  CB  THR D 448      45.873  43.468  28.133  1.00 22.66           C  
ATOM   4907  OG1 THR D 448      46.597  44.379  27.298  1.00 30.46           O  
ATOM   4908  CG2 THR D 448      46.840  42.808  29.092  1.00 22.86           C  
ATOM   4909  H   THR D 448      47.071  41.726  26.568  1.00  0.00           H  
ATOM   4910  HG1 THR D 448      47.452  43.997  27.136  1.00  0.00           H  
ATOM   4911  N   PRO D 449      43.243  43.739  26.501  1.00 24.16           N  
ATOM   4912  CA  PRO D 449      42.559  44.649  25.577  1.00 20.21           C  
ATOM   4913  C   PRO D 449      43.478  45.701  24.954  1.00 23.49           C  
ATOM   4914  O   PRO D 449      43.432  45.935  23.744  1.00 23.27           O  
ATOM   4915  CB  PRO D 449      41.474  45.275  26.448  1.00 15.40           C  
ATOM   4916  CG  PRO D 449      41.118  44.191  27.388  1.00 10.31           C  
ATOM   4917  CD  PRO D 449      42.404  43.440  27.676  1.00 22.70           C  
ATOM   4918  N   GLN D 450      44.374  46.264  25.762  1.00 27.90           N  
ATOM   4919  CA  GLN D 450      45.366  47.214  25.254  1.00 28.00           C  
ATOM   4920  C   GLN D 450      46.300  46.584  24.208  1.00 26.20           C  
ATOM   4921  O   GLN D 450      46.525  47.160  23.139  1.00 30.87           O  
ATOM   4922  CB  GLN D 450      46.187  47.802  26.407  1.00 34.97           C  
ATOM   4923  CG  GLN D 450      47.109  48.936  25.984  0.00 35.86           C  
ATOM   4924  CD  GLN D 450      47.753  49.639  27.160  0.00 38.56           C  
ATOM   4925  OE1 GLN D 450      48.613  49.083  27.838  0.00 41.02           O  
ATOM   4926  NE2 GLN D 450      47.347  50.874  27.403  0.00 39.77           N  
ATOM   4927  H   GLN D 450      44.306  46.098  26.730  1.00  0.00           H  
ATOM   4928 HE21 GLN D 450      47.815  51.316  28.132  1.00  0.00           H  
ATOM   4929 HE22 GLN D 450      46.643  51.253  26.845  1.00  0.00           H  
ATOM   4930  N   ASP D 451      46.757  45.362  24.469  1.00 19.25           N  
ATOM   4931  CA  ASP D 451      47.603  44.649  23.514  1.00 18.22           C  
ATOM   4932  C   ASP D 451      46.863  44.351  22.217  1.00 23.43           C  
ATOM   4933  O   ASP D 451      47.408  44.524  21.128  1.00 28.22           O  
ATOM   4934  CB  ASP D 451      48.115  43.342  24.118  1.00 22.73           C  
ATOM   4935  CG  ASP D 451      49.105  43.567  25.251  1.00 33.41           C  
ATOM   4936  OD1 ASP D 451      49.868  44.560  25.195  1.00 31.27           O  
ATOM   4937  OD2 ASP D 451      49.121  42.750  26.199  1.00 34.64           O  
ATOM   4938  H   ASP D 451      46.451  44.951  25.305  1.00  0.00           H  
ATOM   4939  N   LEU D 452      45.597  43.965  22.343  1.00 26.87           N  
ATOM   4940  CA  LEU D 452      44.747  43.690  21.186  1.00 22.44           C  
ATOM   4941  C   LEU D 452      44.507  44.947  20.348  1.00 19.69           C  
ATOM   4942  O   LEU D 452      44.605  44.913  19.121  1.00 19.32           O  
ATOM   4943  CB  LEU D 452      43.414  43.101  21.652  1.00 18.49           C  
ATOM   4944  CG  LEU D 452      43.517  41.736  22.335  1.00 12.13           C  
ATOM   4945  CD1 LEU D 452      42.216  41.405  23.024  1.00 10.93           C  
ATOM   4946  CD2 LEU D 452      43.869  40.675  21.309  1.00 14.04           C  
ATOM   4947  H   LEU D 452      45.235  43.839  23.242  1.00  0.00           H  
ATOM   4948  N   ASN D 453      44.340  46.079  21.024  1.00 24.00           N  
ATOM   4949  CA  ASN D 453      44.197  47.367  20.347  1.00 27.62           C  
ATOM   4950  C   ASN D 453      45.493  47.837  19.688  1.00 30.15           C  
ATOM   4951  O   ASN D 453      45.467  48.443  18.618  1.00 33.18           O  
ATOM   4952  CB  ASN D 453      43.698  48.426  21.332  1.00 29.32           C  
ATOM   4953  CG  ASN D 453      42.237  48.242  21.683  1.00 31.15           C  
ATOM   4954  OD1 ASN D 453      41.471  47.711  20.893  1.00 33.26           O  
ATOM   4955  ND2 ASN D 453      41.857  48.633  22.885  1.00 29.38           N  
ATOM   4956  H   ASN D 453      44.233  46.021  21.995  1.00  0.00           H  
ATOM   4957 HD21 ASN D 453      40.903  48.503  23.050  1.00  0.00           H  
ATOM   4958 HD22 ASN D 453      42.511  49.000  23.494  1.00  0.00           H  
ATOM   4959  N   THR D 454      46.626  47.519  20.307  1.00 31.23           N  
ATOM   4960  CA  THR D 454      47.932  47.785  19.706  1.00 28.45           C  
ATOM   4961  C   THR D 454      48.101  47.004  18.396  1.00 24.74           C  
ATOM   4962  O   THR D 454      48.517  47.562  17.380  1.00 22.37           O  
ATOM   4963  CB  THR D 454      49.085  47.412  20.674  1.00 30.72           C  
ATOM   4964  OG1 THR D 454      48.939  48.143  21.899  1.00 31.26           O  
ATOM   4965  CG2 THR D 454      50.440  47.756  20.060  1.00 32.35           C  
ATOM   4966  H   THR D 454      46.562  47.088  21.183  1.00  0.00           H  
ATOM   4967  HG1 THR D 454      48.020  48.206  22.180  1.00  0.00           H  
ATOM   4968  N   MET D 455      47.674  45.744  18.399  1.00 22.57           N  
ATOM   4969  CA  MET D 455      47.682  44.918  17.189  1.00 24.18           C  
ATOM   4970  C   MET D 455      46.790  45.465  16.070  1.00 29.48           C  
ATOM   4971  O   MET D 455      47.141  45.391  14.892  1.00 27.15           O  
ATOM   4972  CB  MET D 455      47.245  43.492  17.516  1.00 19.87           C  
ATOM   4973  CG  MET D 455      48.228  42.714  18.358  1.00 21.01           C  
ATOM   4974  SD  MET D 455      47.703  41.011  18.537  1.00 28.34           S  
ATOM   4975  CE  MET D 455      48.397  40.284  17.025  1.00 20.61           C  
ATOM   4976  H   MET D 455      47.391  45.350  19.254  1.00  0.00           H  
ATOM   4977  N   LEU D 456      45.622  45.984  16.438  1.00 27.80           N  
ATOM   4978  CA  LEU D 456      44.694  46.545  15.456  1.00 26.49           C  
ATOM   4979  C   LEU D 456      45.153  47.890  14.893  1.00 28.91           C  
ATOM   4980  O   LEU D 456      45.136  48.100  13.678  1.00 32.17           O  
ATOM   4981  CB  LEU D 456      43.300  46.699  16.067  1.00 20.93           C  
ATOM   4982  CG  LEU D 456      42.643  45.422  16.594  1.00 15.14           C  
ATOM   4983  CD1 LEU D 456      41.253  45.752  17.089  1.00 12.10           C  
ATOM   4984  CD2 LEU D 456      42.595  44.358  15.505  1.00  6.60           C  
ATOM   4985  H   LEU D 456      45.357  45.906  17.381  1.00  0.00           H  
ATOM   4986  N   ASN D 457      45.628  48.770  15.768  1.00 28.38           N  
ATOM   4987  CA  ASN D 457      46.031  50.114  15.361  1.00 30.98           C  
ATOM   4988  C   ASN D 457      47.373  50.152  14.630  1.00 33.73           C  
ATOM   4989  O   ASN D 457      47.774  51.192  14.110  1.00 39.20           O  
ATOM   4990  CB  ASN D 457      46.083  51.039  16.575  1.00 32.46           C  
ATOM   4991  CG  ASN D 457      44.761  51.111  17.306  1.00 40.91           C  
ATOM   4992  OD1 ASN D 457      43.723  50.723  16.779  1.00 42.23           O  
ATOM   4993  ND2 ASN D 457      44.797  51.581  18.540  1.00 52.50           N  
ATOM   4994  H   ASN D 457      45.640  48.516  16.711  1.00  0.00           H  
ATOM   4995 HD21 ASN D 457      43.916  51.614  18.951  1.00  0.00           H  
ATOM   4996 HD22 ASN D 457      45.642  51.848  18.944  1.00  0.00           H  
ATOM   4997  N   THR D 458      48.082  49.029  14.625  1.00 33.71           N  
ATOM   4998  CA  THR D 458      49.330  48.931  13.876  1.00 39.19           C  
ATOM   4999  C   THR D 458      49.082  48.578  12.406  1.00 39.40           C  
ATOM   5000  O   THR D 458      49.987  48.672  11.572  1.00 40.14           O  
ATOM   5001  CB  THR D 458      50.295  47.890  14.513  1.00 41.34           C  
ATOM   5002  OG1 THR D 458      51.620  48.091  14.007  1.00 49.85           O  
ATOM   5003  CG2 THR D 458      49.854  46.471  14.194  1.00 42.37           C  
ATOM   5004  H   THR D 458      47.792  48.297  15.207  1.00  0.00           H  
ATOM   5005  HG1 THR D 458      51.569  48.056  13.048  1.00  0.00           H  
ATOM   5006  N   VAL D 459      47.846  48.203  12.085  1.00 39.64           N  
ATOM   5007  CA  VAL D 459      47.464  47.906  10.705  1.00 40.65           C  
ATOM   5008  C   VAL D 459      47.347  49.199   9.894  1.00 41.21           C  
ATOM   5009  O   VAL D 459      46.348  49.914   9.979  1.00 42.86           O  
ATOM   5010  CB  VAL D 459      46.125  47.130  10.650  1.00 40.78           C  
ATOM   5011  CG1 VAL D 459      45.706  46.897   9.210  1.00 37.49           C  
ATOM   5012  CG2 VAL D 459      46.268  45.797  11.372  1.00 44.46           C  
ATOM   5013  H   VAL D 459      47.160  48.155  12.785  1.00  0.00           H  
ATOM   5014  N   GLY D 460      48.449  49.585   9.261  0.00 41.11           N  
ATOM   5015  CA  GLY D 460      48.514  50.881   8.606  0.00 40.63           C  
ATOM   5016  C   GLY D 460      48.056  50.900   7.159  0.00 40.11           C  
ATOM   5017  O   GLY D 460      48.882  50.905   6.247  0.00 40.11           O  
ATOM   5018  H   GLY D 460      49.243  49.023   9.373  1.00  0.00           H  
ATOM   5019  N   GLY D 461      46.743  50.867   6.948  0.00 39.31           N  
ATOM   5020  CA  GLY D 461      46.206  51.040   5.607  0.00 37.49           C  
ATOM   5021  C   GLY D 461      45.197  49.999   5.147  0.00 35.84           C  
ATOM   5022  O   GLY D 461      45.417  49.306   4.156  0.00 35.95           O  
ATOM   5023  H   GLY D 461      46.191  50.763   7.752  1.00  0.00           H  
ATOM   5024  N   HIS D 462      44.098  49.864   5.885  0.00 33.76           N  
ATOM   5025  CA  HIS D 462      42.986  48.998   5.481  0.00 31.23           C  
ATOM   5026  C   HIS D 462      41.659  49.579   5.982  0.00 29.18           C  
ATOM   5027  O   HIS D 462      40.856  48.877   6.599  0.00 28.66           O  
ATOM   5028  CB  HIS D 462      43.178  47.580   6.043  0.00 31.78           C  
ATOM   5029  CG  HIS D 462      44.207  46.769   5.315  0.00 32.09           C  
ATOM   5030  ND1 HIS D 462      43.921  46.049   4.174  0.00 31.92           N  
ATOM   5031  CD2 HIS D 462      45.519  46.551   5.575  0.00 32.16           C  
ATOM   5032  CE1 HIS D 462      45.009  45.424   3.763  0.00 29.67           C  
ATOM   5033  NE2 HIS D 462      45.993  45.712   4.596  0.00 31.76           N  
ATOM   5034  H   HIS D 462      44.073  50.358   6.732  1.00  0.00           H  
ATOM   5035  HD1 HIS D 462      43.068  46.017   3.692  1.00  0.00           H  
ATOM   5036  HE2 HIS D 462      46.912  45.368   4.507  1.00  0.00           H  
ATOM   5037  N   GLN D 463      41.373  50.813   5.576  0.00 25.01           N  
ATOM   5038  CA  GLN D 463      40.443  51.674   6.308  0.00 25.44           C  
ATOM   5039  C   GLN D 463      39.009  51.149   6.403  0.00 25.66           C  
ATOM   5040  O   GLN D 463      38.437  51.078   7.492  0.00 27.68           O  
ATOM   5041  CB  GLN D 463      40.438  53.076   5.690  0.00 25.91           C  
ATOM   5042  CG  GLN D 463      39.989  54.175   6.643  0.00 24.98           C  
ATOM   5043  CD  GLN D 463      38.696  54.838   6.208  0.00 26.59           C  
ATOM   5044  OE1 GLN D 463      37.729  54.168   5.857  0.00 28.20           O  
ATOM   5045  NE2 GLN D 463      38.680  56.159   6.215  0.00 25.80           N  
ATOM   5046  H   GLN D 463      41.804  51.139   4.760  1.00  0.00           H  
ATOM   5047 HE21 GLN D 463      37.829  56.557   5.953  1.00  0.00           H  
ATOM   5048 HE22 GLN D 463      39.479  56.651   6.479  1.00  0.00           H  
ATOM   5049  N   ALA D 464      38.440  50.769   5.265  1.00 25.04           N  
ATOM   5050  CA  ALA D 464      37.049  50.322   5.200  1.00 23.11           C  
ATOM   5051  C   ALA D 464      36.810  49.082   6.061  1.00 27.06           C  
ATOM   5052  O   ALA D 464      35.855  49.029   6.838  1.00 31.09           O  
ATOM   5053  CB  ALA D 464      36.661  50.039   3.746  1.00 21.35           C  
ATOM   5054  H   ALA D 464      38.977  50.832   4.458  1.00  0.00           H  
ATOM   5055  N   ALA D 465      37.745  48.138   5.997  1.00 26.46           N  
ATOM   5056  CA  ALA D 465      37.666  46.910   6.781  1.00 25.18           C  
ATOM   5057  C   ALA D 465      37.791  47.176   8.283  1.00 22.59           C  
ATOM   5058  O   ALA D 465      37.027  46.637   9.079  1.00 29.13           O  
ATOM   5059  CB  ALA D 465      38.742  45.940   6.328  1.00 21.34           C  
ATOM   5060  H   ALA D 465      38.506  48.286   5.405  1.00  0.00           H  
ATOM   5061  N   MET D 466      38.708  48.063   8.658  1.00 25.18           N  
ATOM   5062  CA  MET D 466      38.920  48.395  10.070  1.00 27.98           C  
ATOM   5063  C   MET D 466      37.710  49.100  10.682  1.00 27.11           C  
ATOM   5064  O   MET D 466      37.382  48.888  11.849  1.00 30.65           O  
ATOM   5065  CB  MET D 466      40.167  49.270  10.244  1.00 26.60           C  
ATOM   5066  CG  MET D 466      41.469  48.570   9.892  1.00 26.74           C  
ATOM   5067  SD  MET D 466      41.589  46.894  10.562  1.00 37.89           S  
ATOM   5068  CE  MET D 466      42.139  47.244  12.218  1.00 33.28           C  
ATOM   5069  H   MET D 466      39.268  48.480   7.971  1.00  0.00           H  
ATOM   5070  N   GLN D 467      37.017  49.891   9.869  1.00 30.60           N  
ATOM   5071  CA  GLN D 467      35.764  50.527  10.275  1.00 29.19           C  
ATOM   5072  C   GLN D 467      34.660  49.485  10.481  1.00 28.31           C  
ATOM   5073  O   GLN D 467      33.865  49.578  11.418  1.00 28.49           O  
ATOM   5074  CB  GLN D 467      35.327  51.538   9.212  1.00 34.11           C  
ATOM   5075  CG  GLN D 467      34.353  52.598   9.702  0.00 48.11           C  
ATOM   5076  CD  GLN D 467      34.025  53.625   8.632  0.00 55.37           C  
ATOM   5077  OE1 GLN D 467      32.862  53.927   8.382  0.00 61.28           O  
ATOM   5078  NE2 GLN D 467      35.051  54.171   8.000  0.00 58.95           N  
ATOM   5079  H   GLN D 467      37.394  50.093   8.988  1.00  0.00           H  
ATOM   5080 HE21 GLN D 467      34.774  54.815   7.324  1.00  0.00           H  
ATOM   5081 HE22 GLN D 467      35.967  53.914   8.210  1.00  0.00           H  
ATOM   5082  N   MET D 468      34.660  48.462   9.633  1.00 27.96           N  
ATOM   5083  CA  MET D 468      33.718  47.346   9.729  1.00 27.04           C  
ATOM   5084  C   MET D 468      33.952  46.515  11.002  1.00 29.33           C  
ATOM   5085  O   MET D 468      33.007  46.156  11.711  1.00 28.21           O  
ATOM   5086  CB  MET D 468      33.873  46.451   8.496  1.00 30.17           C  
ATOM   5087  CG  MET D 468      32.577  45.959   7.882  1.00 43.69           C  
ATOM   5088  SD  MET D 468      32.893  44.917   6.432  1.00 53.23           S  
ATOM   5089  CE  MET D 468      33.494  46.145   5.252  1.00 53.38           C  
ATOM   5090  H   MET D 468      35.284  48.495   8.875  1.00  0.00           H  
ATOM   5091  N   LEU D 469      35.217  46.200  11.271  1.00 27.98           N  
ATOM   5092  CA  LEU D 469      35.615  45.477  12.480  1.00 25.85           C  
ATOM   5093  C   LEU D 469      35.263  46.265  13.750  1.00 24.56           C  
ATOM   5094  O   LEU D 469      34.692  45.714  14.698  1.00 24.60           O  
ATOM   5095  CB  LEU D 469      37.124  45.196  12.436  1.00 27.36           C  
ATOM   5096  CG  LEU D 469      37.839  44.679  13.692  1.00 28.68           C  
ATOM   5097  CD1 LEU D 469      37.476  43.227  13.950  1.00 22.03           C  
ATOM   5098  CD2 LEU D 469      39.343  44.826  13.514  1.00 22.91           C  
ATOM   5099  H   LEU D 469      35.890  46.422  10.595  1.00  0.00           H  
ATOM   5100  N   LYS D 470      35.538  47.569  13.723  1.00 22.54           N  
ATOM   5101  CA  LYS D 470      35.244  48.460  14.846  1.00 19.20           C  
ATOM   5102  C   LYS D 470      33.756  48.491  15.195  1.00 20.98           C  
ATOM   5103  O   LYS D 470      33.380  48.325  16.354  1.00 25.25           O  
ATOM   5104  CB  LYS D 470      35.729  49.878  14.534  1.00 15.85           C  
ATOM   5105  CG  LYS D 470      36.071  50.694  15.768  0.00 17.73           C  
ATOM   5106  CD  LYS D 470      37.364  50.211  16.407  0.00 17.36           C  
ATOM   5107  CE  LYS D 470      37.435  50.582  17.881  0.00 17.90           C  
ATOM   5108  NZ  LYS D 470      37.230  52.039  18.115  0.00 20.59           N  
ATOM   5109  H   LYS D 470      36.003  47.926  12.936  1.00  0.00           H  
ATOM   5110  HZ1 LYS D 470      37.918  52.588  17.561  1.00  0.00           H  
ATOM   5111  HZ2 LYS D 470      36.265  52.298  17.826  1.00  0.00           H  
ATOM   5112  HZ3 LYS D 470      37.353  52.243  19.127  1.00  0.00           H  
ATOM   5113  N   GLU D 471      32.910  48.622  14.178  1.00 24.55           N  
ATOM   5114  CA  GLU D 471      31.464  48.572  14.370  1.00 21.69           C  
ATOM   5115  C   GLU D 471      31.010  47.250  14.996  1.00 23.22           C  
ATOM   5116  O   GLU D 471      30.233  47.245  15.951  1.00 26.63           O  
ATOM   5117  CB  GLU D 471      30.746  48.799  13.036  1.00 23.09           C  
ATOM   5118  CG  GLU D 471      29.242  48.995  13.167  0.00 23.92           C  
ATOM   5119  CD  GLU D 471      28.554  49.163  11.827  0.00 24.68           C  
ATOM   5120  OE1 GLU D 471      28.183  48.139  11.215  0.00 24.79           O  
ATOM   5121  OE2 GLU D 471      28.372  50.319  11.391  0.00 24.73           O  
ATOM   5122  H   GLU D 471      33.278  48.823  13.288  1.00  0.00           H  
ATOM   5123  N   THR D 472      31.542  46.136  14.498  1.00 22.16           N  
ATOM   5124  CA  THR D 472      31.238  44.821  15.068  1.00 22.37           C  
ATOM   5125  C   THR D 472      31.629  44.717  16.546  1.00 25.14           C  
ATOM   5126  O   THR D 472      30.860  44.208  17.367  1.00 25.01           O  
ATOM   5127  CB  THR D 472      31.949  43.701  14.286  1.00 18.96           C  
ATOM   5128  OG1 THR D 472      31.433  43.660  12.952  1.00 24.23           O  
ATOM   5129  CG2 THR D 472      31.716  42.342  14.944  1.00 12.43           C  
ATOM   5130  H   THR D 472      32.142  46.207  13.719  1.00  0.00           H  
ATOM   5131  HG1 THR D 472      31.175  44.539  12.661  1.00  0.00           H  
ATOM   5132  N   ILE D 473      32.802  45.242  16.888  1.00 25.89           N  
ATOM   5133  CA  ILE D 473      33.243  45.289  18.281  1.00 23.65           C  
ATOM   5134  C   ILE D 473      32.285  46.145  19.120  1.00 24.11           C  
ATOM   5135  O   ILE D 473      31.838  45.725  20.187  1.00 26.36           O  
ATOM   5136  CB  ILE D 473      34.685  45.856  18.396  1.00 20.35           C  
ATOM   5137  CG1 ILE D 473      35.686  44.874  17.782  1.00 19.62           C  
ATOM   5138  CG2 ILE D 473      35.040  46.105  19.852  1.00 18.12           C  
ATOM   5139  CD1 ILE D 473      37.074  45.462  17.580  1.00 17.87           C  
ATOM   5140  H   ILE D 473      33.404  45.561  16.179  1.00  0.00           H  
ATOM   5141  N   ASN D 474      31.907  47.305  18.591  1.00 20.73           N  
ATOM   5142  CA  ASN D 474      31.007  48.217  19.290  1.00 17.85           C  
ATOM   5143  C   ASN D 474      29.614  47.629  19.501  1.00 23.90           C  
ATOM   5144  O   ASN D 474      28.974  47.888  20.519  1.00 26.47           O  
ATOM   5145  CB  ASN D 474      30.903  49.534  18.531  1.00 17.43           C  
ATOM   5146  CG  ASN D 474      32.170  50.366  18.618  1.00 23.26           C  
ATOM   5147  OD1 ASN D 474      32.221  51.477  18.110  1.00 33.07           O  
ATOM   5148  ND2 ASN D 474      33.202  49.829  19.249  1.00 27.74           N  
ATOM   5149  H   ASN D 474      32.260  47.546  17.707  1.00  0.00           H  
ATOM   5150 HD21 ASN D 474      33.922  50.485  19.289  1.00  0.00           H  
ATOM   5151 HD22 ASN D 474      33.247  48.934  19.618  1.00  0.00           H  
ATOM   5152  N   GLU D 475      29.164  46.819  18.549  1.00 23.01           N  
ATOM   5153  CA  GLU D 475      27.917  46.075  18.693  1.00 25.27           C  
ATOM   5154  C   GLU D 475      28.014  45.054  19.822  1.00 22.88           C  
ATOM   5155  O   GLU D 475      27.151  45.000  20.699  1.00 25.72           O  
ATOM   5156  CB  GLU D 475      27.575  45.363  17.384  1.00 25.71           C  
ATOM   5157  CG  GLU D 475      27.210  46.299  16.244  1.00 26.16           C  
ATOM   5158  CD  GLU D 475      27.096  45.586  14.911  1.00 41.28           C  
ATOM   5159  OE1 GLU D 475      27.265  44.345  14.868  1.00 46.28           O  
ATOM   5160  OE2 GLU D 475      26.835  46.269  13.897  1.00 51.55           O  
ATOM   5161  H   GLU D 475      29.662  46.771  17.708  1.00  0.00           H  
ATOM   5162  N   GLU D 476      29.105  44.292  19.830  1.00 24.44           N  
ATOM   5163  CA  GLU D 476      29.349  43.291  20.870  1.00 20.80           C  
ATOM   5164  C   GLU D 476      29.501  43.926  22.251  1.00 17.12           C  
ATOM   5165  O   GLU D 476      29.029  43.382  23.249  1.00 22.35           O  
ATOM   5166  CB  GLU D 476      30.604  42.485  20.541  1.00 29.07           C  
ATOM   5167  CG  GLU D 476      30.487  41.610  19.306  1.00 34.30           C  
ATOM   5168  CD  GLU D 476      29.421  40.542  19.442  1.00 40.32           C  
ATOM   5169  OE1 GLU D 476      29.321  39.926  20.526  1.00 44.74           O  
ATOM   5170  OE2 GLU D 476      28.692  40.306  18.453  1.00 49.17           O  
ATOM   5171  H   GLU D 476      29.746  44.393  19.091  1.00  0.00           H  
ATOM   5172  N   ALA D 477      30.117  45.103  22.288  1.00 11.02           N  
ATOM   5173  CA  ALA D 477      30.248  45.878  23.512  1.00 15.54           C  
ATOM   5174  C   ALA D 477      28.890  46.360  24.027  1.00 24.12           C  
ATOM   5175  O   ALA D 477      28.623  46.315  25.236  1.00 25.08           O  
ATOM   5176  CB  ALA D 477      31.176  47.061  23.273  1.00 12.99           C  
ATOM   5177  H   ALA D 477      30.526  45.421  21.461  1.00  0.00           H  
ATOM   5178  N   ALA D 478      28.020  46.768  23.103  1.00 22.82           N  
ATOM   5179  CA  ALA D 478      26.663  47.195  23.443  1.00 16.81           C  
ATOM   5180  C   ALA D 478      25.800  46.023  23.902  1.00 18.86           C  
ATOM   5181  O   ALA D 478      25.015  46.153  24.844  1.00 28.51           O  
ATOM   5182  CB  ALA D 478      26.020  47.884  22.253  1.00 21.79           C  
ATOM   5183  H   ALA D 478      28.320  46.831  22.170  1.00  0.00           H  
ATOM   5184  N   GLU D 479      25.982  44.868  23.269  1.00 20.09           N  
ATOM   5185  CA  GLU D 479      25.316  43.637  23.695  1.00 23.88           C  
ATOM   5186  C   GLU D 479      25.726  43.209  25.102  1.00 32.07           C  
ATOM   5187  O   GLU D 479      24.889  42.764  25.891  1.00 35.56           O  
ATOM   5188  CB  GLU D 479      25.616  42.500  22.717  1.00 29.48           C  
ATOM   5189  CG  GLU D 479      24.524  42.251  21.688  1.00 39.49           C  
ATOM   5190  CD  GLU D 479      23.188  41.906  22.321  1.00 42.43           C  
ATOM   5191  OE1 GLU D 479      22.979  40.728  22.682  1.00 48.41           O  
ATOM   5192  OE2 GLU D 479      22.344  42.814  22.450  1.00 39.21           O  
ATOM   5193  H   GLU D 479      26.541  44.879  22.468  1.00  0.00           H  
ATOM   5194  N   TRP D 480      27.015  43.341  25.412  1.00 33.56           N  
ATOM   5195  CA  TRP D 480      27.528  43.030  26.748  1.00 30.17           C  
ATOM   5196  C   TRP D 480      26.809  43.846  27.826  1.00 27.60           C  
ATOM   5197  O   TRP D 480      26.294  43.288  28.799  1.00 26.33           O  
ATOM   5198  CB  TRP D 480      29.040  43.294  26.819  1.00 28.08           C  
ATOM   5199  CG  TRP D 480      29.641  42.985  28.167  1.00 14.54           C  
ATOM   5200  CD1 TRP D 480      29.746  43.837  29.236  1.00 10.87           C  
ATOM   5201  CD2 TRP D 480      30.161  41.725  28.605  1.00  8.55           C  
ATOM   5202  NE1 TRP D 480      30.286  43.177  30.310  1.00 16.66           N  
ATOM   5203  CE2 TRP D 480      30.554  41.882  29.951  1.00 16.40           C  
ATOM   5204  CE3 TRP D 480      30.336  40.479  27.990  1.00 10.77           C  
ATOM   5205  CZ2 TRP D 480      31.115  40.838  30.695  1.00 14.14           C  
ATOM   5206  CZ3 TRP D 480      30.892  39.441  28.728  1.00 10.53           C  
ATOM   5207  CH2 TRP D 480      31.275  39.629  30.068  1.00 13.43           C  
ATOM   5208  H   TRP D 480      27.633  43.608  24.694  1.00  0.00           H  
ATOM   5209  HE1 TRP D 480      30.514  43.590  31.180  1.00  0.00           H  
ATOM   5210  N   ASP D 481      26.796  45.164  27.649  1.00 19.77           N  
ATOM   5211  CA  ASP D 481      26.101  46.066  28.561  1.00 23.57           C  
ATOM   5212  C   ASP D 481      24.637  45.677  28.757  1.00 28.82           C  
ATOM   5213  O   ASP D 481      24.177  45.511  29.885  1.00 33.05           O  
ATOM   5214  CB  ASP D 481      26.188  47.503  28.039  1.00 24.57           C  
ATOM   5215  CG  ASP D 481      27.582  48.100  28.185  1.00 30.77           C  
ATOM   5216  OD1 ASP D 481      28.427  47.497  28.880  1.00 30.73           O  
ATOM   5217  OD2 ASP D 481      27.827  49.195  27.634  1.00 31.34           O  
ATOM   5218  H   ASP D 481      27.280  45.528  26.874  1.00  0.00           H  
ATOM   5219  N   ARG D 482      23.948  45.413  27.651  1.00 31.06           N  
ATOM   5220  CA  ARG D 482      22.545  45.015  27.687  1.00 26.90           C  
ATOM   5221  C   ARG D 482      22.338  43.705  28.455  1.00 23.48           C  
ATOM   5222  O   ARG D 482      21.318  43.516  29.123  1.00 31.00           O  
ATOM   5223  CB  ARG D 482      22.016  44.876  26.257  1.00 32.27           C  
ATOM   5224  CG  ARG D 482      20.497  44.884  26.145  1.00 39.55           C  
ATOM   5225  CD  ARG D 482      20.039  44.372  24.789  1.00 35.52           C  
ATOM   5226  NE  ARG D 482      20.513  43.015  24.532  1.00 40.07           N  
ATOM   5227  CZ  ARG D 482      19.860  41.908  24.873  1.00 45.13           C  
ATOM   5228  NH1 ARG D 482      18.751  41.973  25.600  1.00 47.66           N  
ATOM   5229  NH2 ARG D 482      20.344  40.726  24.522  1.00 52.23           N  
ATOM   5230  H   ARG D 482      24.393  45.539  26.784  1.00  0.00           H  
ATOM   5231  HE  ARG D 482      21.421  42.905  24.201  1.00  0.00           H  
ATOM   5232 HH11 ARG D 482      18.379  42.856  25.885  1.00  0.00           H  
ATOM   5233 HH12 ARG D 482      18.266  41.131  25.836  1.00  0.00           H  
ATOM   5234 HH21 ARG D 482      21.202  40.670  24.011  1.00  0.00           H  
ATOM   5235 HH22 ARG D 482      19.859  39.890  24.779  1.00  0.00           H  
ATOM   5236  N   LEU D 483      23.308  42.802  28.359  1.00 17.60           N  
ATOM   5237  CA  LEU D 483      23.229  41.522  29.058  1.00 15.64           C  
ATOM   5238  C   LEU D 483      23.887  41.561  30.440  1.00 20.18           C  
ATOM   5239  O   LEU D 483      23.930  40.550  31.145  1.00 25.08           O  
ATOM   5240  CB  LEU D 483      23.876  40.420  28.219  1.00 18.58           C  
ATOM   5241  CG  LEU D 483      23.309  40.159  26.824  1.00 23.04           C  
ATOM   5242  CD1 LEU D 483      24.204  39.169  26.117  1.00 28.41           C  
ATOM   5243  CD2 LEU D 483      21.889  39.626  26.910  1.00 28.05           C  
ATOM   5244  H   LEU D 483      24.040  42.991  27.735  1.00  0.00           H  
ATOM   5245  N   HIS D 484      24.448  42.709  30.807  1.00 18.62           N  
ATOM   5246  CA  HIS D 484      25.157  42.831  32.080  1.00 23.97           C  
ATOM   5247  C   HIS D 484      24.827  44.125  32.819  1.00 24.62           C  
ATOM   5248  O   HIS D 484      25.661  45.025  32.910  1.00 30.28           O  
ATOM   5249  CB  HIS D 484      26.673  42.737  31.856  1.00 20.91           C  
ATOM   5250  CG  HIS D 484      27.131  41.392  31.387  1.00 18.52           C  
ATOM   5251  ND1 HIS D 484      27.091  41.014  30.061  1.00 20.03           N  
ATOM   5252  CD2 HIS D 484      27.542  40.300  32.075  1.00 16.78           C  
ATOM   5253  CE1 HIS D 484      27.443  39.745  29.954  1.00 14.01           C  
ATOM   5254  NE2 HIS D 484      27.724  39.290  31.161  1.00 21.48           N  
ATOM   5255  H   HIS D 484      24.352  43.489  30.220  1.00  0.00           H  
ATOM   5256  HD1 HIS D 484      26.840  41.592  29.312  1.00  0.00           H  
ATOM   5257  HE2 HIS D 484      28.016  38.378  31.366  1.00  0.00           H  
ATOM   5258  N   PRO D 485      23.646  44.186  33.454  1.00 24.96           N  
ATOM   5259  CA  PRO D 485      23.277  45.355  34.262  1.00 26.78           C  
ATOM   5260  C   PRO D 485      24.215  45.600  35.456  1.00 27.78           C  
ATOM   5261  O   PRO D 485      24.648  44.668  36.141  1.00 26.48           O  
ATOM   5262  CB  PRO D 485      21.847  45.041  34.709  1.00 21.86           C  
ATOM   5263  CG  PRO D 485      21.779  43.545  34.688  1.00 29.61           C  
ATOM   5264  CD  PRO D 485      22.612  43.137  33.507  1.00 27.84           C  
ATOM   5265  N   VAL D 486      24.531  46.864  35.693  1.00 26.93           N  
ATOM   5266  CA  VAL D 486      25.471  47.224  36.743  1.00 30.46           C  
ATOM   5267  C   VAL D 486      24.822  47.374  38.117  1.00 26.95           C  
ATOM   5268  O   VAL D 486      23.722  47.906  38.247  1.00 25.91           O  
ATOM   5269  CB  VAL D 486      26.231  48.520  36.392  1.00 30.51           C  
ATOM   5270  CG1 VAL D 486      27.387  48.198  35.463  1.00 31.99           C  
ATOM   5271  CG2 VAL D 486      25.294  49.527  35.742  1.00 34.63           C  
ATOM   5272  H   VAL D 486      24.097  47.536  35.137  1.00  0.00           H  
ATOM   5273  N   HIS D 487      25.474  46.816  39.129  1.00 20.90           N  
ATOM   5274  CA  HIS D 487      25.050  47.017  40.509  1.00 19.79           C  
ATOM   5275  C   HIS D 487      25.507  48.380  41.016  1.00 20.76           C  
ATOM   5276  O   HIS D 487      26.701  48.671  41.027  1.00 23.11           O  
ATOM   5277  CB  HIS D 487      25.629  45.928  41.402  1.00 13.21           C  
ATOM   5278  CG  HIS D 487      25.203  44.548  41.020  1.00  6.04           C  
ATOM   5279  ND1 HIS D 487      24.233  43.851  41.707  1.00 14.18           N  
ATOM   5280  CD2 HIS D 487      25.627  43.727  40.032  1.00  9.79           C  
ATOM   5281  CE1 HIS D 487      24.073  42.662  41.155  1.00 16.19           C  
ATOM   5282  NE2 HIS D 487      24.908  42.561  40.138  1.00 21.50           N  
ATOM   5283  H   HIS D 487      26.290  46.333  38.902  1.00  0.00           H  
ATOM   5284  HD1 HIS D 487      23.752  44.109  42.530  1.00  0.00           H  
ATOM   5285  HE2 HIS D 487      24.972  41.791  39.540  1.00  0.00           H  
ATOM   5286  N   ALA D 488      24.551  49.227  41.382  1.00 15.78           N  
ATOM   5287  CA  ALA D 488      24.862  50.555  41.890  1.00 17.18           C  
ATOM   5288  C   ALA D 488      25.620  50.467  43.204  1.00 23.02           C  
ATOM   5289  O   ALA D 488      25.446  49.514  43.970  1.00 24.91           O  
ATOM   5290  CB  ALA D 488      23.587  51.357  42.080  1.00 18.90           C  
ATOM   5291  H   ALA D 488      23.619  48.960  41.245  1.00  0.00           H  
ATOM   5292  N   GLY D 489      26.410  51.496  43.486  1.00 25.69           N  
ATOM   5293  CA  GLY D 489      27.217  51.512  44.692  1.00 31.31           C  
ATOM   5294  C   GLY D 489      28.508  52.284  44.498  1.00 31.81           C  
ATOM   5295  O   GLY D 489      28.901  52.552  43.363  1.00 37.54           O  
ATOM   5296  H   GLY D 489      26.525  52.186  42.796  1.00  0.00           H  
ATOM   5297  N   PRO D 490      29.137  52.754  45.585  1.00 32.04           N  
ATOM   5298  CA  PRO D 490      30.546  53.153  45.508  1.00 28.96           C  
ATOM   5299  C   PRO D 490      31.501  51.960  45.523  1.00 23.69           C  
ATOM   5300  O   PRO D 490      31.248  50.953  46.176  1.00 20.56           O  
ATOM   5301  CB  PRO D 490      30.725  54.047  46.734  1.00 26.97           C  
ATOM   5302  CG  PRO D 490      29.714  53.549  47.696  1.00 27.78           C  
ATOM   5303  CD  PRO D 490      28.524  53.162  46.860  1.00 30.24           C  
ATOM   5304  N   ILE D 491      32.561  52.049  44.732  1.00 27.56           N  
ATOM   5305  CA  ILE D 491      33.602  51.028  44.747  1.00 28.52           C  
ATOM   5306  C   ILE D 491      34.564  51.278  45.911  1.00 30.66           C  
ATOM   5307  O   ILE D 491      35.002  52.410  46.134  1.00 29.83           O  
ATOM   5308  CB  ILE D 491      34.399  51.020  43.422  1.00 27.60           C  
ATOM   5309  CG1 ILE D 491      33.440  50.990  42.229  1.00 22.27           C  
ATOM   5310  CG2 ILE D 491      35.314  49.805  43.369  1.00 23.88           C  
ATOM   5311  CD1 ILE D 491      32.634  49.710  42.117  1.00 16.78           C  
ATOM   5312  H   ILE D 491      32.596  52.801  44.111  1.00  0.00           H  
ATOM   5313  N   ALA D 492      34.784  50.245  46.720  1.00 33.15           N  
ATOM   5314  CA  ALA D 492      35.736  50.315  47.829  1.00 33.93           C  
ATOM   5315  C   ALA D 492      37.177  50.235  47.326  1.00 40.99           C  
ATOM   5316  O   ALA D 492      37.441  49.659  46.266  1.00 44.91           O  
ATOM   5317  CB  ALA D 492      35.467  49.183  48.817  1.00 28.51           C  
ATOM   5318  H   ALA D 492      34.269  49.430  46.560  1.00  0.00           H  
ATOM   5319  N   PRO D 493      38.139  50.723  48.127  1.00 47.66           N  
ATOM   5320  CA  PRO D 493      39.551  50.376  47.922  1.00 50.30           C  
ATOM   5321  C   PRO D 493      39.791  48.866  47.923  1.00 53.58           C  
ATOM   5322  O   PRO D 493      39.091  48.113  48.605  1.00 54.09           O  
ATOM   5323  CB  PRO D 493      40.256  51.060  49.091  1.00 49.96           C  
ATOM   5324  CG  PRO D 493      39.364  52.196  49.438  1.00 49.39           C  
ATOM   5325  CD  PRO D 493      37.974  51.660  49.251  1.00 47.75           C  
ATOM   5326  N   GLY D 494      40.733  48.421  47.100  1.00 58.67           N  
ATOM   5327  CA  GLY D 494      41.046  47.003  47.033  1.00 63.12           C  
ATOM   5328  C   GLY D 494      40.430  46.304  45.835  1.00 61.61           C  
ATOM   5329  O   GLY D 494      41.114  45.571  45.121  1.00 65.49           O  
ATOM   5330  H   GLY D 494      41.197  49.064  46.530  1.00  0.00           H  
ATOM   5331  N   GLN D 495      39.138  46.528  45.618  0.00 60.01           N  
ATOM   5332  CA  GLN D 495      38.436  45.954  44.473  0.00 57.40           C  
ATOM   5333  C   GLN D 495      38.224  46.974  43.352  0.00 56.34           C  
ATOM   5334  O   GLN D 495      38.715  48.102  43.421  0.00 55.76           O  
ATOM   5335  CB  GLN D 495      37.085  45.381  44.912  0.00 56.42           C  
ATOM   5336  CG  GLN D 495      37.186  44.102  45.729  0.00 54.79           C  
ATOM   5337  CD  GLN D 495      36.039  43.148  45.459  0.00 54.20           C  
ATOM   5338  OE1 GLN D 495      36.190  42.170  44.728  0.00 53.25           O  
ATOM   5339  NE2 GLN D 495      34.884  43.431  46.037  0.00 54.15           N  
ATOM   5340  H   GLN D 495      38.678  47.146  46.223  1.00  0.00           H  
ATOM   5341 HE21 GLN D 495      34.158  42.820  45.815  1.00  0.00           H  
ATOM   5342 HE22 GLN D 495      34.806  44.213  46.614  1.00  0.00           H  
ATOM   5343  N   MET D 496      37.494  46.568  42.318  0.00 55.27           N  
ATOM   5344  CA  MET D 496      37.218  47.438  41.178  0.00 53.72           C  
ATOM   5345  C   MET D 496      35.774  47.300  40.684  0.00 51.92           C  
ATOM   5346  O   MET D 496      34.928  46.719  41.363  0.00 51.19           O  
ATOM   5347  CB  MET D 496      38.200  47.135  40.040  0.00 54.58           C  
ATOM   5348  CG  MET D 496      38.186  45.691  39.567  0.00 52.98           C  
ATOM   5349  SD  MET D 496      39.769  45.172  38.883  0.00 53.34           S  
ATOM   5350  CE  MET D 496      40.490  44.357  40.306  0.00 54.58           C  
ATOM   5351  H   MET D 496      37.117  45.668  42.329  1.00  0.00           H  
ATOM   5352  N   ARG D 497      35.496  47.867  39.515  1.00 51.73           N  
ATOM   5353  CA  ARG D 497      34.157  47.848  38.929  1.00 43.88           C  
ATOM   5354  C   ARG D 497      33.832  46.516  38.263  1.00 43.32           C  
ATOM   5355  O   ARG D 497      34.708  45.672  38.072  1.00 45.18           O  
ATOM   5356  CB  ARG D 497      34.035  48.958  37.885  1.00 40.92           C  
ATOM   5357  CG  ARG D 497      34.414  50.332  38.390  1.00 48.48           C  
ATOM   5358  CD  ARG D 497      34.786  51.246  37.242  1.00 45.67           C  
ATOM   5359  NE  ARG D 497      36.055  50.862  36.635  1.00 49.42           N  
ATOM   5360  CZ  ARG D 497      36.249  50.732  35.327  1.00 51.85           C  
ATOM   5361  NH1 ARG D 497      35.258  50.954  34.478  1.00 56.83           N  
ATOM   5362  NH2 ARG D 497      37.436  50.374  34.868  1.00 54.01           N  
ATOM   5363  H   ARG D 497      36.222  48.287  39.016  1.00  0.00           H  
ATOM   5364  HE  ARG D 497      36.822  50.717  37.228  1.00  0.00           H  
ATOM   5365 HH11 ARG D 497      34.347  51.206  34.801  1.00  0.00           H  
ATOM   5366 HH12 ARG D 497      35.427  50.846  33.500  1.00  0.00           H  
ATOM   5367 HH21 ARG D 497      38.167  50.205  35.527  1.00  0.00           H  
ATOM   5368 HH22 ARG D 497      37.608  50.281  33.888  1.00  0.00           H  
ATOM   5369  N   GLU D 498      32.567  46.341  37.895  1.00 42.79           N  
ATOM   5370  CA  GLU D 498      32.199  45.367  36.866  1.00 41.92           C  
ATOM   5371  C   GLU D 498      32.551  45.983  35.513  1.00 38.55           C  
ATOM   5372  O   GLU D 498      32.201  47.137  35.245  1.00 39.08           O  
ATOM   5373  CB  GLU D 498      30.698  45.076  36.901  1.00 40.18           C  
ATOM   5374  CG  GLU D 498      30.137  44.791  38.279  1.00 46.15           C  
ATOM   5375  CD  GLU D 498      28.765  45.400  38.472  1.00 47.87           C  
ATOM   5376  OE1 GLU D 498      28.689  46.584  38.863  1.00 48.40           O  
ATOM   5377  OE2 GLU D 498      27.763  44.709  38.199  1.00 47.92           O  
ATOM   5378  H   GLU D 498      31.887  46.881  38.342  1.00  0.00           H  
ATOM   5379  N   PRO D 499      33.317  45.262  34.677  1.00 32.27           N  
ATOM   5380  CA  PRO D 499      33.664  45.863  33.386  1.00 28.21           C  
ATOM   5381  C   PRO D 499      32.451  46.062  32.471  1.00 30.36           C  
ATOM   5382  O   PRO D 499      31.559  45.214  32.394  1.00 31.54           O  
ATOM   5383  CB  PRO D 499      34.661  44.874  32.796  1.00 24.25           C  
ATOM   5384  CG  PRO D 499      34.242  43.566  33.371  1.00 26.25           C  
ATOM   5385  CD  PRO D 499      33.807  43.875  34.781  1.00 28.33           C  
ATOM   5386  N   ARG D 500      32.373  47.241  31.867  1.00 28.66           N  
ATOM   5387  CA  ARG D 500      31.425  47.498  30.789  1.00 26.67           C  
ATOM   5388  C   ARG D 500      32.057  47.088  29.455  1.00 30.79           C  
ATOM   5389  O   ARG D 500      33.260  46.828  29.391  1.00 37.02           O  
ATOM   5390  CB  ARG D 500      31.065  48.988  30.759  1.00 27.05           C  
ATOM   5391  CG  ARG D 500      30.842  49.611  32.133  1.00 26.49           C  
ATOM   5392  CD  ARG D 500      29.391  49.500  32.574  1.00 31.76           C  
ATOM   5393  NE  ARG D 500      28.881  48.137  32.426  1.00 36.51           N  
ATOM   5394  CZ  ARG D 500      27.648  47.843  32.028  1.00 37.17           C  
ATOM   5395  NH1 ARG D 500      26.731  48.782  31.985  1.00 44.24           N  
ATOM   5396  NH2 ARG D 500      27.291  46.593  31.806  1.00 36.73           N  
ATOM   5397  H   ARG D 500      32.923  47.947  32.242  1.00  0.00           H  
ATOM   5398  HE  ARG D 500      29.465  47.383  32.592  1.00  0.00           H  
ATOM   5399 HH11 ARG D 500      26.367  49.025  32.833  1.00  0.00           H  
ATOM   5400 HH12 ARG D 500      26.654  49.233  31.106  1.00  0.00           H  
ATOM   5401 HH21 ARG D 500      27.990  45.916  31.931  1.00  0.00           H  
ATOM   5402 HH22 ARG D 500      26.351  46.355  31.523  1.00  0.00           H  
ATOM   5403  N   GLY D 501      31.268  47.080  28.383  1.00 31.18           N  
ATOM   5404  CA  GLY D 501      31.795  46.725  27.072  1.00 22.77           C  
ATOM   5405  C   GLY D 501      32.955  47.601  26.625  1.00 24.14           C  
ATOM   5406  O   GLY D 501      33.964  47.111  26.122  1.00 28.85           O  
ATOM   5407  H   GLY D 501      30.327  47.275  28.491  1.00  0.00           H  
ATOM   5408  N   SER D 502      32.848  48.894  26.907  1.00 24.43           N  
ATOM   5409  CA  SER D 502      33.912  49.853  26.623  1.00 23.58           C  
ATOM   5410  C   SER D 502      35.195  49.564  27.411  1.00 26.75           C  
ATOM   5411  O   SER D 502      36.288  49.962  27.006  1.00 29.26           O  
ATOM   5412  CB  SER D 502      33.421  51.263  26.948  1.00 28.85           C  
ATOM   5413  OG  SER D 502      34.349  52.242  26.523  1.00 48.22           O  
ATOM   5414  H   SER D 502      31.989  49.199  27.256  1.00  0.00           H  
ATOM   5415  HG  SER D 502      35.189  52.106  26.985  1.00  0.00           H  
ATOM   5416  N   ASP D 503      35.045  48.921  28.567  1.00 22.19           N  
ATOM   5417  CA  ASP D 503      36.180  48.507  29.388  1.00 17.04           C  
ATOM   5418  C   ASP D 503      36.845  47.261  28.818  1.00 18.02           C  
ATOM   5419  O   ASP D 503      38.071  47.164  28.776  1.00 27.99           O  
ATOM   5420  CB  ASP D 503      35.723  48.210  30.818  1.00 23.36           C  
ATOM   5421  CG  ASP D 503      35.316  49.456  31.576  1.00 22.27           C  
ATOM   5422  OD1 ASP D 503      35.979  50.500  31.419  1.00 19.86           O  
ATOM   5423  OD2 ASP D 503      34.362  49.372  32.377  1.00 25.42           O  
ATOM   5424  H   ASP D 503      34.141  48.689  28.845  1.00  0.00           H  
ATOM   5425  N   ILE D 504      36.031  46.283  28.444  1.00 12.02           N  
ATOM   5426  CA  ILE D 504      36.529  45.073  27.801  1.00 13.75           C  
ATOM   5427  C   ILE D 504      37.246  45.406  26.492  1.00 18.12           C  
ATOM   5428  O   ILE D 504      38.263  44.800  26.161  1.00 23.09           O  
ATOM   5429  CB  ILE D 504      35.374  44.092  27.524  1.00 15.84           C  
ATOM   5430  CG1 ILE D 504      34.709  43.702  28.844  1.00 12.16           C  
ATOM   5431  CG2 ILE D 504      35.886  42.848  26.796  1.00 15.39           C  
ATOM   5432  CD1 ILE D 504      33.618  42.674  28.699  1.00 15.02           C  
ATOM   5433  H   ILE D 504      35.072  46.383  28.611  1.00  0.00           H  
ATOM   5434  N   ALA D 505      36.758  46.434  25.803  1.00 18.32           N  
ATOM   5435  CA  ALA D 505      37.375  46.911  24.567  1.00 22.16           C  
ATOM   5436  C   ALA D 505      38.608  47.781  24.821  1.00 20.82           C  
ATOM   5437  O   ALA D 505      39.305  48.172  23.888  1.00 23.55           O  
ATOM   5438  CB  ALA D 505      36.350  47.683  23.743  1.00 16.99           C  
ATOM   5439  H   ALA D 505      35.901  46.802  26.088  1.00  0.00           H  
ATOM   5440  N   GLY D 506      38.837  48.127  26.083  1.00 23.55           N  
ATOM   5441  CA  GLY D 506      39.995  48.922  26.443  1.00 20.93           C  
ATOM   5442  C   GLY D 506      39.872  50.415  26.195  1.00 26.95           C  
ATOM   5443  O   GLY D 506      40.858  51.137  26.319  1.00 34.31           O  
ATOM   5444  H   GLY D 506      38.276  47.750  26.781  1.00  0.00           H  
ATOM   5445  N   THR D 507      38.678  50.906  25.884  1.00 24.36           N  
ATOM   5446  CA  THR D 507      38.528  52.333  25.588  1.00 26.84           C  
ATOM   5447  C   THR D 507      38.266  53.186  26.823  1.00 27.00           C  
ATOM   5448  O   THR D 507      38.574  54.376  26.842  1.00 22.23           O  
ATOM   5449  CB  THR D 507      37.411  52.589  24.564  1.00 29.51           C  
ATOM   5450  OG1 THR D 507      36.253  51.828  24.916  1.00 30.49           O  
ATOM   5451  CG2 THR D 507      37.875  52.183  23.173  1.00 32.30           C  
ATOM   5452  H   THR D 507      37.896  50.317  25.813  1.00  0.00           H  
ATOM   5453  HG1 THR D 507      35.456  52.377  24.859  1.00  0.00           H  
ATOM   5454  N   THR D 508      37.709  52.568  27.859  1.00 31.21           N  
ATOM   5455  CA  THR D 508      37.473  53.248  29.131  1.00 34.93           C  
ATOM   5456  C   THR D 508      38.101  52.505  30.310  1.00 40.62           C  
ATOM   5457  O   THR D 508      37.643  52.625  31.449  1.00 41.05           O  
ATOM   5458  CB  THR D 508      35.973  53.390  29.421  1.00 35.08           C  
ATOM   5459  OG1 THR D 508      35.341  52.111  29.282  1.00 34.74           O  
ATOM   5460  CG2 THR D 508      35.335  54.398  28.478  1.00 35.93           C  
ATOM   5461  H   THR D 508      37.376  51.658  27.706  1.00  0.00           H  
ATOM   5462  HG1 THR D 508      35.117  51.881  30.188  1.00  0.00           H  
ATOM   5463  N   SER D 509      39.129  51.712  30.031  1.00 38.58           N  
ATOM   5464  CA  SER D 509      39.793  50.942  31.075  1.00 38.12           C  
ATOM   5465  C   SER D 509      41.306  51.041  30.969  1.00 39.82           C  
ATOM   5466  O   SER D 509      41.870  50.909  29.883  1.00 42.07           O  
ATOM   5467  CB  SER D 509      39.378  49.475  31.001  1.00 37.94           C  
ATOM   5468  OG  SER D 509      39.950  48.847  29.868  1.00 44.47           O  
ATOM   5469  H   SER D 509      39.471  51.684  29.114  1.00  0.00           H  
ATOM   5470  HG  SER D 509      39.472  48.023  29.683  1.00  0.00           H  
ATOM   5471  N   THR D 510      41.954  51.330  32.092  1.00 39.99           N  
ATOM   5472  CA  THR D 510      43.414  51.316  32.166  1.00 36.12           C  
ATOM   5473  C   THR D 510      43.962  49.899  32.076  1.00 33.07           C  
ATOM   5474  O   THR D 510      43.296  48.934  32.460  1.00 28.61           O  
ATOM   5475  CB  THR D 510      43.936  51.928  33.484  1.00 39.74           C  
ATOM   5476  OG1 THR D 510      43.665  51.032  34.572  1.00 35.90           O  
ATOM   5477  CG2 THR D 510      43.277  53.274  33.750  1.00 44.65           C  
ATOM   5478  H   THR D 510      41.415  51.667  32.826  1.00  0.00           H  
ATOM   5479  HG1 THR D 510      42.789  51.212  34.931  1.00  0.00           H  
ATOM   5480  N   LEU D 511      45.209  49.790  31.638  1.00 36.16           N  
ATOM   5481  CA  LEU D 511      45.915  48.514  31.630  1.00 41.03           C  
ATOM   5482  C   LEU D 511      45.904  47.892  33.021  1.00 42.94           C  
ATOM   5483  O   LEU D 511      45.628  46.704  33.171  1.00 46.60           O  
ATOM   5484  CB  LEU D 511      47.356  48.721  31.165  1.00 43.89           C  
ATOM   5485  CG  LEU D 511      48.276  47.503  31.127  1.00 38.76           C  
ATOM   5486  CD1 LEU D 511      47.711  46.432  30.206  1.00 36.53           C  
ATOM   5487  CD2 LEU D 511      49.642  47.955  30.655  1.00 46.09           C  
ATOM   5488  H   LEU D 511      45.657  50.587  31.293  1.00  0.00           H  
ATOM   5489  N   GLN D 512      46.077  48.735  34.036  1.00 42.34           N  
ATOM   5490  CA  GLN D 512      46.019  48.312  35.434  1.00 42.81           C  
ATOM   5491  C   GLN D 512      44.704  47.603  35.781  1.00 43.85           C  
ATOM   5492  O   GLN D 512      44.704  46.556  36.439  1.00 42.21           O  
ATOM   5493  CB  GLN D 512      46.207  49.521  36.357  1.00 47.09           C  
ATOM   5494  CG  GLN D 512      47.541  50.238  36.199  0.00 40.29           C  
ATOM   5495  CD  GLN D 512      47.437  51.483  35.339  0.00 39.26           C  
ATOM   5496  OE1 GLN D 512      47.124  51.409  34.153  0.00 36.47           O  
ATOM   5497  NE2 GLN D 512      47.685  52.636  35.937  0.00 38.62           N  
ATOM   5498  H   GLN D 512      46.278  49.667  33.812  1.00  0.00           H  
ATOM   5499 HE21 GLN D 512      47.625  53.422  35.361  1.00  0.00           H  
ATOM   5500 HE22 GLN D 512      47.918  52.659  36.884  1.00  0.00           H  
ATOM   5501  N   GLU D 513      43.594  48.147  35.285  1.00 39.92           N  
ATOM   5502  CA  GLU D 513      42.272  47.579  35.544  1.00 35.55           C  
ATOM   5503  C   GLU D 513      42.039  46.284  34.778  1.00 30.81           C  
ATOM   5504  O   GLU D 513      41.504  45.318  35.323  1.00 30.80           O  
ATOM   5505  CB  GLU D 513      41.181  48.588  35.190  1.00 43.79           C  
ATOM   5506  CG  GLU D 513      41.040  49.712  36.201  1.00 46.44           C  
ATOM   5507  CD  GLU D 513      40.250  50.893  35.671  1.00 53.31           C  
ATOM   5508  OE1 GLU D 513      40.323  51.175  34.456  1.00 46.61           O  
ATOM   5509  OE2 GLU D 513      39.555  51.547  36.479  1.00 60.99           O  
ATOM   5510  H   GLU D 513      43.696  48.956  34.740  1.00  0.00           H  
ATOM   5511  N   GLN D 514      42.481  46.253  33.526  1.00 28.85           N  
ATOM   5512  CA  GLN D 514      42.380  45.045  32.709  1.00 28.30           C  
ATOM   5513  C   GLN D 514      43.172  43.901  33.337  1.00 28.66           C  
ATOM   5514  O   GLN D 514      42.676  42.778  33.450  1.00 30.08           O  
ATOM   5515  CB  GLN D 514      42.899  45.319  31.295  1.00 28.61           C  
ATOM   5516  CG  GLN D 514      42.141  46.407  30.545  1.00 17.15           C  
ATOM   5517  CD  GLN D 514      42.943  46.986  29.394  1.00 14.82           C  
ATOM   5518  OE1 GLN D 514      43.752  46.297  28.778  1.00 21.22           O  
ATOM   5519  NE2 GLN D 514      42.723  48.254  29.099  1.00 10.65           N  
ATOM   5520  H   GLN D 514      42.873  47.072  33.155  1.00  0.00           H  
ATOM   5521 HE21 GLN D 514      43.286  48.584  28.370  1.00  0.00           H  
ATOM   5522 HE22 GLN D 514      42.051  48.773  29.584  1.00  0.00           H  
ATOM   5523  N   ILE D 515      44.387  44.209  33.787  1.00 33.52           N  
ATOM   5524  CA  ILE D 515      45.212  43.249  34.520  1.00 38.56           C  
ATOM   5525  C   ILE D 515      44.492  42.778  35.785  1.00 39.51           C  
ATOM   5526  O   ILE D 515      44.414  41.581  36.045  1.00 39.85           O  
ATOM   5527  CB  ILE D 515      46.587  43.862  34.911  1.00 41.23           C  
ATOM   5528  CG1 ILE D 515      47.377  44.228  33.652  1.00 38.94           C  
ATOM   5529  CG2 ILE D 515      47.398  42.865  35.736  1.00 36.18           C  
ATOM   5530  CD1 ILE D 515      48.428  45.289  33.877  1.00 32.56           C  
ATOM   5531  H   ILE D 515      44.734  45.102  33.598  1.00  0.00           H  
ATOM   5532  N   GLY D 516      43.855  43.712  36.485  1.00 38.11           N  
ATOM   5533  CA  GLY D 516      43.056  43.361  37.650  1.00 39.41           C  
ATOM   5534  C   GLY D 516      41.893  42.413  37.395  1.00 37.97           C  
ATOM   5535  O   GLY D 516      41.658  41.487  38.176  1.00 38.30           O  
ATOM   5536  H   GLY D 516      43.985  44.654  36.252  1.00  0.00           H  
ATOM   5537  N   TRP D 517      41.141  42.660  36.325  1.00 39.26           N  
ATOM   5538  CA  TRP D 517      40.028  41.785  35.947  1.00 38.42           C  
ATOM   5539  C   TRP D 517      40.522  40.404  35.518  1.00 41.68           C  
ATOM   5540  O   TRP D 517      39.931  39.378  35.878  1.00 42.41           O  
ATOM   5541  CB  TRP D 517      39.206  42.417  34.814  1.00 30.27           C  
ATOM   5542  CG  TRP D 517      38.352  43.566  35.255  1.00 23.04           C  
ATOM   5543  CD1 TRP D 517      37.592  43.633  36.389  1.00 26.34           C  
ATOM   5544  CD2 TRP D 517      38.214  44.837  34.605  1.00 20.04           C  
ATOM   5545  NE1 TRP D 517      37.003  44.870  36.493  1.00 22.00           N  
ATOM   5546  CE2 TRP D 517      37.367  45.630  35.414  1.00 21.12           C  
ATOM   5547  CE3 TRP D 517      38.720  45.383  33.418  1.00 21.64           C  
ATOM   5548  CZ2 TRP D 517      37.018  46.941  35.075  1.00 20.23           C  
ATOM   5549  CZ3 TRP D 517      38.372  46.689  33.080  1.00 18.40           C  
ATOM   5550  CH2 TRP D 517      37.529  47.451  33.908  1.00 24.09           C  
ATOM   5551  H   TRP D 517      41.332  43.469  35.810  1.00  0.00           H  
ATOM   5552  HE1 TRP D 517      36.374  45.128  37.207  1.00  0.00           H  
ATOM   5553  N   MET D 518      41.636  40.386  34.789  1.00 43.33           N  
ATOM   5554  CA  MET D 518      42.241  39.143  34.314  1.00 46.45           C  
ATOM   5555  C   MET D 518      42.853  38.315  35.443  1.00 47.51           C  
ATOM   5556  O   MET D 518      42.582  37.119  35.563  1.00 46.39           O  
ATOM   5557  CB  MET D 518      43.308  39.448  33.261  1.00 45.83           C  
ATOM   5558  CG  MET D 518      42.737  39.800  31.898  1.00 46.53           C  
ATOM   5559  SD  MET D 518      44.003  40.125  30.659  1.00 37.22           S  
ATOM   5560  CE  MET D 518      43.892  41.848  30.567  1.00 44.55           C  
ATOM   5561  H   MET D 518      42.050  41.249  34.575  1.00  0.00           H  
ATOM   5562  N   THR D 519      43.639  38.969  36.295  1.00 51.15           N  
ATOM   5563  CA  THR D 519      44.258  38.321  37.451  1.00 55.22           C  
ATOM   5564  C   THR D 519      43.304  38.290  38.649  1.00 59.53           C  
ATOM   5565  O   THR D 519      43.547  38.927  39.679  1.00 58.74           O  
ATOM   5566  CB  THR D 519      45.564  39.041  37.870  1.00 57.54           C  
ATOM   5567  OG1 THR D 519      45.272  40.383  38.276  1.00 57.28           O  
ATOM   5568  CG2 THR D 519      46.551  39.073  36.710  1.00 53.48           C  
ATOM   5569  H   THR D 519      43.741  39.927  36.177  1.00  0.00           H  
ATOM   5570  HG1 THR D 519      44.665  40.378  39.030  1.00  0.00           H  
ATOM   5571  N   HIS D 520      42.206  37.555  38.498  1.00 60.67           N  
ATOM   5572  CA  HIS D 520      41.176  37.482  39.530  1.00 59.54           C  
ATOM   5573  C   HIS D 520      40.689  36.047  39.717  1.00 57.83           C  
ATOM   5574  O   HIS D 520      40.555  35.300  38.755  1.00 52.33           O  
ATOM   5575  CB  HIS D 520      39.995  38.387  39.158  1.00 63.89           C  
ATOM   5576  CG  HIS D 520      39.063  38.667  40.296  1.00 68.64           C  
ATOM   5577  ND1 HIS D 520      37.922  37.928  40.525  1.00 70.53           N  
ATOM   5578  CD2 HIS D 520      39.110  39.598  41.279  1.00 73.11           C  
ATOM   5579  CE1 HIS D 520      37.311  38.384  41.604  1.00 74.01           C  
ATOM   5580  NE2 HIS D 520      38.010  39.398  42.079  1.00 75.28           N  
ATOM   5581  H   HIS D 520      42.101  37.087  37.637  1.00  0.00           H  
ATOM   5582  HD1 HIS D 520      37.468  37.328  39.905  1.00  0.00           H  
ATOM   5583  HE2 HIS D 520      37.776  39.909  42.887  1.00  0.00           H  
ATOM   5584  N   ASN D 521      40.461  35.653  40.965  1.00 60.43           N  
ATOM   5585  CA  ASN D 521      39.872  34.347  41.249  1.00 62.28           C  
ATOM   5586  C   ASN D 521      38.423  34.515  41.711  1.00 61.05           C  
ATOM   5587  O   ASN D 521      38.152  35.286  42.634  1.00 58.17           O  
ATOM   5588  CB  ASN D 521      40.691  33.613  42.317  1.00 65.61           C  
ATOM   5589  CG  ASN D 521      40.611  32.099  42.179  1.00 69.18           C  
ATOM   5590  OD1 ASN D 521      39.568  31.498  42.420  1.00 72.64           O  
ATOM   5591  ND2 ASN D 521      41.709  31.481  41.776  1.00 66.48           N  
ATOM   5592  H   ASN D 521      40.756  36.219  41.705  1.00  0.00           H  
ATOM   5593 HD21 ASN D 521      41.586  30.515  41.689  1.00  0.00           H  
ATOM   5594 HD22 ASN D 521      42.531  31.964  41.584  1.00  0.00           H  
ATOM   5595  N   PRO D 522      37.468  33.991  40.922  1.00 60.99           N  
ATOM   5596  CA  PRO D 522      37.621  33.703  39.489  1.00 57.90           C  
ATOM   5597  C   PRO D 522      37.428  34.953  38.620  1.00 56.91           C  
ATOM   5598  O   PRO D 522      36.795  35.923  39.047  1.00 53.26           O  
ATOM   5599  CB  PRO D 522      36.543  32.656  39.230  1.00 57.11           C  
ATOM   5600  CG  PRO D 522      35.454  33.034  40.180  1.00 60.59           C  
ATOM   5601  CD  PRO D 522      36.144  33.577  41.419  1.00 63.53           C  
ATOM   5602  N   PRO D 523      38.082  34.995  37.447  1.00 56.63           N  
ATOM   5603  CA  PRO D 523      38.410  36.268  36.797  1.00 53.39           C  
ATOM   5604  C   PRO D 523      37.285  36.812  35.923  1.00 50.92           C  
ATOM   5605  O   PRO D 523      36.304  36.119  35.641  1.00 52.85           O  
ATOM   5606  CB  PRO D 523      39.630  35.917  35.957  1.00 51.57           C  
ATOM   5607  CG  PRO D 523      39.348  34.511  35.522  1.00 50.57           C  
ATOM   5608  CD  PRO D 523      38.619  33.850  36.686  1.00 57.51           C  
ATOM   5609  N   ILE D 524      37.434  38.060  35.497  1.00 43.32           N  
ATOM   5610  CA  ILE D 524      36.740  38.527  34.308  1.00 36.34           C  
ATOM   5611  C   ILE D 524      37.755  38.570  33.165  1.00 26.69           C  
ATOM   5612  O   ILE D 524      38.594  39.467  33.095  1.00 29.42           O  
ATOM   5613  CB  ILE D 524      36.117  39.929  34.506  1.00 36.08           C  
ATOM   5614  CG1 ILE D 524      35.117  39.909  35.665  1.00 36.49           C  
ATOM   5615  CG2 ILE D 524      35.393  40.353  33.239  1.00 35.67           C  
ATOM   5616  CD1 ILE D 524      35.696  40.361  36.984  1.00 43.80           C  
ATOM   5617  H   ILE D 524      38.083  38.643  35.943  1.00  0.00           H  
ATOM   5618  N   PRO D 525      37.764  37.531  32.324  1.00 16.11           N  
ATOM   5619  CA  PRO D 525      38.752  37.354  31.254  1.00 19.42           C  
ATOM   5620  C   PRO D 525      38.555  38.351  30.108  1.00 18.61           C  
ATOM   5621  O   PRO D 525      38.286  37.964  28.969  1.00 22.67           O  
ATOM   5622  CB  PRO D 525      38.533  35.906  30.793  1.00 17.81           C  
ATOM   5623  CG  PRO D 525      37.354  35.379  31.604  1.00 15.16           C  
ATOM   5624  CD  PRO D 525      36.669  36.559  32.205  1.00 15.57           C  
ATOM   5625  N   VAL D 526      38.741  39.632  30.408  1.00 16.10           N  
ATOM   5626  CA  VAL D 526      38.473  40.701  29.453  1.00 16.09           C  
ATOM   5627  C   VAL D 526      39.298  40.594  28.167  1.00 19.16           C  
ATOM   5628  O   VAL D 526      38.831  40.966  27.090  1.00 18.09           O  
ATOM   5629  CB  VAL D 526      38.700  42.092  30.094  1.00 23.32           C  
ATOM   5630  CG1 VAL D 526      37.679  42.324  31.202  1.00 19.72           C  
ATOM   5631  CG2 VAL D 526      40.119  42.207  30.641  1.00 18.96           C  
ATOM   5632  H   VAL D 526      39.054  39.848  31.310  1.00  0.00           H  
ATOM   5633  N   GLY D 527      40.476  39.987  28.268  1.00 19.48           N  
ATOM   5634  CA  GLY D 527      41.294  39.763  27.089  1.00 15.31           C  
ATOM   5635  C   GLY D 527      40.684  38.726  26.165  1.00 16.85           C  
ATOM   5636  O   GLY D 527      40.543  38.955  24.963  1.00 21.08           O  
ATOM   5637  H   GLY D 527      40.782  39.671  29.140  1.00  0.00           H  
ATOM   5638  N   GLU D 528      40.208  37.633  26.751  1.00 13.42           N  
ATOM   5639  CA  GLU D 528      39.617  36.545  25.980  1.00 17.79           C  
ATOM   5640  C   GLU D 528      38.234  36.909  25.419  1.00 21.04           C  
ATOM   5641  O   GLU D 528      37.882  36.510  24.308  1.00 21.21           O  
ATOM   5642  CB  GLU D 528      39.531  35.277  26.836  1.00 14.08           C  
ATOM   5643  CG  GLU D 528      40.879  34.769  27.340  0.00 14.02           C  
ATOM   5644  CD  GLU D 528      41.900  34.594  26.228  0.00 13.08           C  
ATOM   5645  OE1 GLU D 528      41.762  33.641  25.432  0.00 12.70           O  
ATOM   5646  OE2 GLU D 528      42.846  35.407  26.156  0.00 13.34           O  
ATOM   5647  H   GLU D 528      40.191  37.611  27.730  1.00  0.00           H  
ATOM   5648  N   ILE D 529      37.483  37.714  26.165  1.00 19.34           N  
ATOM   5649  CA  ILE D 529      36.176  38.195  25.719  1.00 19.03           C  
ATOM   5650  C   ILE D 529      36.321  39.155  24.539  1.00 16.57           C  
ATOM   5651  O   ILE D 529      35.739  38.934  23.479  1.00 16.21           O  
ATOM   5652  CB  ILE D 529      35.416  38.906  26.876  1.00 22.86           C  
ATOM   5653  CG1 ILE D 529      35.119  37.905  28.000  1.00 19.20           C  
ATOM   5654  CG2 ILE D 529      34.112  39.521  26.363  1.00 15.25           C  
ATOM   5655  CD1 ILE D 529      34.728  38.553  29.315  1.00 11.57           C  
ATOM   5656  H   ILE D 529      37.817  37.952  27.055  1.00  0.00           H  
ATOM   5657  N   TYR D 530      37.169  40.169  24.695  1.00 17.80           N  
ATOM   5658  CA  TYR D 530      37.441  41.119  23.618  1.00 12.47           C  
ATOM   5659  C   TYR D 530      37.972  40.429  22.361  1.00 17.32           C  
ATOM   5660  O   TYR D 530      37.519  40.722  21.252  1.00 22.05           O  
ATOM   5661  CB  TYR D 530      38.435  42.182  24.084  1.00 10.33           C  
ATOM   5662  CG  TYR D 530      38.631  43.327  23.112  1.00 10.08           C  
ATOM   5663  CD1 TYR D 530      37.632  43.682  22.211  1.00 12.09           C  
ATOM   5664  CD2 TYR D 530      39.810  44.076  23.116  1.00 11.82           C  
ATOM   5665  CE1 TYR D 530      37.796  44.750  21.343  1.00 13.74           C  
ATOM   5666  CE2 TYR D 530      39.987  45.152  22.247  1.00 12.47           C  
ATOM   5667  CZ  TYR D 530      38.972  45.481  21.365  1.00 21.57           C  
ATOM   5668  OH  TYR D 530      39.111  46.545  20.506  1.00 24.95           O  
ATOM   5669  H   TYR D 530      37.607  40.300  25.564  1.00  0.00           H  
ATOM   5670  HH  TYR D 530      39.909  47.023  20.714  1.00  0.00           H  
ATOM   5671  N   LYS D 531      38.882  39.475  22.537  1.00 15.17           N  
ATOM   5672  CA  LYS D 531      39.430  38.735  21.404  1.00 17.85           C  
ATOM   5673  C   LYS D 531      38.333  38.041  20.590  1.00 20.82           C  
ATOM   5674  O   LYS D 531      38.347  38.086  19.360  1.00 21.35           O  
ATOM   5675  CB  LYS D 531      40.457  37.705  21.878  1.00 15.79           C  
ATOM   5676  CG  LYS D 531      41.222  37.049  20.739  1.00 19.29           C  
ATOM   5677  CD  LYS D 531      41.894  35.760  21.170  1.00 25.51           C  
ATOM   5678  CE  LYS D 531      43.158  36.024  21.974  1.00 31.68           C  
ATOM   5679  NZ  LYS D 531      43.975  34.783  22.110  1.00 39.16           N  
ATOM   5680  H   LYS D 531      39.239  39.323  23.440  1.00  0.00           H  
ATOM   5681  HZ1 LYS D 531      44.184  34.385  21.173  1.00  0.00           H  
ATOM   5682  HZ2 LYS D 531      44.859  35.002  22.608  1.00  0.00           H  
ATOM   5683  HZ3 LYS D 531      43.429  34.089  22.664  1.00  0.00           H  
ATOM   5684  N   ARG D 532      37.332  37.497  21.280  1.00 23.47           N  
ATOM   5685  CA  ARG D 532      36.171  36.883  20.624  1.00 19.58           C  
ATOM   5686  C   ARG D 532      35.379  37.876  19.778  1.00 16.00           C  
ATOM   5687  O   ARG D 532      34.967  37.559  18.666  1.00 23.97           O  
ATOM   5688  CB  ARG D 532      35.235  36.252  21.659  1.00 22.92           C  
ATOM   5689  CG  ARG D 532      35.751  34.954  22.261  1.00 30.64           C  
ATOM   5690  CD  ARG D 532      34.621  34.122  22.851  1.00 35.18           C  
ATOM   5691  NE  ARG D 532      33.940  34.803  23.952  1.00 37.01           N  
ATOM   5692  CZ  ARG D 532      34.117  34.511  25.237  1.00 36.62           C  
ATOM   5693  NH1 ARG D 532      34.960  33.550  25.598  1.00 31.49           N  
ATOM   5694  NH2 ARG D 532      33.451  35.184  26.164  1.00 36.04           N  
ATOM   5695  H   ARG D 532      37.397  37.486  22.261  1.00  0.00           H  
ATOM   5696  HE  ARG D 532      33.310  35.519  23.731  1.00  0.00           H  
ATOM   5697 HH11 ARG D 532      35.477  33.039  24.913  1.00  0.00           H  
ATOM   5698 HH12 ARG D 532      35.088  33.349  26.570  1.00  0.00           H  
ATOM   5699 HH21 ARG D 532      32.819  35.909  25.890  1.00  0.00           H  
ATOM   5700 HH22 ARG D 532      33.582  34.975  27.134  1.00  0.00           H  
ATOM   5701  N   TRP D 533      35.214  39.092  20.284  1.00 15.14           N  
ATOM   5702  CA  TRP D 533      34.565  40.163  19.526  1.00 19.34           C  
ATOM   5703  C   TRP D 533      35.369  40.534  18.274  1.00 24.09           C  
ATOM   5704  O   TRP D 533      34.800  40.825  17.220  1.00 25.78           O  
ATOM   5705  CB  TRP D 533      34.393  41.411  20.400  1.00  9.68           C  
ATOM   5706  CG  TRP D 533      33.612  41.183  21.655  1.00  6.18           C  
ATOM   5707  CD1 TRP D 533      32.935  40.048  22.009  1.00  3.23           C  
ATOM   5708  CD2 TRP D 533      33.398  42.124  22.710  1.00  4.96           C  
ATOM   5709  NE1 TRP D 533      32.315  40.231  23.221  1.00 12.83           N  
ATOM   5710  CE2 TRP D 533      32.576  41.497  23.671  1.00  2.84           C  
ATOM   5711  CE3 TRP D 533      33.822  43.442  22.937  1.00 10.86           C  
ATOM   5712  CZ2 TRP D 533      32.164  42.139  24.839  1.00  2.01           C  
ATOM   5713  CZ3 TRP D 533      33.415  44.079  24.098  1.00 13.67           C  
ATOM   5714  CH2 TRP D 533      32.591  43.424  25.036  1.00 14.69           C  
ATOM   5715  H   TRP D 533      35.531  39.252  21.201  1.00  0.00           H  
ATOM   5716  HE1 TRP D 533      31.836  39.538  23.727  1.00  0.00           H  
ATOM   5717  N   ILE D 534      36.694  40.519  18.401  1.00 23.11           N  
ATOM   5718  CA  ILE D 534      37.587  40.794  17.275  1.00 21.13           C  
ATOM   5719  C   ILE D 534      37.561  39.668  16.239  1.00 17.06           C  
ATOM   5720  O   ILE D 534      37.528  39.925  15.038  1.00 21.19           O  
ATOM   5721  CB  ILE D 534      39.053  41.022  17.755  1.00 17.81           C  
ATOM   5722  CG1 ILE D 534      39.129  42.273  18.631  1.00 14.83           C  
ATOM   5723  CG2 ILE D 534      39.982  41.205  16.564  1.00  3.78           C  
ATOM   5724  CD1 ILE D 534      40.491  42.516  19.238  1.00 17.63           C  
ATOM   5725  H   ILE D 534      37.062  40.370  19.299  1.00  0.00           H  
ATOM   5726  N   ILE D 535      37.499  38.426  16.707  1.00 15.80           N  
ATOM   5727  CA  ILE D 535      37.443  37.267  15.815  1.00 20.96           C  
ATOM   5728  C   ILE D 535      36.142  37.227  15.005  1.00 22.86           C  
ATOM   5729  O   ILE D 535      36.149  36.848  13.834  1.00 25.91           O  
ATOM   5730  CB  ILE D 535      37.604  35.939  16.609  1.00 21.28           C  
ATOM   5731  CG1 ILE D 535      38.993  35.879  17.258  1.00 20.55           C  
ATOM   5732  CG2 ILE D 535      37.403  34.735  15.693  1.00 10.14           C  
ATOM   5733  CD1 ILE D 535      40.145  35.852  16.281  1.00 21.35           C  
ATOM   5734  H   ILE D 535      37.528  38.300  17.677  1.00  0.00           H  
ATOM   5735  N   LEU D 536      35.045  37.679  15.608  1.00 19.31           N  
ATOM   5736  CA  LEU D 536      33.764  37.785  14.907  1.00 20.09           C  
ATOM   5737  C   LEU D 536      33.780  38.880  13.837  1.00 20.27           C  
ATOM   5738  O   LEU D 536      33.299  38.676  12.722  1.00 28.15           O  
ATOM   5739  CB  LEU D 536      32.634  38.065  15.900  1.00 20.65           C  
ATOM   5740  CG  LEU D 536      32.152  36.897  16.758  1.00 17.91           C  
ATOM   5741  CD1 LEU D 536      31.219  37.433  17.834  1.00 25.08           C  
ATOM   5742  CD2 LEU D 536      31.457  35.853  15.898  1.00  8.71           C  
ATOM   5743  H   LEU D 536      35.099  37.877  16.571  1.00  0.00           H  
ATOM   5744  N   GLY D 537      34.334  40.037  14.181  1.00 18.43           N  
ATOM   5745  CA  GLY D 537      34.538  41.088  13.199  1.00 17.70           C  
ATOM   5746  C   GLY D 537      35.461  40.691  12.059  1.00 18.59           C  
ATOM   5747  O   GLY D 537      35.222  41.050  10.904  1.00 18.69           O  
ATOM   5748  H   GLY D 537      34.556  40.202  15.127  1.00  0.00           H  
ATOM   5749  N   LEU D 538      36.516  39.948  12.383  1.00 19.18           N  
ATOM   5750  CA  LEU D 538      37.428  39.410  11.376  1.00 16.79           C  
ATOM   5751  C   LEU D 538      36.694  38.493  10.406  1.00 19.09           C  
ATOM   5752  O   LEU D 538      36.807  38.660   9.200  1.00 24.11           O  
ATOM   5753  CB  LEU D 538      38.576  38.634  12.034  1.00 13.04           C  
ATOM   5754  CG  LEU D 538      39.693  39.400  12.750  1.00  9.64           C  
ATOM   5755  CD1 LEU D 538      40.791  38.428  13.121  1.00 10.61           C  
ATOM   5756  CD2 LEU D 538      40.246  40.494  11.869  1.00 10.55           C  
ATOM   5757  H   LEU D 538      36.713  39.835  13.334  1.00  0.00           H  
ATOM   5758  N   ASN D 539      35.912  37.554  10.934  1.00 19.17           N  
ATOM   5759  CA  ASN D 539      35.137  36.639  10.092  1.00 22.83           C  
ATOM   5760  C   ASN D 539      34.240  37.381   9.095  1.00 21.79           C  
ATOM   5761  O   ASN D 539      34.269  37.094   7.898  1.00 24.14           O  
ATOM   5762  CB  ASN D 539      34.294  35.702  10.961  1.00 22.30           C  
ATOM   5763  CG  ASN D 539      35.024  34.418  11.314  1.00 24.85           C  
ATOM   5764  OD1 ASN D 539      34.987  33.445  10.569  1.00 34.40           O  
ATOM   5765  ND2 ASN D 539      35.692  34.412  12.451  1.00 32.71           N  
ATOM   5766  H   ASN D 539      35.889  37.475  11.910  1.00  0.00           H  
ATOM   5767 HD21 ASN D 539      36.146  33.569  12.629  1.00  0.00           H  
ATOM   5768 HD22 ASN D 539      35.692  35.200  13.023  1.00  0.00           H  
ATOM   5769  N   LYS D 540      33.581  38.434   9.576  1.00 20.17           N  
ATOM   5770  CA  LYS D 540      32.768  39.326   8.744  1.00 18.60           C  
ATOM   5771  C   LYS D 540      33.545  39.986   7.595  1.00 26.89           C  
ATOM   5772  O   LYS D 540      33.110  39.951   6.441  1.00 30.15           O  
ATOM   5773  CB  LYS D 540      32.141  40.409   9.627  1.00 21.82           C  
ATOM   5774  CG  LYS D 540      31.243  41.403   8.908  0.00 21.45           C  
ATOM   5775  CD  LYS D 540      30.804  42.501   9.864  0.00 21.56           C  
ATOM   5776  CE  LYS D 540      29.950  43.549   9.174  0.00 21.90           C  
ATOM   5777  NZ  LYS D 540      29.633  44.678  10.094  0.00 20.40           N  
ATOM   5778  H   LYS D 540      33.594  38.568  10.547  1.00  0.00           H  
ATOM   5779  HZ1 LYS D 540      29.125  44.313  10.925  1.00  0.00           H  
ATOM   5780  HZ2 LYS D 540      30.516  45.130  10.406  1.00  0.00           H  
ATOM   5781  HZ3 LYS D 540      29.040  45.379   9.605  1.00  0.00           H  
ATOM   5782  N   ILE D 541      34.679  40.611   7.907  1.00 30.95           N  
ATOM   5783  CA  ILE D 541      35.487  41.262   6.873  1.00 33.96           C  
ATOM   5784  C   ILE D 541      36.294  40.270   6.027  1.00 37.46           C  
ATOM   5785  O   ILE D 541      36.566  40.523   4.857  1.00 38.13           O  
ATOM   5786  CB  ILE D 541      36.436  42.339   7.471  1.00 35.11           C  
ATOM   5787  CG1 ILE D 541      37.494  41.702   8.373  1.00 40.82           C  
ATOM   5788  CG2 ILE D 541      35.634  43.363   8.257  1.00 30.45           C  
ATOM   5789  CD1 ILE D 541      38.453  42.718   8.993  1.00 34.31           C  
ATOM   5790  H   ILE D 541      34.937  40.667   8.855  1.00  0.00           H  
ATOM   5791  N   VAL D 542      36.501  39.077   6.571  1.00 43.13           N  
ATOM   5792  CA  VAL D 542      37.162  37.983   5.863  1.00 41.15           C  
ATOM   5793  C   VAL D 542      36.246  37.370   4.795  1.00 46.74           C  
ATOM   5794  O   VAL D 542      36.723  36.790   3.819  1.00 49.85           O  
ATOM   5795  CB  VAL D 542      37.628  36.888   6.874  1.00 41.92           C  
ATOM   5796  CG1 VAL D 542      37.804  35.549   6.197  1.00 32.24           C  
ATOM   5797  CG2 VAL D 542      38.933  37.311   7.528  1.00 36.25           C  
ATOM   5798  H   VAL D 542      36.192  38.934   7.483  1.00  0.00           H  
ATOM   5799  N   ARG D 543      34.933  37.470   4.999  1.00 45.28           N  
ATOM   5800  CA  ARG D 543      33.977  37.037   3.983  1.00 46.56           C  
ATOM   5801  C   ARG D 543      33.595  38.165   3.024  1.00 50.97           C  
ATOM   5802  O   ARG D 543      32.956  37.926   2.001  1.00 59.34           O  
ATOM   5803  CB  ARG D 543      32.717  36.454   4.634  1.00 41.64           C  
ATOM   5804  CG  ARG D 543      31.711  37.489   5.101  1.00 52.92           C  
ATOM   5805  CD  ARG D 543      30.283  36.971   5.002  1.00 55.10           C  
ATOM   5806  NE  ARG D 543      29.311  37.945   5.500  1.00 54.23           N  
ATOM   5807  CZ  ARG D 543      29.034  38.144   6.787  1.00 52.26           C  
ATOM   5808  NH1 ARG D 543      29.611  37.404   7.724  1.00 49.59           N  
ATOM   5809  NH2 ARG D 543      28.158  39.076   7.137  1.00 55.22           N  
ATOM   5810  H   ARG D 543      34.622  37.712   5.896  1.00  0.00           H  
ATOM   5811  HE  ARG D 543      28.815  38.473   4.841  1.00  0.00           H  
ATOM   5812 HH11 ARG D 543      30.277  36.707   7.475  1.00  0.00           H  
ATOM   5813 HH12 ARG D 543      29.405  37.575   8.688  1.00  0.00           H  
ATOM   5814 HH21 ARG D 543      27.698  39.615   6.431  1.00  0.00           H  
ATOM   5815 HH22 ARG D 543      27.950  39.233   8.102  1.00  0.00           H  
ATOM   5816  N   MET D 544      33.905  39.401   3.403  1.00 53.50           N  
ATOM   5817  CA  MET D 544      33.690  40.551   2.524  1.00 54.92           C  
ATOM   5818  C   MET D 544      34.776  40.648   1.446  1.00 55.59           C  
ATOM   5819  O   MET D 544      34.533  41.165   0.351  1.00 53.73           O  
ATOM   5820  CB  MET D 544      33.660  41.842   3.347  1.00 59.24           C  
ATOM   5821  CG  MET D 544      33.516  43.117   2.526  1.00 64.01           C  
ATOM   5822  SD  MET D 544      31.902  43.284   1.740  1.00 78.66           S  
ATOM   5823  CE  MET D 544      31.001  44.193   3.005  1.00 67.39           C  
ATOM   5824  H   MET D 544      34.308  39.515   4.285  1.00  0.00           H  
ATOM   5825  N   TYR D 545      35.975  40.180   1.780  1.00 51.40           N  
ATOM   5826  CA  TYR D 545      37.113  40.237   0.872  1.00 48.10           C  
ATOM   5827  C   TYR D 545      37.618  38.844   0.477  1.00 49.18           C  
ATOM   5828  O   TYR D 545      38.650  38.772  -0.225  1.00 48.69           O  
ATOM   5829  CB  TYR D 545      38.249  41.040   1.513  1.00 46.38           C  
ATOM   5830  CG  TYR D 545      37.908  42.489   1.790  1.00 43.56           C  
ATOM   5831  CD1 TYR D 545      37.241  42.857   2.958  1.00 41.03           C  
ATOM   5832  CD2 TYR D 545      38.291  43.497   0.905  1.00 41.63           C  
ATOM   5833  CE1 TYR D 545      36.967  44.192   3.243  1.00 40.07           C  
ATOM   5834  CE2 TYR D 545      38.022  44.834   1.179  1.00 43.48           C  
ATOM   5835  CZ  TYR D 545      37.363  45.174   2.352  1.00 45.29           C  
ATOM   5836  OH  TYR D 545      37.123  46.498   2.642  1.00 48.17           O  
ATOM   5837  OXT TYR D 545      36.966  37.840   0.838  1.00 50.42           O  
ATOM   5838  H   TYR D 545      36.111  39.676   2.602  1.00  0.00           H  
ATOM   5839  HH  TYR D 545      37.250  46.998   1.832  1.00  0.00           H  
TER    5840      TYR D 545                                                      
HETATM 5841  O   HOH A1010       6.337  61.107  58.214  1.00 16.34           O  
HETATM 5842  H1  HOH A1010       6.284  61.770  58.915  1.00  0.00           H  
HETATM 5843  H2  HOH A1010       5.420  60.846  58.099  1.00  0.00           H  
HETATM 5844  O   HOH A1011      17.898  61.373  46.581  1.00 17.26           O  
HETATM 5845  H1  HOH A1011      18.127  62.138  47.113  1.00  0.00           H  
HETATM 5846  H2  HOH A1011      18.629  60.768  46.738  1.00  0.00           H  
HETATM 5847  O   HOH A1012       7.450  55.459  55.343  1.00  7.69           O  
HETATM 5848  H1  HOH A1012       7.995  56.219  55.081  1.00  0.00           H  
HETATM 5849  H2  HOH A1012       7.419  55.621  56.294  1.00  0.00           H  
HETATM 5850  O   HOH A1013      21.875  64.379  42.316  1.00 10.51           O  
HETATM 5851  H1  HOH A1013      21.338  64.397  41.509  1.00  0.00           H  
HETATM 5852  H2  HOH A1013      21.248  64.655  42.998  1.00  0.00           H  
HETATM 5853  O   HOH A1014      16.972  63.740  65.244  1.00 43.33           O  
HETATM 5854  H1  HOH A1014      16.315  64.394  65.496  1.00  0.00           H  
HETATM 5855  H2  HOH A1014      17.741  63.991  65.757  1.00  0.00           H  
HETATM 5856  O   HOH A1015      26.831  68.200  47.043  1.00 12.22           O  
HETATM 5857  H1  HOH A1015      26.174  67.712  47.569  1.00  0.00           H  
HETATM 5858  H2  HOH A1015      26.278  68.641  46.374  1.00  0.00           H  
HETATM 5859  O   HOH A1016      17.214  50.226  52.064  1.00 28.18           O  
HETATM 5860  H1  HOH A1016      16.304  50.521  52.201  1.00  0.00           H  
HETATM 5861  H2  HOH A1016      17.139  49.275  52.152  1.00  0.00           H  
HETATM 5862  O   HOH A1017      26.998  62.171  61.759  1.00 30.10           O  
HETATM 5863  H1  HOH A1017      27.131  62.397  60.836  1.00  0.00           H  
HETATM 5864  H2  HOH A1017      26.178  62.644  61.962  1.00  0.00           H  
HETATM 5865  O   HOH A1019      36.431  64.775  51.451  1.00 29.60           O  
HETATM 5866  H1  HOH A1019      36.430  64.892  50.505  1.00  0.00           H  
HETATM 5867  H2  HOH A1019      35.965  63.950  51.623  1.00  0.00           H  
HETATM 5868  O   HOH A1020      25.462  60.687  42.606  1.00 11.87           O  
HETATM 5869  H1  HOH A1020      25.571  61.385  41.960  1.00  0.00           H  
HETATM 5870  H2  HOH A1020      24.507  60.495  42.572  1.00  0.00           H  
HETATM 5871  O   HOH A1021      28.416  63.820  59.451  1.00 34.47           O  
HETATM 5872  H1  HOH A1021      28.942  63.011  59.524  1.00  0.00           H  
HETATM 5873  H2  HOH A1021      28.915  64.443  59.983  1.00  0.00           H  
HETATM 5874  O   HOH A1024      33.335  60.224  53.920  1.00 21.52           O  
HETATM 5875  H1  HOH A1024      33.358  59.289  54.153  1.00  0.00           H  
HETATM 5876  H2  HOH A1024      33.042  60.588  54.758  1.00  0.00           H  
HETATM 5877  O   HOH A1025      32.676  72.615  46.443  1.00 13.74           O  
HETATM 5878  H1  HOH A1025      32.753  71.818  45.919  1.00  0.00           H  
HETATM 5879  H2  HOH A1025      32.328  72.276  47.276  1.00  0.00           H  
HETATM 5880  O   HOH A1026       7.158  57.969  48.352  1.00 23.42           O  
HETATM 5881  H1  HOH A1026       7.628  58.684  48.791  1.00  0.00           H  
HETATM 5882  H2  HOH A1026       7.719  57.219  48.565  1.00  0.00           H  
HETATM 5883  O   HOH A1027      13.086  68.689  50.448  1.00 19.74           O  
HETATM 5884  H1  HOH A1027      12.274  68.465  50.009  1.00  0.00           H  
HETATM 5885  H2  HOH A1027      12.800  69.403  51.054  1.00  0.00           H  
HETATM 5886  O   HOH A1028      23.231  79.215  48.710  1.00 28.30           O  
HETATM 5887  H1  HOH A1028      22.797  79.017  47.853  1.00  0.00           H  
HETATM 5888  H2  HOH A1028      23.739  80.003  48.500  1.00  0.00           H  
HETATM 5889  O   HOH A1029      22.607  75.204  43.207  1.00 17.56           O  
HETATM 5890  H1  HOH A1029      21.872  74.943  42.645  1.00  0.00           H  
HETATM 5891  H2  HOH A1029      22.481  74.666  44.000  1.00  0.00           H  
HETATM 5892  O   HOH A1030      22.697  77.315  50.558  1.00 26.92           O  
HETATM 5893  H1  HOH A1030      22.324  76.697  49.923  1.00  0.00           H  
HETATM 5894  H2  HOH A1030      22.975  78.056  49.981  1.00  0.00           H  
HETATM 5895  O   HOH A1031      20.944  55.912  43.252  1.00 12.50           O  
HETATM 5896  H1  HOH A1031      21.070  55.930  44.213  1.00  0.00           H  
HETATM 5897  H2  HOH A1031      21.820  55.657  42.967  1.00  0.00           H  
HETATM 5898  O   HOH A1032      26.086  71.978  39.316  1.00 27.10           O  
HETATM 5899  H1  HOH A1032      25.548  71.173  39.411  1.00  0.00           H  
HETATM 5900  H2  HOH A1032      25.639  72.583  39.898  1.00  0.00           H  
HETATM 5901  O   HOH A1034      28.578  65.843  46.373  1.00 17.31           O  
HETATM 5902  H1  HOH A1034      29.244  66.093  47.015  1.00  0.00           H  
HETATM 5903  H2  HOH A1034      28.037  66.652  46.358  1.00  0.00           H  
HETATM 5904  O   HOH A1049      20.711  54.295  41.003  1.00 35.62           O  
HETATM 5905  H1  HOH A1049      21.431  54.359  41.638  1.00  0.00           H  
HETATM 5906  H2  HOH A1049      20.932  54.974  40.345  1.00  0.00           H  
HETATM 5907  O   HOH A1050      18.805  53.492  42.721  1.00 38.79           O  
HETATM 5908  H1  HOH A1050      18.584  52.678  42.247  1.00  0.00           H  
HETATM 5909  H2  HOH A1050      19.472  53.878  42.106  1.00  0.00           H  
HETATM 5910  O   HOH A1053      15.665  46.577  49.576  1.00 23.34           O  
HETATM 5911  H1  HOH A1053      16.416  47.055  49.938  1.00  0.00           H  
HETATM 5912  H2  HOH A1053      15.569  46.944  48.696  1.00  0.00           H  
HETATM 5913  O   HOH A1055       6.627  61.715  61.411  1.00 38.88           O  
HETATM 5914  H1  HOH A1055       7.152  60.961  61.142  1.00  0.00           H  
HETATM 5915  H2  HOH A1055       7.172  62.464  61.146  1.00  0.00           H  
HETATM 5916  O   HOH A1059      15.293  43.039  59.606  1.00 31.33           O  
HETATM 5917  H1  HOH A1059      15.989  43.540  59.154  1.00  0.00           H  
HETATM 5918  H2  HOH A1059      15.803  42.271  59.859  1.00  0.00           H  
HETATM 5919  O   HOH A1060      17.433  54.340  69.021  1.00 38.44           O  
HETATM 5920  H1  HOH A1060      17.327  55.175  69.484  1.00  0.00           H  
HETATM 5921  H2  HOH A1060      17.464  53.687  69.724  1.00  0.00           H  
HETATM 5922  O   HOH A1061      20.380  42.845  54.765  1.00 29.63           O  
HETATM 5923  H1  HOH A1061      21.165  42.278  54.742  1.00  0.00           H  
HETATM 5924  H2  HOH A1061      20.736  43.654  54.383  1.00  0.00           H  
HETATM 5925  O   HOH A1062      18.746  47.529  49.134  1.00 19.51           O  
HETATM 5926  H1  HOH A1062      18.073  47.108  48.589  1.00  0.00           H  
HETATM 5927  H2  HOH A1062      18.437  47.374  50.035  1.00  0.00           H  
HETATM 5928  O   HOH A1063      24.912  59.579  38.883  1.00  8.21           O  
HETATM 5929  H1  HOH A1063      25.873  59.684  38.960  1.00  0.00           H  
HETATM 5930  H2  HOH A1063      24.517  60.096  39.585  1.00  0.00           H  
HETATM 5931  O   HOH A1064       8.918  54.711  52.941  1.00 30.13           O  
HETATM 5932  H1  HOH A1064       8.273  54.255  52.367  1.00  0.00           H  
HETATM 5933  H2  HOH A1064       8.390  54.905  53.734  1.00  0.00           H  
HETATM 5934  O   HOH A1065      23.986  73.145  42.211  1.00 19.08           O  
HETATM 5935  H1  HOH A1065      24.019  73.326  41.271  1.00  0.00           H  
HETATM 5936  H2  HOH A1065      23.770  74.014  42.597  1.00  0.00           H  
HETATM 5937  O   HOH A1066      21.951  78.516  46.449  1.00 24.21           O  
HETATM 5938  H1  HOH A1066      22.139  78.428  45.508  1.00  0.00           H  
HETATM 5939  H2  HOH A1066      21.790  77.601  46.717  1.00  0.00           H  
HETATM 5940  O   HOH A1067      28.973  70.414  40.757  1.00 15.57           O  
HETATM 5941  H1  HOH A1067      29.060  69.642  40.188  1.00  0.00           H  
HETATM 5942  H2  HOH A1067      29.517  71.068  40.296  1.00  0.00           H  
HETATM 5943  O   HOH A1068      29.056  72.980  41.418  1.00 17.71           O  
HETATM 5944  H1  HOH A1068      28.855  72.102  41.774  1.00  0.00           H  
HETATM 5945  H2  HOH A1068      28.268  73.157  40.899  1.00  0.00           H  
HETATM 5946  O   HOH A1069      30.931  64.270  46.617  1.00 45.53           O  
HETATM 5947  H1  HOH A1069      30.972  65.200  46.883  1.00  0.00           H  
HETATM 5948  H2  HOH A1069      30.060  64.251  46.170  1.00  0.00           H  
HETATM 5949  O   HOH A1073      28.026  63.309  36.269  1.00 48.02           O  
HETATM 5950  H1  HOH A1073      27.080  63.403  36.397  1.00  0.00           H  
HETATM 5951  H2  HOH A1073      28.368  62.910  37.071  1.00  0.00           H  
HETATM 5952  O   HOH A1076       7.411  50.845  51.149  1.00 20.40           O  
HETATM 5953  H1  HOH A1076       8.260  51.067  50.747  1.00  0.00           H  
HETATM 5954  H2  HOH A1076       7.684  50.171  51.786  1.00  0.00           H  
HETATM 5955  O   HOH A1077       7.117  53.473  51.327  1.00 26.64           O  
HETATM 5956  H1  HOH A1077       6.859  52.569  51.598  1.00  0.00           H  
HETATM 5957  H2  HOH A1077       6.281  53.937  51.250  1.00  0.00           H  
HETATM 5958  O   HOH A1079      12.234  70.473  52.244  1.00 19.44           O  
HETATM 5959  H1  HOH A1079      12.943  71.068  52.540  1.00  0.00           H  
HETATM 5960  H2  HOH A1079      11.607  70.547  52.968  1.00  0.00           H  
HETATM 5961  O   HOH A1080      28.369  60.418  39.072  1.00 28.29           O  
HETATM 5962  H1  HOH A1080      28.209  61.150  39.664  1.00  0.00           H  
HETATM 5963  H2  HOH A1080      28.950  59.868  39.606  1.00  0.00           H  
HETATM 5964  O   HOH A1081      23.546  41.263  51.643  1.00 29.70           O  
HETATM 5965  H1  HOH A1081      23.160  41.799  52.349  1.00  0.00           H  
HETATM 5966  H2  HOH A1081      23.703  41.893  50.938  1.00  0.00           H  
HETATM 5967  O   HOH A1083      11.517  67.919  58.624  1.00 16.30           O  
HETATM 5968  H1  HOH A1083      11.363  67.342  59.390  1.00  0.00           H  
HETATM 5969  H2  HOH A1083      10.995  68.672  58.956  1.00  0.00           H  
HETATM 5970  O   HOH A1089      13.178  64.426  68.037  1.00 46.33           O  
HETATM 5971  H1  HOH A1089      13.756  64.995  67.541  1.00  0.00           H  
HETATM 5972  H2  HOH A1089      12.283  64.652  67.778  1.00  0.00           H  
HETATM 5973  O   HOH A1090      13.913  60.420  67.129  1.00 58.25           O  
HETATM 5974  H1  HOH A1090      14.035  60.769  68.011  1.00  0.00           H  
HETATM 5975  H2  HOH A1090      14.723  60.678  66.667  1.00  0.00           H  
HETATM 5976  O   HOH A1091      16.810  60.911  66.279  1.00 31.45           O  
HETATM 5977  H1  HOH A1091      17.293  61.257  67.031  1.00  0.00           H  
HETATM 5978  H2  HOH A1091      17.386  61.079  65.528  1.00  0.00           H  
HETATM 5979  O   HOH A1097      13.371  49.724  65.049  1.00 28.27           O  
HETATM 5980  H1  HOH A1097      12.642  50.212  64.666  1.00  0.00           H  
HETATM 5981  H2  HOH A1097      13.965  49.536  64.315  1.00  0.00           H  
HETATM 5982  O   HOH A1103      30.468  44.811  46.187  1.00 32.91           O  
HETATM 5983  H1  HOH A1103      30.491  44.425  47.074  1.00  0.00           H  
HETATM 5984  H2  HOH A1103      29.555  44.683  45.938  1.00  0.00           H  
HETATM 5985  O   HOH A1104      26.073  43.034  48.754  1.00 30.75           O  
HETATM 5986  H1  HOH A1104      25.300  43.149  49.311  1.00  0.00           H  
HETATM 5987  H2  HOH A1104      25.725  42.928  47.869  1.00  0.00           H  
HETATM 5988  O   HOH A1107      32.459  54.710  43.080  1.00 30.15           O  
HETATM 5989  H1  HOH A1107      32.437  54.875  42.128  1.00  0.00           H  
HETATM 5990  H2  HOH A1107      33.402  54.556  43.239  1.00  0.00           H  
HETATM 5991  O   HOH B1001      40.230   5.081  42.088  1.00  9.65           O  
HETATM 5992  H1  HOH B1001      40.073   4.297  41.560  1.00  0.00           H  
HETATM 5993  H2  HOH B1001      41.178   5.266  41.976  1.00  0.00           H  
HETATM 5994  O   HOH B1002      39.304  -1.508  47.872  1.00 25.66           O  
HETATM 5995  H1  HOH B1002      39.816  -0.788  48.270  1.00  0.00           H  
HETATM 5996  H2  HOH B1002      39.961  -2.001  47.364  1.00  0.00           H  
HETATM 5997  O   HOH B1003      37.609   0.605  47.090  1.00  9.79           O  
HETATM 5998  H1  HOH B1003      38.051  -0.136  46.660  1.00  0.00           H  
HETATM 5999  H2  HOH B1003      36.927   0.173  47.617  1.00  0.00           H  
HETATM 6000  O   HOH B1004      47.846   5.423  46.047  1.00 18.39           O  
HETATM 6001  H1  HOH B1004      47.669   4.776  46.735  1.00  0.00           H  
HETATM 6002  H2  HOH B1004      47.091   6.017  46.104  1.00  0.00           H  
HETATM 6003  O   HOH B1006      47.204  18.961  45.688  1.00  9.80           O  
HETATM 6004  H1  HOH B1006      48.029  19.087  45.213  1.00  0.00           H  
HETATM 6005  H2  HOH B1006      47.422  19.214  46.604  1.00  0.00           H  
HETATM 6006  O   HOH B1033      46.912  12.605  40.458  1.00 22.87           O  
HETATM 6007  H1  HOH B1033      47.743  12.989  40.736  1.00  0.00           H  
HETATM 6008  H2  HOH B1033      46.741  13.112  39.653  1.00  0.00           H  
HETATM 6009  O   HOH B1035      58.408  12.947  53.183  1.00 26.36           O  
HETATM 6010  H1  HOH B1035      57.821  12.210  52.979  1.00  0.00           H  
HETATM 6011  H2  HOH B1035      58.393  12.913  54.148  1.00  0.00           H  
HETATM 6012  O   HOH B1036      57.966  16.825  47.871  1.00 33.20           O  
HETATM 6013  H1  HOH B1036      57.042  16.578  47.965  1.00  0.00           H  
HETATM 6014  H2  HOH B1036      58.049  17.500  48.555  1.00  0.00           H  
HETATM 6015  O   HOH B1037      57.300  15.924  44.882  1.00 36.12           O  
HETATM 6016  H1  HOH B1037      56.742  16.171  45.633  1.00  0.00           H  
HETATM 6017  H2  HOH B1037      57.526  16.777  44.508  1.00  0.00           H  
HETATM 6018  O   HOH B1038      46.228  24.447  35.339  1.00 14.39           O  
HETATM 6019  H1  HOH B1038      46.277  24.875  34.481  1.00  0.00           H  
HETATM 6020  H2  HOH B1038      45.822  25.090  35.916  1.00  0.00           H  
HETATM 6021  O   HOH B1039      51.734  17.044  36.026  1.00 12.50           O  
HETATM 6022  H1  HOH B1039      51.653  17.041  35.069  1.00  0.00           H  
HETATM 6023  H2  HOH B1039      51.493  16.129  36.221  1.00  0.00           H  
HETATM 6024  O   HOH B1040      45.169  25.077  50.360  1.00 29.34           O  
HETATM 6025  H1  HOH B1040      44.348  24.768  49.944  1.00  0.00           H  
HETATM 6026  H2  HOH B1040      45.620  24.230  50.408  1.00  0.00           H  
HETATM 6027  O   HOH B1041      43.583   1.505  42.520  1.00 10.40           O  
HETATM 6028  H1  HOH B1041      44.203   1.435  43.263  1.00  0.00           H  
HETATM 6029  H2  HOH B1041      44.174   1.485  41.752  1.00  0.00           H  
HETATM 6030  O   HOH B1042      52.684  -0.868  51.423  1.00 15.33           O  
HETATM 6031  H1  HOH B1042      53.093  -0.349  50.734  1.00  0.00           H  
HETATM 6032  H2  HOH B1042      53.306  -1.584  51.568  1.00  0.00           H  
HETATM 6033  O   HOH B1051      50.058  20.573  45.836  1.00 35.24           O  
HETATM 6034  H1  HOH B1051      49.253  20.210  46.203  1.00  0.00           H  
HETATM 6035  H2  HOH B1051      50.184  20.119  45.007  1.00  0.00           H  
HETATM 6036  O   HOH B1052      50.673  26.128  54.691  1.00 32.34           O  
HETATM 6037  H1  HOH B1052      49.887  25.619  54.445  1.00  0.00           H  
HETATM 6038  H2  HOH B1052      50.289  27.005  54.724  1.00  0.00           H  
HETATM 6039  O   HOH B1054      42.540  -6.952  44.094  1.00 24.39           O  
HETATM 6040  H1  HOH B1054      42.361  -6.743  43.169  1.00  0.00           H  
HETATM 6041  H2  HOH B1054      42.645  -7.906  44.102  1.00  0.00           H  
HETATM 6042  O   HOH B1056      40.794   5.459  38.481  1.00 12.73           O  
HETATM 6043  H1  HOH B1056      39.904   5.129  38.632  1.00  0.00           H  
HETATM 6044  H2  HOH B1056      41.327   5.117  39.204  1.00  0.00           H  
HETATM 6045  O   HOH B1070      44.836   9.740  41.964  1.00 18.21           O  
HETATM 6046  H1  HOH B1070      44.732   9.956  42.900  1.00  0.00           H  
HETATM 6047  H2  HOH B1070      44.084  10.210  41.575  1.00  0.00           H  
HETATM 6048  O   HOH B1071      48.532  17.460  49.091  1.00 24.70           O  
HETATM 6049  H1  HOH B1071      49.431  17.166  49.287  1.00  0.00           H  
HETATM 6050  H2  HOH B1071      48.651  18.408  49.000  1.00  0.00           H  
HETATM 6051  O   HOH B1072      58.579   8.911  46.913  1.00 36.01           O  
HETATM 6052  H1  HOH B1072      58.034   8.438  47.548  1.00  0.00           H  
HETATM 6053  H2  HOH B1072      58.123   9.754  46.832  1.00  0.00           H  
HETATM 6054  O   HOH B1082      40.552 -10.806  45.776  1.00 41.79           O  
HETATM 6055  H1  HOH B1082      41.108 -10.267  46.340  1.00  0.00           H  
HETATM 6056  H2  HOH B1082      40.829 -11.709  45.928  1.00  0.00           H  
HETATM 6057  O   HOH B1106      32.979  10.951  41.620  1.00 14.25           O  
HETATM 6058  H1  HOH B1106      32.768  10.266  40.969  1.00  0.00           H  
HETATM 6059  H2  HOH B1106      32.092  11.162  41.947  1.00  0.00           H  
HETATM 6060  O   HOH C1005      40.709  18.716  41.943  1.00 14.34           O  
HETATM 6061  H1  HOH C1005      40.067  18.079  42.307  1.00  0.00           H  
HETATM 6062  H2  HOH C1005      40.559  18.509  41.016  1.00  0.00           H  
HETATM 6063  O   HOH C1007      16.369  22.395   5.380  1.00 32.80           O  
HETATM 6064  H1  HOH C1007      15.957  23.258   5.516  1.00  0.00           H  
HETATM 6065  H2  HOH C1007      16.828  22.526   4.542  1.00  0.00           H  
HETATM 6066  O   HOH C1008      23.868  27.744  28.283  1.00  3.86           O  
HETATM 6067  H1  HOH C1008      23.056  28.106  27.915  1.00  0.00           H  
HETATM 6068  H2  HOH C1008      23.621  27.625  29.214  1.00  0.00           H  
HETATM 6069  O   HOH C1022      37.295  26.593  21.555  1.00 15.71           O  
HETATM 6070  H1  HOH C1022      36.962  27.057  20.794  1.00  0.00           H  
HETATM 6071  H2  HOH C1022      36.999  25.691  21.418  1.00  0.00           H  
HETATM 6072  O   HOH C1043      26.864  22.651   0.738  1.00 25.89           O  
HETATM 6073  H1  HOH C1043      27.085  23.382   0.153  1.00  0.00           H  
HETATM 6074  H2  HOH C1043      27.281  21.889   0.315  1.00  0.00           H  
HETATM 6075  O   HOH C1044      26.427  20.284  -1.061  1.00  8.90           O  
HETATM 6076  H1  HOH C1044      26.582  19.548  -1.665  1.00  0.00           H  
HETATM 6077  H2  HOH C1044      26.380  21.030  -1.665  1.00  0.00           H  
HETATM 6078  O   HOH C1045      23.442  16.771   0.710  1.00 11.07           O  
HETATM 6079  H1  HOH C1045      23.089  16.408  -0.100  1.00  0.00           H  
HETATM 6080  H2  HOH C1045      23.994  16.031   0.995  1.00  0.00           H  
HETATM 6081  O   HOH C1046      16.192  20.355  24.673  1.00 20.21           O  
HETATM 6082  H1  HOH C1046      16.816  21.049  24.503  1.00  0.00           H  
HETATM 6083  H2  HOH C1046      16.005  19.964  23.801  1.00  0.00           H  
HETATM 6084  O   HOH C1047      19.833  12.479  27.012  1.00 16.43           O  
HETATM 6085  H1  HOH C1047      19.547  11.630  27.357  1.00  0.00           H  
HETATM 6086  H2  HOH C1047      19.307  12.573  26.208  1.00  0.00           H  
HETATM 6087  O   HOH C1048      18.956  12.884  29.942  1.00 20.15           O  
HETATM 6088  H1  HOH C1048      19.670  12.447  30.419  1.00  0.00           H  
HETATM 6089  H2  HOH C1048      18.208  12.298  30.090  1.00  0.00           H  
HETATM 6090  O   HOH C1057      19.406  16.916  19.031  1.00 20.82           O  
HETATM 6091  H1  HOH C1057      19.766  17.611  19.584  1.00  0.00           H  
HETATM 6092  H2  HOH C1057      19.998  16.176  19.178  1.00  0.00           H  
HETATM 6093  O   HOH C1074      23.632  29.165  30.850  1.00 27.25           O  
HETATM 6094  H1  HOH C1074      22.927  29.292  31.497  1.00  0.00           H  
HETATM 6095  H2  HOH C1074      23.663  30.000  30.379  1.00  0.00           H  
HETATM 6096  O   HOH C1075      12.733  17.987  30.317  1.00 33.08           O  
HETATM 6097  H1  HOH C1075      12.459  17.073  30.454  1.00  0.00           H  
HETATM 6098  H2  HOH C1075      12.958  18.260  31.225  1.00  0.00           H  
HETATM 6099  O   HOH C1078      22.700  16.078  23.050  1.00 24.77           O  
HETATM 6100  H1  HOH C1078      22.599  15.587  23.873  1.00  0.00           H  
HETATM 6101  H2  HOH C1078      23.517  15.677  22.711  1.00  0.00           H  
HETATM 6102  O   HOH C1084      35.026  22.694  31.475  1.00 43.81           O  
HETATM 6103  H1  HOH C1084      35.797  22.361  31.962  1.00  0.00           H  
HETATM 6104  H2  HOH C1084      34.835  21.939  30.904  1.00  0.00           H  
HETATM 6105  O   HOH C1085      37.334  21.446  32.298  1.00 36.90           O  
HETATM 6106  H1  HOH C1085      38.170  21.058  32.003  1.00  0.00           H  
HETATM 6107  H2  HOH C1085      37.267  21.172  33.211  1.00  0.00           H  
HETATM 6108  O   HOH C1086      34.651  29.052  23.427  1.00 48.29           O  
HETATM 6109  H1  HOH C1086      34.865  28.907  22.507  1.00  0.00           H  
HETATM 6110  H2  HOH C1086      35.483  29.339  23.804  1.00  0.00           H  
HETATM 6111  O   HOH C1087      38.224  27.538  25.535  1.00 31.04           O  
HETATM 6112  H1  HOH C1087      38.726  27.079  24.852  1.00  0.00           H  
HETATM 6113  H2  HOH C1087      38.021  28.369  25.096  1.00  0.00           H  
HETATM 6114  O   HOH C1088      15.715  22.248  35.953  1.00 34.43           O  
HETATM 6115  H1  HOH C1088      16.643  22.242  36.201  1.00  0.00           H  
HETATM 6116  H2  HOH C1088      15.554  23.196  35.808  1.00  0.00           H  
HETATM 6117  O   HOH C1092      31.076  35.057   7.310  1.00 20.17           O  
HETATM 6118  H1  HOH C1092      31.062  35.049   8.273  1.00  0.00           H  
HETATM 6119  H2  HOH C1092      31.445  34.206   7.060  1.00  0.00           H  
HETATM 6120  O   HOH C1094      28.849  36.439  12.410  1.00 31.51           O  
HETATM 6121  H1  HOH C1094      29.403  36.871  11.744  1.00  0.00           H  
HETATM 6122  H2  HOH C1094      28.287  37.180  12.680  1.00  0.00           H  
HETATM 6123  O   HOH C1095      26.362  37.996  12.114  1.00 59.36           O  
HETATM 6124  H1  HOH C1095      26.564  37.710  11.203  1.00  0.00           H  
HETATM 6125  H2  HOH C1095      25.579  38.525  11.988  1.00  0.00           H  
HETATM 6126  O   HOH C1096      25.808  37.523   9.428  1.00 42.15           O  
HETATM 6127  H1  HOH C1096      25.487  36.894   8.770  1.00  0.00           H  
HETATM 6128  H2  HOH C1096      25.288  38.305   9.249  1.00  0.00           H  
HETATM 6129  O   HOH C1100      15.198  19.163  21.700  1.00 44.82           O  
HETATM 6130  H1  HOH C1100      15.030  18.369  21.173  1.00  0.00           H  
HETATM 6131  H2  HOH C1100      15.609  19.725  21.038  1.00  0.00           H  
HETATM 6132  O   HOH C1101      14.140  21.284  33.786  1.00 15.37           O  
HETATM 6133  H1  HOH C1101      14.134  20.321  33.678  1.00  0.00           H  
HETATM 6134  H2  HOH C1101      14.665  21.429  34.602  1.00  0.00           H  
HETATM 6135  O   HOH C1102      14.033  18.621  33.361  1.00 33.43           O  
HETATM 6136  H1  HOH C1102      14.758  17.988  33.491  1.00  0.00           H  
HETATM 6137  H2  HOH C1102      13.666  18.696  34.254  1.00  0.00           H  
HETATM 6138  O   HOH D1009      43.143  50.223  27.405  1.00 31.69           O  
HETATM 6139  H1  HOH D1009      42.716  50.452  28.243  1.00  0.00           H  
HETATM 6140  H2  HOH D1009      42.503  50.587  26.796  1.00  0.00           H  
HETATM 6141  O   HOH D1018      24.796  47.144  45.004  1.00 16.99           O  
HETATM 6142  H1  HOH D1018      24.783  47.836  44.318  1.00  0.00           H  
HETATM 6143  H2  HOH D1018      25.594  47.438  45.477  1.00  0.00           H  
HETATM 6144  O   HOH D1023      43.594  50.252  24.315  1.00 32.56           O  
HETATM 6145  H1  HOH D1023      42.949  50.081  25.011  1.00  0.00           H  
HETATM 6146  H2  HOH D1023      43.865  51.152  24.508  1.00  0.00           H  
HETATM 6147  O   HOH D1058      41.586  37.377  29.750  1.00 11.90           O  
HETATM 6148  H1  HOH D1058      42.380  37.381  30.299  1.00  0.00           H  
HETATM 6149  H2  HOH D1058      41.874  36.875  28.982  1.00  0.00           H  
HETATM 6150  O   HOH D1093      30.079  38.995  12.495  1.00 20.42           O  
HETATM 6151  H1  HOH D1093      31.014  39.138  12.667  1.00  0.00           H  
HETATM 6152  H2  HOH D1093      29.633  39.710  12.953  1.00  0.00           H  
HETATM 6153  O   HOH D1098      30.082  43.142  33.634  1.00 44.15           O  
HETATM 6154  H1  HOH D1098      29.885  43.316  34.554  1.00  0.00           H  
HETATM 6155  H2  HOH D1098      30.507  43.960  33.344  1.00  0.00           H  
HETATM 6156  O   HOH D1099      30.859  41.583   4.834  1.00 35.34           O  
HETATM 6157  H1  HOH D1099      30.797  41.207   3.954  1.00  0.00           H  
HETATM 6158  H2  HOH D1099      31.509  41.030   5.283  1.00  0.00           H  
HETATM 6159  O   HOH D1105      26.057  44.769  44.244  1.00 41.06           O  
HETATM 6160  H1  HOH D1105      26.962  44.928  44.531  1.00  0.00           H  
HETATM 6161  H2  HOH D1105      25.577  45.548  44.572  1.00  0.00           H  
MASTER      336    0    0   20   22    0    0    6 4884    4    0   50          
END                                                                             

"""

def run_rfdiffusion(api_key, input_pdb):
    url = "https://health.api.nvidia.com/v1/biology/ipd/rfdiffusion/generate"
    headers = {"Authorization": f"Bearer {api_key}"}
    payload = {
        "input_pdb": input_pdb,
        "contigs": "A20-50/0",
        "hotspot_res": ['A30', 'A31', 'A32'],
        "diffusion_steps": 30,
        "sampling_temp": 0.5,
        "allow_backbone_sampling": True,
        "use_solvent": False
    }

    response = requests.post(url=url, headers=headers, json=payload)
    return response

def save_output(response, output_file="output.pdb"):
    print(response, f"Saving to {output_file}:\n", response.text[:200], "...")
    Path(output_file).write_text(json.loads(response.text)["output.pdb"])

def main():
    api_key = get_api_key()
    input_pdb = get_pdb_content()
    response = run_rfdiffusion(api_key, input_pdb)
    save_output(response)

if __name__ == "__main__":
    main()