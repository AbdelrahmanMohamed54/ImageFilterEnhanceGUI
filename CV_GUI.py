"""
Author: Abdelrahman Mohamed (22201965)

GUI creation and filter connections
Image display/representation on GUI

"""

import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
from canny_edge import canny_edge  # Import the canny_edge function
import cv2
from Gaussian_blur import gaussian_blur  # Import the gaussian_blur function
from Sharpening_filter import sharpen_image

# Create the main application window
window = tk.Tk()
window.title("Image Filter and Enhancement")
# Get the screen width and height
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Set the window's geometry to cover the screen
window.geometry(f"{screen_width}x{screen_height}+0+0")

window.configure(bg="#333333")

# Allow the window to be resizable
window.resizable(True, True)


# Function to apply the selected filter or enhancement
def apply_filter():
    selected_filter = filter_dropdown.get()
    if selected_filter == "Choose a filter":
        messagebox.showerror("Error", "Please select a filter")
        return

    if selected_filter == "Canny edge detection":
        # Get the path of the selected image
        image_path = image_path_entry.get()

        # Load the image
        image = cv2.imread(image_path)

        # Define the low and high thresholds for double thresholding

        canny_threshold_entry_1 = canny_threshold_entry1.get()
        canny_threshold_entry_2 = canny_threshold_entry2.get()

        if canny_threshold_entry_1 == "":
            low_threshold = 100  # Default low_threshold if not provided by the user
        else:
            low_threshold = int(canny_threshold_entry_1)

        if canny_threshold_entry_2 == "":
            high_threshold = 200  # Default high_threshold  value if not provided by the user
        else:
            high_threshold = int(canny_threshold_entry_1)

        # Apply Canny edge detection
        edges = canny_edge(image, low_threshold, high_threshold)

        # Save the filtered image
        cv2.imwrite('filtered_image.jpg', edges)

        resized_original_image = cv2.resize(image, (450, 450))  # Adjust the size as needed

        # Display the original image
        cv2.imshow('Original Image', resized_original_image)
        cv2.moveWindow('Original Image', 25, 140)  # Set the position of the window

        # Display the filtered image
        filtered_image = cv2.imread('filtered_image.jpg')
        # Resize the filtered image
        resized_filtered_image = cv2.resize(filtered_image, (450, 450))  # Adjust the size as needed
        cv2.imshow('Filtered Image', resized_filtered_image)
        cv2.moveWindow('Filtered Image', 1047, 140)  # Set the position of the window

    elif selected_filter == "Gaussian blur":
        # Get the path of the selected image
        image_path = image_path_entry.get()

        image = cv2.imread(image_path)

        kernel_size_entry_value = gaussian_kernel_size_entry.get()
        sigma_entry_value = gaussian_std_dev_entry.get()

        if kernel_size_entry_value == "":
            kernel_size = (25, 25)  # Default kernel size if not provided by the user
        else:
            kernel_size = tuple(map(int, kernel_size_entry_value.split(',')))

        if sigma_entry_value == "":
            sigma = 15  # Default sigma value if not provided by the user
        else:
            sigma = float(sigma_entry_value)

        blurred_image = gaussian_blur(image, kernel_size, sigma)

        resized_original_image = cv2.resize(image, (450, 450))  # Adjust the size as needed
        # Resize the filtered image
        resized_Blured_image = cv2.resize(blurred_image, (450, 450))  # Adjust the size as needed

        # Save the filtered image
        cv2.imwrite('Blured_image.jpg', blurred_image)

        # Display the original and blurred images
        cv2.imshow("Original Image", resized_original_image)
        cv2.moveWindow('Original Image', 25, 140)  # Set the position of the window
        cv2.imshow("Blurred Image", resized_Blured_image)
        cv2.moveWindow('Blurred Image', 1047, 140)  # Set the position of the window

    elif selected_filter == "Sharpening":

        # Get the sharpening factor from the entry
        sharpening_entry_value = sharpening_entry.get()

        if sharpening_entry_value == "":
            sharpening_factor = 1.0  # Default sharpening factor if not provided by the user
        else:
            sharpening_factor = float(sharpening_entry_value)

        # Get the path of the selected image
        image_path = image_path_entry.get()

        # Load the image
        image = cv2.imread(image_path, cv2.IMREAD_COLOR)

        sharpened_image = sharpen_image(image, sharpening_factor)

        resized_original_image = cv2.resize(image, (450, 450))  # Adjust the size as needed
        # Resize the filtered image
        resized_sharpened_image = cv2.resize(sharpened_image, (450, 450))  # Adjust the size as needed

        # Save the filtered image
        cv2.imwrite('Sharpened_image.jpg', sharpened_image)

        # Display the original and blurred images
        cv2.imshow("Original Image", resized_original_image)
        cv2.moveWindow('Original Image', 25, 140)  # Set the position of the window
        cv2.imshow("Sharpened Image", resized_sharpened_image)
        cv2.moveWindow('Sharpened Image', 1047, 140)  # Set the position of the window

    # Handle other filters/enhancements..., (This comment is to ensure code extensibility)


