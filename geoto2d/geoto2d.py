import json

import click
import cligj
import geojson
from geojson.utils import map_tuples


@click.command()
@cligj.features_in_arg
@cligj.sequence_opt
@cligj.use_rs_opt
def geoto2d(features, sequence, use_rs):
    if sequence:
        for feature in process_features(features):
            if use_rs:
                click.echo(u'\x1e', nl=False)
            click.echo(json.dumps(feature))
    else:
        click.echo(
            json.dumps({
                'type': 'FeatureCollection',
                'features': list(process_features(features))}))


def process_features(features):
    for feature in features:
        gj = geojson.loads(json.dumps(feature))
        yield map_tuples(lambda c: (c[0], c[1]), gj)


if __name__ == '__main__':
    geoto2d()
