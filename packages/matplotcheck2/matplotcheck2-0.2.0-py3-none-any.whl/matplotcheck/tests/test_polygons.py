"""Tests for the vector module"""

import matplotlib
import matplotlib.pyplot as plt
import pytest
import geopandas as gpd
from shapely.geometry import Polygon

from matplotcheck.vector import VectorTester

matplotlib.use("Agg")


@pytest.fixture
def multi_polygon_gdf(basic_polygon):
    """
    A GeoDataFrame containing the basic polygon geometry.
    Returns
    -------
    GeoDataFrame containing the basic_polygon polygon.
    """
    poly_a = Polygon([(3, 5), (2, 3.25), (5.25, 6), (2.25, 2), (2, 2)])
    gdf = gpd.GeoDataFrame(
        [1, 2],
        geometry=[poly_a.buffer(0), basic_polygon.buffer(0)],
        crs="epsg:4326",
    )
    multi_gdf = gpd.GeoDataFrame(
        geometry=gpd.GeoSeries(gdf.union_all()), crs="epsg:4326"
    )
    return multi_gdf


@pytest.fixture
def poly_geo_plot(basic_polygon_gdf):
    """Create a polygon vector tester object."""
    _, ax = plt.subplots()

    basic_polygon_gdf.plot(ax=ax)

    return VectorTester(ax)


@pytest.fixture
def multi_poly_geo_plot(multi_polygon_gdf):
    """Create a mutlipolygon vector tester object."""
    _, ax = plt.subplots()

    multi_polygon_gdf.plot(ax=ax)

    return VectorTester(ax)


def test_list_of_polygons_check(poly_geo_plot, basic_polygon):
    """Check that the polygon assert works with a list of polygons."""
    x, y = basic_polygon.exterior.coords.xy
    poly_list = [list(zip(x, y))]
    poly_geo_plot.assert_polygons(poly_list)
    plt.close("all")


def test_polygon_geodataframe_check(poly_geo_plot, basic_polygon_gdf):
    """Check that the polygon assert works with a polygon geodataframe"""
    poly_geo_plot.assert_polygons(basic_polygon_gdf)
    plt.close("all")


def test_empty_list_polygon_check(poly_geo_plot):
    """Check that the polygon assert fails an empty list."""
    with pytest.raises(ValueError, match="Empty list or GeoDataFrame "):
        poly_geo_plot.assert_polygons([])
        plt.close("all")


def test_empty_list_entry_polygon_check(poly_geo_plot):
    """Check that the polygon assert fails a list with an empty entry."""
    with pytest.raises(ValueError, match="Empty list or GeoDataFrame "):
        poly_geo_plot.assert_polygons([[]])
        plt.close("all")


def test_empty_gdf_polygon_check(poly_geo_plot):
    """Check that the polygon assert fails an empty GeoDataFrame."""
    with pytest.raises(ValueError, match="Empty list or GeoDataFrame "):
        poly_geo_plot.assert_polygons(gpd.GeoDataFrame([]))
        plt.close("all")


def test_polygon_dec_check(poly_geo_plot, basic_polygon):
    """
    Check that the polygon assert passes when the polygon is off by less than
    the maximum decimal precision.
    """
    x, y = basic_polygon.exterior.coords.xy
    poly_list = [[(x[0] + 0.1, x[1]) for x in list(zip(x, y))]]
    poly_geo_plot.assert_polygons(poly_list, dec=1)
    plt.close("all")


def test_polygon_dec_check_fail(poly_geo_plot, basic_polygon):
    """
    Check that the polygon assert fails when the polygon is off by more than
    the maximum decimal precision.
    """
    with pytest.raises(AssertionError, match="Incorrect Polygon"):
        x, y = basic_polygon.exterior.coords.xy
        poly_list = [(x[0] + 0.5, x[1]) for x in list(zip(x, y))]
        poly_geo_plot.assert_polygons(poly_list, dec=1)
        plt.close("all")


def test_polygon_custom_fail_message(poly_geo_plot, basic_polygon):
    """Check that the corrct error message is raised when polygons fail"""
    with pytest.raises(AssertionError, match="Test Message"):
        x, y = basic_polygon.exterior.coords.xy
        poly_list = [(x[0] + 0.5, x[1]) for x in list(zip(x, y))]
        poly_geo_plot.assert_polygons(poly_list, m="Test Message")
        plt.close("all")


def test_multi_polygon_pass(multi_poly_geo_plot, multi_polygon_gdf):
    """Check a multipolygon passes"""
    multi_poly_geo_plot.assert_polygons(multi_polygon_gdf)
    plt.close("all")
