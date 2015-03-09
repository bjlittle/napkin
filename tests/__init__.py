from cartopy.tests.mpl import ImageTesting
import os


ImageTesting.root_image_results = os.path.dirname(__file__)
ImageTesting.image_output_directory = os.path.join(os.path.dirname(__file__),
                                                   'result_images')
