import requests
import urllib3
import logging
urllib3.disable_warnings()


log = logging.getLogger("rest")
json_headers = {"Content-type": "application/json;charset=UTF-8", "Accept": "application/json"}
REQ_TIMEOUT = 5


def invoke_api(
        url="",
        auth=None,
        token=None,
        json=True,
        method="GET",
        data='',
        timeout=REQ_TIMEOUT,
        headers={},
        return_headers=False):
    try:
        h = json_headers if json else ""

        if token is not None:
            ht = {"Authorization": "Bearer {}".format(token)}
            h = dict(h, **ht)

        if len(headers) > 0:
            h = dict(h, **headers)

        response = requests.request(
            method=method,
            url=url,
            data=data,
            headers=h,
            auth=auth,
            verify=False,
            timeout=timeout)
        response.raise_for_status()
        log.debug("Return: %s", str(response.status_code))
        data = response.json() if json and len(response.content) > 0 else response.content
        if return_headers:
            return data, response.headers
        else:
            return data
    except requests.exceptions.HTTPError as e:
        log.error(e)
        if e.response is not None:
            log.error(e.response)
        raise e
    except requests.exceptions.ConnectionError as e:
        log.error("Exception: %s on %s", e, url)
        raise e
    except requests.exceptions.Timeout as e:
        log.error("Request [%s] timed out", url)
        raise e
    except requests.exceptions.ConnectionError as e:
        log.error("Error connecting to  [%s]", url)
        raise e
