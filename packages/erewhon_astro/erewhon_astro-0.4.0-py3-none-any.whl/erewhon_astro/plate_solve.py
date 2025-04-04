import json
import os
import subprocess
import tempfile
import time

import requests
from astroquery.astrometry_net import AstrometryNet
from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict
from astropy import wcs


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='../../.env', env_file_encoding='utf-8')


class Calibration(BaseModel):
    """Calibration model."""
    dec: float
    ra: float
    width_arcsec: float
    height_arcsec: float
    orientation: float
    parity: float
    pixscale: float
    radius: float = 0.0


class Annotation(BaseModel):
    """Annotation model."""
    type: str
    names: list[str]
    pixelx: float
    pixely: float
    radius: float

class AnnotationResponse(BaseModel):
    """Annotation response model."""
    status: str
    annotations: list[Annotation]

class Solution(BaseModel):
    """Solution model."""
    calibration: Calibration | None = None
    annotations: list[Annotation]
    job_id: int | None = None
    local_solve: bool = False


class PlateSolve(BaseSettings):
    """Plate solve model."""
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')

    astrometry_api_key: str = ''

    def solve(self, image_path, *, local_solve=False) -> Solution:
        """Solve plate for an image."""
        if local_solve:
            # todo : remove need for external script
            # We put temporary output in a temp directory
            # that gets cleaned up when done.
            with tempfile.TemporaryDirectory() as temp_dir:
                with tempfile.NamedTemporaryFile(mode='w+', delete=False) as temp_file:
                    output = subprocess.Popen(["solve-field",
                                               "--overwrite",
                                               "--no-plots",
                                               "--dir", temp_dir,
                                               "--wcs", temp_file.name,
                                               image_path],
                                              stdout=subprocess.PIPE,
                                              stderr=subprocess.DEVNULL).stdout.read()

                    lines = subprocess.Popen(["wcsinfo", temp_file.name], stdout=subprocess.PIPE).stdout.readlines()
                    values = {}
                    for line in lines:
                        k, v = line.decode().strip().split(" ")
                        values[k] = v

                    match values["fieldunits"]:
                        case "arcminutes":
                            field_scale = 60.0
                        case "arcseconds":
                            field_scale = 1.0
                        case "degrees":
                            field_scale = 3600.0
                        case _:
                            field_scale = 1.0

                    calibration = Calibration(
                        ra=float(values.get("crval0", 0)),
                        dec=float(values.get("crval1", 0)),
                        width_arcsec=field_scale * float(values.get("fieldw", 0)),
                        height_arcsec=field_scale * float(values.get("fieldh", 0)),
                        orientation=float(values.get("orientation", 0)),
                        parity=int(values.get("parity", 0)),
                        pixscale=float(values.get("pixscale", 0)),
                        # radius=float(values["radius"]),
                    )

                    output = subprocess.Popen(["plot-constellations",
                                               "-L",
                                               "-w", temp_file.name,
                                               "-N",
                                               "-J",
                                               "-B",
                                               ],
                                              stdout=subprocess.DEVNULL,
                                              stderr=subprocess.PIPE).stderr.read()
                    response = AnnotationResponse.model_validate_json(output)
                    print("Plot:", response)

                    return Solution(
                        local_solve=local_solve,
                        calibration=calibration,
                        annotations=response.annotations)

        # Create an Astroquery instance
        an = AstrometryNet()
        an.api_key = self.astrometry_api_key

        # Wait up to 5 minutes for the solution. (Once I move to local solver this should no longer be necessary.)
        wcs_header, submission_id = an.solve_from_image(image_path,
                                                        allow_commercial_use='n',
                                                        return_submission_id=True,
                                                        solve_timeout=300)

        job_id = None
        wait_count = 0
        processing_finished = None

        ## Wait for submission to complete...
        while not processing_finished and wait_count <= 5:
            response = requests.get(f'https://nova.astrometry.net/api/submissions/{submission_id}')
            submission = response.json()
            processing_finished = submission['processing_finished']
            if processing_finished:
                job_id = submission['jobs'][0]
            else:
                time.sleep(5)

        if not processing_finished:
            return None

        response = requests.get(f'https://nova.astrometry.net/api/jobs/{job_id}/annotations')
        annotations = response.json()['annotations']
        response = requests.get(f'https://nova.astrometry.net/api/jobs/{job_id}/calibration')
        calibration = response.json()

        return Solution(local_solve=True, job_id=job_id,
                        calibration=calibration, annotations=annotations)


if __name__ == "__main__":
    plate_solve = PlateSolve()
    solution = plate_solve.solve("test_images/test_image.jpg")
    print(solution)

# #!/usr/bin/env sh
#
# INPUT="$1"
# OUTPUT="./tmp.wcs"
#
# DIR="/opt/homebrew/Cellar/astrometry-net/0.97/data"
# if [ -r "/Volumes/T7 Shield/AstroPhotos/AstrometryData" ]; then
#     DIR="/Volumes/T7 Shield/AstroPhotos/AstrometryData"
# fi
#
# #echo "$0 Solving...."
# solve-field --overwrite              \
#             --no-plots               \
#             --index-dir  "$DIR"      \
#             --wcs        "$OUTPUT"   \
#             "$INPUT"
# #> /dev/null 2>&1
#
# #            --corr       none        \
# #            --new-fits   none        \
# #            --scamp      none        \
# #            --index-xyls none        \
# #            --axy        none        \
# #            --pnm        none        \
# #            --kmz        none        \
#
# if [ -r "$OUTPUT" ]; then
#   #echo "$0 Plotting constellations"
#   plot-constellations \
#       -L \
#       -w "$OUTPUT" \
#       -N \
#       -J \
#       -B \
#       -D \
#       -d /opt/homebrew/opt/astrometry-net/data/hd.fits \
#       2>&1 1>/dev/null
# else
#     echo '[]'
# fi
#
# #echo "$0 Done"
# #/bin/rm "$OUTPUT"
#
# # 2>&1 1>/dev/null | jq .annotations
