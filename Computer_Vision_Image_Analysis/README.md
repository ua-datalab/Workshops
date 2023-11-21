# Computer Vision: Image Analysis

## Why Computer Vision (CV)?

In today's technological landscape, the implementation of Computer Vision (CV) stands as a transformative force, wielding a myriad of possibilities and advancements across diverse domains. Its applicability spans a wide spectrum, from [bolstering medical diagnostics by swiftly analyzing MRI scans](https://www.nature.com/articles/d41586-023-03482-9) to [fortifying autonomous vehicles with the vision to navigate complex terrains](https://www.nytimes.com/2023/08/21/technology/waymo-driverless-cars-san-francisco.html). 

Computer Vision has already made significant strides, revolutionizing fields like [retail through automated checkout systems](https://towardsdatascience.com/how-the-amazon-go-store-works-a-deep-dive-3fde9d9939e9) and [facial recognition for enhanced security measures](https://www.tsa.gov/news/press/factsheets/facial-recognition-technology). It holds the promise of simplifying daily life, automating tasks such as fruit recognition for sorting in agriculture or enhancing augmented reality experiences for immersive interactions. 

Yet, this dynamic field bears its challenges, as interpreting and understanding visual data under varying conditions remains intricate, while also offering accessible tools and methods for those delving into its realm. From the ease of leveraging Python libraries like [OpenCV](https://opencv.org/), known for its robust image processing capabilities, to the deep learning prowess of [TensorFlow](https://www.tensorflow.org/) and [PyTorch](https://pytorch.org/) for intricate neural network designs, aspiring graduates and computer engineering enthusiasts have an array of sophisticated tools at their disposal. 

The flexibility and accessibility of these libraries render the entry into Computer Vision both engaging and intellectually stimulating, fostering a rich ground for exploration and innovation among budding professionals.

### Challenges

In the realm of Computer Vision, an array of challenges persists, transcending both classical and CNN approaches. 

- **Variability and Invariance**: Images vary significantly in terms of lighting, object poses, backgrounds, and other environmental factors. *Example*: Using images of apples taken in various lighting conditions (bright sunlight, dim indoor light, and shadowed areas).

- **Object Recognition and Classification**: Accurately recognizing and categorizing objects within images, especially in cluttered scenes or for fine-grained recognition. *Example*: Presenting images of apples placed amidst a cluttered environment with other fruits or objects.

- **Semantic Understanding and Context**: Understanding the context and semantics of images, including distinguishing objects and their relationships. Example: Showcasing images where apples are placed in diverse contexts: some in a fruit bowl, some on a tree, and some in a kitchen setting. 

- **Data Annotation and Labeling**: Annotating and labeling large datasets for training deep learning models is particularly challenging for CNNs. This includes the need for large volumes of accurately labeled data, which is essential for training CNNs. *Example*: Providing datasets of various apple varieties, sizes, and conditions (ripe, unripe, different colors). 

- **Interpretability of AI Models**: Creating AI models that can explain their decision-making processes is more pertinent to CNNs. Ensuring interpretability, especially in critical applications like healthcare and autonomous vehicles, is an essential challenge for deep learning models. *Example*: Showcasing how a CNN model identifies apples in images and discussing the challenge of explaining why the model identified specific regions or features as apples. 

## A Classical Approach to Computer Vision

One of the most popular libraries of classical CV is [OpenCV](https://opencv.org/). OpenCV works alongside [NumPy](https://numpy.org/), used to quantify the image files and apply changes. Initially developed by Intel, OpenCV had first been given the [open-source BSD Licence](https://github.com/opencv/opencv/blob/4.4.0/LICENSE) (versions <=4.4.0), then the [Apache Licence](https://github.com/opencv/opencv/blob/master/LICENSE) (versions >=4.5.0) allowing the software to maintain an Open status and be open source.

OpenCV focuses on the manipulation and image processing prior to extracting information. As a library, OpenCv is extensively used today in well established pipelines of object detection, as it helps with preparing and modifying images for more modern methods of CV such as CNN. Among other functions, OpenCV can be used for [image filtering](https://docs.opencv.org/4.x/d4/d86/group__imgproc__filter.html), transformations ([geometric](https://docs.opencv.org/4.x/da/d54/group__imgproc__transform.html), [miscellaneous](https://docs.opencv.org/4.x/d7/d1b/group__imgproc__misc.html)), [motion analysis and object tracking](https://docs.opencv.org/4.x/d7/df3/group__imgproc__motion.html), [image segmentation](https://docs.opencv.org/4.x/d3/d47/group__imgproc__segmentation.html), and [feature](https://docs.opencv.org/4.x/dd/d1a/group__imgproc__feature.html) and [object](https://docs.opencv.org/4.x/df/dfb/group__imgproc__object.html) detection. 

In the example Jupyter Notebook, we use OpenCV to count and detect objects (i.e. apples) in an image. To achieve this, OpenCV is used in such a manner where the edges of an object are detected first and then the object is counted. This process involves the following steps:

1. Convert image to black and white. Since our goal is to count still objects in an image, the conversion to black and white helps with removing not needed features (colors). 
2. Blurring the image using [Gaussian Blur](https://en.wikipedia.org/wiki/Gaussian_blur): this helps with the reduction of noise in the image 
    
    ![gaussian](https://docs.opencv.org/4.x/gaussian.jpg)
3. Finding the edges of the blurred objects using the [Canny edge detector](https://en.wikipedia.org/wiki/Canny_edge_detector) 
    
    ![canny](https://docs.opencv.org/4.x/canny1.jpg)
4. Finding and counting the contours of the objects 
    
    ![contour](https://docs.opencv.org/4.x/approx.jpg)

## Implementing Convolutional Neural Networks (CNN) to CV

CNNs are widely used in computer vision tasks like image classification, object detection, and segmentation. Revisiting CNN:

- CNNs are a class of deep neural networks designed for processing **grid-like data**, primarily used for image analysis.
- They consist of *layers* that automatically learn *hierarchical features* from input data, reducing the need for manual feature engineering.
- Convolutional layers use learnable filters to extract features from local regions of the input.
- Pooling layers downsample feature maps, preserving important information and reducing spatial dimensions.
- Fully connected layers at the end of the network make class predictions based on the learned features.
- They excel at capturing intricate patterns and are robust to variations like object positioning in images.
- Benefits include hierarchical feature learning, translation invariance, scalability, and state-of-the-art performance in visual tasks.
- CNNs have transformed how we approach image analysis, automating feature extraction and enabling end-to-end learning.

![CNN](https://miro.medium.com/v2/resize:fit:720/format:webp/1*kkyW7BR5FZJq4_oBTx3OPQ.png)

(image credits: [Towards Data Science](https://towardsdatascience.com/convolutional-neural-networks-explained-9cc5188c4939). Original image developed by [MathWorks](https://www.mathworks.com/videos/introduction-to-deep-learning-what-are-convolutional-neural-networks--1489512765771.html))

### Explaining the Layers
#### The Convolutional Layer

The convolutional layer is a fundamental component of CNNs designed to efficiently process grid-like data, such as images. It plays a crucial role in extracting meaningful features from input data through the application of convolution operations, which use filters (kernels) to scan across the input creating feature maps from the original image.

![con_layer1](https://i.stack.imgur.com/Bxix6.png)

(image source: [StackOverflow](https://stackoverflow.com/questions/51008505/kernels-and-weights-in-convolutional-neural-networks))

![con_layer2](https://upload.wikimedia.org/wikipedia/commons/1/19/2D_Convolution_Animation.gif)

(image credits: *Convolution*, [Wikipedia](https://en.wikipedia.org/wiki/Convolution))

In the figure above, a 3x3 kernel is applied to the values of the image. This is called a **convolutional operation** and the resulting output is referred as a **feature map**.

An additional layer, Rectified Linear Unit (ReLU) replaces negative pixes with zeroes.

#### The Pooling Layer

The Pooling Layer is often also called the downsampling layer, as it reduces the spatial size of the image. This helps with retaining important features and lowering the complexity of the image. Pooling can help with preventing overfitting by "summarizing a region" and overall computational efficiencty by reducing the computational requirements.

#### Flattening and Fully Connected Layers

The **Flattening layer** converts the 2D feature maps into a 1D vector. This transformation prepares the extracted features for input to the **fully connected layers**, which make global predictions based on the flattened features. Neurons in these layers are connected to all neurons from the previous layer. 

![flat](https://miro.medium.com/v2/resize:fit:720/format:webp/1*IWUxuBpqn2VuV-7Ubr01ng.png)

(image credits: *The Most Intuitive and Easiest Guide for Convolutional Neural Network*, [Towards Data Science](https://towardsdatascience.com/the-most-intuitive-and-easiest-guide-for-convolutional-neural-network-3607be47480))

---

## Diving Deeper in Computer Vision

- **OpenCV**: 
    - OpenCV can also be used for video processing, the OpenCV website offers some tutorials in the Other tutorials section:
        - [How to use Background Subtraction Methods](https://docs.opencv.org/4.x/d3/dd5/tutorial_table_of_content_other.html)
        - [Meabshift and Camshift](https://docs.opencv.org/4.x/d7/d00/tutorial_meanshift.html)
        - [Optical Flow](https://docs.opencv.org/4.x/d4/dee/tutorial_optical_flow.html)
    - [A good step by step how-to on video analysis using OpenCV by Kardi Teknomo](https://people.revoledu.com/kardi/tutorial/Python/Video+Analysis+using+OpenCV-Python.html)
    - [Video Data Processing with Python and OpenCV](https://www.youtube.com/watch?v=AxIc-vGaHQ0)

- **CNN**:
    - [What are Convolutional Neural Networks?](https://www.youtube.com/watch?v=QzY57FaENXg) An accessible and simple explananation of CNN
    - [How convolutional neural networks work, in depth](https://www.youtube.com/watch?v=JB8T_zN7ZC0) A more advanced video explanining CNN
    - [But what is convolution?](https://www.youtube.com/watch?v=KuXjwB4LzSA) Popular science and math YouTuber 3Blue1Brown covering the topic of convolution

[Paperswithcode offers an excellent section on real life applications of CV.](https://paperswithcode.com/methods/area/computer-vision)