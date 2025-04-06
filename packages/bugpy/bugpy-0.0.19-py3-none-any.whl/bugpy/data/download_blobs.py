""" Functions for pulling data from s3 """

import os
from functools import partial
import boto3
import pandas as pd
from .tools import client_connect, resource_connect, flatten_filepath, join_filepath
import io
import librosa

from bugpy.utils import multithread, add_directory_to_fileseries

def find_missing(filelist, directory) -> list:
    """ Identifies files that exist in filelist but not in directory

        :param filelist: list of files to be found
        :type filelist: pandas.Series or list
        :param directory: directory to find them in
        :return: files which exist in the filelist but not in the directory
    """

    if type(filelist) == pd.Series:
        filelist = filelist.values
    full_filelist = pd.DataFrame(filelist, columns=['s3_loc'])
    full_filelist['local'] = add_directory_to_fileseries(directory, full_filelist['s3_loc'])

    downloaded_files = [join_filepath(dp, f) for dp, dn, fn in os.walk(os.path.expanduser(directory)) for f in fn]

    missing = set(full_filelist['local']).difference(downloaded_files)
    full_filelist = full_filelist[full_filelist['local'].isin(missing)]

    return list(full_filelist['s3_loc'])

def download_one_file(s3_filename: str, bucket: str, output: str, s3_client=None,
                      flatten_filestructure=False, reconnect=True, serial=True) -> str:
    """ Download a single file from S3

        :param s3_filename: S3 object name
        :param bucket : S3 bucket where files are hosted
        :param output: Dir to store the files
        :param s3_client: S3 client
        :type s3_client: boto3.client
        :param flatten_filestructure: determines whether directory structure is recreated or flattened
        :param reconnect: whether to attempt to create a new s3 session
        :param serial: whether this function will be run serially or in multithreaded
        :return: path of downloaded file
    """
    if reconnect or s3_client is None:
        s3_client = client_connect()

    if flatten_filestructure:
        s3_savename = flatten_filepath(s3_filename)
    else:
        folders = os.path.split(s3_filename)[0]
        if not os.path.isdir(join_filepath(output, folders)):
            os.makedirs(join_filepath(output, folders))
        s3_savename = s3_filename

    output_file = join_filepath(output, s3_savename)

    if serial:
        try:
            s3_client.download_file(
                Bucket=bucket, Key=s3_filename, Filename=output_file
            )
        except Exception as e:
            print(f"Error in downloading {bucket + '/' + s3_filename} to {output_file}")
            print(e)
    else:
        s3_client.download_file(
            Bucket=bucket, Key=s3_filename, Filename=output_file
        )

    return output_file


def _build_download_dirs(filelist, output):
    folders = filelist.str.rsplit('/', n=1).str[0].unique()
    for folder in folders:
        if not os.path.isdir(join_filepath(output, folder)):
            os.makedirs(join_filepath(output, folder))


def collect_one_from_bucket(file_location, bucket):
    """ Stream an object from an s3 bucket

        :param file_location: location on s3
        :type file_location: str
        :param bucket: name of the s3 bucket to collect from, or Bucket object
        :type bucket: str or boto3.resource('s3').Bucket
        :return: body of streamed file (varies depending on filetype)
    """
    if type(bucket) == str:
        s3_resource = resource_connect()
        bucket = s3_resource.Bucket(bucket)

    file_object = bucket.Object(file_location)

    response = file_object.get()
    file_stream = response['Body']

    return file_stream

def stream_one_audiofile(file_location, bucket, desired_sr=None):
    file_stream = collect_one_from_bucket(file_location, bucket)
    audio_bytes = io.BytesIO(file_stream.read())
    sr = {}
    if desired_sr is not None:
        sr['sr']=desired_sr
    audio, sr = librosa.load(audio_bytes, **sr)

    return audio, sr


def download_filelist(filelist, output_dir, aws_bucket, flatten_filestructure=False, redownload=False) -> list:
    """ Downloads an iterable list of filenames

        :param filelist : iterable of filenames in blob storage to be downloaded
        :type filelist: list
        :param output_dir: dir to store the files
        :type output_dir: str
        :param flatten_filestructure: determines whether directory structure is recreated or flattened
        :type flatten_filestructure: bool
        :param redownload: determines whether files should be redownloaded
        :type redownload: bool
        :param aws_bucket: name of bucket to download from
        :type aws_bucket: str
        :return: list of files which failed to download
    """

    session = boto3.Session()
    client = session.client("s3")

    filelist = pd.Series(filelist).dropna()
    filelist = filelist.drop_duplicates()
    filelist = filelist[filelist != '']

    # The client is shared between threads
    func = partial(download_one_file, bucket=aws_bucket, output=output_dir, s3_client=client,
                   flatten_filestructure=flatten_filestructure, reconnect=False, serial=False)

    if redownload:
        files_to_download = filelist
    else:
        files_to_download = find_missing(filelist, output_dir)
        if len(filelist) > len(files_to_download):
            print(f"Some files already downloaded, downloading {len(files_to_download)} new files")
        else:
            print(f"Downloading {len(files_to_download)} new files")

    if len(files_to_download) == 0:
        return []

    if not flatten_filestructure:
        _build_download_dirs(pd.Series(files_to_download), output_dir)

    failed_downloads, _ = multithread(files_to_download,
                                      func,
                                      description="Downloading files from S3",
                                      retry=True)

    print(f"Successfully downloaded {len(files_to_download) - len(failed_downloads)} files.")

    if len(failed_downloads) > 0:
        print(f"WARNING! There were {len(failed_downloads)} failed downloads!")
        return failed_downloads

    return []
