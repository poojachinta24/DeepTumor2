import cv2
import numpy as np
from tensorflow.keras.models import load_model
from PIL import Image
from keras.preprocessing.image import img_to_array

def predict(image_path):
    print(image_path)
    image = cv2.imread(image_path)

    # Read and process the saved image
    img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(img)

    # Resize the image to match the model's expected input size
    img = img.resize((64, 64))  # Replace with your model's input size

    # Convert the image to an array
    img_array = img_to_array(img)

    # Normalize the image array (if your model requires it)
    img_array = img_array / 255.0

    # Expand dimensions to match the input shape (batch size, height, width, channels)
    img_array = np.expand_dims(img_array, axis=0)

    # Load the pre-trained model
    model = load_model('tumor_detection_model.keras')

    # Make the prediction
    predictions = model.predict(img_array)

    # Determine the prediction result
    if predictions[0][0] >= 0.5:
        prediction = 'yes'
    else:
        prediction = 'no'

    # Output the prediction
    print(f'Tumor Prediction: {prediction}')
    return prediction