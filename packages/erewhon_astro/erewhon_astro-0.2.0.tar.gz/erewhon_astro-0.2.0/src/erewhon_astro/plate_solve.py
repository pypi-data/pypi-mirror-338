import json
import subprocess
import time

import requests
from astroquery.astrometry_net import AstrometryNet
from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


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
    radius: float


class Annotation(BaseModel):
    """Annotation model."""
    type: str
    names: list[str]
    pixelx: float
    pixely: float
    radius: float

class Solution(BaseModel):
    """Solution model."""
    calibration: Calibration | None = None
    annotations: list[Annotation]


class PlateSolve(BaseSettings):
    """Plate solve model."""
    model_config = SettingsConfigDict(env_file='../../.env', env_file_encoding='utf-8')

    astrometry_api_key: str = ''

    def solve(self, image_path, *, local_solve=False) -> Solution:
        """Solve plate for an image."""
        if local_solve:
            # todo : remove need for external script
            output = subprocess.Popen(["./scripts/solve.sh", image_path], stdout=subprocess.PIPE).stdout.read()
            print(f"Output: {output}")
            _json = json.loads(output)
            return Solution(annotations=_json["annotations"])

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

        return Solution(calibration=calibration, annotations=annotations)

if __name__ == "__main__":
    plate_solve = PlateSolve()
    solution = plate_solve.solve("test_images/test_image.jpg")
    print(solution)