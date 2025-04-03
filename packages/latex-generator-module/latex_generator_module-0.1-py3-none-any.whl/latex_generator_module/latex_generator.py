def generate_latex_table(data, caption="My Table", label="tab:mytable"):
    cols = len(data[0])
    latex_code = "\\documentclass{article}\n"
    latex_code += "\\usepackage{graphicx}\n"
    latex_code += "\\usepackage{caption}\n"
    latex_code += "\\usepackage{float}\n"
    latex_code += "\\begin{document}\n\n"
    
    latex_code += "\\begin{table}[H]\n"
    latex_code += "\\centering\n"
    latex_code += "\\begin{tabular}{" + "|c" * cols + "|}\n"
    latex_code += "\\hline\n"

    for row in data:
        latex_code += " & ".join(map(str, row)) + " \\\\\n"
        latex_code += "\\hline\n"

    latex_code += "\\end{tabular}\n"
    latex_code += f"\\caption{{{caption}}}\n"
    latex_code += f"\\label{{{label}}}\n"
    latex_code += "\\end{table}\n\n"

    latex_code += "\\end{document}\n"
    return latex_code


def generate_latex_image(image_path, caption="An example image", label="fig:example"):
    latex_code = "\\documentclass{article}\n"
    latex_code += "\\usepackage{graphicx}\n"
    latex_code += "\\usepackage{caption}\n"
    latex_code += "\\usepackage{float}\n"
    latex_code += "\\begin{document}\n\n"

    latex_code += "\\begin{figure}[H]\n"
    latex_code += "\\centering\n"
    latex_code += f"\\includegraphics[width=0.8\\textwidth]{{{image_path}}}\n"
    latex_code += f"\\caption{{{caption}}}\n"
    latex_code += f"\\label{{{label}}}\n"
    latex_code += "\\end{figure}\n\n"

    latex_code += "\\end{document}\n"
    return latex_code