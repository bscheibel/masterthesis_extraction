import read_data
import read_text_lines
import merge_pandas



file = "drawings/GV_12.DXF"
file_out = "GV12_extracted.csv"
read_text_lines.read(file, file_out)
read_data.read_dimensions(file_out)