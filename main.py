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


def main(uuid, filepath, db, eps):
    filename = order_bounding_boxes_in_each_block.pdf_to_html(uuid, filepath)
    #print(filename)
    result, number_blocks, number_words= order_bounding_boxes_in_each_block.get_bound_box(filename)  ##get coordinates+text out of html file into array of arrays
    if eps == '0':
        if number_words > 500:
            eps = 7
        else:
            eps = 1
    #print(eps)
    isos = order_bounding_boxes_in_each_block.extract_isos(result)
    res = clustering_precomputed_dbscan.cluster_and_preprocess(result,eps)
    clean_arrays = read_from_clustered_merged.read("/home/bscheibel/PycharmProjects/dxf_reader/temporary/values_clusteredfrom_precomputed_dbscan.csv")
    tables = order_bounding_boxes_in_each_block.get_tables(clean_arrays)
    pretty = regex_clean_new.print_clean(clean_arrays)
    res, details_dict = organize_drawing_according_to_details_new.main_function(pretty, tables)
    #print(res)

    json_isos = json.dumps(isos)
    json_result = json.dumps(res)
    json_details =json.dumps(details_dict)
    write_redis(uuid+"dims", json_result, db)
    write_redis(uuid+"isos",json_isos, db)
    write_redis(uuid+"eps", str(number_blocks)+","+str(number_words), db)
    write_redis(uuid+"details",json_details ,db)
    #print(json_details)
    #print(redis.Redis('localhost').get(uuid+"dims"))
    #print(result)

if __name__ == "__main__":
    uuid = sys.argv[1]
    filename = sys.argv[2]
    db = sys.argv[3]
    eps = sys.argv[4]
    main(uuid,filename, db, eps)

#main("33333", "/home/bscheibel/PycharmProjects/dxf_reader/drawings/5152166_Rev04.pdf", "localhost",3)
