import order_bounding_boxes_in_each_block
import clustering_precomputed_dbscan
import read_from_clustered_merged
import regex_clean_new
import organize_drawing_according_to_details_new
import json
import redis
import sys

def write_redis(uuid, result, db_params):
    #db = redis.Redis(unix_socket_path='/tmp/redis.sock',db=7)
    db = redis.Redis("localhost")
    db.set(uuid, result)


def main(uuid, filepath, db, eps):
    #db = redis.ConnectionPool(connection_class=redis.UnixDomainSocketConnection, path="/tmp/redis.sock")

    #db  = redis.Redis(unix_socket_path='/tmp/redis.sock')


    #path = "/home/centurio/Projects/engineering_drawings_extraction"
    path = "/home/bscheibel/PycharmProjects/engineering_drawings_extraction"
    filename = order_bounding_boxes_in_each_block.pdf_to_html(uuid, filepath, path)
    #print(filename)
    result, number_blocks, number_words= order_bounding_boxes_in_each_block.get_bound_box(filename)  ##get coordinates+text out of html file into array of arrays
    print("words:" + str(number_words),"blocks:" + str(number_blocks))
    if eps == '0':
        if number_words > 500:
            eps = 7
        else:
            eps = 1
    isos, general_tol = order_bounding_boxes_in_each_block.extract_isos(result)
    print(general_tol)
    res = clustering_precomputed_dbscan.cluster_and_preprocess(result,eps, path)
    clean_arrays = read_from_clustered_merged.read(path+"/temporary/values_clusteredfrom_precomputed_dbscan.csv")
    tables = order_bounding_boxes_in_each_block.get_tables(clean_arrays)
    pretty = regex_clean_new.print_clean(clean_arrays)
    res, details_dict = organize_drawing_according_to_details_new.main_function(pretty, tables)

    json_isos = json.dumps(isos)
    json_result = json.dumps(res)
    json_details =json.dumps(details_dict)
    write_redis(uuid+"tol", general_tol,db)
    write_redis(uuid+"dims", json_result, db)
    write_redis(uuid+"isos",json_isos, db)
    write_redis(uuid+"eps", str(number_blocks)+","+str(number_words), db)
    write_redis(uuid+"details",json_details ,db)


if __name__ == "__main__":
    uuid = sys.argv[1]
    filename = sys.argv[2]
    db = sys.argv[3]
    eps = sys.argv[4]
    main(uuid,filename, db, eps)

#main("33333", "/home/centurio/Projects/engineering_drawings_extraction/drawings/5152166_Rev04.pdf", "'/tmp/redis.sock', db=7",3)
