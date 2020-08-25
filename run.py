from sys import path
from google_images_download import google_images_download, main
import tkinter

response = google_images_download.googleimagesdownload()

search_queries =[]
def downloadimages(query,output_dir):
    paths = ""

    # keywords is the search query
    # format is the image file format
    # limit is the number of images to be downloaded
    # print urs is to print the image file url
    # size is the image size which can
    # be specified manually ("large, medium, icon")
    # aspect ratio denotes the height width ratio
    # of images to download. ("tall, square, wide, panoramic")
    arguments = {"keywords": query,
                 "format": "jpg",
                 "limit": 5,
                 "print_urls": True,
                 "size": "medium",
                 "aspect_ratio": "panoramic",
                 "output-directory" : output_dir}

    try:
        # pass the arguments to the function
        paths = response.download(arguments) 
        # print absolute path of the downloaded images
        print(paths)  
    
    # Handling File NotFound Error
    except FileNotFoundError:
        # Providing arguments for the searched query
        try:
            # pass the arguments to the function
            paths = response.download(arguments) 
            # print absolute path of the downloaded images
            print(paths)  
        except:
            pass


# Driver Code
query_words=[""]
def callback():
    output_dir = path_input.get()
    query_words=(search_input.get()).split(',')
    for query in query_words:
        downloadimages(query,output_dir)

GUI = True

if GUI:

    main_window=tkinter.Tk()
    main_window.bind("<Escape>", lambda e: main_window.quit())

    main_label = tkinter.Label(main_window,text="Press Esc to quit!").grid(row=0,sticky='W')

    search_label = tkinter.Label(main_window,text="Enter your search term here!").grid(row=1,sticky='W')
    search_input=tkinter.Entry(main_window).grid(row=1,column=1,sticky='e')

    path_label = tkinter.Label(main_window,text="Enter where you want the image(s) to go to!").grid(row=2,sticky='W')
    path_input = tkinter.Entry(main_window).grid(row=2,column=1,sticky='e')

    b = tkinter.Button(main_window, text="Download Images", command=callback).grid(row=3)

    main_window.mainloop()