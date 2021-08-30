# Hacky script to just dump the contents of every table to json files
import os
import psycopg2.errors
from pathlib import Path

from sqlalchemy.dialects.postgresql import psycopg2

from steampipe_alchemy import SteamPipe, models
import steampipe_alchemy
from steampipe_alchemy.models import AwsWellarchitectedWorkload, AwsDynamodbGlobalTable, AwsEc2TransitGateway, AwsVpc, \
    AwsEc2Instance


def main():
    steam = SteamPipe()
    steam.install(['aws'])
    steam.update_config(aws={  # Modifies ~/.local/share/steampipe_alchemy/config/aws.spc
        "plugin": "aws",
        "regions": [
            "eu-north-1",
            "ap-south-1",
            "eu-west-3",
            "eu-west-2",
            "eu-west-1",
            "ap-northeast-3",
            "ap-northeast-2",
            "ap-northeast-1",
            "sa-east-1",
            "ca-central-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "eu-central-1",
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2"
        ],
    })
    steam.start()
    os.mkdir('output')
    steampipe_alchemy.all_models.remove(AwsEc2Instance)

    for model in steampipe_alchemy.all_models:
        # print(model.__name__)
        with (Path('output')/model.__name__).open(mode='w+') as f:
            try:
                for i in steam.query(model):
                    print('.', end='')
                    f.write(i.to_json() + "\n")
            except Exception as e:
                print(e)
                try:
                    steam.db.rollback()
                except Exception as e:
                    steam.start()


# TODO: Seems like the atexit hook in start is throwing an exception at the end of the run for some reason.
if __name__ == '__main__':
    main()
