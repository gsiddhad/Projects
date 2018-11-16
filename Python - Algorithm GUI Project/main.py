# Algorthms GUI Project / main.py
# Created on: 07-Nov-2018
# Author: Gourav Siddhad

from tkinter import Listbox, Label, scrolledtext
from tkinter.ttk import Entry

from bptree import BPTree
from bst import BST
from lcs import LCS
from mst_graph import MST_Graph
from radix import Radix
from scc_graph import SCC_Graph
from tsort import TSort
import subprocess as sp
import tkinter as tk


def main():
    master = tk.Tk()
    master.title('Algorithms')
#     width, height = 810, 400
    width, height = 1200, 400
    xcord = master.winfo_screenwidth() / 2 - width / 2
    ycord = master.winfo_screenheight() / 2 - height / 2
    master.geometry("%dx%d+%d+%d" % (width, height, xcord, ycord))

    labelAlgo = Label(master, text = "Algorithms")
    labelAlgo.grid(row = 0, column = 0)

    labelInput = Label(master, text = "Input")
    labelInput.grid(row = 0, column = 1)

    labelOutput = Label(master, text = "Output")
    labelOutput.grid(row = 0, column = 3)

    algoLbox = Listbox(master, width = 30, height = 20, borderwidth = 5)
    algoLbox.insert(1, "Binary Search Tree")
    algoLbox.insert(2, "Radix Sort")
    algoLbox.insert(3, "Prim's MST")
    algoLbox.insert(4, "Prim's MST - Double")
    algoLbox.insert(5, "Strongly Connected Components")
    algoLbox.insert(6, "Topological Sort")
    algoLbox.insert(7, "Lowest Common Subsequence")
    algoLbox.insert(8, "B+ Tree")
    algoLbox.configure(justify = 'center')
    algoLbox.grid(row = 1, column = 0)

    def load():
        inputScrollText.delete(1.0, tk.END)
        fileName = get_inputfilename(algoLbox.curselection()[0])
        with open(fileName, 'r') as Input:
            for line in Input:
                inputScrollText.insert('insert', line)

    def get_inputfilename(ch):
        if ch is 0:
            return 'input\\input_bst.txt'
        elif ch is 1:
            return 'input\\input_radix.txt'
        elif ch is 2:
            return 'input\\input_mst.txt'
        elif ch is 3:
            return 'input\\input_mst.txt'
        elif ch is 4:
            return 'input\\input_scc.txt'
        elif ch is 5:
            return 'input\\input_tsort.txt'
        elif ch is 6:
            return 'input\\input_lcs.txt'
        elif ch is 7:
            return 'input\\input_bptree.txt'

    def edit():
        programName = "notepad.exe"
        fileName = get_inputfilename(algoLbox.curselection()[0])
        sp.Popen([programName, fileName])

    def perform():
        outputScrollText.delete(1.0, tk.END)
        ch = algoLbox.curselection()[0]
        fileName = get_inputfilename(ch)
        output = None

        if ch is 0:
            tree = BST()
            tree.read_File(fileName)
            output = tree.print_tree()

            output = output + '\n\nDelete 10\n'
            output = output + str(tree.delete(10)) + '\n'
            output = output + tree.print_tree()

            output = output + '\n\nDelete 19\n'
            output = output + str(tree.delete(19)) + '\n'
            output = output + tree.print_tree()

            output = output + '\n\nInsert 15\n'
            tree.insert(15)
            output = output + tree.print_tree()

        elif ch is 1:
            radix = Radix()
            radix.read_File(fileName)
            radix.sort()
            output = radix.displayOutput()

        elif ch is 2:
            graph = MST_Graph()
            graph.read_File(fileName)
            parent = graph.primMST()
            output = graph.printMST(parent)

        elif ch is 3:
            graph = MST_Graph()
            graph.read_File(fileName)
            parent = graph.primMST()
            output = 'First Round\n' + graph.printMST(parent)

            graph.double_prim(parent)
            parent = graph.primMST()
            output = output + '\n\nSecond Round\n' + graph.printMST(parent)

        elif ch is 4:
            graph = SCC_Graph()
            graph.read_File(fileName)
            output = 'Strongly Connected Components\n'
            output = output + graph.printSCCs()

        elif ch is 5:
            # ToDo
            tsort = TSort()
            tsort.read_File(fileName)
            output = tsort.display_graph()
            output = output + tsort.display_sorting()

        elif ch is 6:
            lcs = LCS()
            lcs.readInput(fileName)
            output = lcs.genTable()

        elif ch is 7:
            bptree = BPTree(3)
            bptree.read_File(fileName)
            output = bptree

        outputScrollText.insert('insert', output)

    def clearall():
        inputScrollText.delete(1.0, tk.END)
        outputScrollText.delete(1.0, tk.END)

    def about():
        inputScrollText.delete(1.0, tk.END)
        outputScrollText.delete(1.0, tk.END)
        output = 'CS531L - Algorithms Assignment\nCreated by Gourav Siddhad\n1811010\nPDPM IIITDMJ\n'
        outputScrollText.insert('insert', output)

    algoFrame = tk.Frame(master, padx = 5, pady = 5)
    algoFrame.grid(row = 2, column = 0)
    aboutButton = tk.Button(algoFrame, text = 'About', width = 10, command = about)
    aboutButton.grid(row = 2, column = 0)
    loadButton = tk.Button(algoFrame, text = 'Load', width = 10, command = load)
    loadButton.grid(row = 2, column = 1)
    algoFrame.pack_slaves()

    inputScrollText = scrolledtext.ScrolledText(master, width = 35, height = 20, padx = 5, pady = 5)
    inputScrollText.grid(row = 1, column = 1)
    outputScrollText = scrolledtext.ScrolledText(master, width = 83, height = 20, padx = 5, pady = 5)
    outputScrollText.grid(row = 1, column = 3)

    inputFrame = tk.Frame(master, padx = 5, pady = 5)
    inputFrame.grid(row = 2, column = 1)
    editButton = tk.Button(inputFrame, text = 'Edit', width = 10, command = edit)
    editButton.grid(row = 0, column = 0)
    performButton = tk.Button(inputFrame, text = 'Perform', width = 10, command = perform)
    performButton.grid(row = 0, column = 1)

    buttonFrame = tk.Frame(master, padx = 5, pady = 5)
    buttonFrame.grid(row = 2, column = 3)
    clearallButton = tk.Button(buttonFrame, text = 'Clear All', width = 10, command = clearall)
    clearallButton.grid(row = 0, column = 0)
    quitButton = tk.Button(buttonFrame, text = 'Quit', width = 10, command = master.destroy)
    quitButton.grid(row = 0, column = 1)

    master.mainloop()


if __name__ == '__main__':
    main()
