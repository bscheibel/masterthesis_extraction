import organize_drawing_according_to_details_new
import order_bounding_boxes_in_each_block
import clustering_precomputed_dbscan
import read_from_clustered_merged
import regex_clean_new
import organize_drawing_according_to_details_new
import json
import redis
import sys

def write_redis(uuid, result, db_params):
    db = redis.Redis(db_params)
    db.set(uuid, result)


def main(uuid, filepath, db):
    filename = order_bounding_boxes_in_each_block.pdf_to_html(uuid, filepath)
    print(filename)
    result = order_bounding_boxes_in_each_block.get_bound_box(filename)  ##get coordinates+text out of html file into array of arrays
    isos = order_bounding_boxes_in_each_block.extract_isos(result)
    res = clustering_precomputed_dbscan.cluster_and_preprocess(result)
    clean_arrays = read_from_clustered_merged.read("/home/bscheibel/PycharmProjects/dxf_reader/temporary/values_clusteredfrom_precomputed_dbscan.csv")
    pretty = regex_clean_new.print_clean(clean_arrays)
    res = organize_drawing_according_to_details_new.main_function(pretty)
    #print(res)

    json_isos = json.dumps(isos)
    json_result = json.dumps(res)
    write_redis(uuid+"dims", json_result, db)
    write_redis(uuid+"isos",json_isos, db)
    #print(redis.Redis('localhost').get(uuid+"dims"))
    #print(result)

if __name__ == "__main__":
    uuid = sys.argv[1]
    filename = sys.argv[2]
    db = sys.argv[3]
    main(uuid,filename, db)

#main("33333", "/home/bscheibel/PycharmProjects/dxf_reader/drawings/GV_12.PDF", "localhost")
