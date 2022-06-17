from shapely.geometry import Point, Polygon, LineString, MultiPolygon, MultiPoint, MultiLineString


class GeoJson:

    def point(self, coordinates, chose_point):
        point = Point(coordinates)
        point = Point(coordinates)
        return point.contains(chose_point)

    def polygon(self, coordinates, chose_point):
        polygon = Polygon([tuple(i) for i in coordinates[0]])
        return polygon.contains(chose_point)

    def linestring(self, coordinates, chose_point):
        line_string = LineString(coordinates)
        return line_string.contains(chose_point)

    def multipoint(self, coordinates, chose_point):
        multi_point = MultiPoint(coordinates)
        return multi_point.contains(chose_point)

    def multilinestring(self, coordinates, chose_point):
        multi_line_string = MultiLineString(coordinates)
        return multi_line_string.contains(chose_point)

    def multipolygon(self, coordinates, chose_point):
        c = []
        for i in coordinates:
            for j in i:
                polygon = Polygon([tuple(i) for i in j])
                if polygon.contains(chose_point) is True:
                    return True
                else:
                    continue
        return False
