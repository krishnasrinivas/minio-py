# -*- coding: utf-8 -*-
# Minio Python Library for Amazon S3 compatible cloud storage, (C) 2015 Minio, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from minio import Minio

__author__ = 'minio'

client = Minio('https://s3.amazonaws.com',
               access_key='YOUR-ACCESSKEYID',
               secret_key='YOUR-SECRETACCESSKEY')

# List all objects in bucket
objects = client.list_objects('my-bucket')
for obj in objects:
    print obj.bucket, obj.key, obj.last_modified, obj.etag, obj.size, obj.content_type

# List all objects in bucket that begin with hello
objects = client.list_objects('my-bucket', prefix='hello')
for obj in objects:
    print obj.bucket, obj.key, obj.last_modified, obj.etag, obj.size, obj.content_type

# List all object paths in bucket that begin with hello up to the first / after hello
# e.g.
# hello/object
# hello/dir/

objects = client.list_objects('my-bucket', prefix='hello/', recursive=False)
for obj in objects:
    print obj.bucket, obj.key, obj.last_modified, obj.etag, obj.size, obj.content_type
