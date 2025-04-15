Project 11: Jack Compiler – VM Code Generator

This directory contains my solution to Project 11 of the Nand2Tetris course, which focuses on extending the Jack compiler to generate VM code from the parsed Jack source code. 
The project builds on the work done in Project 10 by adding a VM code generation phase, translating the syntax tree into low-level VM instructions.

Files
SymbolTable.py
Implements the symbol table used to store and manage variables, constants, and functions.
This file handles symbol management during the compilation process, allowing the compiler to keep track of the program's identifiers.

VMWriter.py
Responsible for writing VM code. 
This file generates the corresponding VM instructions for the Jack code, 
including arithmetic operations, variable assignments, function calls, and control flow operations.

analyser.py
It opens a Tkinter folder selection window, allowing the user to select a directory containing Jack files.
The script processes the .jack files in the selected directory, generating the intermediate XML files for syntax analysis and ultimately producing the VM code.

compilationengine.py
Implements the compilation engine that processes the token stream and syntax tree generated in Project 10. 
In Project 11, it has been extended to translate the syntax tree into VM instructions.

tokeniser.py
Implements the tokenizer and performs lexical analysis. 
It breaks the Jack source code into tokens, as in Project 10, and feeds them into the compilation engine for further processing.
