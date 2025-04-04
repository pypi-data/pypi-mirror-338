"""
ExportsFactory export a city and the buildings of a city
SPDX - License - Identifier: LGPL - 3.0 - or -later
Copyright © 2019 - 2025 Concordia CERC group
Code Contributor: Koa Wells kekoa.wells@concordia.ca
"""

from pathlib import Path

from hub.exports.results_factory_formats.csv import Csv

class ResultsExportFactory:
  """
  Exports factory class for results and hub building data
  """

  def __init__(self, city, handler, path):
    """
    :param city: the city object to export
    :param handler: the handler object determine output file format
    :param path: the path to export results
    """

    self._city = city
    self._handler = '_' + handler.lower()
    if isinstance(path, str):
      path = Path(path)
    self._path = path

  @property
  def _csv(self):
    """
    Export city results to csv file
    :return: none
    """
    return Csv(self._city, self._path)

  @property
  def _geojson(self):
    """
    Export city results to a geojson file
    :return: none
    """
    #todo: add geojson handler
    raise NotImplementedError()

  @property
  def _parquet(self):
    """
    Export city results to a parquet file
    :return: none
    """
    #todo: add parquet handler
    raise NotImplementedError()

  def export(self):
    """
    Export the city given to the class using the given export type handler
    :return: None
    """
    return getattr(self, self._handler, lambda: None)