# Function to load the image
def load_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        global image, original_image
        image = Image.open(file_path)
        original_image = ImageTk.PhotoImage(image)
        image_path_entry.delete(0, tk.END)
        image_path_entry.insert(0, file_path)


# Function to show the Gaussian blur parameters
def show_gaussian_parameters():
    gaussian_label.pack()
    gaussian_kernel_size_label.pack(pady=(10, 0))
    gaussian_kernel_size_entry.pack()
    gaussian_std_dev_label.pack(pady=(10, 0))
    gaussian_std_dev_entry.pack(pady=(10, 20))
    Gaussian_info_label.pack()


# Function to hide the Gaussian blur parameters
def hide_gaussian_parameters():
    gaussian_label.pack_forget()
    gaussian_kernel_size_label.pack_forget()
    gaussian_kernel_size_entry.pack_forget()
    gaussian_std_dev_label.pack_forget()
    gaussian_std_dev_entry.pack_forget()
    Gaussian_info_label.pack_forget()


# Function to show the Canny edge detector parameters
def show_canny_parameters():
    canny_label.pack()
    canny_threshold_label1.pack(pady=(10, 0))
    canny_threshold_entry1.pack()
    canny_threshold_label2.pack(pady=(10, 0))
    canny_threshold_entry2.pack(pady=(10, 20))
    canny_info_label.pack()


# Function to hide the Canny edge detector parameters
def hide_canny_parameters():
    canny_label.pack_forget()
    canny_threshold_label1.pack_forget()
    canny_threshold_entry1.pack_forget()
    canny_threshold_label2.pack_forget()
    canny_threshold_entry2.pack_forget()
    canny_info_label.pack_forget()


# Function to show the sharpening parameter
def show_sharpening_parameter():
    Sharpening_title_label.pack()
    sharpening_label.pack(pady=(10, 0))
    sharpening_entry.pack(pady=(10, 65))
    Sharpening_info_label.pack()


# Function to hide the sharpening parameter
def hide_sharpening_parameter():
    sharpening_label.pack_forget()
    sharpening_entry.pack_forget()
    Sharpening_title_label.pack_forget()
    Sharpening_info_label.pack_forget()


# Set a bold title above the dropdown menu
title_label = tk.Label(window, text="Image Filter and Enhancement", font=("Arial", 14, "bold"), bg="#333333",
                       fg="#FFFFE0")
title_label.pack(pady=20)

# Create a frame for the dropdown menu and buttons
frame = tk.Frame(window)
frame.pack(pady=(0, 55), padx=20)
frame.configure(bg="#333333")

# Create the label for filter selection
filter_label = tk.Label(frame, text="Select a filter or enhancement:", bg="#333333", fg="white")
filter_label.pack(pady=(20, 0))

# Create the dropdown menu for filter selection
filter_dropdown = tk.StringVar(window)
filter_dropdown.set("Choose a filter")  # Default value

filter_options = ["Gaussian blur", "Canny edge detection", "Sharpening"]

filter_menu = tk.OptionMenu(frame, filter_dropdown, *filter_options)
# Set the background color to light gray
filter_menu.config(bg='#808080', highlightthickness=0, highlightbackground='#808080')
filter_menu.pack(pady=(10, 0))

# Create a frame for the parameters
parameters_frame = tk.Frame(window)
parameters_frame.pack(pady=20, padx=20)
parameters_frame.configure(bg="#333333")

# Gaussian blur parameters
gaussian_label = tk.Label(parameters_frame, text="Gaussian blur parameters:", bg="#333333", fg="white")
gaussian_label.pack()

gaussian_kernel_size_label = tk.Label(parameters_frame, text="--> Kernel size: [ex: 5,5 ]", bg="#333333", fg="white")
gaussian_kernel_size_label.pack(pady=(10, 0))

gaussian_kernel_size_entry = tk.Entry(parameters_frame, bg="#808080")
gaussian_kernel_size_entry.pack()

