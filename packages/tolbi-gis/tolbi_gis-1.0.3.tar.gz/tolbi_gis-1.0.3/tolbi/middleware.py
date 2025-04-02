import logging
import pandas as pd
import geopandas as gpd
from pathlib import Path
from django.utils.deprecation import MiddlewareMixin
from django.core.files.uploadedfile import SimpleUploadedFile

logger = logging.getLogger(__name__)


def drop_z_pygeos(gdf) -> gpd.GeoSeries:
  ''' Drop Z coordinates from GeoSeries, returns GeoSeries
  '''
  return gpd.GeoSeries.from_wkb(gdf.to_wkb(output_dimension=2))

def valid_features(gdf) -> gpd.GeoDataFrame:
    '''Remove invalid features'''
    valid_mask = gdf.geometry.apply(lambda geom: geom.is_valid)
    valid_gdf = gdf[valid_mask]
    return valid_gdf

def drop_date_columns(gdf) -> gpd.GeoDataFrame:
    '''Drop Date columns (no serializable)'''
    date_cols = []
    for col in gdf.columns:
        if pd.api.types.is_datetime64_any_dtype(gdf[col]):
            date_cols.append(col)

    gdf = gdf.drop(columns=date_cols)
    return gdf


class GeoExplodeMiddleware(MiddlewareMixin):
    """
    Transform a geojson file received via geopandas
    Explodes MultiType geometries to singe Types
    """

    def process_request(self, request):
        if request.method=="POST" and 'multipart/form-data' in request.content_type:
            for key, content in request.FILES.items():
                if Path(content.name).suffix.lower() == ".geojson":
                    try:
                        gdf = gpd.read_file(content.file)
                        exploded_gdf = gdf.explode(ignore_index=True)
                        normalized = drop_date_columns(exploded_gdf)
                        normalized['geometry'] = drop_z_pygeos(normalized.geometry)
                        validgdf = valid_features(normalized)
                        new_content = validgdf.to_json(to_wgs84=True).encode()
                        new_file = SimpleUploadedFile(
                            name=content.name,
                            content=new_content,
                            content_type=content.content_type
                        )
                        request.FILES[key] = new_file

                    except Exception as e:
                        logger.info(f"Something went wrong {e}")
                        pass

        return self.get_response(request)
