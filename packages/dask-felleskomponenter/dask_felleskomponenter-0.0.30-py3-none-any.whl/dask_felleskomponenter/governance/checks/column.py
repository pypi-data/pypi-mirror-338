from typing import List
from .common import MetadataError
from src.dask_felleskomponenter.governance.main import TableMetadata

def check_romlig_representasjonstype(metadata: TableMetadata, context: List) -> List[MetadataError]:
    kodeliste_url = "https://register.geonorge.no/api/register/romlig-representasjonstype "

    if metadata.romlig_representasjonstype is None:
        error_obj = MetadataError(catalog=metadata.catalog, 
                                     schema=metadata.schema, 
                                     table=metadata.table, 
                                     column=None, 
                                     description="🔴 Feil: 'romlig_representasjonstype' mangler i column properties. Type: <romlig_representasjonstype> - gyldige verdier finner du her: " + kodeliste_url, 
                                     solution=f"ALTER TABLE {metadata.catalog}.{metadata.schema}.{metadata.table} SET TBLPROPERTIES ( 'romlig_representasjonstype' = '<<SETT_ROMLIG_REPRESENTASJONSTYPE_HER>>')")
        context.append(error_obj)
    
    return context

# Spør Tom om denne
""" def check_epsg_koder(metadata: TableMetadata, context: List[MetadataError]) -> List[MetadataError]:
    kodeliste_url = "https://register.geonorge.no/api/register/epsg-koder"

    if not check_codelist_value(kodeliste_url, metadata.epsg_koder, override_kodeliste_keyword="epsgcode"):
        valid_values = get_valid_codelist_values(kodeliste_url, "epsgcode")
        context.append(_generate_metadata_error(metadata.catalog, metadata.schema, metadata.table, "epsg_koder", "epsg_koder", metadata.epsg_koder == None, f"gyldige verdier: {valid_values}"))
    
    return context """