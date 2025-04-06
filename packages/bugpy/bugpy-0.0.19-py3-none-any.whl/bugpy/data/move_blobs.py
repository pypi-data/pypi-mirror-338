""" Functions for moving files between/within or deleting files from s3 buckets """

from bugpy.utils import multithread, get_credentials
from functools import partial
from io import BytesIO
import pandas as pd
import boto3
import os


def _delete_one_file(file, bucket, s3_client, verbose=False):
    """Deletes one file from s3"""

    try:
        s3_client.Object(bucket, file).delete()
    except Exception as e:
        if verbose:
            print("Delete error!")
            print(f"file: {file}")
            print(f"bucket: {bucket}")
        raise e


def _copy_one_file(input_file, from_bucket, to_bucket, prefix='', verbose=False):
    """For use in multithreaded processes - copies a file from one s3 bucket to another"""

    from_file, to_file = input_file
    copy_source = {
        'Bucket': from_bucket.name,
        'Key': from_file
    }

    try:
        to_bucket.copy(copy_source, os.path.join(prefix, to_file))
    except Exception as e:
        if verbose:
            print(f"input_file: {input_file}")
            print(f"copy_source: {copy_source}")
            print(f"to_file: {to_file}")
            print(f"from_file: {from_file}")
            print(f"to_bucket: {to_bucket}")
        raise e


def move_one_file(input_file, from_bucket, to_bucket, s3=None, prefix='', verbose=False, extension=None):
    """ Moves a file from one s3 bucket to another

        :param input_file: name of file to be moved
        :type input_file: str
        :param from_bucket: name of bucket to be moved from
        :type from_bucket: str
        :param to_bucket: either name of bucket to be moved to or s3 Bucket object for destination bucket
        :type to_bucket: str or boto3.Session().resource('s3').Bucket
        :param s3: s3 resource from boto3
        :type s3: boto3.Session().resource('s3')
        :param prefix: folder structure for destination if not same as origin
        :type prefix: str
        :param verbose: whether to be loud about it
        :type verbose: bool
    """

    if s3 is None:
        session = boto3.Session()
        s3 = session.resource('s3')
        s3_client = session.client("s3")

    if type(to_bucket) == str:
        to_bucket = s3.Bucket(to_bucket)

    if type(from_bucket) == str:
        from_bucket = s3.Bucket(from_bucket)

    from_file, to_file = input_file

    _copy_one_file(input_file, from_bucket, to_bucket, extension, prefix, verbose, s3_client)
    _delete_one_file(from_file, from_bucket, s3, verbose)


def copy_files(sourcelist, destlist, from_bucket, to_bucket, prefix=''):
    """ Copy a list of blobs from one bucket to another

        :param sourcelist: list of original files, from from_bucket root directory
        :param destlist: list of output locations for files, from to_bucket root directory
        :param from_bucket: the aws source bucket
        :param to_bucket: the aws destination bucket
        :param prefix: any desired folder prefix for output files, defaults to ''
        :return: list of filenames which failed to copy
    """

    if len(sourcelist) != len(destlist):
        raise Exception("sourcelist and destlist must be the same length!")

    s3 = boto3.resource('s3', aws_access_key_id=get_credentials('s3', 'API_KEY'),
                        aws_secret_access_key=get_credentials('s3', 'SECRET_KEY'),
                        endpoint_url=get_credentials('s3', 'ENDPOINT'))

    to_bucket = s3.Bucket(to_bucket)
    from_bucket = s3.Bucket(from_bucket)

    func = partial(_copy_one_file, from_bucket=from_bucket, to_bucket=to_bucket,
                   prefix=prefix)

    inputs = pd.Series(zip(sourcelist, destlist))

    failures, outputs = multithread(inputs, func,
                                    description=f"Copying files from {from_bucket.name} to {to_bucket.name}")

    if len(failures) > 0:
        print(f"Copied {len(inputs) - len(failures)} files with {len(failures)} failures.")

    return failures


def delete_files(filelist, bucket, s3=None):
    """ Delete files from s3

        :param filelist: the list of files to delete, from the bucket's root directory
        :param bucket: the aws bucket to delete files from
        :param s3: established s3 connection, autoconnects if None,defaults to None
        :return: list of files whic failed to delete
    """
    if s3 is None:
        session = boto3.Session()
        s3 = session.resource('s3')

    func = partial(_delete_one_file, bucket=bucket, s3_client=s3)

    failures, successes = multithread(filelist, func, description=f"Deleting files from {bucket}")

    if len(failures) > 0:
        print(f"Deleted {len(successes)} files with {len(failures)} failures.")

    return failures


def move_files(sourcelist, destlist, from_bucket, to_bucket, prefix='', s3=None, verbose=False):
    """ Move a list of blobs from one bucket to another

        :param sourcelist: list of original files, from from_bucket root directory
        :param destlist: list of output locations for files, from to_bucket root directory
        :param from_bucket: the aws source bucket
        :param to_bucket: the aws destination bucket
        :param prefix: any desired folder prefix for output files, defaults to ''
        :param s3: established s3 connection, autoconnects if None, defaults to None
        :param verbose: whether to be loud about it
        :return: list of files which failed to be moved
    """

    if s3 is None:
        session = boto3.Session()
        s3 = session.resource('s3')

    destbucket = s3.Bucket(to_bucket)

    func = partial(move_one_file, from_bucket=from_bucket, to_bucket=destbucket, s3=s3, prefix=prefix, verbose=verbose)

    inputs = pd.Series(zip(sourcelist, destlist))

    failures = multithread(inputs, func, description=f"Moving files from {from_bucket} to {to_bucket}")

    if len(failures) > 0:
        print(f"Moved {len(inputs) - len(failures)} files with {len(failures)} failures.")

    return failures
