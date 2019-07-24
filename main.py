import read_data
import read_text_lines
#import merge_pandas



file = "drawings/5129275.dxf"
file_out = "5129275_extracted.csv"
read_text_lines.read(file, file_out)
read_data.read_dimensions(file_out, 0)