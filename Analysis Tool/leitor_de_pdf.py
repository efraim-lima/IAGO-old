import tkinter as tk
import PyPDF2
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile
from docx import Document
import docx

root = tk.Tk()

canvas = tk.Canvas(root, width = 600, height = 300)
canvas.grid(columnspan=3, rowspan = 3)

logo = Image.open('C:/Users/efrai/Desktop/YT/__YT__/__API__/IAGO.png')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image = logo)
logo_label.image = logo
logo_label.grid(column = 1, row = 0)

instructions = tk.Label(root, text="Hello, I'm IAGO \n your video content Artificial Inteligence", font = 'Helvetica')
instructions.grid(columnspan = 3, column = 0, row =1)

def open_file():
    browse_text.set('loading...')
    file = askopenfile(parent=root, mode='rb',title = 'Choose a file', filetypes=[('PDF file', '*.pdf'), ('Word file' ,'*.docx')])

    if file:
        try:
            read_pdf = PyPDF2.PdfFileReader(file)
            page = read_pdf.getPage(0)
            page_content = page.extractText()
            print(page_content)
        except:
            doc = docx.Document(file)
            page_content = []
            for para in doc.paragraphs:
                page_content.append(para.text)


        text_box = tk.Text(root, height=50, padx=30, pady=15)
        text_box.insert(1.0, page_content)
        text_box.tag_configure('center', justify='center')
        text_box.tag_add('center', 1.0, 'end')
        text_box.grid(column=1, row= 3)

        browse_text.set("browse")

browse_text = tk.StringVar()
browse_btn = tk.Button(root, textvariable=browse_text, command = lambda:open_file(), font = 'Helvetica', bg = '#20bebe', fg = 'white', height = 2, width = 15)
browse_text.set('Browse')
browse_btn.grid(column =1, row=2)

canvas = tk.Canvas(root, width = 600, height = 250)
canvas.grid(columnspan=3)

root.mainloop()