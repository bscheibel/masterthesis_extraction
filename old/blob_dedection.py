import text_to_image
encoded_image_path = text_to_image.encode_file("/home/bscheibel/PycharmProjects/engineering_drawings_extraction/drawings/5129275_Rev01-GV12.txt", "output_image.png")

import imgkit
imgkit.from_file('/home/bscheibel/PycharmProjects/engineering_drawings_extraction/drawings/5129275_Rev01-GV12.html', 'out.jpg')