import gzip
import shutil


def decompress_gz_file(gz_file_path , out_uncompressed_file_path) :
    with gzip.open(gz_file_path , 'rb') as f_in :
        with open(out_uncompressed_file_path , 'wb') as f_out :
            shutil.copyfileobj(f_in , f_out)
    print(f"Decompressed {gz_file_path} to {out_uncompressed_file_path}")
