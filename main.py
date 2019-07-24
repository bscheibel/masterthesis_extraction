import read_data
import read_text_lines
#import merge_pandas



file = "drawings/5152166.dxf"
file_out = "5152166_extracted.csv"
read_text_lines.read(file, file_out)
read_data.read_dimensions(file_out, 0)