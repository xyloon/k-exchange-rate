# k-exchange-rate

## how to use

* get API key from this [site](https://www.koreaexim.go.kr/site/program/openapi/openApiView?menuid=001003002002001&apino=2&viewtype=C)
* Install required package
    ```bash
    pip install -r requirements.txt
    ```
* Execution
    ```bash
    python kexr/exec.py --start-date 2018-01-02 --end-date 2018-01-02 --key THE_KEY_YOU_HAVE_GOT_FROM_KOREAEXIM_SITE --dbfile THE_DBFILE_PATHNAME_YOU_WANT_USE
    ```