#### Medium Requirment convert report to a HTMl 
## Idk how to get it to PDF without using LateX so may just have to manually print to PDF or write a script for that.

import subprocess

def convert_notebook_to_html(notebook_path):
    """Convert Jupyter notebook to HTML."""
    html_output_path = notebook_path.replace('.ipynb', '.html')
    subprocess.run(['jupyter', 'nbconvert', '--to', 'html', notebook_path])
    print(f"Converted notebook to HTML: {html_output_path}")
    return html_output_path


## For converting to PDF we used this website: 



def main():
    notebook_path = 'census2021.ipynb'  # Change this to your notebook's path
    
    # Convert notebook to HTML
    convert_notebook_to_html(notebook_path)
    convert_notebook_to_pdf(notebook_path)

if __name__ == "__main__":
    main()
