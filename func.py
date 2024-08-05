#
# hello-python version 1.0.
#
# Copyright (c) 2020 Oracle, Inc.  All rights reserved.
# Licensed under the Universal Permissive License v 1.0 as shown at https://oss.oracle.com/licenses/upl.
#

import io
import json

from fdk import response

import requests
bucket_url = 'https://objectstorage.us-chicago-1.oraclecloud.com/p/j8d1ZFSVLZnXbJM07BW4ogJg-TEyu9uwb0or5vGoBPSRgDbyI2aj7lMynpBZ5rMw/n/axnwnsavbb9n/b/vision_service/o/'

def handler(ctx, data: io.BytesIO=None):
    print("Entering Python Hello World handler", flush=True)
    name = "World"
    try:
        body = json.loads(data.getvalue())
        name = body.get("name")
    except (Exception, ValueError) as ex:
        print(str(ex), flush=True)

    try:
        r = requests.get(bucket_url)
        objects = r.json()['objects']
    except Exception as requestError:
        return response.Response(
            ctx, response_data=json.dumps(
                {"RequestError": str(requestError)}),
            headers={"Content-Type": "application/json"}
        )

    for object in objects:
        try:
            name = bucket_url + object['name'].replace(' ', '%20')
        except Exception as e:
            return response.Response(
                ctx, response_data=json.dumps(
                    {"EncodingError": str(e)}),
                headers={"Content-Type": "application/json"}
            )

    print("Vale of name = ", name, flush=True)
    print("Exiting Python Hello World handler", flush=True)
    return response.Response(
        ctx, response_data=json.dumps(
            {"message": "Hello {0}".format(name)}),
        headers={"Content-Type": "application/json"}
    )

# import io
# import json
# # from flask import Flask, jsonify, request

# # import cv2
# # import face_recognition
# # import urllib.request
# # import numpy as np
# # import requests
# # import base64
# # from PIL import Image
# # import io
# from fdk import response

# # known_face_encodings = []
# # known_face_names = []
# # bucket_url = 'https://objectstorage.us-chicago-1.oraclecloud.com/p/j8d1ZFSVLZnXbJM07BW4ogJg-TEyu9uwb0or5vGoBPSRgDbyI2aj7lMynpBZ5rMw/n/axnwnsavbb9n/b/vision_service/o/'

# def handler(ctx, data: io.BytesIO=None):  
#     # try:
#     #     try:
#     #         r = requests.get(bucket_url)
#     #         objects = r.json()['objects']
#     #     except Exception as requestError:
#     #         # return jsonify({"RequestError": str(requestError)}), 400
#     #         return response.Response(
#     #             ctx, response_data=json.dumps(
#     #                 {"RequestError": str(requestError)}),
#     #             headers={"Content-Type": "application/json"}
#     #         )

#     #     for object in objects:
#     #         try:
#     #             bucketImage = urllib.request.urlopen(bucket_url + object['name'].replace(' ', '%20'))
#     #             arr = np.asarray(bytearray(bucketImage.read()), dtype=np.uint8)
#     #             img = cv2.imdecode(arr, -1)
#     #             rgb_img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#     #             img_encoding = face_recognition.face_encodings(rgb_img2)[0]
#     #             known_face_encodings.append(img_encoding)
#     #             known_face_names.append(object['name'])
#     #         except Exception as e:
#     #             # return jsonify({"EncodingError": str(e)}), 400
#     #             return response.Response(
#     #                 ctx, response_data=json.dumps(
#     #                     {"EncodingError": str(e)}),
#     #                 headers={"Content-Type": "application/json"}
#     #             )

#     #     try:
#     #         np.save('known_face_encodings.npy', known_face_encodings)
#     #     except Exception as faceEncodingfileError:
#     #         # return jsonify({"FaceEncodingFileError": str(faceEncodingfileError)}), 400
#     #         return response.Response(
#     #             ctx, response_data=json.dumps(
#     #                 {"FaceEncodingFileError": str(faceEncodingfileError)}),
#     #             headers={"Content-Type": "application/json"}
#     #         )
#     #     try:
#     #         with open("known_face_names.txt", "w") as txt_file:
#     #             for line in known_face_names:
#     #                 txt_file.write(line + "\n")
#     #     except Exception as faceNamefileError:
#     #         # return jsonify({"FaceNameFileError": str(faceNamefileError)}), 400
#     #         return response.Response(
#     #             ctx, response_data=json.dumps(
#     #                 {"FaceNameFileError": str(faceNamefileError)}),
#     #             headers={"Content-Type": "application/json"}
#     #         )
#     #     # response = jsonify({"status": "completed"})
#     #     # return response
#     #     return response.Response(
#     #         ctx, response_data=json.dumps(
#     #             {"status": "completed"}),
#     #         headers={"Content-Type": "application/json"}
#     #     )
#     # except Exception as genErr:
#         # return response.Response(
#         #     ctx, response_data=json.dumps(
#         #         {"genErr": str(genErr)}),
#         #     headers={"Content-Type": "application/json"}
#         # )