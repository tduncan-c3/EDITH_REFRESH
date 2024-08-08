#
# hello-python version 1.0.
#
# Copyright (c) 2020 Oracle, Inc.  All rights reserved.
# Licensed under the Universal Permissive License v 1.0 as shown at https://oss.oracle.com/licenses/upl.
#

import io
import json

from fdk import response

import cv2
import face_recognition
import requests
import urllib.request
import numpy as np

def handler(ctx, data: io.BytesIO=None):
    return response.Response(
        ctx, response_data=json.dumps(
            {"message": "Hello"}),
        headers={"Content-Type": "application/json"}
    )
