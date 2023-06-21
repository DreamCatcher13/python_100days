from tkinter import *
from tkinter import filedialog, messagebox, font
from PIL import Image, ImageDraw, ImageFont

###  GLOBAL VARs  ###
MARK = "python"
FONT = ImageFont.truetype('arial.ttf', 18)
IMAGE = ""
BG = "#c5ccfa"

def select_img():
    global IMAGE
    img_path.delete(0, END)
    filetypes = (('All files', '*.*'),)
    img_file = filedialog.askopenfilename(title='Select your image', filetypes=filetypes)
    img_path.insert(0, img_file.split('/')[-1])
    IMAGE = img_file

def put_watermark():
    global IMAGE
    if IMAGE:
        name, ext = IMAGE.split('/')[-1].split('.')
        if ext not in ['png', 'jpeg', 'jpg', 'bmp']:
            messagebox.showerror(title="Error!", message="""The app supports following images:
            PNG, JPEG, BMP""")
            IMAGE = ""
        else:
            out_file = IMAGE.rsplit('/', 1)[0] + '/' + name + "_marked." + ext
            im =  Image.open(IMAGE) 
            w, h = im.size
            mark = mark_text.get()
            font = ImageFont.truetype('arial.ttf', 18)
            draw = ImageDraw.Draw(im)
            t_dim = draw.textbbox(xy=(0,0), text=mark, font=font)
            x = w - t_dim[2] -3
            y = h - t_dim[3] -3
            draw.text((x,y), mark, font=font, fill="azure")
            im.save(out_file)
            im.close()
            IMAGE = ""
            messagebox.showinfo(title="Success!", message=f"""Your image has been successfully watermarked :)
New image: 
{out_file}""")
    else:
        messagebox.showerror(title="Error!", message="You should select image first")

### MAIN WINDOW ###
window = Tk()
window.title("Watermarking app")
window.config(padx=15, pady=15, bg=BG)

select_button = Button(text="Select your image", command=select_img)
watermark = Button(text="Put a watermark", command=put_watermark)
mark_l = Label(text="Your watermark", bg=BG)
img_l = Label(text="Your image", bg=BG)
mark_text = Entry(width=20)
mark_text.insert(0, MARK)
img_path = Entry(width=20)

mark_l.grid(column=1, row=1, pady=5)
mark_text.grid(column=2, row=1, padx=5, pady=5)
img_l.grid(column=1, row=2, pady=5)
img_path.grid(column=2, row=2, padx=5, pady=5)
select_button.grid(column=3, row=2, padx=5, pady=5)
watermark.grid(column=2, row=4)


window.mainloop()
