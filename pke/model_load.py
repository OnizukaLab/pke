from gensim.models.wrappers import FastText
import zipfile

def fasttext_load(model_file):
    if model_file[-4:] == '.bin':
            model = FastText.load_fasttext_format(model_file)

    elif model_file[-4:] == '.zip':
        with zipfile.ZipFile(model_file) as existing_zip:
            filename = existing_zip.namelist()
            bin_filelist = [ f for f in filename if f[-4:] == '.bin' ]
            bin_file = existing_zip.extract(bin_filelist[0])
            model = FastText.load_fasttext_format(bin_file)
            
    return model