import nbformat
import os

def strip_output(nb):
    for cell in nb.cells:
        if cell.cell_type == 'code':
            cell.outputs = []
            cell.execution_count = None
        elif cell.cell_type == 'markdown':
            cell.outputs = []

    return nb

def strip_notebook_output(nb_path):
    with open(nb_path, 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)

    nb = strip_output(nb)

    with open(nb_path, 'w', encoding='utf-8') as f:
        nbformat.write(nb, f)

for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.ipynb'):
            nb_path = os.path.join(root, file)
            strip_notebook_output(nb_path)