gaussian_std_dev_label = tk.Label(parameters_frame, text="--> Sigma:", bg="#333333", fg="white")
gaussian_std_dev_label.pack(pady=(10, 0))

gaussian_std_dev_entry = tk.Entry(parameters_frame, bg="#808080")
gaussian_std_dev_entry.pack(pady=(0, 30))

# Canny edge detector parameters
canny_label = tk.Label(parameters_frame, text="Canny edge detector parameters:", bg="#333333", fg="white")
canny_label.pack()

canny_threshold_label1 = tk.Label(parameters_frame, text="--> Threshold value 1:", bg="#333333", fg="white")
canny_threshold_label1.pack(pady=(10, 0))

canny_threshold_entry1 = tk.Entry(parameters_frame, bg="#808080")
canny_threshold_entry1.pack()

canny_threshold_label2 = tk.Label(parameters_frame, text="--> Threshold value 2:", bg="#333333", fg="white")
canny_threshold_label2.pack(pady=(10, 0))

canny_threshold_entry2 = tk.Entry(parameters_frame, bg="#808080")
canny_threshold_entry2.pack(pady=(0, 30))

# Sharpening parameter
Sharpening_title_label = tk.Label(parameters_frame, text="Sharpening Filter parameters:", bg="#333333", fg="white")
Sharpening_title_label.pack()

sharpening_label = tk.Label(parameters_frame, text="--> Sharpening factor:", bg="#333333", fg="white")
sharpening_label.pack(pady=(10, 10))

sharpening_entry = tk.Entry(parameters_frame, bg="#808080")
sharpening_entry.pack()

# display the photos that contain the information about each filter:

# Read the canny edge filter information image
image = Image.open("canny_edge_info.png")

# Define the desired width and height for the resized image
width = 500
height = 250

# Resize the image
resized_image = image.resize((width, height), Image.LANCZOS)

# Convert the resized image to PhotoImage format
image_tk = ImageTk.PhotoImage(resized_image)

# Create a label to display the resizable image
canny_info_label = tk.Label(parameters_frame, image=image_tk)

# Read the Gaussian blur edge filter information image
image = Image.open("Gaussian_blur_info.png")

# Define the desired width and height for the resized image
width = 500
height = 250

# Resize the image
Gaussian_resized_image = image.resize((width, height), Image.LANCZOS)

# Convert the resized image to PhotoImage format
Gaussian_image_tk = ImageTk.PhotoImage(Gaussian_resized_image)

# Create a label to display the resizable image
Gaussian_info_label = tk.Label(parameters_frame, image=Gaussian_image_tk)

# Read the Gaussian blur edge filter information image
image = Image.open("Sharpenning_information.png")

# Define the desired width and height for the resized image
width = 500
height = 250

# Resize the image
Sharpening_resized_image = image.resize((width, height), Image.LANCZOS)

# Convert the resized image to PhotoImage format
Sharpening_image_tk = ImageTk.PhotoImage(Sharpening_resized_image)

# Create a label to display the resizable image
Sharpening_info_label = tk.Label(parameters_frame, image=Sharpening_image_tk)


# Function to handle the filter selection
def on_filter_select(*args):
    selected_filter = filter_dropdown.get()
    if selected_filter == "Gaussian blur":
        show_gaussian_parameters()
        hide_canny_parameters()
        hide_sharpening_parameter()
    elif selected_filter == "Canny edge detection":
        show_canny_parameters()
        hide_gaussian_parameters()
        hide_sharpening_parameter()
    elif selected_filter == "Sharpening":
        hide_gaussian_parameters()
        hide_canny_parameters()
        show_sharpening_parameter()


# Bind the on_filter_select function to the dropdown menu selection
filter_dropdown.trace("w", on_filter_select)

# Create a frame for the image selection
image_selection_frame = tk.Frame(window)
image_selection_frame.pack(pady=20)
image_selection_frame.configure(bg="#333333")

# Image Path input field
image_path_label = tk.Label(image_selection_frame, text="Image path:", bg="#333333", fg="white")
image_path_label.pack(side="left")

image_path_entry = tk.Entry(image_selection_frame, bg="#808080")
image_path_entry.pack(side="left")

# Load Image button
load_button = tk.Button(image_selection_frame, text="Load Image", command=load_image, font=("Arial", 12), width=15,
                        bg="lightblue")
load_button.pack(side="left", padx=(30, 0))

# Apply Filter button
apply_button = tk.Button(window, text="Apply Filter", command=apply_filter, font=("Arial", 12), width=15,
                         bg="lightgreen")
apply_button.pack(pady=10)

# Run the main event loop
window.mainloop()
