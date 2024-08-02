import json
import sys
from typing import List

import typer


import steampipe_alchemy
from steampipe_alchemy import all_models, AwsConfig, models

app = typer.Typer(pretty_exceptions_enable=False)

all_regions = [
    "ap-south-1",
    "eu-north-1",
    "eu-west-3",
    "eu-west-2",
    "eu-west-1",
    "ap-northeast-3",
    "ap-northeast-2",
    "ap-northeast-1",
    "ca-central-1",
    "sa-east-1",
    "ap-southeast-1",
    "ap-southeast-2",
    "eu-central-1",
    "us-east-1",
    "us-east-2",
    "us-west-1",
    "us-west-2",
]

@app.command()
def main(
    profile: str = typer.Option('default'),
    regions: str = typer.Argument(all_regions),
):
    steam = steampipe_alchemy.SteamPipe()
    steam.update_config(
        aws=AwsConfig(
            profile=profile,
            regions=regions.split(','),
        )
    )
    steam.install(['aws'])
    steam.start()

    for row in steam.query(models.AwsIamRole).all():
        print(row.to_json())

    steam.stop()


if __name__ == '__main__':
    app()
