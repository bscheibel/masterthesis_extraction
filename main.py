import read_text_lines
import merge_pandas
import read_data

drawing = "drawings/Stahl_Adapterplatte.DXF"
file_out = "temporary/extracted_Stahladapter.csv"
#file_out = "temporary/extracted_GV_12.csv"
#file_out = "temporary/extracted_Laeufer.csv"
#read_text_lines.read(drawing, file_out)
#merge_pandas.merge_lines(file_out)
read_data.read_dimensions(file_out, 0)