import tensorflow as tf
from tensorflow.keras import models
from tensorflow.keras.layers import * 
from tensorflow.keras.activations import * 
from tensorflow.keras.models import Sequential

#Creation of a U-Net model, a CNN architecture commonly used for (biomedical) image segmentation. 

#Creation of two convolutional layers where the image is downsampled (reduced in size) to capture higher-level features
def down_block(x, filters, use_maxpool = True):
    x = Conv2D(filters, 3, padding= 'same')(x) #Applies a 2D convolution with kernel (filters) of typical CNN dimension 3x3
    x = BatchNormalization()(x) #Normalization
    x = LeakyReLU()(x) #Activation function, allowing small negative values compared to ReLU
    x = Conv2D(filters, 3, padding= 'same')(x) #Additional layer with same components
    x = BatchNormalization()(x)
    x = LeakyReLU()(x)
    if use_maxpool == True: 
        return  MaxPooling2D(strides= (2,2))(x), x #Reduces the spatial resolution (with a stride 2x2) of the feature maps
    else:
        return x

#Creation of two convolutional layers where the image is upsampled (increased in size) to reconstruct detailed features. y is the feature maps.
def up_block(x,y, filters): 
    x = UpSampling2D()(x) #Upsample the input feature map x
    x = Concatenate(axis = 3)([x,y]) #Concatenates the upsampled feature map with the corresponding feature map y
    x = Conv2D(filters, 3, padding= 'same')(x) #Applies a 2D convolution with kernel (filters) of typical CNN dimension 3x3
    x = BatchNormalization()(x)
    x = LeakyReLU()(x)
    x = Conv2D(filters, 3, padding= 'same')(x) #Additional layer with same components
    x = BatchNormalization()(x)
    x = LeakyReLU()(x)
    return x

#Building of the U-Net architecture and its components
def Unet(input_size = (256, 256, 3), *, classes, dropout):
    filter = [64,128,256,512, 1024] #list of filter sizes 
    # encode
    input = Input(shape = input_size) #defines the input size
    x, temp1 = down_block(input, filter[0]) #using the down_block function and storing intermediate feature maps from temp1 to temp4
    x, temp2 = down_block(x, filter[1])
    x, temp3 = down_block(x, filter[2])
    x, temp4 = down_block(x, filter[3])
    x = down_block(x, filter[4], use_maxpool= False) #Adding the final layer
    # decode 
    x = up_block(x, temp4, filter[3]) #Construction of the upsampling path using previous feature maps from downsampling
    x = up_block(x, temp3, filter[2])
    x = up_block(x, temp2, filter[1])
    x = up_block(x, temp1, filter[0])
    x = Dropout(dropout)(x) #Prevents overfitting
    output = Conv2D(classes, 1, activation= 'softmax')(x) #Predict class probabilities for each pixel
    model = models.Model(input, output, name = 'unet') #Construct the U-Net model
    model.summary()
    return model
if __name__ == '__main__': #Ensure direct execution
    model = Unet((224,224,3), classes= 2, dropout= 0.2)
    model.summary()

