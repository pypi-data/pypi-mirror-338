# README

This directory hosts code and intermediate data for downloading missing Sentinel-2 L2A from Google Cloud Storage (GCS).

## General Procedure

0. This assumes the existence of a `gsutil` in the system and the account running this procedure should logged into google cloud.

    Please refer to [documentation](https://cloud.google.com/storage/docs/gsutil_install) of `gsutil`
    for installation, registration, and logged in.

1. Run `fetch_metadata.py` to create the metadata sqlite database for available Sentinel-2 L2A scenes in Google Cloud Storage.

    Run the following command `python fetch_metadata.py` to download and
    save the sqlite database in the file path `<current-working-directory>/metadata/sentinel2_l2a_gcs.sqlite.db`

    Or Run `python fetch_metadata.py --help` for more controlling options.

2. Run `query_metadata.py` to examine number of scenes that need to be downloaded.

    For example, you can use the following command to query all scenes that are available in GCS for tile T48RVV
    in date period 2021-01-01 to present, with cloud cover less than 70%.

    ```bash
    python query_metadata.py by-tile T48RVV 2021-01-01 None --cloud-cover-upper 70
    ```

    You can also use the script with `by-zone`, `by-zones`, `by-location` sub-command for other commonly used queries.
    Please run `python query_metadata.py [sub-command] --help` to check more controlling options for each sub-command.

3. Run `download_images.py` to download designated scenes.

    For example, you can use the following command to download all scenes that are available in GCS for tile T48RVV
    in date period 2021-01-01 to present, with cloud cover less than 70%, to the directory `/NAS/sentinel2` and skipping existing scenes,
    and save downloading status files to `<current-working-directory>/status`.

    ```bash
    python download_metadata.py by-tile T48RVV 2021-01-01 None --cloud-cover-upper 70 --skip-exist True --dir-dest /NAS/sentinel2 --dir-status ./status --dry-run False
    ```

    You can also use the script with `by-zone`, `by-zones`, `by-location` sub-command for other commonly used queries.
    Please run `python download_images.py [sub-command] --help` to check more controlling options for each sub-command.
