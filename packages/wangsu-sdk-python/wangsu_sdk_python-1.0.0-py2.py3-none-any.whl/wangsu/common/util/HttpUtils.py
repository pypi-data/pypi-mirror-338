import logging
import requests
from requests.exceptions import RequestException

logger = logging.getLogger(__name__)


class HttpUtils:

    @staticmethod
    def call(request_msg):
        response = None
        try:
            headers = request_msg.headers
            method = request_msg.method
            url = request_msg.url
            body = request_msg.body

            if method == 'POST':
                response = requests.post(url, headers=headers, data=body)
            elif method == 'GET':
                response = requests.get(url, headers=headers)
            elif method == 'PUT':
                response = requests.put(url, headers=headers, data=body)
            elif method == 'DELETE':
                response = requests.delete(url, headers=headers)
            else:
                logger.error(f"not support this http method : {method}")
                return None

            response.raise_for_status()
            return response.text

        except RequestException as e:
            request_id = response.headers.get('x-cnc-request-id')
            logger.error(f"unexpected HTTP status code: {response.status_code}, request_id:{request_id}, response:{response.text}")
            return response.content.decode('utf-8')
