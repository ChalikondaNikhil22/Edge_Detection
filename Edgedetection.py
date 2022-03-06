from helper_functions import *

#-----------------------FILL IN THE FOLDER WHERE YOUR IMAGE EXISTS--------------------------
datafolder = "C:/Users/Nikhil Chalikonda/Desktop/Python_Assign1/images/"
imgpath = datafolder + "1.jpg" 
#----------------------------------------STARTER CODE----------------------------------------
# Convert the color image to grayscale and returns the grayscale pixels 
pixel_values = read_colorimg(imgpath)
# The returned pixel values INCLUDE 2 boundary rows and 2 boundary colns. Therefore,
numb_rows = len(pixel_values) - 2
numb_colns = len(pixel_values[0]) - 2
#
#----------------------------------------WRITE YOUR CODE HERE----------------------------------------
# Create a data structure to store updated pixel information
new_pixel_values =  [[0 for j in range(numb_colns)] for i in range(numb_rows)]
# Define the 3 x 3 mask as a tuple of tuples
mask = ((-1,-1,-1),(-1,8,-1),(-1,-1,-1))

# Implement a function to slice a part from the image as a 2D list
def get_slice_2d_list(matrix_data_list,present_rows_in_matrix,present_columns_in_matrix):
    matrixresult=[extracting_matrix[present_columns_in_matrix-1:present_columns_in_matrix+2] for extracting_matrix in matrix_data_list[present_rows_in_matrix-1:present_rows_in_matrix+2]]
    return matrixresult

# Implement a function to flatten a 2D list or a 2D tuple
def flatten(givenlist):
    matrix_2d_flattened=[j for i in givenlist for j in i]
    return matrix_2d_flattened

for rowsofmatrix in range(1,numb_rows+1):
    for columnsofmatrix in range(1,numb_colns+1):
# For each of the pixel values, excluding the boundary values
    # Create little local 3x3 box using list slicing
        neighbour_pixels=get_slice_2d_list(pixel_values,rowsofmatrix,columnsofmatrix)
        filteringdata=flatten(mask)
        flattenedresult=flatten(neighbour_pixels)
    # Apply the mask
        mult_result = map(lambda masking,imagepixels: masking * imagepixels,filteringdata,flattenedresult)
        adding_all_the_data=sum(list(mult_result))
        new_pixel_values[rowsofmatrix-1][columnsofmatrix-1]=adding_all_the_data       
    # Sum all the multiplied values and set the new pixel value
#        
#----------------------------------------END YOUR CODE HERE----------------------------------------
# Verify your result
verify_result(pixel_values, new_pixel_values, mask)
# View the original image and the edges of the image
view_images(imgpath, new_pixel_values)